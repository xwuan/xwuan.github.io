const fs = require('fs');

const vsTableHTML = '<div class="card fi" style="margin-top: 14px;">' +
'    <div class="card-head">' +
'      <div class="card-ico" style="background: linear-gradient(135deg, #f59e0b, #fbbf24);">🏆</div>' +
'      <div class="card-ttl" style="color: #fbbf24;">Locket Thường vs Locket Gold</div>' +
'    </div>' +
'    <div style="overflow-x: auto; -webkit-overflow-scrolling: touch;">' +
'      <table class="vs-table">' +
'        <tr>' +
'          <th>Tính năng</th>' +
'          <th>Free 😴</th>' +
'          <th style="color:#fbbf24">Gold ✨</th>' +
'        </tr>' +
'        <tr>' +
'          <td>Quảng cáo</td>' +
'          <td>Chèn quảng cáo</td>' +
'          <td>🚫 Không quảng cáo</td>' +
'        </tr>' +
'        <tr>' +
'          <td>Video Locket</td>' +
'          <td>Giới hạn</td>' +
'          <td>Video 5s hoặc 15s</td>' +
'        </tr>' +
'        <tr>' +
'          <td>Tải ảnh từ thư viện</td>' +
'          <td>Chỉ chụp trực tiếp</td>' +
'          <td>Tải mọi ảnh từ máy</td>' +
'        </tr>' +
'        <tr>' +
'          <td>Biểu tượng App</td>' +
'          <td>Mặc định</td>' +
'          <td>Nhiều Icon tùy chỉnh</td>' +
'        </tr>' +
'        <tr>' +
'          <td>Huy hiệu Gold</td>' +
'          <td>Không có</td>' +
'          <td>Huy hiệu đặc quyền</td>' +
'        </tr>' +
'      </table>' +
'    </div>' +
'  </div>';

let content = fs.readFileSync('locket.html', 'utf8');

// Use regex to replace the table container entirely
content = content.replace(/<div class="card fi" style="margin-top: 14px;">[\s\S]*?<\/table>\s*<\/div>\s*<\/div>/, vsTableHTML);

fs.writeFileSync('locket.html', content, 'utf8');
console.log('Fixed locket table');