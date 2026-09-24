══════════════════════════════════════════════════
 SỔ ACC XWUAN — BẢN QUYỂN SỔ LẬT TRANG (FLIPBOOK)
══════════════════════════════════════════════════

▶ ĐẶC ĐIỂM BẢN NÀY
   · Không còn cuộn trang dài — website là một QUYỂN SỔ thật sự:
     bìa trước → mục lục → các trang nội dung → bìa sau (liên hệ)
   · Lật trang giấy 3D:
       - Chạm/vào góc phải hay góc trái của sổ
       - Nút «trước / sau», phím mũi tên ←/→
       - Vuốt ngang (mobile)
       - Mục lục, tab dán cạnh sổ, nút tròn dưới đáy: tự lật/nhảy tới trang
   · Tự adapt màn hình:
       - Desktop (≥860px): sổ mở 2 trang như sách thật, lật quanh gáy giữa
       - Mobile (<860px): sổ 1 trang, lật quanh lò xo gáy trái
     Nội dung tự co giãn theo khổ giấy, không bao giờ tràn x
   · Nhảy xa (>2 trang): hiệu ứng fade nhanh nhẹ máy; nhảy gần: lật thật từng tờ
   · 📖 CHẠM ĐỂ MỞ SỔ: đứng ở bìa, chạm/kéo BẤT KỲ đâu trên bìa là sổ mở ra
     (kèm hiệu ứng «thở» nhẹ mời gọi + bắn pháo ✨⭐ lúc mở bìa lần đầu)
   · 🖐️ KÉO GÓC TRANG ĐỂ LẬT: bám góc phải/trái của sổ kéo bằng chuột hoặc
     ngón tay — tờ giấy quay theo tay thời gian thực; thả ra:
     kéo quá nửa trang (hoặc hất nhanh) → lật nốt, kéo nhẹ → đàn hồi về.
     Vuốt nhanh mọi nơi trên sổ vẫn lật trang như cũ. Click vào góc vẫn lật.
   · 🔊 ÂM THANH LẬT GIẤY: tiếng giấy «xoẹt» tổng hợp bằng Web Audio
     (không cần file âm thanh), nút 🔊/🔇 để bật–tắt, web nhớ lựa chọn của khách
   · 📖 NHỚ VỊ TRÍ ĐANG ĐỌC: khách đọc đến đâu, mở lại web tự mở đúng trang đó
     (kèm thông báo nhỏ «đã mở lại trang bạn đọc dở») — mỗi trang web nhớ riêng
   · Không JS: trang vẫn đọc được dạng danh sách (fallback noscript)

▶ DEPLOY LÊN GITHUB PAGES
   Push toàn bộ 9 file .html lên repo xwuan.github.io (nhánh main, thư mục gốc)
   → https://xwuan.github.io chạy ngay, không cần build, không cần thư mục images

▶ CÁC TRANG (9 FILE HTML)
   index.html            Trang chủ — quyển sổ tổng (bìa, giá, dịch vụ, FAQ…)
   capcut.html           CapCut Pro        20k/7 ngày · 80k/30 ngày
   canva.html            Canva Pro         20k/30 ngày · 130k/năm
   youtube.html          YouTube Premium   40k/30 ngày
   netflix.html          Netflix 4K UHD    45k/30 ngày
   google-ai.html        Google AI Pro     60k/năm (không BH)
   meitu.html            Meitu SVIP        90k/30 ngày
   locket.html           Locket Gold       50k–180k
   windows-pricing.html  Windows & Office  80k–220k + combo

▶ SỬA NỘI DUNG / GIÁ VỀ SAU
   - Giá & chữ: sửa trong pages_data.py
   - Giao diện khung sổ, hiệu ứng: sửa trong shell.py
   - Chạy: python3 build.py → cả 9 trang tự tạo lại đồng bộ
   (Hoặc sửa thẳng từng file .html cũng được.)

▶ LIÊN HỆ ĐÃ GẮN SẴN (trên bìa sau mọi quyển sổ)
   Zalo: 0822.307.662 · Facebook: xwuan1 · TikTok: @xwuan2
   Đổi số Zalo: tìm & thay "0822307662" trong các file .html
   (hoặc sửa trong shell.py + pages_data.py rồi build lại)

▶ ẢNH FEEDBACK KHÁCH HÀNG (trang chủ, mặt "Feedback khách hàng")
   · Đã có 3 ảnh MẪU (có đóng dấu MẪU) trong thư mục images/
   · Thay bằng ảnh feedback thật: chỉ cần chép đè lên
       images/fb1.jpg · images/fb2.jpg · images/fb3.jpg
     (khung ngang ~640px là đẹp nhất; thiếu ảnh sẽ tự hiện khung nhắc thay ảnh)
   · Ảnh phải hoặc mất mạng: khung tự chuyển thành chỗ trống, không vỡ giao diện

▶ NÚT ZALO NỔI (mobile)
   · Trên màn hình < 860px tự hiện nút tròn màu Zalo góc phải
   · Bấm là mở thẳng chat Zalo 0822.307.662

▶ CẤU TRÚC FILE GỐC
   shell.py        khung sổ + engine lật trang (CSS/JS dùng chung)
   pages_data.py   nội dung các mặt giấy của 9 trang
   build.py        script ghép & xuất 9 trang
   fontface.css    font viết tay tiếng Việt (base64 — dùng offline)
