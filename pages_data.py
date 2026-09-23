# -*- coding: utf-8 -*-
"""Nội dung các trang — lấy từ xwuan.github.io (pricing.js + index + trang chi tiết)."""

ZALO = 'https://zalo.me/0822307662'

SQUIG_RED = '<svg class="squig" width="200" height="14" viewBox="0 0 200 14" fill="none" aria-hidden="true"><path d="M4 9 C 30 3 46 12 68 8 S 112 3 132 8 S 186 12 196 6" stroke="#d94f43" stroke-width="4" stroke-linecap="round"/></svg>'
SQUIG_BLUE = '<svg class="squig blue" width="200" height="14" viewBox="0 0 200 14" fill="none" aria-hidden="true"><path d="M4 9 C 30 3 46 12 68 8 S 112 3 132 8 S 186 12 196 6" stroke="#4a7fb5" stroke-width="4" stroke-linecap="round"/></svg>'
SQUIG_GREEN = '<svg class="squig green" width="200" height="14" viewBox="0 0 200 14" fill="none" aria-hidden="true"><path d="M4 9 C 30 3 46 12 68 8 S 112 3 132 8 S 186 12 196 6" stroke="#58a05f" stroke-width="4" stroke-linecap="round"/></svg>'

INDEX_TABS = [('#banggia', '📋 Bảng giá'), ('#uytin', '🤝 Cam kết'), ('#review', '⭐ Nhận xét'), ('#faq', '❓ Hỏi–đáp'), ('#lienhe', '📞 Liên hệ')]
DET_TABS = [('index.html', '🏠 Trang chủ'), ('#goigoi', '💰 Gói giá'), ('#sosanh', '⚖️ So sánh'), ('#camket', '🛡️ Cam kết'), ('#lienhe', '📞 Liên hệ')]
WIN_TABS = [('index.html', '🏠 Trang chủ'), ('#goigoi', '💰 Bảng giá'), ('#combo', '🔥 Combo'), ('#camket', '🛡️ Cam kết'), ('#lienhe', '📞 Liên hệ')]
LOCKET_TABS = [('index.html', '🏠 Trang chủ'), ('#goigoi', '💰 Gói giá'), ('#sosanh', '🏆 Gold vs Free'), ('#camket', '🛡️ Cam kết'), ('#lienhe', '📞 Liên hệ')]


def card(badge_cls, badge, icon, name, desc, old, price, unit, deal, feats, href, cta='Xem chi tiết →'):
    f = '\n              '.join('<li>%s</li>' % x for x in feats)
    deal_html = '<p class="deal-note">%s</p>' % deal if deal else ''
    old_html = '<p class="old-price">giá gốc <s>%s</s></p>' % old if old else ''
    return '''<article class="card r-a reveal">
            <span class="tape"></span>
            <span class="badge %s">%s</span>
            <div class="p-icon">%s</div>
            <h3>%s</h3>
            <p class="desc">%s</p>
            %s
            <p class="price">%s <small>/ %s</small></p>
            %s
            <ul class="feat">
              %s
            </ul>
            <a class="btn btn-card" href="%s">%s</a>
            <a class="zalo-mini" href="%s" target="_blank" rel="noopener">💬 mua nhanh qua Zalo</a>
          </article>''' % (badge_cls, badge, icon, name, desc, old_html, price, unit, deal_html, f, href, cta, ZALO)


def hero_burst():
    import math
    cx = cy = 80.0
    pts = []
    n = 16
    for i in range(n * 2):
        r = 79 if i % 2 == 0 else 59
        a = math.pi * i / n - math.pi / 2
        j = 1 + (0.012 * ((i * 37) % 5 - 2))
        pts.append('%.1f %.1f' % (cx + r * j * math.cos(a), cy + r * j * math.sin(a)))
    return ', '.join(pts)


# ═══════════════════════════════ TRANG CHỦ ═══════════════════════════════
INDEX_CONTENT = """
<!-- ═══ HERO ═══ -->
      <section class="hero" id="top">
        <div class="hero-text reveal in">
          <span class="pill">🔥 Bảng giá mới nhất tháng 09/2026</span>
          <h1>
            <span class="small-line">CapCut · Canva · YouTube · Netflix · Gemini…</span>
            Acc xịn <span class="hl">CHỈ 2–5/10 GIÁ GỐC!</span>
          </h1>
          <p class="lead">
            Acc premium nâng cấp chính chủ, <b>bảo hành full thời gian</b> theo gói, kích hoạt
            <b>2–5 phút</b> sau khi nhắn Zalo. Hỗ trợ hỏi đáp <b>24/24</b> — nhanh · sạch · uy tín ✨
          </p>
          <div class="cta">
            <a class="btn btn-red" href="#banggia">📋 Xem bảng giá</a>
            <a class="btn btn-line" href="%(ZALO)s" target="_blank" rel="noopener">💬 Nhắn Zalo ngay</a>
          </div>
          <ul class="hero-stats">
            <li><b>2–5 phút</b><span>kích hoạt</span></li>
            <li><b>24/24</b><span>hỗ trợ hỏi đáp</span></li>
            <li><b>6 tháng</b><span>BH Win/Office</span></li>
          </ul>
        </div>

        <div class="hero-art" aria-hidden="true">
          <svg class="burst" viewBox="0 0 160 160">
            <polygon points="%(BURST)s" fill="#e2574c" stroke="#8f2c24" stroke-width="3" stroke-linejoin="round"/>
            <g transform="rotate(-9 80 80)" fill="#fff7e0" text-anchor="middle" font-family="'Shantell Sans','Patrick Hand',cursive" font-weight="700">
              <text x="80" y="64" font-size="24">RẺ HƠN</text>
              <text x="80" y="96" font-size="31">50–90%%</text>
              <text x="80" y="122" font-size="15">so với giá gốc!</text>
            </g>
          </svg>
          <div class="polaroid">
            <span class="tape tape-plain"></span>
            <div class="ph-img">🎨🎬🤖</div>
            <div class="ph-cap">mua 1 lần — xài tưng bừng ✌️</div>
          </div>
          <span class="mini-sticker s1">⚡ kích hoạt 2–5 phút</span>
          <span class="mini-sticker s2">🛡️ bảo hành full</span>
          <svg class="hero-arrow" viewBox="0 0 130 60" fill="none">
            <path d="M124 8 C 96 34, 62 46, 10 42" stroke="#5c4a2e" stroke-width="3" stroke-linecap="round" stroke-dasharray="7 6"/>
            <path d="M22 32 L8 42 L24 50" stroke="#5c4a2e" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
          <span class="arrow-note">kéo xuống xem giá nè!</span>
        </div>
      </section>

      <!-- ═══ BẢNG GIÁ ═══ -->
      <section class="sec" id="banggia">
        <h2 class="h-scrap"><span class="ico">📋</span>Bảng giá hôm nay</h2>
        %(SQ_RED)s

        <div class="cards">
          %(CARD_CAPCUT)s
          %(CARD_CANVA)s
          %(CARD_YOUTUBE)s
          %(CARD_NETFLIX)s
          %(CARD_GEMINI)s
          %(CARD_MEITU)s
        </div>

        <div class="more-accs reveal">
          <span class="more-label">👉 Trang chi tiết từng acc:</span>
          <a class="chip" href="capcut.html">🎬 CapCut Pro</a>
          <a class="chip" href="canva.html">🎨 Canva Pro</a>
          <a class="chip" href="youtube.html">▶️ YouTube Premium</a>
          <a class="chip" href="netflix.html">🍿 Netflix 4K</a>
          <a class="chip" href="google-ai.html">🤖 Google AI Pro</a>
          <a class="chip" href="meitu.html">📸 Meitu SVIP</a>
          <a class="chip" href="locket.html">✨ Locket Gold</a>
          <a class="chip" href="windows-pricing.html">💻 Windows &amp; Office</a>
        </div>
        <p class="disclaimer">* Giá tham khảo, cập nhật 09/2026 — nhắn Zalo để lấy báo giá mới nhất nha!</p>
      </section>

      <!-- ═══ LOCKET GOLD ═══ -->
      <section class="sec" id="locket">
        <h2 class="h-scrap"><span class="ico">✨</span>Locket Gold — ghim khoảnh khắc</h2>
        %(SQ_BLUE)s
        <div class="wide-card w-pink reveal">
          <span class="tape tape-plain"></span>
          <h3>✨ Locket Gold</h3>
          <p class="w-sub">An toàn 100%% · không ảnh hưởng iCloud cá nhân · hỗ trợ cả iOS &amp; Android</p>
          <div class="wide-grid">
            <div class="wide-col">
              <h4>🎥 Gói Quay 5s</h4>
              <ul class="price3">
                <li>6 tháng <b>50k</b></li>
                <li>1 năm <b>80k</b></li>
                <li>Vĩnh viễn ♾️ <b>150k</b></li>
              </ul>
            </div>
            <div class="wide-col">
              <h4>🎬 Gói Quay 15s</h4>
              <ul class="price3">
                <li>6 tháng <b>60k</b></li>
                <li>1 năm <b>100k</b></li>
                <li>Vĩnh viễn ♾️ <b>180k</b></li>
              </ul>
            </div>
          </div>
          <p style="margin-top:18px"><a class="btn btn-green" href="locket.html">Xem chi tiết Locket →</a></p>
        </div>
      </section>

      <!-- ═══ WINDOWS & OFFICE ═══ -->
      <section class="sec" id="winoffice">
        <h2 class="h-scrap"><span class="ico">💻</span>Windows &amp; Office — cài đặt kỹ thuật</h2>
        %(SQ_GREEN)s
        <div class="wide-card w-blue reveal">
          <span class="tape tape-plain"></span>
          <h3>🖥️ Dịch vụ cài đặt</h3>
          <p class="w-sub">Giá minh bạch · Không phát sinh · Xong trong 30–60 phút · 🛡️ Bảo hành lỗi phát sinh 6 tháng</p>
          <ul class="svc-list">
            <li class="svc-row"><span>🪟 Windows Chuẩn Microsoft<small>ISO gốc, driver đầy đủ, ổn định cao</small></span><b>150k – 180k</b></li>
            <li class="svc-row"><span>⚡ Windows Tối Ưu Hiệu Năng<small>nhẹ – mượt cho máy cũ / RAM 4GB</small></span><b>100k – 120k</b></li>
            <li class="svc-row"><span>📘 Microsoft Office<small>Word, Excel, PowerPoint — 365 / 2021 / 2019</small></span><b>80k – 120k</b></li>
            <li class="svc-row"><span>🔥 Combo Win Chuẩn + Office<span class="save-stamp">tiết kiệm ~30k</span></span><b>200k – 220k</b></li>
            <li class="svc-row"><span>⚡ Combo Win Tối Ưu + Office<span class="save-stamp">tiết kiệm ~20k</span></span><b>160k – 180k</b></li>
          </ul>
          <p style="margin-top:18px"><a class="btn btn-green" href="windows-pricing.html">Xem bảng giá Win &amp; Office →</a></p>
        </div>
      </section>

      <!-- ═══ CAM KẾT ═══ -->
      <section class="sec" id="uytin">
        <h2 class="h-scrap"><span class="ico">🤝</span>Cam kết chất lượng ghi trong sổ</h2>
        %(SQ_RED)s
        <div class="grid2 reveal">
          <ul class="checklist">
            <li><span class="cbx">✓</span><span><b>Sao lưu dữ liệu an toàn</b> — cài Win/Office giữ nguyên dữ liệu của bạn.</span></li>
            <li><span class="cbx">✓</span><span><b>Hỗ trợ cực kỳ nhanh chóng</b> — kích hoạt acc trong 2–5 phút sau khi chốt đơn.</span></li>
            <li><span class="cbx">✓</span><span><b>Hỏi đáp 24/24</b> — liên hệ Zalo bất cứ lúc nào, phản hồi nhiệt tình.</span></li>
          </ul>
          <ul class="checklist">
            <li><span class="cbx">✓</span><span><b>Win/Office bảo hành 6 tháng</b> — lỗi phát sinh được xử lý miễn phí.</span></li>
            <li><span class="cbx">✓</span><span><b>Locket bảo hành tận tâm</b> — kể cả khi bạn đổi máy mới vẫn hỗ trợ miễn phí.</span></li>
            <li><span class="cbx">✓</span><span><b>Acc premium ổn định</b> — gặp lỗi là hỗ trợ 1 đổi 1 ngay lập tức 🤝</span></li>
          </ul>
        </div>

        <h2 class="h-scrap" style="margin-top:56px"><span class="ico">✍️</span>Đặt acc — 3 bước thật nhanh</h2>
        <ol class="steps reveal">
          <li>
            <span class="num">1</span>
            <h4>Nhắn Zalo / Facebook</h4>
            <p>Chọn acc + gói thời gian, mình báo giá chốt đơn ngay.</p>
          </li>
          <li>
            <span class="num">2</span>
            <h4>Xwuan kích hoạt</h4>
            <p>Nâng cấp / kích hoạt acc cho bạn trong 2–5 phút.</p>
          </li>
          <li>
            <span class="num">3</span>
            <h4>Dùng ngay + bảo hành</h4>
            <p>Dùng thoải mái, có lỗi là hỗ trợ 1 đổi 1 suốt thời gian gói.</p>
          </li>
        </ol>
      </section>

      <!-- ═══ NHẬN XÉT ═══ -->
      <section class="sec" id="review">
        <h2 class="h-scrap"><span class="ico">⭐</span>Sổ nhận xét của khách</h2>
        %(SQ_GREEN)s
        <div class="notes">
          <figure class="note n-yellow reveal">
            <span class="tape tape-plain"></span>
            <blockquote>“Đang cần edit video gấp, nhắn Zalo 5 phút sau có CapCut Pro luôn. Xuất 4K mượt, không watermark!”</blockquote>
            <figcaption>— Một bạn làm TikTok 🎬<small>CapCut Pro 30 ngày · feedback mẫu</small></figcaption>
          </figure>
          <figure class="note n-pink reveal" style="--d:.08s">
            <span class="tape tape-plain"></span>
            <blockquote>“Netflix 4K có profile riêng + mã PIN, cả nhà xem chung mà không lo dính phim của nhau. Đáng tiền!”</blockquote>
            <figcaption>— Một khách hàng dễ tính 🍿<small>Netflix 4K UHD · feedback mẫu</small></figcaption>
          </figure>
          <figure class="note n-blue reveal" style="--d:.16s">
            <span class="tape tape-plain"></span>
            <blockquote>“Locket Gold vĩnh viễn rẻ hơn hẳn chỗ khác, đổi điện thoại mới vẫn được hỗ trợ激活 miễn phí. 10 điểm!”</blockquote>
            <figcaption>— Một bạn iOS 📸<small>Locket Gold · feedback mẫu</small></figcaption>
          </figure>
          <figure class="note note-empty reveal" style="--d:.24s">
            <span>🔖</span>
            <span>Trang trống — đánh giá của <b>bạn</b> sẽ nằm ở đây ✍️</span>
          </figure>
        </div>
      </section>

      <!-- ═══ FAQ ═══ -->
      <section class="sec" id="faq">
        <h2 class="h-scrap"><span class="ico">❓</span>Hỏi – đáp vụn vặt</h2>
        %(SQ_RED)s
        <div class="faq reveal">
          <details open>
            <summary><span class="plus">+</span>Acc giá rẻ vậy dùng có ổn định không?</summary>
            <p>Acc được nâng cấp chính chủ và quản lý kỹ nên rất ổn định. Rủi ro nào xảy ra trong thời gian gói (mất quyền, lỗi đăng nhập…), bạn chỉ cần nhắn Zalo — mình hỗ trợ <b>1 đổi 1 ngay</b> và bảo hành full thời gian sử dụng.</p>
          </details>
          <details>
            <summary><span class="plus">+</span>Mua xong bao lâu nhận được acc?</summary>
            <p>Rất nhanh — chỉ <b>2–5 phút</b> kể từ khi chốt đơn. Kích hoạt qua email hoặc gửi thẳng tài khoản tùy dịch vụ, kèm hướng dẫn cài đặt tận tình nếu bạn cần.</p>
          </details>
          <details>
            <summary><span class="plus">+</span>Đặt mua và thanh toán như thế nào?</summary>
            <p>Bạn nhắn Zalo (<b>0822.307.662</b>) hoặc Facebook để chốt đơn, sau đó thanh toán chuyển khoản — với dịch vụ cài đặt Win/Office có thể trao đổi phương thức tiện hơn qua Zalo. Xong là nhận acc ngay!</p>
          </details>
          <details>
            <summary><span class="plus">+</span>Sao Google AI Pro lại không bảo hành?</summary>
            <p>Đây là <b>gói siêu rẻ phi lợi nhuận</b> dành riêng cho học sinh, sinh viên nên giá siết sát gốc — vì vậy không kèm bảo hành. Đổi lại chỉ 60k là dùng Gemini 3.1 Pro + Google One 2TB trọn <b>1 năm</b> 😄</p>
          </details>
          <details>
            <summary><span class="plus">+</span>Cài Windows / Office mất bao lâu, bảo hành ra sao?</summary>
            <p>Thường xong trong <b>30–60 phút</b>: Windows chuẩn Microsoft hoặc tối ưu cho máy yếu, Office 365/2021/2019 đầy đủ. Giữ nguyên dữ liệu, không phát sinh chi phí và <b>bảo hành lỗi phát sinh 6 tháng</b>.</p>
          </details>
        </div>
      </section>
""" % {
    'ZALO': ZALO,
    'BURST': hero_burst(),
    'SQ_RED': SQUIG_RED, 'SQ_BLUE': SQUIG_BLUE, 'SQ_GREEN': SQUIG_GREEN,
    'CARD_CAPCUT': card('b-pink', '🔥 PHỔ BIẾN NHẤT', '🎬', 'CapCut Pro', 'Dựng video mượt, kho template khủng', '~250.000đ/tháng', '20k', '7 ngày', 'hoặc <b>80k / 30 ngày</b> 🤩', ['Không watermark', 'Hiệu ứng &amp; font Premium', 'Xuất video 4K', 'Cloud 100GB'], 'capcut.html'),
    'CARD_CANVA': card('b-blue', '💛 TIẾT KIỆM ~90%', '🎨', 'Canva Pro', 'Thiết kế – slide – xóa phông siêu mượt', '~1.300.000đ/năm', '130k', '1 năm', 'hoặc <b>20k / 30 ngày</b>', ['100M+ mẫu &amp; ảnh Pro', 'Xóa phông 1 chạm', 'AI Magic Studio', 'Lưu trữ 1TB'], 'canva.html'),
    'CARD_YOUTUBE': card('', '🎵 KÈM YT MUSIC', '▶️', 'YouTube Premium', 'Xem video không quảng cáo một giây', '79.000đ/tháng', '40k', '30 ngày', '', ['Chặn 100% quảng cáo', 'Tắt màn hình vẫn nghe nhạc', 'YT Music Premium', '4K + HDR'], 'youtube.html'),
    'CARD_NETFLIX': card('b-green', '🔥 4K HDR', '🍿', 'Netflix 4K UHD', 'Phim chuẩn 4K, xem mọi thiết bị', '273.000đ/tháng', '45k', '30 ngày', 'rẻ hơn <b>228k</b> mỗi tháng 🤯', ['Chất lượng 4K UHD + HDR', 'Profile riêng + mã PIN', 'Smart TV, laptop, điện thoại', 'Tải phim offline'], 'netflix.html'),
    'CARD_GEMINI': card('b-gray', '⚠️ KHÔNG BẢO HÀNH', '🤖', 'Google AI Pro', 'Gemini 3.1 Pro + Google One 2TB', '~5.800.000đ/năm', '60k', '1 năm', 'siêu rẻ phi lợi nhuận cho HSSV', ['Gemini 3.1 Pro mới nhất', 'Ngữ cảnh 1 triệu token', 'Tạo ảnh Imagen 3', 'Tích hợp Docs &amp; Gmail'], 'google-ai.html'),
    'CARD_MEITU': card('', '👑 FULL SVIP', '📸', 'Meitu SVIP', 'Chỉnh ảnh &amp; video chuyên nghiệp', '249.000đ/tháng', '90k', '30 ngày', '', ['AI làm nét ảnh 4K', 'Filter hot trend TikTok', 'Không dính watermark', 'Không quảng cáo'], 'meitu.html'),
}


# ═══════════════════════════ DÙNG CHUNG TRANG CHI TIẾT ═══════════════════════════
def d_hero(icon, pill, title, tag):
    return '''<a class="crumb" href="index.html">← Quay về trang chủ</a>
      <section class="d-hero">
        <div class="d-icon" aria-hidden="true">%s</div>
        <div>
          <span class="pill">%s</span>
          <h1 class="d-title">%s</h1>
          <p class="d-tag">%s</p>
        </div>
      </section>''' % (icon, pill, title, tag)


def pkg_card(badge_cls, badge, name, price, unit, feats, deal=None, note=None):
    f = '\n              '.join('<li>%s</li>' % x for x in feats)
    deal_html = '<p class="deal-note">%s</p>' % deal if deal else ''
    note_html = '<p class="disclaimer" style="margin-top:8px">%s</p>' % note if note else ''
    return '''<article class="card r-b reveal" style="--d:.08s">
            <span class="tape"></span>
            <span class="badge %s">%s</span>
            <h3>%s</h3>
            <p class="price">%s <small>/ %s</small></p>
            %s
            <ul class="feat">
              %s
            </ul>
            <a class="btn btn-card" href="%s" target="_blank" rel="noopener">💬 Mua gói này qua Zalo</a>
            %s
          </article>''' % (badge_cls, badge, name, price, unit, deal_html, f, ZALO, note_html)


def cmp_table(head, rows, hot_row=None):
    th = ''.join('<th>%s</th>' % x for x in head)
    body = []
    for i, r in enumerate(rows):
        cls = ' class="hot"' if hot_row is not None and i == hot_row else ''
        tds = []
        for j, c in enumerate(r):
            if j == 0:
                tds.append('<td>%s</td>' % c)
            else:
                tds.append('<td class="%s">%s</td>' % (c[0], c[1]))
        body.append('<tr%s>%s</tr>' % (cls, ''.join(tds)))
    return '''<table class="cmp reveal">
          <thead><tr>%s</tr></thead>
          <tbody>
            %s
          </tbody>
        </table>''' % (th, '\n            '.join(body))


def receipt(rows, save):
    rr = []
    for lab, val, big in rows:
        cls = 'big' if big else ''
        v = '<s>%s</s>' % val if not big else '<b>%s</b>' % val
        rr.append('<div class="r-row %s"><span class="lab">%s</span><span class="val">%s</span></div>' % (cls, lab, v))
    return '''<div class="receipt reveal">
          <h3>💰 So sánh giá</h3>
          %s
          <span class="r-save">%s</span>
        </div>''' % ('\n          '.join(rr), save)


def check2col(col1, col2):
    def li(x):
        return '<li><span class="cbx">✓</span><span>%s</span></li>' % x
    a = '\n              '.join(li(x) for x in col1)
    b = '\n              '.join(li(x) for x in col2)
    return '''<div class="grid2 reveal">
          <ul class="checklist">
              %s
          </ul>
          <ul class="checklist">
              %s
          </ul>
        </div>''' % (a, b)


def steps(s1, s2, s3):
    return '''<ol class="steps reveal">
          <li><span class="num">1</span><h4>%s</h4><p>%s</p></li>
          <li><span class="num">2</span><h4>%s</h4><p>%s</p></li>
          <li><span class="num">3</span><h4>%s</h4><p>%s</p></li>
        </ol>''' % (s1[0], s1[1], s2[0], s2[1], s3[0], s3[1])


def camket_section(title, sq, grid, step):
    return '''
      <section class="sec" id="camket">
        <h2 class="h-scrap"><span class="ico">🛡️</span>%s</h2>
        %s
        %s
        <h2 class="h-scrap" style="margin-top:56px"><span class="ico">🚀</span>Cách thức hoạt động</h2>
        %s
      </section>''' % (title, sq, grid, step)
