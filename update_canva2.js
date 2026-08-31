const fs = require('fs');

let content = fs.readFileSync('canva.html', 'utf8');

const pricingCSS = 
"        .pricing-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 16px; margin-bottom: 24px; margin-top: 16px; }\n" +
"        .price-card { background: var(--card); border: 1px solid var(--border); border-radius: var(--r); padding: 16px; text-align: center; position: relative; }\n" +
"        .price-card.best { background: linear-gradient(to bottom, var(--card), var(--card2)); border-color: var(--accent); box-shadow: 0 4px 12px rgba(0, 212, 255, 0.15); }\n" +
"        .badge-best { position: absolute; top: -10px; left: 50%; transform: translateX(-50%); background: linear-gradient(135deg, var(--accent), #0055ff); color: #fff; font-size: 11px; font-weight: 700; padding: 2px 8px; border-radius: 12px; white-space: nowrap; }\n" +
"        .price-title { font-size: 15px; font-weight: 600; margin-bottom: 8px; color: var(--text); }\n" +
"        .price-amount { font-size: 24px; font-weight: 700; font-family: 'Syne', sans-serif; color: var(--accent); margin-bottom: 4px; }\n" +
"        .price-shield { font-size: 12px; color: var(--muted); margin-top: 8px; }\n";

if (!content.includes('.pricing-grid {')) {
    content = content.replace('</style>', pricingCSS + '</style>');
}

// Find the start of the card d-1 fi block and the end
const oldHtml = '<div class="card d-1 fi">\n            <div class="price-box">\n                <div class="price" data-price-key="canva">130k<span> / 1 năm</span></div>\n                <div class="warranty">🛡️ Bảo hành full thời gian</div>\n            </div>\n        </div>';

const newHtml = '<div class="pricing-grid obs-el fi" style="--delay: 0.1s">\n            <div class="price-card">\n                <div class="price-title">Gói 30 ngày</div>\n                <div class="price-amount" data-price-key="canva_1m">20k</div>\n                <div class="price-shield">🛡️ Bảo hành full thời gian</div>\n            </div>\n            <div class="price-card best">\n                <div class="badge-best">Phổ biến nhất</div>\n                <div class="price-title">Gói 1 Năm</div>\n                <div class="price-amount" data-price-key="canva">130k</div>\n                <div class="price-shield">🛡️ Bảo hành full thời gian</div>\n            </div>\n        </div>';

content = content.replace(oldHtml, newHtml);

fs.writeFileSync('canva.html', content, 'utf8');
console.log('Updated canva.html successfully!');