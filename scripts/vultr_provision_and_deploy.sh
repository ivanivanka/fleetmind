#!/usr/bin/env bash
set -euo pipefail

# Provision a Vultr VM and deploy FleetMind via Docker Compose.
# Requires: VULTR_API_KEY (Vultr v2 API token) + GEMINI_API_KEY (optional).

need() { command -v "$1" >/dev/null 2>&1 || { echo "Missing dependency: $1" >&2; exit 1; }; }
need curl
need jq
need ssh
need nc

VULTR_API_KEY="${VULTR_API_KEY:?VULTR_API_KEY is required}"
REGION="${VULTR_REGION:-sjc}"
PLAN="${VULTR_PLAN:-vc2-1c-1gb}"
OS_ID="${VULTR_OS_ID:-1743}" # Ubuntu 22.04 LTS x64
SSH_KEY_NAME="${VULTR_SSH_KEY_NAME:-fleetmind-codex}"
SSH_PUBKEY_PATH="${VULTR_SSH_PUBKEY_PATH:-$HOME/.ssh/id_rsa.pub}"

LABEL="${VULTR_LABEL:-fleetmind-demo-$(date +%m%d-%H%M)}"
HOST_PORT="${HOST_PORT:-80}"
GEMINI_MODEL="${GEMINI_MODEL:-gemini-flash-latest}"

api() {
  local method="$1"; shift
  local url="$1"; shift
  if [ "$#" -gt 0 ]; then
    curl -sS -X "$method" -H "Authorization: Bearer $VULTR_API_KEY" -H "Content-Type: application/json" "$url" -d "$1"
  else
    curl -sS -X "$method" -H "Authorization: Bearer $VULTR_API_KEY" "$url"
  fi
}

if [ ! -f "$SSH_PUBKEY_PATH" ]; then
  echo "SSH public key not found: $SSH_PUBKEY_PATH" >&2
  exit 1
fi

PUBKEY="$(cat "$SSH_PUBKEY_PATH")"

echo "Ensuring Vultr SSH key exists ($SSH_KEY_NAME)..."
SSHKEY_ID="$(api GET "https://api.vultr.com/v2/ssh-keys" | jq -r --arg name "$SSH_KEY_NAME" '.ssh_keys[] | select(.name==$name) | .id' | head -n1 || true)"
if [ -z "${SSHKEY_ID:-}" ]; then
  payload="$(jq -n --arg name "$SSH_KEY_NAME" --arg key "$PUBKEY" '{name:$name, ssh_key:$key}')"
  SSHKEY_ID="$(api POST "https://api.vultr.com/v2/ssh-keys" "$payload" | jq -r '.ssh_key.id')"
fi

echo "Creating instance ($LABEL) in $REGION/$PLAN..."
payload="$(jq -n \
  --arg region "$REGION" \
  --arg plan "$PLAN" \
  --arg label "$LABEL" \
  --arg hostname "$LABEL" \
  --arg sshkey "$SSHKEY_ID" \
  --argjson os_id "$OS_ID" \
  '{region:$region, plan:$plan, os_id:$os_id, label:$label, hostname:$hostname, sshkey_id:[$sshkey], enable_ipv6:true}'
)"
INSTANCE_ID="$(api POST "https://api.vultr.com/v2/instances" "$payload" | jq -r '.instance.id')"

echo "Waiting for instance to become active..."
IP=""
for _ in $(seq 1 60); do
  resp="$(api GET "https://api.vultr.com/v2/instances/$INSTANCE_ID")"
  st="$(echo "$resp" | jq -r '.instance.status')"
  IP="$(echo "$resp" | jq -r '.instance.main_ip')"
  if [ "$st" = "active" ] && [ -n "$IP" ] && [ "$IP" != "null" ]; then
    break
  fi
  sleep 5
done
if [ -z "$IP" ] || [ "$IP" = "null" ]; then
  echo "Instance did not get an IP in time. Instance ID: $INSTANCE_ID" >&2
  exit 1
fi

echo "Waiting for SSH to come up on $IP..."
for _ in $(seq 1 60); do
  if nc -z "$IP" 22 >/dev/null 2>&1; then
    break
  fi
  sleep 2
done

SSH_OPTS=(-o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -o ConnectTimeout=10)

echo "Installing Docker on the VM..."
ssh "${SSH_OPTS[@]}" root@"$IP" "apt-get update -y && apt-get install -y curl git && curl -fsSL https://get.docker.com | sh"

echo "Deploying FleetMind..."
ssh "${SSH_OPTS[@]}" root@"$IP" "rm -rf /opt/fleetmind && git clone --depth 1 https://github.com/ivanivanka/fleetmind.git /opt/fleetmind"

# Write env without echoing values to stdout (base64 avoids quoting edge-cases).
ENV_CONTENT="$(printf 'HOST_PORT=%s\nGEMINI_MODEL=%s\n' "$HOST_PORT" "$GEMINI_MODEL")"
if [ -n "${GEMINI_API_KEY:-}" ]; then
  ENV_CONTENT+="$(printf 'GEMINI_API_KEY=%s\n' "$GEMINI_API_KEY")"
fi
ENV_B64="$(printf '%s' "$ENV_CONTENT" | base64 | tr -d '\n')"
ssh "${SSH_OPTS[@]}" root@"$IP" "install -m 600 /dev/null /opt/fleetmind/.env && printf '%s' '$ENV_B64' | base64 -d > /opt/fleetmind/.env"

ssh "${SSH_OPTS[@]}" root@"$IP" "cd /opt/fleetmind && docker compose up -d --build"

echo
echo "Deployed:"
echo "  URL: http://$IP:$HOST_PORT/"
echo "  Health: http://$IP:$HOST_PORT/healthz"
echo "  Instance ID: $INSTANCE_ID"
