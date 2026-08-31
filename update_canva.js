const fs = require('fs');

let content = fs.readFileSync('canva.html', 'utf8');

// Add CSS for pricing-grid if missing
const pricingCSS = 
        .pricing-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
            gap: 16px;
            margin-bottom: 24px;
            margin-top: 16px;
        }
        .price-card {
            background: var(--card);
            border: 1px solid var(--border);
            border-radius: var(--r);
            padding: 16px;
            text-align: center;
            position: relative;
        }
        .price-card.best {
            background: linear-gradient(to bottom, var(--card), var(--card2));
            border-color: var(--accent);
            box-shadow: 0 4px 12px rgba(0, 212, 255, 0.15);
        }
        .badge-best {
            position: absolute;
            top: -10px;
            left: 50%;
            transform: translateX(-50%);
            background: linear-gradient(135deg, var(--accent), #0055ff);
            color: #fff;
            font-size: 11px;
            font-weight: 700;
            padding: 2px 8px;
            border-radius: 12px;
            white-space: nowrap;
        }
        .price-title {
            font-size: 15px;
            font-weight: 600;
            margin-bottom: 8px;
            color: var(--text);
        }
        .price-amount {
            font-size: 24px;
            font-weight: 700;
            font-family: 'Syne', sans-serif;
            color: var(--accent);
            margin-bottom: 4px;
        }
        .price-shield {
            font-size: 12px;
            color: var(--muted);
            margin-top: 8px;
        }
;
if (!content.includes('.pricing-grid {')) {
    content = content.replace('</style>', pricingCSS + '\n</style>');
}

// Replace the old pricing block
const oldBlock = <div class="card d-1 fi">
            <div class="price-box">
                <div class="price" data-price-key="canva">130k<span> / 1 năm</span></div>
                <div class="warranty">🛡️ Bảo hành full thời gian</div>
            </div>
        </div>;
const newBlock = <div class="pricing-grid obs-el fi" style="--delay: 0.1s">
            <div class="price-card">
                <div class="price-title">Gói 30 ngày</div>
                <div class="price-amount" data-price-key="canva_1m">20k</div>
                <div class="price-shield">🛡️ Bảo hành full thời gian</div>
            </div>
            <div class="price-card best">
                <div class="badge-best">Phổ biến nhất</div>
                <div class="price-title">Gói 1 Năm</div>
                <div class="price-amount" data-price-key="canva">130k</div>
                <div class="price-shield">🛡️ Bảo hành full thời gian</div>
            </div>
        </div>;

content = content.replace(oldBlock, newBlock);

fs.writeFileSync('canva.html', content, 'utf8');
console.log('Updated canva.html');