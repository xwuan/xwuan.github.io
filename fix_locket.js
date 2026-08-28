const fs = require('fs');

const vsTableHTML = 
  <div class="card fi" style="margin-top: 14px;">
    <div class="card-head">
      <div class="card-ico" style="background: linear-gradient(135deg, #f59e0b, #fbbf24);">??</div>
      <div class="card-ttl" style="color: #fbbf24;">Locket Thu?ng vs Locket Gold</div>
    </div>
    <div style="overflow-x: auto; -webkit-overflow-scrolling: touch;">
      <table class="vs-table">
        <tr>
          <th>Tính nang</th>
          <th>Free ??</th>
          <th style="color:#fbbf24">Gold ?</th>
        </tr>
        <tr>
          <td>T?i ?nh t? thu vi?n</td>
          <td>Ch? ch?p tr?c ti?p</td>
          <td>T?i m?i ?nh t? máy</td>
        </tr>
        <tr>
          <td>Video Locket</td>
          <td>Gi?i h?n</td>
          <td>Lên t?i 5 phút</td>
        </tr>
        <tr>
          <td>Bi?u tu?ng App</td>
          <td>M?c d?nh</td>
          <td>Nhi?u Icon tùy ch?nh</td>
        </tr>
        <tr>
          <td>Huy hi?u Gold</td>
          <td>Không có</td>
          <td>Huy hi?u d?c quy?n</td>
        </tr>
        <tr>
          <td>L?ch s? ?nh</td>
          <td>H?n ch?</td>
          <td>Xem l?i toàn b?</td>
        </tr>
      </table>
    </div>
  </div>
;

const vsTableCSS = 
/* Comparison Table */
.vs-table { width: 100%; border-collapse: separate; border-spacing: 0; font-size: 0.9rem; min-width: 280px; }
.vs-table th, .vs-table td { padding: 12px 8px; border-bottom: 1px solid rgba(255,255,255,0.1); text-align: left; }
.vs-table th { font-weight: 600; color: #a1a1aa; }
.vs-table td:nth-child(2) { color: #a1a1aa; width: 35%; }
.vs-table td:nth-child(3) { color: #fcd34d; font-weight: 500; width: 35%; }
.vs-table tr:last-child th, .vs-table tr:last-child td { border-bottom: none; }
@media (max-width: 420px) {
  .vs-table { font-size: 13px; }
  .vs-table th, .vs-table td { padding: 9px 6px; }
}
;

let content = fs.readFileSync('locket.html', 'utf8');

// Replace background with a rich dark purple gradient instead of pure black
content = content.replace(/body\s*\{\s*background:\s*#[0-9a-fA-F]+\s*!important;/g, "body { background: linear-gradient(135deg, #1e1332 0%, #0c0814 100%) !important;");

// Inject table CSS if not present
if (!content.includes('.vs-table')) {
    content = content.replace('/* FADE-IN ANIMATION */', vsTableCSS + '\n/* FADE-IN ANIMATION */');
}

// Inject table HTML before the COMMITMENT card
if (!content.includes('Locket Thu?ng vs Locket Gold')) {
    content = content.replace('<!-- COMMITMENT -->', vsTableHTML + '\n  <!-- COMMITMENT -->');
}

fs.writeFileSync('locket.html', content);
console.log('Fixed locket.html');
