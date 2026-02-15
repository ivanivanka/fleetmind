/* Markster FleetMind AI - Dashboard Frontend (v2 — pitch-ready visuals) */

const canvas = document.getElementById('warehouse-canvas');
const ctx = canvas.getContext('2d');

let state = null;
let prevState = null;
let ws = null;
let selectedRobot = null;
let startTime = Date.now();
let cellSize = 20;
let _actionTimer = null;
let animT = 0;           // 0..1 interpolation progress
let lastStateTime = 0;   // when we last received a state update
let dashOffset = 0;       // animated dashes

// Colors
const COLORS = {
    floor: '#0d0d0d',
    shelf: '#1e1e1e',
    shelfBorder: '#2a2a2a',
    charge: '#1a1400',
    chargeBorder: '#ffaa00',
    pickup: '#0a1a30',
    pickupBorder: '#3388ff',
    dropoff: '#1a0a28',
    dropoffBorder: '#aa44ff',
    grid: '#141414',
    robot: {
        idle: '#555555',
        moving_to_pickup: '#00cc44',
        picking: '#00ff55',
        moving_to_dropoff: '#3388ff',
        dropping: '#5599ff',
        moving_to_charge: '#ffaa00',
        charging: '#ff8800',
        error: '#ff3344',
    },
};

// Previous robot positions for interpolation
let prevPositions = {};

function lerp(a, b, t) {
    return a + (b - a) * Math.min(Math.max(t, 0), 1);
}

// -- WebSocket Connection --
function connect() {
    const proto = location.protocol === 'https:' ? 'wss' : 'ws';
    ws = new WebSocket(`${proto}://${location.host}/ws`);

    ws.onopen = () => {
        document.getElementById('ws-status').textContent = 'Connected';
        document.getElementById('ws-status').style.color = '#00cc44';
    };

    ws.onmessage = (e) => {
        const data = JSON.parse(e.data);
        if (data.type === 'state_update') {
            // Save previous positions for interpolation
            if (state && state.robots) {
                for (const r of state.robots) {
                    prevPositions[r.id] = { x: r.x, y: r.y };
                }
            }
            prevState = state;
            state = data;
            lastStateTime = performance.now();
            animT = 0;
            updateDashboard();
        }
    };

    ws.onclose = () => {
        document.getElementById('ws-status').textContent = 'Reconnecting';
        document.getElementById('ws-status').style.color = '#ffaa00';
        setTimeout(connect, 2000);
    };

    ws.onerror = () => {
        document.getElementById('ws-status').textContent = 'Error';
        document.getElementById('ws-status').style.color = '#ff3344';
    };
}

// -- Canvas Rendering --
function resizeCanvas() {
    if (!state) return;
    const wrapper = document.querySelector('.canvas-wrapper');
    const maxW = wrapper.clientWidth - 24;
    const maxH = wrapper.clientHeight - 24;
    const gridW = state.grid.width;
    const gridH = state.grid.height;

    cellSize = Math.min(Math.floor(maxW / gridW), Math.floor(maxH / gridH), 24);
    cellSize = Math.max(cellSize, 10);

    canvas.width = gridW * cellSize;
    canvas.height = gridH * cellSize;
}

function drawRoundedRect(x, y, w, h, r) {
    ctx.beginPath();
    ctx.moveTo(x + r, y);
    ctx.lineTo(x + w - r, y);
    ctx.quadraticCurveTo(x + w, y, x + w, y + r);
    ctx.lineTo(x + w, y + h - r);
    ctx.quadraticCurveTo(x + w, y + h, x + w - r, y + h);
    ctx.lineTo(x + r, y + h);
    ctx.quadraticCurveTo(x, y + h, x, y + h - r);
    ctx.lineTo(x, y + r);
    ctx.quadraticCurveTo(x, y, x + r, y);
    ctx.closePath();
}

function render() {
    if (!state) return;
    resizeCanvas();

    const { grid, robots, tasks } = state;
    const w = grid.width;
    const h = grid.height;

    // Interpolation progress (smooth over ~400ms between state updates)
    const elapsed = performance.now() - lastStateTime;
    animT = Math.min(elapsed / 400, 1);

    // Animated dash offset
    dashOffset = (performance.now() / 80) % 12;

    // Clear
    ctx.fillStyle = COLORS.floor;
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    // Subtle grid (very faint)
    ctx.strokeStyle = COLORS.grid;
    ctx.lineWidth = 0.3;
    for (let x = 0; x <= w; x++) {
        ctx.beginPath();
        ctx.moveTo(x * cellSize, 0);
        ctx.lineTo(x * cellSize, h * cellSize);
        ctx.stroke();
    }
    for (let y = 0; y <= h; y++) {
        ctx.beginPath();
        ctx.moveTo(0, y * cellSize);
        ctx.lineTo(w * cellSize, y * cellSize);
        ctx.stroke();
    }

    // Cells
    for (let y = 0; y < h; y++) {
        for (let x = 0; x < w; x++) {
            const cell = grid.cells[y][x];
            const cx = x * cellSize;
            const cy = y * cellSize;

            if (cell === 1) {
                // Shelf — subtle with rounded corners
                ctx.fillStyle = COLORS.shelf;
                drawRoundedRect(cx + 1, cy + 1, cellSize - 2, cellSize - 2, 2);
                ctx.fill();
                ctx.strokeStyle = COLORS.shelfBorder;
                ctx.lineWidth = 0.3;
                ctx.stroke();
            } else if (cell === 2) {
                // Charging station — warm glow
                ctx.fillStyle = COLORS.charge;
                ctx.fillRect(cx, cy, cellSize, cellSize);
                ctx.strokeStyle = COLORS.chargeBorder;
                ctx.lineWidth = 1.5;
                ctx.strokeRect(cx + 2, cy + 2, cellSize - 4, cellSize - 4);
                ctx.fillStyle = COLORS.chargeBorder;
                ctx.font = `${cellSize * 0.5}px sans-serif`;
                ctx.textAlign = 'center';
                ctx.textBaseline = 'middle';
                ctx.fillText('\u26A1', cx + cellSize / 2, cy + cellSize / 2);
            } else if (cell === 3) {
                // Pickup zone
                ctx.fillStyle = COLORS.pickup;
                ctx.fillRect(cx, cy, cellSize, cellSize);
                ctx.strokeStyle = COLORS.pickupBorder;
                ctx.lineWidth = 0.8;
                ctx.strokeRect(cx + 1, cy + 1, cellSize - 2, cellSize - 2);
            } else if (cell === 4) {
                // Dropoff zone
                ctx.fillStyle = COLORS.dropoff;
                ctx.fillRect(cx, cy, cellSize, cellSize);
                ctx.strokeStyle = COLORS.dropoffBorder;
                ctx.lineWidth = 0.8;
                ctx.strokeRect(cx + 1, cy + 1, cellSize - 2, cellSize - 2);
            }
        }
    }

    // Zone labels (only if cells are large enough)
    if (cellSize >= 14) {
        ctx.font = `bold ${Math.max(8, cellSize * 0.4)}px ${getComputedStyle(document.body).fontFamily}`;
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';

        // Label pickup zones
        for (const pz of grid.pickup_zones || []) {
            ctx.fillStyle = '#3388ff60';
            ctx.fillText('P', pz.x * cellSize + cellSize / 2, pz.y * cellSize + cellSize / 2);
        }
        // Label dropoff zones
        for (const dz of grid.dropoff_zones || []) {
            ctx.fillStyle = '#aa44ff60';
            ctx.fillText('D', dz.x * cellSize + cellSize / 2, dz.y * cellSize + cellSize / 2);
        }
    }

    // Robot paths — animated dashes
    for (const robot of robots) {
        if (robot.path && robot.path.length > 0) {
            const color = COLORS.robot[robot.state] || '#666';
            ctx.strokeStyle = color + '30';
            ctx.lineWidth = 2;
            ctx.setLineDash([4, 4]);
            ctx.lineDashOffset = -dashOffset;

            // Get interpolated robot position
            const prev = prevPositions[robot.id] || { x: robot.x, y: robot.y };
            const rx = lerp(prev.x, robot.x, animT) * cellSize + cellSize / 2;
            const ry = lerp(prev.y, robot.y, animT) * cellSize + cellSize / 2;

            ctx.beginPath();
            ctx.moveTo(rx, ry);
            for (const p of robot.path) {
                ctx.lineTo(p.x * cellSize + cellSize / 2, p.y * cellSize + cellSize / 2);
            }
            ctx.stroke();
            ctx.setLineDash([]);
            ctx.lineDashOffset = 0;

            // Target marker — pulsing ring
            if (robot.target) {
                const tx = robot.target.x * cellSize + cellSize / 2;
                const ty = robot.target.y * cellSize + cellSize / 2;
                const pulse = 0.8 + Math.sin(performance.now() / 300) * 0.2;
                ctx.strokeStyle = color + '50';
                ctx.lineWidth = 1.5;
                ctx.beginPath();
                ctx.arc(tx, ty, cellSize / 3 * pulse, 0, Math.PI * 2);
                ctx.stroke();
            }
        }
    }

    // Robots — smooth interpolated positions, rounded rectangle shape
    for (const robot of robots) {
        const prev = prevPositions[robot.id] || { x: robot.x, y: robot.y };
        const rx = lerp(prev.x, robot.x, animT) * cellSize + cellSize / 2;
        const ry = lerp(prev.y, robot.y, animT) * cellSize + cellSize / 2;
        const size = cellSize * 0.72;
        const half = size / 2;
        const color = COLORS.robot[robot.state] || '#555';

        // Glow for active/selected robots
        const isActive = robot.state !== 'idle';
        if (selectedRobot === robot.id || isActive) {
            ctx.shadowColor = color;
            ctx.shadowBlur = selectedRobot === robot.id ? 14 : 6;
        }

        // Robot body — rounded rectangle
        ctx.fillStyle = color;
        drawRoundedRect(rx - half, ry - half, size, size, cellSize * 0.15);
        ctx.fill();

        // Border
        ctx.strokeStyle = 'rgba(255,255,255,0.12)';
        ctx.lineWidth = 0.8;
        ctx.stroke();

        // Inner detail — smaller rounded rect for "sensor" look
        if (cellSize >= 14) {
            ctx.fillStyle = 'rgba(0,0,0,0.3)';
            const innerSize = size * 0.5;
            const innerHalf = innerSize / 2;
            drawRoundedRect(rx - innerHalf, ry - innerHalf, innerSize, innerSize, cellSize * 0.08);
            ctx.fill();
        }

        ctx.shadowColor = 'transparent';
        ctx.shadowBlur = 0;

        // Direction indicator — small triangle showing movement direction
        if (robot.path && robot.path.length > 0 && cellSize >= 12) {
            const nextP = robot.path[0];
            const dx = nextP.x - robot.x;
            const dy = nextP.y - robot.y;
            if (dx !== 0 || dy !== 0) {
                const angle = Math.atan2(dy, dx);
                const arrowDist = half + 2;
                const ax = rx + Math.cos(angle) * arrowDist;
                const ay = ry + Math.sin(angle) * arrowDist;
                ctx.fillStyle = color;
                ctx.beginPath();
                ctx.arc(ax, ay, 2, 0, Math.PI * 2);
                ctx.fill();
            }
        }

        // Robot ID label
        if (cellSize >= 16) {
            ctx.fillStyle = '#fff';
            ctx.font = `bold ${Math.max(cellSize * 0.28, 7)}px monospace`;
            ctx.textAlign = 'center';
            ctx.textBaseline = 'middle';
            ctx.fillText(robot.id.replace('R0', '').replace('R', ''), rx, ry);
        }

        // Battery indicator bar
        if (cellSize >= 14) {
            const barW = size;
            const barH = 2.5;
            const barX = rx - barW / 2;
            const barY = ry + half + 3;
            // Background
            ctx.fillStyle = 'rgba(0,0,0,0.5)';
            drawRoundedRect(barX, barY, barW, barH, 1);
            ctx.fill();
            // Fill
            const battColor = robot.battery > 50 ? '#00cc44' : robot.battery > 20 ? '#ffaa00' : '#ff3344';
            ctx.fillStyle = battColor;
            const fillW = barW * (robot.battery / 100);
            if (fillW > 2) {
                drawRoundedRect(barX, barY, fillW, barH, 1);
                ctx.fill();
            }
        }
    }
}

// -- Animation Loop (60fps smooth rendering) --
function animationLoop() {
    if (state) {
        render();
    }
    requestAnimationFrame(animationLoop);
}

// -- Dashboard Updates --
function setActionStatus(text, kind = '') {
    const el = document.getElementById('action-status');
    if (!el) return;
    el.className = 'action-status' + (kind ? ' ' + kind : '');
    el.textContent = text || '';
    if (_actionTimer) clearTimeout(_actionTimer);
    if (text) _actionTimer = setTimeout(() => { el.textContent = ''; el.className = 'action-status'; }, 3500);
}

function updateDashboard() {
    if (!state) return;
    const { metrics, robots, tasks, alerts, tick } = state;

    // Topbar
    document.getElementById('tick-count').textContent = tick;
    const elapsed = Math.floor((Date.now() - startTime) / 1000);
    const mins = Math.floor(elapsed / 60);
    const secs = elapsed % 60;
    document.getElementById('uptime').textContent = `${mins}:${secs.toString().padStart(2, '0')}`;

    // Metrics bar
    document.getElementById('m-throughput').textContent = metrics.throughput_per_minute.toFixed(1);
    document.getElementById('m-completed').textContent = metrics.tasks_completed;
    document.getElementById('m-failed').textContent = `${metrics.tasks_failed} failed`;
    document.getElementById('m-queue').textContent = metrics.tasks_in_queue;

    const util = Math.round(metrics.fleet_utilization * 100);
    const utilEl = document.getElementById('m-utilization');
    utilEl.textContent = util + '%';
    utilEl.className = 'value ' + (util > 60 ? 'green' : util > 30 ? '' : 'yellow');
    document.getElementById('m-active').textContent = `${metrics.robots_active} active`;

    const battEl = document.getElementById('m-battery');
    const batt = Math.round(metrics.avg_battery);
    battEl.textContent = batt + '%';
    battEl.className = 'value ' + (batt > 50 ? 'green' : batt > 25 ? 'yellow' : 'red');
    document.getElementById('m-charging').textContent = `${metrics.robots_charging} charging`;

    document.getElementById('m-distance').textContent = Math.round(metrics.total_distance);

    // Pause / E-stop UI
    const paused = !!state.paused;
    const badge = document.getElementById('sim-badge');
    const status = document.getElementById('sim-status');
    if (badge && status) {
        badge.classList.toggle('live', !paused);
        badge.classList.toggle('paused', paused);
        status.textContent = paused ? 'Simulation Paused' : 'Simulation Live';
    }
    const estopBtn = document.getElementById('estop-btn');
    if (estopBtn) {
        estopBtn.textContent = paused ? 'Resume' : 'E-Stop All';
        estopBtn.className = paused ? 'btn primary' : 'btn danger';
    }

    // Fleet list
    document.getElementById('fleet-count').textContent = robots.length;
    const robotList = document.getElementById('robot-list');
    robotList.innerHTML = robots.map(r => {
        const stateClass = r.state === 'idle' ? 'idle'
            : r.state === 'charging' || r.state === 'moving_to_charge' ? 'charging'
            : r.state === 'error' ? 'error'
            : 'active';
        const battColor = r.battery > 50 ? '#00cc44' : r.battery > 20 ? '#ffaa00' : '#ff3344';
        const selected = selectedRobot === r.id ? ' selected' : '';
        return `<div class="robot-item${selected}" onclick="selectRobot('${r.id}')">
            <div class="robot-icon ${stateClass}">${r.id.replace('R0','').replace('R','')}</div>
            <div class="robot-info">
                <div class="name">${r.name} <span style="color:var(--text-muted);font-size:10px">${r.id}</span></div>
                <div class="state">${r.state.replace(/_/g, ' ')}${r.task_id ? ' - ' + r.task_id : ''}</div>
            </div>
            <div class="robot-battery">
                <div class="pct" style="color:${battColor}">${Math.round(r.battery)}%</div>
                <div class="battery-bar"><div class="battery-fill" style="width:${r.battery}%;background:${battColor}"></div></div>
            </div>
        </div>`;
    }).join('');

    // Task list
    document.getElementById('task-count').textContent = tasks.length;
    const taskList = document.getElementById('task-list');
    taskList.innerHTML = tasks.slice(0, 15).map(t => `
        <div class="task-item">
            <div class="task-priority-dot ${t.priority}"></div>
            <div class="task-info">
                <div class="order-id">${t.order_id}</div>
                <div class="item-name">${t.item}</div>
            </div>
            <div class="task-status ${t.status}">${t.status.replace(/_/g, ' ')}</div>
        </div>
    `).join('');

    // Alerts
    document.getElementById('alert-count').textContent = alerts.length;
    const alertList = document.getElementById('alert-list');
    if (alerts.length === 0) {
        alertList.innerHTML = '<div class="empty-state">No active alerts</div>';
    } else {
        alertList.innerHTML = alerts.map(a => {
            const icon = a.type === 'low_battery' ? '\u26A0'
                : a.type === 'stuck' ? '\u26D4'
                : a.type === 'failed_task' ? '\u2716'
                : '\u25BC';
            return `<div class="alert-item">
                <div class="alert-icon ${a.type}">${icon}</div>
                <div class="alert-text">${a.message}</div>
                <button class="alert-dismiss" onclick="dismissAlert('${a.id}')">\u2715</button>
            </div>`;
        }).join('');
    }
}

// -- Actions --
function selectRobot(id) {
    selectedRobot = selectedRobot === id ? null : id;
}

async function addTask() {
    try {
        const res = await fetch('/api/tasks/create', { method: 'POST' });
        const data = await res.json();
        if (data && data.status === 'created') {
            setActionStatus(`Task created: ${data.task_id}`, 'ok');
        } else {
            setActionStatus('Task create failed', 'err');
        }
    } catch (e) {
        setActionStatus('Task create failed', 'err');
    }
}

async function requestAIInsight() {
    const el = document.getElementById('ai-insight');
    el.textContent = 'Analyzing fleet patterns...';
    try {
        const res = await fetch('/api/ai/insight?mode=gemini');
        const data = await res.json();
        el.textContent = data.insight;
        setActionStatus(`AI insight updated (${data.source || 'unknown'})`, data.source === 'gemini' ? 'ok' : 'warn');
    } catch (e) {
        el.textContent = 'AI analysis unavailable';
        setActionStatus('AI insight failed', 'err');
    }
}

async function dismissAlert(id) {
    try {
        await fetch(`/api/alerts/${id}/acknowledge`, { method: 'POST' });
    } catch (e) {
        console.error('Failed to dismiss alert:', e);
    }
}

async function emergencyStopAll() {
    if (!state) return;
    try {
        if (state.paused) {
            await fetch('/api/sim/resume', { method: 'POST' });
            setActionStatus('Simulation resumed', 'ok');
        } else {
            await fetch('/api/sim/pause', { method: 'POST' });
            setActionStatus('E-stop engaged (paused)', 'warn');
        }
    } catch (e) {
        setActionStatus('E-stop failed', 'err');
    }
}

async function resetDemo() {
    try {
        setActionStatus('Resetting demo...', 'warn');
        await fetch('/api/sim/reset', { method: 'POST' });
        selectedRobot = null;
        prevPositions = {};
        startTime = Date.now();
        setActionStatus('Demo reset', 'ok');
    } catch (e) {
        setActionStatus('Demo reset failed', 'err');
    }
}

// -- Canvas interaction --
canvas.addEventListener('click', (e) => {
    if (!state) return;
    const rect = canvas.getBoundingClientRect();
    const mx = e.clientX - rect.left;
    const my = e.clientY - rect.top;
    const gx = Math.floor(mx / cellSize);
    const gy = Math.floor(my / cellSize);

    for (const robot of state.robots) {
        if (robot.x === gx && robot.y === gy) {
            selectRobot(robot.id);
            return;
        }
    }
    selectedRobot = null;
});

// -- AI Insight auto-refresh --
setInterval(async () => {
    try {
        const res = await fetch('/api/ai/insight?mode=rules');
        const data = await res.json();
        document.getElementById('ai-insight').textContent = data.insight;
    } catch (e) { /* ignore */ }
}, 15000);

// -- Window resize --
window.addEventListener('resize', () => { if (state) render(); });

// -- Init --
connect();
requestAnimationFrame(animationLoop);
