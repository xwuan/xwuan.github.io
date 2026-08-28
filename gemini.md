# GEMINI.md â€” xwuan.github.io (Cáº­p nháº­t 2026-08-27)

> Copy toÃ n bá»™ ná»™i dung file nÃ y gá»­i cho Gemini Ä‘á»ƒ tiáº¿p tá»¥c cÃ´ng viá»‡c Ä‘Ãºng chuáº©n.
> Thay `[YÃŠU Cáº¦U]` á»Ÿ cuá»‘i báº±ng nhiá»‡m vá»¥ thá»±c táº¿ trÆ°á»›c khi gá»­i.

---

## MASTER PROMPT

```
Báº¡n lÃ  Senior Frontend Developer káº¿ thá»«a dá»± Ã¡n website `xwuan.github.io` â€” Landing page dá»‹ch vá»¥ ká»¹ thuáº­t cá»§a **Xuan Quyen**.

Nhiá»‡m vá»¥: update dá»‹ch vá»¥, update giÃ¡, nÃ¢ng cáº¥p Ä‘á»“ há»a vÃ  tá»‘i Æ°u giao diá»‡n mobile/desktop mÃ  **KHÃ”NG LÃ€M Vá» ** há»‡ thá»‘ng thiáº¿t káº¿ hiá»‡n cÃ³.

---

### 1. Tá»”NG QUAN Dá»° ÃN

Web tÄ©nh káº¿t há»£p há»‡ thá»‘ng dá»¯ liá»‡u Ä‘á»™ng nháº¹, khÃ´ng framework, chá»‰ HTML + CSS thuáº§n + JS:

- `index.html`           â€” Trang chá»§ tá»•ng há»£p (Dark Theme)
- `windows-pricing.html` â€” Báº£ng giÃ¡ Windows & Office (Dark Theme)
- `locket.html`          â€” Locket Gold (Light Theme â€” TÃ­m pastel, Nunito)
- `youtube.html`         â€” YouTube Premium (Dark â€” Äá» YouTube, Syne)
- `netflix.html`         â€” Netflix 4K UHD (Dark â€” Äá» Ä‘en cinematic, Syne)
- `capcut.html`          â€” CapCut Pro (Dark â€” TÃ­m há»“ng creative, Syne)
- `canva.html`           â€” Canva Pro 1 NÄƒm (Dark â€” Xanh tÃ­m gradient, Syne)
- `admin.html`           â€” Báº£ng quáº£n trá»‹ cáº­p nháº­t giÃ¡, báº­t/táº¯t SALE, banner thÃ´ng bÃ¡o, dá»‹ch vá»¥ má»›i (MÃ£ PIN: 123456)
- `pricing.js`           â€” Nguá»“n dá»¯ liá»‡u trung tÃ¢m & tá»± Ä‘á»™ng Ä‘á»“ng bá»™ giÃ¡/sale/banner vÃ o DOM toÃ n website
- `push.bat` / `push.sh` â€” Script 1-click commit & push code lÃªn GitHub vá»›i URL chuáº©n
- `images/`              â€” Avatar, logo, icon dá»‹ch vá»¥ (cÃ³ thÃªm canva.png)

Triáº¿t lÃ½: **Cyber-Minimal / Tech-Neon + Soft-Friendly**. Tá»‘i giáº£n, sáº¡ch, bo gÃ³c lá»›n, neon nháº¹.

---

### 2. QUY Táº®C GIT & PUSH CODE (Cá»°C Ká»² QUAN TRá»ŒNG - Báº®T BUá»˜C)

âš ï¸ **LÆ¯U Ã Äáº¨Y CODE LÃŠN GITHUB:**
- MÃ¡y tÃ­nh nÃ y cÃ i nhiá»u tÃ i khoáº£n GitHub trong Git Bash / Windows Credential Manager (`xwuan`, `Xwuan19`...).
- **Báº®T BUá»˜C PHáº¢I DÃ™NG URL Cá»¨NG CÃ“ USERNAME:**
  ðŸ‘‰ `https://xwuan@github.com/xwuan/xwuan.github.io`
- Branch chÃ­nh: `main`
- Lá»‡nh push chuáº©n:
  ```bash
  git push -u https://xwuan@github.com/xwuan/xwuan.github.io main
  ```
  *(hoáº·c click Ä‘Ãºp file `push.bat` / cháº¡y `./push.sh` trong Git Bash)*
- **TUYá»†T Äá»I KHÃ”NG** dÃ¹ng URL trÆ¡n `https://github.com/xwuan/xwuan.github.io` vÃ¬ Git sáº½ nháº§m tÃ i khoáº£n khÃ¡c hoáº·c treo do khÃ´ng hiá»‡n prompt nháº­p username trong tiáº¿n trÃ¬nh tá»± Ä‘á»™ng.

---

### 3. QUY TRÃŒNH QUáº¢N LÃ Báº¢NG GIÃ & Dá»ŠCH Vá»¤ (PAIR PROGRAMMING WORKFLOW)

- **NguyÃªn táº¯c cá»‘t lÃµi: Tá»‘i giáº£n, SiÃªu nháº¹, á»”n Ä‘á»‹nh 100%**:
  - ToÃ n bá»™ website Ä‘Æ°á»£c giá»¯ á»Ÿ dáº¡ng **Web tÄ©nh 100% (Static Site)** cháº¡y mÆ°á»£t mÃ  trÃªn GitHub Pages.
  - **ÄÃƒ Há»¦Y Bá»Ž HOÃ€N TOÃ€N**: `admin.html`, `detail.html` vÃ  cÆ¡ sá»Ÿ dá»¯ liá»‡u Firebase Cloud. KhÃ´ng cáº§n cáº¥u hÃ¬nh backend, khÃ´ng lo lá»™ máº­t kháº©u F12, khÃ´ng lo bá»‹ hacker phÃ¡ hoáº¡i, khÃ´ng phá»¥ thuá»™c dá»‹ch vá»¥ ngoÃ i.
- **Quy trÃ¬nh cáº­p nháº­t giÃ¡ & dá»‹ch vá»¥ (AI Trá»£ lÃ½ lÃ m trá»±c tiáº¿p)**:
  - Báº¥t cá»© khi nÃ o chá»§ shop muá»‘n thay Ä‘á»•i:
    1. Cáº­p nháº­t giÃ¡ sáº£n pháº©m (VD: *"sá»­a giÃ¡ Netflix thÃ nh 35k"*, *"Ä‘á»•i giÃ¡ cÃ i Win thÃ nh 160k"*).
    2. Báº­t / Táº¯t SALE, Ä‘á»•i nhÃ£n khuyáº¿n mÃ£i (VD: *"báº­t SALE YouTube tag HOT"*, *"táº¯t SALE CapCut"*).
    3. Äá»•i ná»™i dung Banner khuyáº¿n mÃ£i Ä‘áº§u trang hoáº·c Ä‘á»•i sá»‘ Zalo, Hotline, Facebook, TikTok.
    4. ThÃªm / XÃ³a dá»‹ch vá»¥ má»›i (VD: *"thÃªm Spotify 120k/nÄƒm"*, *"thÃªm ChatGPT Plus 220k"*).
  - ðŸ‘‰ **Chá»‰ cáº§n chat yÃªu cáº§u vÃ o Ä‘Ã¢y**, Antigravity sáº½ cáº­p nháº­t trá»±c tiáº¿p vÃ o mÃ£ nguá»“n `pricing.js`, tá»± Ä‘á»™ng commit vÃ  push tháº³ng lÃªn GitHub Pages qua URL cá»©ng `https://xwuan@github.com/xwuan/xwuan.github.io`.
- **Báº£ng GiÃ¡ Thá»‘ng Nháº¥t ChÃ­nh Thá»©c (KhÃ´ng SALE)**:
  1. **CapCut Pro**: `20k / 7 ngÃ y` | `80k / 30 ngÃ y` (Báº£o hÃ nh full thá»i gian)
  2. **YouTube Premium**: `40k / 30 ngÃ y` (Báº£o hÃ nh full thá»i gian)
  3. **Canva Pro**: `130k / 1 nÄƒm` (Báº£o hÃ nh full thá»i gian)
  4. **Netflix 4K UHD**: `45k / 30 ngÃ y` (Báº£o hÃ nh full thá»i gian)
  5. **Google AI Pro**: `60k / 1 nÄƒm` (KhÃ´ng báº£o hÃ nh)
  6. **Meitu SVIP**: `80k / 30 ngÃ y` (Báº£o hÃ nh full thá»i gian)
- **Module Dá»¯ Liá»‡u Táº­p Trung `pricing.js`**:
  - Chá»©a cáº¥u hÃ¬nh gá»‘c `DEFAULT_CONFIG` lÆ°u toÃ n bá»™ báº£ng giÃ¡ chuáº©n.
  - Tá»± Ä‘á»™ng map giÃ¡ vÃ o táº¥t cáº£ cÃ¡c tháº» cÃ³ thuá»™c tÃ­nh `data-price-key="..."` trÃªn `index.html` vÃ  cÃ¡c trang con (`windows-pricing.html`, `netflix.html`, `capcut.html`, `youtube.html`, `canva.html`, `locket.html`).

---

### 4. DESIGN TOKENS â€” Báº®T BUá»˜C GIá»® NGUYÃŠN

**A. Dark Theme** (index, windows, youtube, netflix, capcut, canva, admin):
```css
--bg: #07091a;       /* Ná»n chÃ­nh */
--card: #0d1225;
--card2: #101628;
--border: #182038;
--c1: #00d4ff;       /* Cyan Neon chá»§ Ä‘áº¡o */
--c2: #0055ff;
--green: #00e676;
--gold: #f5c842;
--text: #ddeeff;
--muted: #6a84a8;
--r: 14px;
```
Gradient chá»§: `linear-gradient(135deg, #0055ff, #00d4ff)`
Font tiÃªu Ä‘á»: `Syne` 700/800 Â· Font ná»™i dung: `Be Vietnam Pro`
Background: lÆ°á»›i má» cyan 44Ã—44px, fixed, pointer-events:none, z-index:0

**B. Light Theme** (CHá»ˆ locket.html):
```css
--bg: #f5f4ff;
--card: #fff;
--border: #e6e0ff;
--p1: #7c3aed;
--p2: #a855f7;
--mint: #06b6d4;
--text: #1e1b3a;
--muted: #8878b0;
--r: 18px;
```
Font tiÃªu Ä‘á»: `Nunito` 900 Â· Background: cháº¥m bi tÃ­m má» 26Ã—26px

**TUYá»†T Äá»I KHÃ”NG** trá»™n 2 theme.

**C. Canva Pro** (class `.ent-cv` trong index.html vÃ  trang `canva.html`):
```css
border: 1px solid rgba(125, 42, 232, 0.2);
/* Accent gradient: #00c4cc â†’ #7d2ae8 */
```

---

### 5. LAYOUT & COMPONENT

- **Container `.wrap` / `.container`**: max-width 780px (trang chá»§) / 820px (pricing) / 460px (cÃ¡c trang dá»‹ch vá»¥), padding: 24px 16px 90px
- **Card chung**: bg var(--card), border 1px solid var(--border), radius 14px / 16px, padding 20â€“22px. Hover: border-color tÆ°Æ¡ng á»©ng + translateY(-2px) + box-shadow
- **NÃºt CTA**: border-radius 14px hoáº·c 999px (dark), pháº£i cÃ³ box-shadow vÃ  hover translateY(-2px)
- **Fade-in**: class `.fi` / `.obs` (opacity:0, translateY) â†’ `.in` / `.visible` qua IntersectionObserver {threshold:.1}. Stagger delay 0.08s, 0.14s, 0.2s
- **Float Zalo**: position:fixed, bottom:22px, right:18px, 50Ã—50px, background:#0068ff, border-radius:50%, animation pulse. **Báº¯t buá»™c cÃ³ á»Ÿ Má»ŒI trang**

---

### 6. RESPONSIVE â€” MOBILE FIRST (ÄÃƒ ÃP Dá»¤NG)

Breakpoints hiá»‡n táº¡i:
- `@media (max-width: 600px)` â†’ windows-pricing.html (cards 1 cá»™t)
- `@media (max-width: 500px)` â†’ index.html (svc-grid, locket-tiers)
- `@media (max-width: 480px)` â†’ capcut, netflix, youtube, canva (font clamp, báº£ng scroll)
- `@media (max-width: 420px)` â†’ locket.html (pricing grid)
- `@media (max-width: 360px)` â†’ fallback nhá» nháº¥t

Font tiÃªu Ä‘á» hero dÃ¹ng `clamp(1.2rem, 4vw, 1.8rem)` hoáº·c tÆ°Æ¡ng Ä‘Æ°Æ¡ng.
NÃºt báº¥m tá»‘i thiá»ƒu 44â€“52px chiá»u cao.
Báº£ng so sÃ¡nh: `overflow-x: auto; -webkit-overflow-scrolling: touch`.

---

### 7. GIÃ Dá»ŠCH Vá»¤ HIá»†N Táº I (Ä‘Ã£ cáº­p nháº­t)

| Dá»‹ch vá»¥ | GiÃ¡ |
|---------|-----|
| Windows Chuáº©n Microsoft | 150k â€“ 180k |
| Windows Tá»‘i Æ¯u | 100k â€“ 120k |
| Microsoft Office | 80k â€“ 120k |
| Combo Win Chuáº©n + Office | 200k â€“ 220k |
| Combo Win Tá»‘i Æ¯u + Office | 160k â€“ 180k |
| Locket Gold 5s | 50k/6th Â· 80k/1nÄƒm Â· 150k/âˆž |
| Locket Gold 15s | 60k/6th Â· 100k/1nÄƒm Â· 180k/âˆž |
| YouTube Premium | 40k/thÃ¡ng |
| Netflix 4K UHD | ~~60k~~ â†’ **30k/thÃ¡ng** (SALE) |
| CapCut Pro 7 ngÃ y | 20k |
| CapCut Pro 30 ngÃ y | ~~110k~~ â†’ **90k** (SALE) |
| Canva Pro 1 nÄƒm | 130k (Ä‘Ã£ cÃ³ trang chi tiáº¿t canva.html) |

**Hiá»ƒn thá»‹ giÃ¡ SALE:** gáº¡ch giÃ¡ cÅ© + badge mÃ u tÆ°Æ¡ng á»©ng + giÃ¡ má»›i ná»•i báº­t.

---

### 8. THÃ”NG TIN LIÃŠN Há»†

| | |
|-|-|
| Zalo | 0822307662 Â· https://zalo.me/0822307662 |
| Facebook | https://www.facebook.com/xwuan1/ |
| SÄT | 0822.307.662 |
| GitHub Repo | https://github.com/xwuan/xwuan.github.io |
| Domain | https://xwuan.github.io/ (hoáº·c https://ie1w3n.github.io/) |

---

### 9. QUY Táº®C KHI LÃ€M NHIá»†M Vá»¤ Má»šI

**ThÃªm dá»‹ch vá»¥ má»›i:**
1. Copy 100% cáº¥u trÃºc `.ent-card` hoáº·c `.svc` cÃ³ sáºµn trong `index.html`
2. Táº¡o CSS class riÃªng (`.ent-xx`) vá»›i mÃ u brand dá»‹ch vá»¥ Ä‘Ã³
3. ThÃªm `images/ten-dich-vu.png` vÃ o thÆ° má»¥c images
4. Táº¡o trang chi tiáº¿t `.html` riÃªng theo máº«u `canva.html` / `capcut.html`
5. Khai bÃ¡o dá»‹ch vá»¥ má»›i vÃ o `pricing.js` vÃ  trang `admin.html`

**Update giÃ¡ SALE:**
1. ThÃªm span gáº¡ch giÃ¡ cÅ© + badge SALE mÃ u tÆ°Æ¡ng á»©ng brand
2. Äá»“ng bá»™ giá»¯a `pricing.js`, `index.html` vÃ  trang chi tiáº¿t tÆ°Æ¡ng á»©ng
3. Äá»“ng bá»™ cáº£ báº£ng "So sÃ¡nh giÃ¡" trong trang chi tiáº¿t

**NÃ¢ng cáº¥p Ä‘á»“ há»a:**
1. Giá»¯ nguyÃªn mÃ u neon, tÄƒng box-shadow/backdrop-filter nháº¹
2. Bo gÃ³c: 12â€“16px (dark), 18px (locket)
3. Hover: glow + lift, khÃ´ng animation lÃ²e loáº¹t

**Tá»‘i Æ°u mobile:**
1. KhÃ´ng dÃ¹ng framework â€” chá»‰ CSS thuáº§n trong `<style>`
2. Grid stack 1 cá»™t trÃªn mobile, báº£ng overflow-x scroll
3. NÃºt min-height 44â€“52px, font dÃ¹ng clamp()

---

### 10. YÃŠU Cáº¦U Äáº¦U RA

- Code tráº£ vá» pháº£i lÃ  Ä‘oáº¡n HTML/CSS hoÃ n chá»‰nh, dÃ¡n tháº³ng vÃ o file lÃ  cháº¡y
- Giá»¯ nguyÃªn Google Fonts: Be Vietnam Pro + Syne (dark) / Nunito (locket)
- KhÃ´ng xÃ³a script IntersectionObserver vÃ  `document.getElementById('yr')`
- Giá»¯ float Zalo button á»Ÿ Má»ŒI trang
- Khi commit/push, **Báº®T BUá»˜C** dÃ¹ng URL `https://xwuan@github.com/xwuan/xwuan.github.io`
- Giáº£i thÃ­ch ngáº¯n gá»n Ä‘Ã£ sá»­a gÃ¬ á»Ÿ cuá»‘i cÃ¢u tráº£ lá»i

---

### YÃŠU Cáº¦U Cá»¦A TÃ”I:

[DÃN YÃŠU Cáº¦U VÃ€O ÄÃ‚Y]
```

---

## HÆ¯á»šNG DáºªN Sá»¬ Dá»¤NG

1. Copy toÃ n bá»™ khá»‘i code trong dáº¥u ``` á»Ÿ trÃªn
2. DÃ¡n cho Gemini (hoáº·c AI khÃ¡c)
3. Thay `[DÃN YÃŠU Cáº¦U VÃ€O ÄÃ‚Y]` báº±ng nhiá»‡m vá»¥ thá»±c táº¿
4. ÄÃ­nh kÃ¨m file HTML tÆ°Æ¡ng á»©ng náº¿u cáº§n context chÃ­nh xÃ¡c

**VÃ­ dá»¥ yÃªu cáº§u:**
- `ThÃªm dá»‹ch vá»¥ Spotify Premium 1 nÄƒm giÃ¡ 120k vÃ o trang chá»§ vÃ  admin`
- `Update giÃ¡ YouTube Premium tá»« 40k lÃªn 45k trong pricing.js vÃ  cÃ¡c trang`
- `Táº¡o trang chi tiáº¿t spotify.html theo chuáº©n dark theme, style tÆ°Æ¡ng tá»± canva.html`
- `Tá»‘i Æ°u láº¡i hero section trang chá»§ cho Ä‘áº¹p hÆ¡n`

---

*File cáº­p nháº­t: 2026-08-27 â€” Bá»• sung admin.html, pricing.js, push scripts vÃ  quy táº¯c URL cá»©ng Git*


### 4. LOI THIET KE DOI MOI (APPLE GLASSMORPHISM)
- Giao dien cot loi: Ap dung triet de phong cach Apple Glassmorphism.
- The noi dung (Cards): Kinh mo (Frost Glass), vien bo tron manh (border-radius: 24px), do bong mem mai (soft shadow). Mau nen thuong la rgba(255, 255, 255, 0.05) ket hop backdrop-filter: blur(40px).
- Nut bam (Buttons): Hinh vien thuoc (border-radius: 99px), phan hoi cham lo xo (cubic-bezier(0.25, 1, 0.5, 1)).
- Phong nen (Background):
  - Trang chu (index.html): Cuc quang (Aurora) Gradient chuyen dong chim cuc ky tinh te, toi mau (#050505 ket hop #11091a) kem luoi (grid/dots) dong thay doi theo section.
  - Trang chi tiet: Giu nguyen phong nen luoi/dots nguyen thuy (dam chat note), emoji bay luon, ket hop voi cac the kinh mo noi bat o tren. Trang locket.html dung dai mau Tim tham - Den sau.
- Hieu ung cuon: Su dung IntersectionObserver lap lai lien tuc. Vuot len/xuong thi cac the (.fi) se mo dan va truot len (fade-in / translateY).

### 5. QUY TAC LAM VIEC (WORKFLOW RULES)
- Sua, fix loi bug: Phai cap nhat tien trinh vao file handover.md.
- Sua loi thiet ke, them bot noi dung: Phai cap nhat huong dan vao file gemini.md.
- Quy trinh: LUON cap nhat Document -> Commit -> Push code.
- **[DESIGN] Đồng bộ Premium Backgrounds:** Nâng cấp tất cả các trang phụ (Capcut, Locket, Youtube, Canva...) lên chuẩn thiết kế mới với nền lưới ma trận phát sáng (grid) và hiệu ứng Emoji trôi nổi, xoay vòng 360 độ (position: fixed).
- **[DESIGN] Mobile App Swipeable Carousels:** Xóa bỏ danh sách xếp chồng dọc nhàm chán trên Mobile. Chuyển toàn bộ danh sách dịch vụ (index.html, windows-pricing.html) sang dạng vuốt ngang (Scroll Snap) hệt như App Store, mang lại cảm giác dùng native app cực kỳ mượt mà.

- **[CONTENT] Sửa đoạn mô tả:** Ngắt dòng (thêm <br>) giữa 'Dịch vụ kỹ thuật & phần mềm' và 'Nhanh · Sạch · Uy tín' ở phần Header trang chủ để tối ưu hiển thị, tránh câu quá dài.

- **[CONTENT] Tối ưu URL:** Loại bỏ đuôi .html khỏi toàn bộ các liên kết nội bộ trên website. Đổi liên kết trỏ về trang chủ từ index.html thành ./ (mặc định) để khi người dùng lướt web, thanh địa chỉ trông sạch sẽ và chuyên nghiệp hơn (ví dụ: xwuan.github.io/capcut thay vì xwuan.github.io/capcut.html).
