/* FleetMind AI Platform - Shared JavaScript */

// Sidebar navigation — highlight active page
(function() {
    const path = window.location.pathname.replace(/\/$/, '');
    const navItems = document.querySelectorAll('.nav-item');
    navItems.forEach(item => {
        const href = item.getAttribute('href');
        if (!href) return;
        const hrefClean = href.replace(/\/$/, '');
        if (path === hrefClean || (path === '/platform' && hrefClean === '/platform/dashboard')) {
            item.classList.add('active');
        }
    });
})();

// Simple sparkline drawing on mini-chart canvases
function drawSparkline(canvasId, data, color) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const w = canvas.width = canvas.offsetWidth * 2;
    const h = canvas.height = canvas.offsetHeight * 2;
    ctx.scale(2, 2);
    const width = canvas.offsetWidth;
    const height = canvas.offsetHeight;

    const max = Math.max(...data);
    const min = Math.min(...data);
    const range = max - min || 1;
    const step = width / (data.length - 1);

    // Fill gradient
    ctx.beginPath();
    ctx.moveTo(0, height);
    data.forEach((v, i) => {
        const x = i * step;
        const y = height - ((v - min) / range) * (height * 0.85) - height * 0.05;
        if (i === 0) ctx.lineTo(x, y);
        else ctx.lineTo(x, y);
    });
    ctx.lineTo(width, height);
    ctx.closePath();
    const grad = ctx.createLinearGradient(0, 0, 0, height);
    grad.addColorStop(0, color + '33');
    grad.addColorStop(1, 'transparent');
    ctx.fillStyle = grad;
    ctx.fill();

    // Line
    ctx.beginPath();
    data.forEach((v, i) => {
        const x = i * step;
        const y = height - ((v - min) / range) * (height * 0.85) - height * 0.05;
        if (i === 0) ctx.moveTo(x, y);
        else ctx.lineTo(x, y);
    });
    ctx.strokeStyle = color;
    ctx.lineWidth = 1.5;
    ctx.stroke();
}

// Line chart
function drawLineChart(canvasId, datasets, labels, opts = {}) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const dpr = 2;
    const w = canvas.offsetWidth;
    const h = canvas.offsetHeight;
    canvas.width = w * dpr;
    canvas.height = h * dpr;
    ctx.scale(dpr, dpr);

    const padLeft = opts.padLeft || 50;
    const padRight = opts.padRight || 20;
    const padTop = opts.padTop || 20;
    const padBottom = opts.padBottom || 40;
    const chartW = w - padLeft - padRight;
    const chartH = h - padTop - padBottom;

    // Find global min/max
    let allVals = [];
    datasets.forEach(ds => allVals.push(...ds.data));
    let gMin = Math.min(...allVals);
    let gMax = Math.max(...allVals);
    if (opts.yMin !== undefined) gMin = opts.yMin;
    if (opts.yMax !== undefined) gMax = opts.yMax;
    const range = gMax - gMin || 1;

    // Grid lines
    ctx.strokeStyle = '#222222';
    ctx.lineWidth = 0.5;
    const gridLines = 5;
    for (let i = 0; i <= gridLines; i++) {
        const y = padTop + (i / gridLines) * chartH;
        ctx.beginPath();
        ctx.moveTo(padLeft, y);
        ctx.lineTo(padLeft + chartW, y);
        ctx.stroke();

        // Y label
        const val = gMax - (i / gridLines) * range;
        ctx.fillStyle = '#555555';
        ctx.font = '10px SF Mono, monospace';
        ctx.textAlign = 'right';
        ctx.fillText(opts.yFormat ? opts.yFormat(val) : val.toFixed(0), padLeft - 8, y + 3);
    }

    // X labels
    if (labels) {
        ctx.fillStyle = '#555555';
        ctx.font = '10px SF Mono, monospace';
        ctx.textAlign = 'center';
        const step = chartW / (labels.length - 1);
        labels.forEach((label, i) => {
            if (i % Math.ceil(labels.length / 8) === 0 || i === labels.length - 1) {
                ctx.fillText(label, padLeft + i * step, h - padBottom + 16);
            }
        });
    }

    // Draw datasets
    datasets.forEach(ds => {
        const data = ds.data;
        const step = chartW / (data.length - 1);

        // Fill
        if (ds.fill) {
            ctx.beginPath();
            ctx.moveTo(padLeft, padTop + chartH);
            data.forEach((v, i) => {
                const x = padLeft + i * step;
                const y = padTop + chartH - ((v - gMin) / range) * chartH;
                ctx.lineTo(x, y);
            });
            ctx.lineTo(padLeft + (data.length - 1) * step, padTop + chartH);
            ctx.closePath();
            const grad = ctx.createLinearGradient(0, padTop, 0, padTop + chartH);
            grad.addColorStop(0, ds.color + '22');
            grad.addColorStop(1, 'transparent');
            ctx.fillStyle = grad;
            ctx.fill();
        }

        // Line
        ctx.beginPath();
        data.forEach((v, i) => {
            const x = padLeft + i * step;
            const y = padTop + chartH - ((v - gMin) / range) * chartH;
            if (i === 0) ctx.moveTo(x, y);
            else ctx.lineTo(x, y);
        });
        ctx.strokeStyle = ds.color;
        ctx.lineWidth = 2;
        ctx.stroke();

        // Dots on last point
        const lastI = data.length - 1;
        const lx = padLeft + lastI * step;
        const ly = padTop + chartH - ((data[lastI] - gMin) / range) * chartH;
        ctx.beginPath();
        ctx.arc(lx, ly, 3, 0, Math.PI * 2);
        ctx.fillStyle = ds.color;
        ctx.fill();
    });
}

// Bar chart
function drawBarChart(canvasId, data, labels, color, opts = {}) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const dpr = 2;
    const w = canvas.offsetWidth;
    const h = canvas.offsetHeight;
    canvas.width = w * dpr;
    canvas.height = h * dpr;
    ctx.scale(dpr, dpr);

    const padLeft = opts.padLeft || 50;
    const padRight = opts.padRight || 20;
    const padTop = opts.padTop || 20;
    const padBottom = opts.padBottom || 40;
    const chartW = w - padLeft - padRight;
    const chartH = h - padTop - padBottom;

    const max = Math.max(...data) * 1.1;
    const barW = (chartW / data.length) * 0.7;
    const gap = (chartW / data.length) * 0.3;

    // Grid
    ctx.strokeStyle = '#222222';
    ctx.lineWidth = 0.5;
    for (let i = 0; i <= 4; i++) {
        const y = padTop + (i / 4) * chartH;
        ctx.beginPath();
        ctx.moveTo(padLeft, y);
        ctx.lineTo(padLeft + chartW, y);
        ctx.stroke();
        const val = max - (i / 4) * max;
        ctx.fillStyle = '#555555';
        ctx.font = '10px SF Mono, monospace';
        ctx.textAlign = 'right';
        ctx.fillText(val.toFixed(0), padLeft - 8, y + 3);
    }

    // Bars
    data.forEach((v, i) => {
        const barH = (v / max) * chartH;
        const x = padLeft + i * (chartW / data.length) + gap / 2;
        const y = padTop + chartH - barH;

        const grad = ctx.createLinearGradient(0, y, 0, padTop + chartH);
        grad.addColorStop(0, color);
        grad.addColorStop(1, color + '44');
        ctx.fillStyle = grad;
        ctx.fillRect(x, y, barW, barH);

        // X label
        if (labels && (i % Math.ceil(data.length / 12) === 0 || i === data.length - 1)) {
            ctx.fillStyle = '#555555';
            ctx.font = '9px SF Mono, monospace';
            ctx.textAlign = 'center';
            ctx.fillText(labels[i], x + barW / 2, padTop + chartH + 14);
        }
    });
}

// Toggle handler
document.addEventListener('click', function(e) {
    if (e.target.closest('.toggle')) {
        const toggle = e.target.closest('.toggle');
        toggle.classList.toggle('on');
    }
});
