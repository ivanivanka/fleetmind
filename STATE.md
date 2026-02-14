# FleetMind State

## Current (2026-02-14)

- Live demo (Vultr): `http://149.28.198.127/`
- Health: `http://149.28.198.127/healthz`
- Vultr instance id: `9120077a-acdb-46d3-970a-394c96cf14ed`
- Region/plan: `sjc` / `vc2-1c-1gb` (Ubuntu 22.04)
- Deployed path on VM: `/opt/fleetmind`
- Runs via: Docker Compose (`docker compose up -d --build`) mapping host `:80` -> container `:8000`

## Redeploy

```bash
ssh root@149.28.198.127 "cd /opt/fleetmind && git pull && docker compose up -d --build"
```

## Stop Demo

```bash
ssh root@149.28.198.127 "cd /opt/fleetmind && docker compose down"
```

## Submission Notes

- Copy/paste notes: `SUBMISSION.md`
- Demo runbook: `DEMO.md`
- Hackathon submission deadline mentioned in WhatsApp: **2026-02-14 5:00 PM PST**
