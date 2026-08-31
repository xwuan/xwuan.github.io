const fs = require('fs');

let content = fs.readFileSync('canva.html', 'utf8');

const newHtml = '<div class="pricing-grid obs-el fi" style="--delay: 0.1s">\n            <div class="price-card">\n                <div class="price-title">Gói 30 ngày</div>\n                <div class="price-amount" data-price-key="canva_1m">20k</div>\n                <div class="price-shield">🛡️ Bảo hành full thời gian</div>\n            </div>\n            <div class="price-card best">\n                <div class="badge-best">Phổ biến nhất</div>\n                <div class="price-title">Gói 1 Năm</div>\n                <div class="price-amount" data-price-key="canva">130k</div>\n                <div class="price-shield">🛡️ Bảo hành full thời gian</div>\n            </div>\n        </div>';

content = content.replace(/<div class="card d-1 fi">\s*<div class="price-box">\s*<div class="price" data-price-key="canva">130k<span> \/ 1 năm<\/span><\/div>\s*<div class="warranty">🛡️ Bảo hành full thời gian<\/div>\s*<\/div>\s*<\/div>/, newHtml);

fs.writeFileSync('canva.html', content, 'utf8');
console.log('Updated canva.html with Regex!');