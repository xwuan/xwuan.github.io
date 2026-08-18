# 📦 HANDOVER — xwuan.github.io

> **Ngày bàn giao:** 2026-08-18
> **Người bàn giao:** AI Assistant (Antigravity / Claude)
> **Dự án:** Landing page dịch vụ kỹ thuật & phần mềm — Xuan Quyen
> **Domain:** https://ie1w3n.github.io/

---

## 1. CẤU TRÚC DỰ ÁN

```
xwuan.github.io-main/
│
├── index.html              # Trang chủ tổng hợp
├── windows-pricing.html    # Báo giá Windows & Office chi tiết
├── locket.html             # Locket Gold (Light Theme)
├── youtube.html            # YouTube Premium
├── netflix.html            # Netflix 4K UHD
├── capcut.html             # CapCut Pro
│
├── PROMPT-MASTER.md        # Master prompt gốc (cũ)
├── handover.md             # File này
├── claude.md               # Master prompt cập nhật (dùng thay PROMPT-MASTER.md)
│
└── images/
    ├── avatar.png          # Ảnh đại diện Xuan Quyen
    ├── canva.png           # Icon Canva Pro (mới thêm 2026-08-18)
    ├── capcut.png
    ├── facebook.png
    ├── locket.png
    ├── logowd.png / logowd2.png
    ├── netflix.png
    ├── office.png
    ├── windows.png / winghost.png
    ├── youtube.png
    └── zalo.png
```

---

## 2. THAY ĐỔI GẦN NHẤT (phiên 2026-08-18)

### 2.1 Cập nhật giá — Sale

| Dịch vụ | Giá cũ | Giá mới | File |
|---------|--------|---------|------|
| Netflix 4K UHD | 60k/tháng | **30k/tháng** 🔴SALE | index.html, netflix.html |
| CapCut Pro 30 ngày | 110k | **90k** 🔴SALE | index.html, capcut.html |

Giá gốc bị gạch hiển thị cùng badge SALE màu tương ứng brand.

### 2.2 Thêm dịch vụ mới — Canva Pro

- **Canva Pro 1 năm — 130k** thêm vào index.html
- Icon: images/canva.png (gradient teal→purple)
- CSS class: .ent-cv — màu brand #00c4cc → #7d2ae8
- Vị trí: cuối section "Tài khoản giải trí & sáng tạo"
- **Chưa có trang chi tiết canva.html** — cần tạo nếu muốn

### 2.3 Loại bỏ

- Nút "CHECK FEEDBACK KHÁCH IU" (link Google Drive) xóa khỏi 4 trang:
  netflix.html, capcut.html, youtube.html, locket.html

### 2.4 Tối ưu Mobile (toàn hệ thống)

| File | Fix chính |
|------|-----------|
| capcut.html | Pricing grid 2→1 cột <480px, font clamp, bảng scroll ngang, touch 50px |
| netflix.html | h1 clamp, bảng scroll, price clamp, nút min-height 50px |
| youtube.html | h1 2rem→clamp, vs-table scroll, pc-row wrap |
| windows-pricing.html | Cards/Combos 1 cột <600px, CTA stack dọc, repair flex-col |
| index.html | ent-grid minmax 220px→160px (fix iPhone 375px) |
| locket.html | Đã OK từ trước — không đổi |

---

## 3. TRẠNG THÁI HIỆN TẠI — GIÁ DỊCH VỤ

| Dịch vụ | Giá | Ghi chú |
|---------|-----|---------|
| Windows Chuẩn Microsoft | 150k – 180k | |
| Windows Tối Ưu | 100k – 120k | |
| Microsoft Office | 80k – 120k | |
| Combo Win Chuẩn + Office | 200k – 220k | Tiết kiệm ~30k |
| Combo Win Tối Ưu + Office | 160k – 180k | Tiết kiệm ~20k |
| Locket Gold (Quay 5s) | 50k/6th · 80k/1năm · 150k/∞ | |
| Locket Gold (Quay 15s) | 60k/6th · 100k/1năm · 180k/∞ | |
| YouTube Premium | 40k/tháng | |
| Netflix 4K UHD | ~~60k~~ → **30k/tháng** | 🔴 SALE |
| CapCut Pro 7 ngày | 20k | |
| CapCut Pro 30 ngày | ~~110k~~ → **90k** | 🔴 SALE |
| Canva Pro 1 năm | 130k | Mới thêm |

---

## 4. LIÊN HỆ & KÊNH

| Kênh | Thông tin |
|------|-----------|
| Zalo | 0822307662 · https://zalo.me/0822307662 |
| Facebook | https://www.facebook.com/xwuan1/ |
| Điện thoại | 0822.307.662 |

---

## 5. KỸ THUẬT — NOTES

### Stack
- Pure HTML + CSS + JS — không framework, không build tool
- Deploy: GitHub Pages tại https://ie1w3n.github.io/
- JS: chỉ dùng IntersectionObserver (fade-in, theme scroll) + new Date().getFullYear()

### Breakpoints đã áp dụng
- max-width: 600px → windows-pricing.html
- max-width: 480px → capcut, netflix, youtube
- max-width: 500px → index.html (svc-grid, locket-tiers)
- max-width: 420px → locket.html (pricing)
- max-width: 360px → breakpoint nhỏ nhất (fallback)

### Fonts (CDN Google Fonts)
- Be Vietnam Pro — nội dung mọi trang
- Syne 700/800 — tiêu đề Dark Theme
- Nunito 900 — tiêu đề Locket (Light Theme)

---

## 6. VIỆC CÒN TỒN ĐỌNG / TODO

- [ ] Tạo trang chi tiết canva.html (hiện Canva Pro chỉ link Zalo trực tiếp)
- [ ] Update footer year windows-pricing.html (hiện ghi cứng 2025)
- [ ] Test thực tế trên iPhone SE (375px) và Android nhỏ sau khi deploy

---

*Handover tự động tạo — 2026-08-18*
