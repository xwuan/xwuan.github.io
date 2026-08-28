const fs = require('fs');
const cssCode = '\n/* PREMIUM APPLE GLASSMORPHISM UPGRADES */\n' +
'.svc-card, .card, .pcard, .ptier, .combo { transition: transform 0.4s cubic-bezier(0.25, 1, 0.5, 1), box-shadow 0.4s ease, border-color 0.4s ease !important; }\n' +
'.svc-card:hover, .card:hover, .pcard:hover, .ptier:hover, .combo:hover { transform: translateY(-8px) scale(1.015) !important; box-shadow: 0 24px 48px rgba(0,0,0,0.5), 0 0 30px rgba(255,255,255,0.08) inset !important; border-color: rgba(255,255,255,0.3) !important; z-index: 10; }\n' +
'.btn, .btn-zalo, .p-btn, .cta-btn { transition: all 0.4s cubic-bezier(0.25, 1, 0.5, 1) !important; position: relative; overflow: hidden; }\n' +
'.btn:hover, .btn-zalo:hover, .p-btn:hover, .cta-btn:hover { transform: scale(1.05) translateY(-2px) !important; box-shadow: 0 10px 25px rgba(255,255,255,0.2), 0 0 15px rgba(255,255,255,0.1) inset !important; filter: brightness(1.1); }\n' +
'h1, h2, .section-title, .brand-name, .card-ttl { text-shadow: 0 4px 20px rgba(255,255,255,0.15); letter-spacing: -0.01em; }\n';

const files = ['index.html', 'youtube.html', 'capcut.html', 'google-ai.html', 'meitu.html', 'netflix.html', 'canva.html', 'locket.html', 'windows-pricing.html'];

for (const file of files) {
    if (!fs.existsSync(file)) continue;
    let content = fs.readFileSync(file, 'utf8');
    if (!content.includes('PREMIUM APPLE GLASSMORPHISM UPGRADES')) {
        content = content.replace('</style>', cssCode + '\n</style>');
        fs.writeFileSync(file, content, 'utf8');
        console.log('Injected premium CSS into ' + file);
    }
}