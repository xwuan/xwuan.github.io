const fs = require('fs');

let handover = fs.readFileSync('handover.md', 'utf8');

const handoverUpdates = 
## 7. NHẬT KÝ SỬA LỖI & TIẾN TRÌNH (2026-08-28)

- [x] Fix lỗi opacity xếp chồng khiến nền trang chủ bị đen thui.
- [x] Sửa lỗi màu CSS timeline (đường dọc + chấm tròn) bị dính viền xám trên nền Glassmorphism.
- [x] Fix lỗi cú pháp CSS \@keyframes\ làm vỡ layout \.wrap\ bung toàn màn hình.
- [x] Khôi phục nền họa tiết (grid/dots) nguyên thủy và thả các emoji bay lượn cho trang chi tiết.
- [x] Fix lỗi nền trắng trên trang \locket.html\ khiến văn bản bị tàng hình.
- [x] Khắc phục thông tin bảng so sánh Locket Gold (Thời lượng quay 5s/15s, Bỏ quảng cáo).
- [x] Thêm hiệu ứng cuộn Fade-in (IntersectionObserver) mượt mà cho toàn bộ các trang chi tiết.

## 8. QUY TẮC LÀM VIỆC (WORKFLOW RULES)
🚨 **LUÔN TUÂN THỦ:**
1. **Sửa, fix lỗi bug:** Phải cập nhật tiến trình vào file \handover.md\.
2. **Sửa lối thiết kế, thêm bớt nội dung:** Phải cập nhật hướng dẫn vào file \gemini.md\.
3. **Quy trình:** LUÔN cập nhật Document -> Commit -> Push code.
;

if (!handover.includes('NHẬT KÝ SỬA LỖI')) {
    handover = handover + '\n' + handoverUpdates;
    fs.writeFileSync('handover.md', handover, 'utf8');
    console.log('Updated handover.md');
}

let gemini = fs.readFileSync('gemini.md', 'utf8');

const geminiDesignUpdates = 

### 4. LỐI THIẾT KẾ ĐỔI MỚI (APPLE GLASSMORPHISM)
- **Giao diện cốt lõi:** Áp dụng triệt để phong cách Apple Glassmorphism.
- **Thẻ nội dung (Cards):** Kính mờ (Frost Glass), viền bo tròn mạnh (\order-radius: 24px\), đổ bóng mềm mại (soft shadow). Màu nền thường là \gba(255, 255, 255, 0.05)\ kết hợp \ackdrop-filter: blur(40px)\.
- **Nút bấm (Buttons):** Hình viên thuốc (\order-radius: 99px\), phản hồi chạm lò xo (\cubic-bezier(0.25, 1, 0.5, 1)\).
- **Phông nền (Background):**
  - Trang chủ (\index.html\): Cực quang (Aurora) Gradient chuyển động chìm cực kỳ tinh tế, tối màu (\#050505\ kết hợp \#11091a\) kèm lưới (grid/dots) động thay đổi theo section.
  - Trang chi tiết: Giữ nguyên phông nền lưới/dots nguyên thủy (đậm chất note), emoji bay lượn, kết hợp với các thẻ kính mờ nổi bật ở trên. Trang \locket.html\ dùng dải màu Tím thẫm - Đen sâu.
- **Hiệu ứng cuộn:** Sử dụng \IntersectionObserver\ lặp lại liên tục. Vuốt lên/xuống thì các thẻ (\.fi\) sẽ mờ dần và trượt lên (\ade-in\ / \	ranslateY\).

### 5. QUY TẮC LÀM VIỆC (WORKFLOW RULES)
🚨 **LUÔN TUÂN THỦ:**
1. **Sửa, fix lỗi bug:** Phải cập nhật tiến trình vào file \handover.md\.
2. **Sửa lối thiết kế, thêm bớt nội dung:** Phải cập nhật hướng dẫn vào file \gemini.md\.
3. **Quy trình:** LUÔN cập nhật Document -> Commit -> Push code.
;

if (!gemini.includes('APPLE GLASSMORPHISM')) {
    gemini = gemini + geminiDesignUpdates;
    fs.writeFileSync('gemini.md', gemini, 'utf8');
    console.log('Updated gemini.md');
}