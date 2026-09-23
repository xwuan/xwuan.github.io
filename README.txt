══════════════════════════════════════════════
 SỔ ACC XWUAN — WEBSITE PHONG CÁCH NOTEBOOK RETRO
══════════════════════════════════════════════

▶ DEPLOY LÊN GITHUB PAGES
   1. Upload (push) toàn bộ 9 file .html lên repo xwuan.github.io
      (nhánh main, để ở thư mục gốc).
   2. Truy cập https://xwuan.github.io — chạy ngay, không cần build.
   Mỗi file HTML tự chứa toàn bộ font + hình vẽ (không cần thư mục images).

▶ CÁC TRANG (9)
   index.html            Trang chủ (bảng giá, Locket, Win/Office, FAQ…)
   capcut.html           CapCut Pro        (20k/7 ngày · 80k/30 ngày)
   canva.html            Canva Pro         (20k/30 ngày · 130k/năm)
   youtube.html          YouTube Premium   (40k/30 ngày)
   netflix.html          Netflix 4K UHD    (45k/30 ngày)
   google-ai.html        Google AI Pro     (60k/năm — không bảo hành)
   meitu.html            Meitu SVIP        (90k/30 ngày)
   locket.html           Locket Gold       (50k–180k)
   windows-pricing.html  Windows & Office  (80k–220k + combo)

▶ MUỐN SỬA GIÁ / NỘI DUNG VỀ SAU
   - Sửa nội dung trong pages_data.py và build.py
   - Chạy:  python3 build.py
   → Cả 9 trang tự động tạo lại, đồng bộ giao diện một lượt.
   (Hoặc sửa trực tiếp từng file .html cũng được.)

▶ THÔNG TIN LIÊN HỆ ĐÃ GẮN SẴN
   Zalo: 0822.307.662 (zalo.me/0822307662)
   Facebook: facebook.com/xwuan1
   TikTok: tiktok.com/@xwuan2
   → Muốn đổi số: tìm & thay "0822307662" trong mọi file .html
     (hoặc sửa trong shell.py rồi build lại).

▶ FILE GỐC
   shell.py       — khung giao diện (CSS + đầu/cuối trang dùng chung)
   pages_data.py  — nội dung từng trang
   build.py       — script ghép & tạo 9 trang
   fontface.css   — font viết tay tiếng Việt (base64, dùng offline được)
