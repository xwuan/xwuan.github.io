# -*- coding: utf-8 -*-
"""Nội dung các MẶT GIẤY của từng trang — dữ liệu gốc từ xwuan.github.io."""

ZALO = 'https://zalo.me/0822307662'
ZALO_TXT = '0822.307.662'


def SQ(c='#d94f43', w=150):
    return ('<svg class="f-squig" width="%d" height="12" viewBox="0 0 200 14" fill="none" aria-hidden="true">'
            '<path d="M4 9 C 30 3 46 12 68 8 S 112 3 132 8 S 186 12 196 6" stroke="%s" stroke-width="4" stroke-linecap="round"/></svg>' % (w, c))


def F(inner, cls='', cover=False):
    c = ' data-cover' if cover else ''
    cic = ' class="%s"' % cls if cls else ''
    return '<div class="face-pad"%s><div class="face-in%s">%s</div></div>' % (c, cic, inner)


def burst_svg(text1, text2, text3):
    import math
    cx = cy = 80.0
    pts = []
    n = 16
    for i in range(n * 2):
        r = 79 if i % 2 == 0 else 59
        a = math.pi * i / n - math.pi / 2
        j = 1 + (0.012 * ((i * 37) % 5 - 2))
        pts.append('%.1f %.1f' % (cx + r * j * math.cos(a), cy + r * j * math.sin(a)))
    return ('<svg class="cov-burst" viewBox="0 0 160 160">'
            '<polygon points="%s" fill="#e2574c" stroke="#8f2c24" stroke-width="3" stroke-linejoin="round"/>'
            '<g transform="rotate(-9 80 80)" fill="#fff7e0" text-anchor="middle" font-family=\'Shantell Sans,Patrick Hand,cursive\' font-weight="700">'
            '<text x="80" y="62" font-size="23">%s</text><text x="80" y="94" font-size="30">%s</text>'
            '<text x="80" y="120" font-size="14">%s</text></g></svg>' % (', '.join(pts), text1, text2, text3))


def prow(icon, name, small, price, unit, link=None, link_href=None):
    lk = ''
    if link and link_href:
        lk = '<a href="%s">%s</a>' % (link_href, link)
    return ('<div class="prow"><span class="ic">%s</span>'
            '<span class="tx"><b>%s</b><small>%s</small></span>'
            '<span class="pr"><b>%s</b><small>%s</small>%s</span></div>' % (icon, name, small, price, unit, lk))


def toc(items):
    lis = []
    for goto, label in items:
        lis.append('<li data-goto="%d"><span class="t">%s</span><span class="dots"></span><b>trang %d</b></li>' % (goto, label, goto))
    return '<ul class="toc">%s</ul>' % '\n'.join(lis)


def toc_face(items, note='bấm vào dòng nào — sổ tự lật đến trang đó nha 👆'):
    return ('<h2 class="f-h"><span class="ico">📑</span>Mục lục</h2>%s%s<p class="f-note">%s</p>'
            % (SQ('#4a7fb5'), toc(items), note))


def cover_face(title, sub, sticker, hint, foot, badges=None, icon=None, burst=None, nav=None, is_home=False):
    mid = ''
    if icon:
        mid += '<div class="cov-icon">%s</div>' % icon
    if burst:
        mid += burst
    bd = ''
    if badges:
        bd = '<div class="cov-badges">%s</div>' % ''.join('<span>%s</span>' % b for b in badges)
    
    nb = ''
    if nav:
        nb_items = ''.join('<button class="cov-btn" data-goto="%d">%s</button>' % (k, lbl) for k, lbl in nav)
        nb = '<div class="cov-nav" aria-label="Mục lục nhanh">%s</div>' % nb_items
        
    top_tools = '<div class="cov-tools">'
    if not is_home:
        top_tools += '<a href="index.html" class="cov-tool-btn" title="Về Sổ Tổng Hợp">🏠 Sổ Tổng</a>'
    top_tools += '<button class="cov-tool-btn" id="btnSnd" aria-label="Bật/tắt âm thanh" title="Âm thanh lật sổ">🔊</button>'
    top_tools += '</div>'

    open_txt = hint if '📖' in hint else ('📖 ' + hint)

    return F('%s<p class="cov-kicker">✦ SỔ ACC XWUAN ✦</p>%s<h1 class="cov-title" style="font-size:1.8em">%s</h1>'
             '<p class="cov-sub">%s</p><span class="cov-sticker">%s</span>%s%s'
             '<button class="btn btn-red cov-open-btn" data-goto="1">%s</button>'
             '<p class="cov-foot">%s</p>'
             % (top_tools, mid, title, sub, sticker, bd, nb, open_txt, foot), cls='cov-in', cover=True)


def back_cover(selected=None, extra_note=None):
    opts = ['ChatGPT Plus', 'CapCut Pro', 'Canva Pro', 'YouTube Premium', 'Netflix 4K UHD',
            'Google AI Pro (Gemini)', 'Meitu SVIP', 'Locket Gold', 'Windows / Office', 'Khác (tư vấn giúp)']
    o = []
    for a in opts:
        sel = ' selected' if a == selected else ''
        o.append('<option%s>%s</option>' % (sel, a))
    note = '<p class="bc-lead">%s</p>' % extra_note if extra_note else ''
    return F('<h2 class="bc-title">📞 Sổ tay liên hệ</h2>%s'
             '<div class="contact-row">'
             '<a class="contact" href="%s" target="_blank" rel="noopener">💬 Zalo: %s</a>'
             '<a class="contact" href="https://www.facebook.com/xwuan1/" target="_blank" rel="noopener">📘 Facebook: Xwuan</a>'
             '<a class="contact" href="https://www.tiktok.com/@xwuan2" target="_blank" rel="noopener">🎵 TikTok: @xwuan2</a>'
             '</div>'
             '<div class="pay-row"><span class="pay-label">cam kết:</span>'
             '<span class="pay">⚡ kích hoạt 2–5 phút</span><span class="pay">🕐 hỗ trợ 24/24</span><span class="pay">🛡️ BH theo gói</span></div>'
             '<form class="order" id="orderForm">'
             '<h3>✍️ Đặt nhanh — ghi vào sổ:</h3>'
             '<div class="row"><input name="ten" placeholder="Tên của bạn…" required>'
             '<input name="sdt" placeholder="SĐT / Zalo…" required></div>'
             '<div class="row"><select name="acc" aria-label="Chọn acc">%s</select>'
             '<input name="ghi" placeholder="Ghi chú (thời gian, số lượng…)"></div>'
             '<button class="btn btn-red" type="submit">📨 Gửi đơn qua Zalo</button>'
             '<p id="formHint" hidden style="color:#ffe9b8;font-size:.85em;margin-top:.4em">Đã chép đơn vào bộ nhớ tạm — dán vào khung chat Zalo nha! 💜</p>'
             '</form>'
             '<div style="text-align:center;margin-top:.5em"><button type="button" class="btn btn-line" data-goto="0">📖 Về bìa trước</button></div>'
             '<p class="fineprint">© 2026 Sổ Acc Xwuan · nhanh · sạch · uy tín · Made with 📓✏️</p>'
             % (note, ZALO, ZALO_TXT, '\n'.join(o)), cls='backcover-in', cover=True)


def check_grid(l, r):
    def lis(items):
        return '\n'.join('<li><span class="cbx">✓</span><span>%s</span></li>' % x for x in items)
    return '<div class="grid2"><ul class="checklist">%s</ul><ul class="checklist">%s</ul></div>' % (lis(l), lis(r))


def commit_steps(l, r, steps3, title='🛡️ Cam kết từ Xwuan'):
    s = []
    for i, (h, p) in enumerate(steps3):
        s.append('<li><span class="num">%d</span><h4>%s</h4><p>%s</p></li>' % (i + 1, h, p))
    return ('<h2 class="f-h"><span class="ico">%s</span>%s</h2>%s%s'
            '<h2 class="f-h" style="margin-top:.7em"><span class="ico">🚀</span>Đặt acc — 3 bước</h2>%s<ol class="steps">%s</ol>'
            % ('🛡️', title.replace('🛡️ ', ''), SQ('#d94f43'), check_grid(l, r), SQ('#58a05f'), '\n'.join(s)))


def receipt_face(rows, save, warn=None):
    rr = []
    for lab, val, big in rows:
        v = '<b>%s</b>' % val if big else '<s>%s</s>' % val
        rr.append('<div class="r-row %s"><span>%s</span><span class="val">%s</span></div>' % ('big' if big else '', lab, v))
    w = '<div style="text-align:center">%s</div>' % warn if warn else ''
    return ('<div class="receipt"><h3>💰 So sánh giá</h3>%s<span class="r-save">%s</span></div>%s'
            % ('\n'.join(rr), save, w))


def cmp_face(head, rows, hot=None):
    th = ''.join('<th>%s</th>' % x for x in head)
    body = []
    for i, r in enumerate(rows):
        cls = ' class="hot"' if hot is not None and i == hot else ''
        tds = ['<td>%s</td>' % r[0]]
        for c in r[1:]:
            tds.append('<td class="%s">%s</td>' % (c[0], c[1]))
        body.append('<tr%s>%s</tr>' % (cls, ''.join(tds)))
    return ('<table class="cmp"><thead><tr>%s</tr></thead><tbody>%s</tbody></table>'
            % (th, '\n'.join(body)))


def faq_face(items, title='❓ Hỏi – đáp vụn vặt'):
    ds = []
    for i, (q, a) in enumerate(items):
        op = ' open' if i == 0 else ''
        ds.append('<details%s><summary><span class="plus">+</span>%s</summary><p>%s</p></details>' % (op, q, a))
    return '<h2 class="f-h"><span class="ico">❓</span>%s</h2>%s<div class="faq">%s</div>' % (title.replace('❓ ', ''), SQ('#d94f43'), '\n'.join(ds))


def notes_face():
    return ('<h2 class="f-h"><span class="ico">⭐</span>Sổ nhận xét của khách</h2>%s'
            '<div class="notes">'
            '<figure class="note n-yellow"><blockquote>“Đang cần edit gấp, nhắn Zalo 5 phút sau có CapCut Pro. Xuất 4K mượt, không watermark!”</blockquote><figcaption>— bạn làm TikTok 🎬<small>CapCut 30 ngày</small></figcaption></figure>'
            '<figure class="note n-pink"><blockquote>“Netflix 4K có profile riêng + mã PIN, cả nhà xem chung không lo dính phim nhau. Đáng tiền!”</blockquote><figcaption>— khách hàng dễ tính 🍿<small>Netflix 4K</small></figcaption></figure>'
            '<figure class="note n-blue"><blockquote>“Locket vĩnh viễn rẻ hơn chỗ khác, đổi máy mới vẫn được hỗ trợ. 10 điểm!”</blockquote><figcaption>— bạn iOS 📸<small>Locket Gold</small></figcaption></figure>'
            '<figure class="note-empty"><span>🔖</span><span>trang trống — đánh giá của <b>bạn</b> sẽ nằm đây ✍️</span></figure>'
            '</div>' % SQ('#58a05f'))


def fb_face():
    pols = []
    for i in (1, 2, 3):
        pols.append(
            '<figure class="fb-pol r%d"><span class="tape tape-plain"></span>'
            '<img src="images/fb%d.jpg" alt="Feedback khách hàng %d" '
            'onerror="this.style.display=\'none\';this.nextElementSibling.style.display=\'flex\'">'
            '<div class="fb-ph">📷<br>thay ảnh feedback thật:<br><small>images/fb%d.jpg</small></div>'
            '<figcaption>feedback khách %d 💌</figcaption></figure>' % (i, i, i, i, i))
    return F('<h2 class="f-h"><span class="ico">⭐</span>Feedback khách hàng</h2>%s'
            '<div class="fb-grid">%s</div>'
            '<p class="f-note">Bạn dùng acc thấy vui? Nhắn feedback qua Zalo — '
            'được dán lên sổ luôn kèm quà nhỏ 🎁 Ảnh bên trên là MẪU — sẽ được thay bằng feedback thật của bạn!</p>'
            % (SQ('#58a05f'), '\n'.join(pols)))


# ═══════════════════════════════ TRANG CHỦ — 11 MẶT ═══════════════════════════════
HOME_NAV = [
    (3, '💥 Bảng giá acc'),
    (5, '💻 Win & Locket'),
    (6, '🤝 Cam kết & BH'),
    (7, '⭐ Feedback'),
    (8, '❓ Hỏi – đáp'),
    (10, '📞 Đặt acc / Zalo')
]
HOME_END = '<div class="big">📓 Hết sổ rồi!</div><p>cảm ơn bạn đã xem hết — muốn mua acc thì lật lại bìa sau nha 💜</p>'

HOME_FACES = [
    # 0 — bìa trước
    cover_face('Sổ Acc <em>Xwuan</em>',
               'CapCut · Canva · Netflix · YouTube · Gemini · Meitu · Locket · Win/Office',
               'giá chỉ 2–5/10 giá gốc!',
               'chạm mở sổ xem giá ›',
               'kích hoạt 2–5 phút · bảo hành full · hỗ trợ 24/24',
               burst=burst_svg('RẺ HƠN', '50–90%', 'so với giá gốc!'),
               nav=HOME_NAV,
               is_home=True),
    # 1 — mục lục
    F(toc_face([(3, '💥 Bảng giá acc (1)'), (4, '🍿 Bảng giá acc (2)'),
                (5, '✨ Locket Gold &amp; 💻 Win/Office'), (6, '🤝 Cam kết &amp; 3 bước đặt'),
                (7, '⭐ Feedback khách hàng'), (8, '⭐ Sổ nhận xét'), (9, '❓ Hỏi – đáp'), (10, '📞 Bìa sau — liên hệ &amp; đặt')])),
    # 2 — hero
    F('<span class="f-kick">🔥 giá mới cập nhật 09/2026</span>'
      '<h1 class="f-h" style="font-size:1.8em;line-height:1.15">Acc xịn<br><span class="hl">CHỈ 2–5/10 GIÁ GỐC!</span></h1>'
      '<p class="f-lead">Acc premium nâng cấp chính chủ, <b>bảo hành full thời gian</b> theo gói, kích hoạt <b>2–5 phút</b> sau khi nhắn Zalo 📮</p>'
      '<div style="display:flex;gap:.5em;flex-wrap:wrap;margin-top:.4em">'
      '<a class="btn btn-red" data-goto="3">📋 Xem bảng giá</a>'
      '<a class="btn btn-line" href="%s" target="_blank" rel="noopener">💬 Nhắn Zalo ngay</a></div>'
      '<div class="stats"><span><b>2–5 phút</b> kích hoạt</span><span><b>24/24</b> hỗ trợ</span><span><b>6 tháng</b> BH Win/Office</span></div>'
      '<p class="f-note">👉 hoặc lật trang bằng nút «trang trước / trang sau» ở dưới</p>' % ZALO),
    # 3 — giá A
    F('<h2 class="f-h"><span class="ico">💥</span>Bảng giá acc (1)</h2>%s'
      '%s%s%s'
      '<p class="f-note">* giá có thể thay đổi — nhắn Zalo lấy báo giá mới nhất nha!</p>'
      % (SQ(),
         prow('🎬', 'CapCut Pro', 'không watermark · hiệu ứng Premium · xuất 4K', '20k', '7 ngày · 80k/30 ngày', 'xem chi tiết →', 'capcut.html'),
         prow('🎨', 'Canva Pro', '100M+ mẫu Pro · xóa phông · AI Magic · 1TB', '20k', '30 ngày · 130k/năm', 'xem chi tiết →', 'canva.html'),
         prow('▶️', 'YouTube Premium', 'không quảng cáo · phát nền · kèm YT Music', '40k', '/ 30 ngày', 'xem chi tiết →', 'youtube.html'))),
    # 4 — giá B
    F('<h2 class="f-h"><span class="ico">🍿</span>Bảng giá acc (2)</h2>%s'
      '%s%s%s'
      '<p class="f-note">✨ còn <b>Locket Gold</b> &amp; <b>Windows/Office</b> — <a class="mini-link" data-goto="5">lật sang trang sau nè ›</a></p>'
      % (SQ(),
         prow('🍿', 'Netflix 4K UHD', '4K HDR · profile riêng + mã PIN · mọi thiết bị', '45k', '/ 30 ngày', 'xem chi tiết →', 'netflix.html'),
         prow('🤖', 'Google AI Pro', 'Gemini 3.1 Pro · 1 triệu token · Google One 2TB', '60k', '/ 1 năm ⚠️ không BH', 'xem chi tiết →', 'google-ai.html'),
         prow('📸', 'Meitu SVIP', 'AI làm nét 4K · filter hot trend · không watermark', '90k', '/ 30 ngày', 'xem chi tiết →', 'meitu.html'))),
    # 5 — dịch vụ Locket + Win
    F('<h2 class="f-h"><span class="ico">✨</span>Locket Gold</h2>%s'
      '<div class="mini2">'
      '<div class="mini"><h4>🎥 Quay 5s</h4><ul class="p3"><li>6 tháng <b>50k</b></li><li>1 năm <b>80k</b></li><li>vĩnh viễn ♾️ <b>150k</b></li></ul></div>'
      '<div class="mini"><h4>🎬 Quay 15s</h4><ul class="p3"><li>6 tháng <b>60k</b></li><li>1 năm <b>100k</b></li><li>vĩnh viễn ♾️ <b>180k</b></li></ul></div>'
      '</div>'
      '<a class="mini-link" href="locket.html">xem chi tiết Locket →</a>'
      '<h2 class="f-h" style="margin-top:.55em"><span class="ico">💻</span>Windows &amp; Office</h2>'
      '<div class="p3" style="background:#fffdf4;border:2px solid rgba(46,61,89,.13);border-radius:12px;padding:.4em .7em;box-shadow:2px 3px 0 rgba(43,32,10,.12)">'
      '<li>🪟 Win chuẩn Microsoft <b>150k–180k</b></li>'
      '<li>⚡ Win tối ưu máy yếu <b>100k–120k</b></li>'
      '<li>📘 Office 365/2021/2019 <b>80k–120k</b></li>'
      '<li>🔥 Combo Win + Office <b>160k–220k</b></li>'
      '</div>'
      '<a class="mini-link" href="windows-pricing.html">xem bảng giá Win &amp; Office →</a>' % SQ('#4a7fb5')),
    # 6 — cam kết + 3 bước
    F(commit_steps(
        ['<b>Sao lưu dữ liệu an toàn</b> — cài Win giữ nguyên dữ liệu',
         'Kích hoạt acc <b>cực nhanh 2–5 phút</b>',
         '<b>Hỏi đáp 24/24</b> — nhắn Zalo bất cứ lúc nào'],
        ['<b>Win/Office bảo hành 6 tháng</b> lỗi phát sinh',
         '<b>Locket bảo hành tận tâm</b> — kể cả khi đổi máy mới',
         'Acc lỗi được <b>1 đổi 1 ngay</b> 🤝'],
        [('Nhắn Zalo / Facebook', 'chọn acc + gói thời gian, chốt đơn ngay.'),
         ('Xwuan kích hoạt', 'nâng cấp acc cho bạn trong 2–5 phút.'),
         ('Dùng ngay + bảo hành', 'có lỗi là hỗ trợ 1 đổi 1 suốt thời gian gói.')],
        title='Cam kết chất lượng')),
    # 7 — nhận xét
    F(notes_face()),
    # 8 — FAQ
    F(faq_face([
        ('Acc giá rẻ vậy có ổn định không?', 'Acc nâng cấp chính chủ, quản lý kỹ nên rất ổn định. Có lỗi trong thời gian gói là hỗ trợ <b>1 đổi 1 ngay</b>, bảo hành full thời gian sử dụng.'),
        ('Mua xong bao lâu nhận được acc?', 'Chỉ <b>2–5 phút</b> kể từ khi chốt đơn — kích hoạt qua email hoặc gửi thẳng tài khoản, kèm hướng dẫn tận tình.'),
        ('Thanh toán như thế nào?', 'Nhắn Zalo (%s) chốt đơn rồi chuyển khoản — dịch vụ cài Win/Office có thể trao đổi cách tiện hơn qua Zalo.' % ZALO_TXT),
        ('Sao Google AI Pro không bảo hành?', 'Đây là <b>gói siêu rẻ phi lợi nhuận</b> cho học sinh, sinh viên nên không kèm bảo hành — đổi lại chỉ 60k dùng Gemini 3.1 Pro + Google One 2TB trọn <b>1 năm</b> 😄'),
        ('Cài Win/Office mất bao lâu?', 'Xong trong <b>30–60 phút</b>, giữ nguyên dữ liệu, không phát sinh chi phí, <b>bảo hành lỗi phát sinh 6 tháng</b>.'),
    ])),
    # 9 — feedback ảnh
    fb_face(),
    # 10 — bìa sau
    back_cover(),
]

# ═══════════════════════════ TRANG CHI TIẾT ACC ═══════════════════════════
ACC_NAV = [
    (2, '💰 Gói giá'),
    (3, '⚖️ So sánh'),
    (4, '💵 Tiết kiệm'),
    (5, '🌟 Lợi ích'),
    (6, '🛡️ Cam kết'),
    (7, '📞 Liên hệ')
]

def acc_faces(icon, name, tagline, sticker, badges, pkgs, cmp_rows, receipt_rows, save,
              benefits, commit_l, commit_r, steps3, selected, faq=None, warn=None,
              toc_note=None, cmp_head=('Tính năng', 'Free 😐', 'Pro ✨'), cmp_hot=None):
    faces = [
        cover_face(name, tagline, sticker, 'chạm mở sổ xem giá ›',
                   ' · '.join(badges), icon=icon, nav=ACC_NAV, is_home=False),
        F(toc_face([(2, '💰 Gói giá trong sổ'), (3, '⚖️ Bảng so sánh'), (4, '💰 So sánh giá tiền'),
                    (5, '🌟 Lợi ích khi dùng'), (6, '🛡️ Cam kết &amp; 3 bước'), (7, '📞 Liên hệ &amp; đặt acc')],
                   note=toc_note or 'giá trong sổ là giá tốt nhất hiện nay nha 😉')),
        F('<h2 class="f-h"><span class="ico">💰</span>Gói giá trong sổ</h2>%s%s%s'
          '<p class="f-note">bấm «💬 mua qua Zalo» là có đơn chốt liền tay ⚡</p>'
          % (SQ(),
             '\n'.join(prow(p['icon'], p['name'], p['small'], p['price'], p['unit'], '💬 mua qua Zalo', ZALO) for p in pkgs),
             ('<div style="text-align:center">%s</div>' % warn) if warn else '')),
        F('<h2 class="f-h"><span class="ico">⚖️</span>Bảng so sánh</h2>%s%s'
          % (SQ('#4a7fb5'), cmp_face(cmp_head, cmp_rows, cmp_hot))),
        F(receipt_face(receipt_rows, save, warn)),
        F('<h2 class="f-h"><span class="ico">🌟</span>Lợi ích khi dùng</h2>%s%s' % (SQ('#58a05f'), check_grid(*benefits))),
        F(commit_steps(commit_l, commit_r, steps3)),
        back_cover(selected),
    ]
    return faces

CAPCUT = dict(
    icon='🎬', name='CapCut Pro',
    tagline='✦ Mở khóa toàn bộ tính năng chỉnh sửa chuyên nghiệp ✦',
    sticker='20k/7 ngày · 80k/30 ngày',
    badges=['🛡️ bảo hành full', '⚡ kích hoạt 2–5 phút'],
    pkgs=[
        dict(icon='🌱', name='Gói 7 ngày', small='Full tính năng Pro · không watermark · BH full', price='20k', unit='/ 7 ngày'),
        dict(icon='🔥', name='Gói 30 ngày', small='Xuất 4K + cloud 100GB · BH full thời gian', price='80k', unit='/ 30 ngày · tiết kiệm ~68%'),
    ],
    cmp_rows=[
        ['Watermark CapCut', ('no', '❌ Có watermark'), ('yes', '✓ Không watermark')],
        ['Hiệu ứng cao cấp', ('no', '🔒 Bị khóa'), ('yes', '✓ Mở khóa toàn bộ')],
        ['Font chữ Premium', ('no', 'Giới hạn'), ('yes', '✓ 500+ font chữ')],
        ['Nhạc bản quyền', ('no', 'Giới hạn'), ('yes', '✓ Kho nhạc không giới hạn')],
        ['Bộ lọc &amp; sticker Pro', ('no', '🔒 Bị khóa'), ('yes', '✓ Toàn bộ bộ lọc Pro')],
        ['Xuất video', ('no', '1080p max'), ('yes', '✓ Xuất 4K chất lượng cao')],
        ['Dung lượng đám mây', ('no', '500MB'), ('yes', '✓ 100GB cloud')],
    ],
    receipt_rows=[('Giá chính hãng CapCut Pro', '~250.000đ / tháng', False),
                  ('Giá tại Sổ Acc Xwuan (30 ngày)', '80.000đ', True)],
    save='🔥 tiết kiệm ~68% · hoặc thử 7 ngày chỉ 20.000đ!',
    benefits=(['<b>Làm video TikTok</b>, Reels, YouTube Shorts',
               'Edit video <b>cho công việc</b> chuyên nghiệp',
               'Sinh viên làm <b>bài tập, project</b> video'],
              ['Freelancer, <b>content creator</b>?',
               'Muốn video <b>đẹp và chuẩn</b> hơn',
               'Phát điên với <b>watermark</b> bản Free 😅']),
    commit_l=['<b>Bảo hành full</b> thời gian sử dụng', 'Kích hoạt trong <b>2–5 phút</b>', 'Dùng cả <b>điện thoại &amp; máy tính</b>'],
    commit_r=['<b>Đổi mới ngay</b> nếu có lỗi', 'Liên hệ <b>bất cứ lúc nào</b>', 'Hướng dẫn cài đặt <b>miễn phí</b>'],
    steps3=[('Nhắn Zalo / Facebook', 'chọn gói 7 ngày hoặc 30 ngày.'),
            ('Xwuan kích hoạt', 'nâng cấp Pro trong 2–5 phút.'),
            ('Sáng tạo thôi!', 'edit thỏa thích · BH suốt thời gian gói.')],
    selected='CapCut Pro',
)

CANVA = dict(
    icon='🎨', name='Canva Pro',
    tagline='✦ 100+ Triệu Mẫu · Xóa Phông 1 Chạm · AI Magic Studio ✦',
    sticker='130k / 1 năm · tiết kiệm ~90%',
    badges=['🛡️ bảo hành 12 tháng', '⚡ kích hoạt 2–5 phút'],
    pkgs=[
        dict(icon='🌿', name='Gói 30 ngày', small='Full tính năng Pro · xóa phông 1 chạm · BH full', price='20k', unit='/ 30 ngày'),
        dict(icon='🔥', name='Gói 1 năm', small='Nâng cấp trên email của bạn · giữ 100% thiết kế cũ', price='130k', unit='/ 1 năm · rẻ hơn ~1,16 triệu'),
    ],
    cmp_rows=[
        ['Kho mẫu &amp; hình ảnh', ('no', 'Giới hạn'), ('yes', '✓ 100M+ mẫu &amp; ảnh Pro')],
        ['Xóa phông', ('no', '🔒 Bị khóa'), ('yes', '✓ Xóa nền 1 click')],
        ['Đổi cỡ Magic Switch', ('no', '🔒 Bị khóa'), ('yes', '✓ Đổi cỡ đa nền tảng')],
        ['AI Magic Studio', ('no', 'Giới hạn lượt'), ('yes', '✓ AI không giới hạn')],
        ['Brand Kit', ('no', '🔒 Không có'), ('yes', '✓ Lưu logo, font, màu')],
        ['Lưu trữ', ('no', '5GB'), ('yes', '✓ 1TB cloud')],
    ],
    receipt_rows=[('Giá chính hãng Canva Pro', '~1.299.000đ / 1 năm', False),
                  ('Giá tại Sổ Acc Xwuan', '130.000đ / 1 năm', True)],
    save='🔥 tiết kiệm ~90% — rẻ hơn 1,16 triệu đồng!',
    benefits=(['Nâng cấp <b>trực tiếp trên email của bạn</b>, giữ 100% thiết kế cũ',
               'Mở khóa toàn bộ <b>ảnh stock, video, đồ họa</b>, font Pro',
               '<b>Xóa phông</b> ảnh &amp; video 1 click'],
              ['Tự động <b>đổi kích thước</b> Story, Banner, Post FB, TikTok',
               '<b>Đồng bộ realtime</b> điện thoại, iPad, máy tính',
               'Kích hoạt qua email trong <b>2–5 phút</b> ⚡']),
    commit_l=['<b>Bảo hành full</b> suốt 12 tháng', 'Gửi lời mời email <b>2–5 phút</b>', '<b>1 đổi 1 ngay</b> nếu gián đoạn'],
    commit_r=['Hỗ trợ Zalo <b>24/7</b> nhiệt tình', 'Dùng trên <b>web + phone + iPad</b>', 'Hướng dẫn <b>miễn phí</b>'],
    steps3=[('Nhắn Zalo', 'gửi email cần nâng cấp Canva Pro.'),
            ('Nhận lời mời Pro', 'kích hoạt trong 2–5 phút.'),
            ('Thiết kế thoải mái', '1TB · AI Magic · BH 1 năm.')],
    selected='Canva Pro',
)

YOUTUBE = dict(
    icon='▶️', name='YouTube Premium',
    tagline='✦ Xem không giới hạn · Không quảng cáo · Nghe nhạc nền ✦',
    sticker='40k / 30 ngày · tiết kiệm ~50%',
    badges=['🛡️ bảo hành full', '🎵 kèm YT Music'],
    pkgs=[
        dict(icon='🎵', name='Gói 30 ngày', small='Chặn 100% quảng cáo · phát nền · kèm YT Music Premium', price='40k', unit='/ 30 ngày'),
    ],
    cmp_rows=[
        ['Quảng cáo', ('no', 'Liên tục 😫'), ('yes', '✓ Không quảng cáo')],
        ['Phát nền', ('no', 'Không hỗ trợ'), ('yes', '✓ Tắt màn hình vẫn nghe')],
        ['Tải offline', ('no', 'Không'), ('yes', '✓ Xem không cần mạng')],
        ['YT Music', ('no', 'Có quảng cáo'), ('yes', '✓ Miễn phí Premium')],
        ['Chất lượng', ('no', 'Tối đa 1080p'), ('yes', '✓ 4K + HDR')],
    ],
    receipt_rows=[('Giá chính hãng', '79.000đ / tháng', False),
                  ('Giá tại Sổ Acc Xwuan', '40.000đ / tháng', True)],
    save='🔥 tiết kiệm ~50% mỗi tháng!',
    benefits=(['<b>Không quảng cáo</b> — xem video liền mạch một giây',
               '<b>Phát nền</b> — tắt màn hình vẫn nghe nhạc',
               '<b>Tải offline</b> xem mọi lúc không cần mạng'],
              ['Kèm <b>YouTube Music Premium</b> không quảng cáo',
               'Xem <b>4K + HDR</b> chất lượng tối đa',
               'Dùng mọi thiết bị: <b>phone, máy tính, TV</b>']),
    commit_l=['<b>Bảo hành full</b> thời gian sử dụng', 'Kích hoạt trong <b>2–5 phút</b>', 'Hỗ trợ mọi thiết bị'],
    commit_r=['<b>Đổi tài khoản</b> nếu có lỗi', 'Phản hồi <b>nhanh mọi lúc</b>', 'Hướng dẫn <b>miễn phí</b>'],
    steps3=[('Nhắn Zalo', 'chọn gói Premium 30 ngày.'),
            ('Xwuan kích hoạt', 'lên Premium trong 2–5 phút.'),
            ('Xem thả ga', 'không quảng cáo · phát nền · YT Music.')],
    selected='YouTube Premium',
)

NETFLIX = dict(
    icon='🍿', name='Netflix 4K UHD',
    tagline='✦ Xem phim không giới hạn · Chuẩn 4K HDR · Mọi thiết bị ✦',
    sticker='45k / 30 ngày · giá hãng 273k!',
    badges=['🛡️ bảo hành full', '🍿 profile + PIN riêng'],
    pkgs=[
        dict(icon='🔥', name='Netflix 4K UHD', small='4K HDR · profile riêng + mã PIN · xem mọi thiết bị', price='45k', unit='/ 30 ngày · trị giá 273k'),
    ],
    cmp_rows=[
        ['Di động', ('no', '480p SD'), ('no', '74.000đ')],
        ['Cơ bản', ('no', '720p HD'), ('no', '114.000đ')],
        ['Tiêu chuẩn', ('no', '1080p FHD'), ('no', '231.000đ')],
        ['Cao cấp (4K)', ('yes', '4K HDR'), ('yes', '45.000đ 🔥 tại sổ')],
    ],
    receipt_rows=[('Giá gốc Netflix Premium (Cao cấp)', '273.000đ / tháng', False),
                  ('Giá tại Sổ Acc Xwuan', '45.000đ / 30 ngày', True)],
    save='🔥 tiết kiệm ~83% — rẻ hơn 228.000đ mỗi tháng!',
    benefits=(['Xem trọn <b>bom tấn &amp; series</b> 4K UHD + HDR',
               'Xem mượt trên <b>Smart TV, laptop, phone, tablet</b>',
               '<b>Profile riêng</b> + mã PIN bảo mật 100%'],
              ['<b>Tải phim offline</b> mọi lúc không cần mạng',
               'Không quảng cáo, âm thanh <b>Dolby Atmos</b>',
               'Nhận tài khoản trong <b>2–5 phút</b> ⚡']),
    commit_l=['<b>Bảo hành full</b> suốt 30 ngày', 'Nhận <b>profile + PIN</b> trong 2–5 phút', '<b>1 đổi 1 ngay</b> nếu lỗi'],
    commit_r=['Hỗ trợ Zalo <b>24/7</b> nhiệt tình', 'Hỗ trợ <b>đổi profile</b> bất kỳ lúc nào', 'Hướng dẫn đăng nhập <b>tận tình</b>'],
    steps3=[('Nhắn Zalo', 'bấm đặt mua hoặc nhắn %s.' % ZALO_TXT),
            ('Nhận tài khoản', 'profile + mã PIN trong 2–5 phút.'),
            ('Bật phim thôi!', 'đăng nhập Netflix và enjoy phim 4K.')],
    selected='Netflix 4K UHD', cmp_head=('Gói', 'Chất lượng', 'Giá'), cmp_hot=3,
)

GEMINI = dict(
    icon='🤖', name='Google AI Pro',
    tagline='✦ Gemini 3.1 Pro · 1 Triệu Token · Google One 2TB ✦',
    sticker='60k / 1 năm · tiết kiệm ~99%',
    badges=['⚡ gói siêu rẻ HSSV', '⚠️ không bảo hành'],
    pkgs=[
        dict(icon='🤯', name='Gói 1 năm', small='Gemini 3.1 Pro · Google One 2TB · kích hoạt sẵn', price='60k', unit='/ 1 năm · rẻ hơn ~5,74 triệu'),
    ],
    cmp_rows=[
        ['Mô hình cốt lõi', ('no', 'Gemini Flash'), ('yes', '✓ Gemini 3.1 Pro')],
        ['Ngữ cảnh Token', ('no', '32.000 tokens'), ('yes', '✓ 1.000.000 tokens')],
        ['Phân tích video &amp; PDF', ('no', '🔒 Giới hạn'), ('yes', '✓ Tải file 1.500 trang')],
        ['Google Workspace', ('no', '🔒 Không có'), ('yes', '✓ Tích hợp Docs, Gmail')],
        ['Vẽ ảnh Imagen 3', ('no', 'Cơ bản'), ('yes', '✓ Ultra HD không giới hạn')],
        ['Lập trình &amp; Debug', ('no', 'Mức vừa'), ('yes', '✓ Chuyên sâu đa ngôn ngữ')],
    ],
    receipt_rows=[('Giá chính hãng Google One AI', '~5.800.000đ / năm', False),
                  ('Giá tại Sổ Acc Xwuan', '60.000đ / 1 năm', True)],
    save='🔥 tiết kiệm ~99% — rẻ hơn 5,7 triệu đồng!',
    warn='⚠️ Gói siêu rẻ phi lợi nhuận cho học sinh, sinh viên — không bảo hành nha!',
    benefits=(['Mô hình <b>Gemini 3.1 Pro</b> tư duy &amp; phân tích vượt trội',
               '<b>Đọc cả sách giáo trình</b> trong vài giây',
               'Viết luận, báo cáo, <b>lập kế hoạch</b> kinh doanh'],
              ['Viết &amp; sửa code <b>Python, JS, C++, SQL</b>',
               'Tạo ảnh nghệ thuật bằng <b>Imagen 3</b>',
               'Kèm <b>Google One 2TB</b> lưu trữ 🗄️']),
    commit_l=['Bàn giao tài khoản trong <b>2–5 phút</b>', 'Hỗ trợ mọi thiết bị', 'Hướng dẫn Zalo <b>24/7</b>'],
    commit_r=['Gói <b>phi lợi nhuận</b> cho HSSV', 'Không bảo hành — <b>giá siết sát nhất</b>', 'Mua nhiều <b>giá tốt hơn</b> 🤝'],
    steps3=[('Nhắn Zalo', 'đăng ký gói Google AI Pro 1 năm.'),
            ('Nhận tài khoản', 'acc kích hoạt sẵn sau 2–5 phút.'),
            ('Sử dụng ngay', 'đăng nhập gemini.google.com trọn 1 năm.')],
    selected='Google AI Pro (Gemini)',
)

MEITU = dict(
    icon='📸', name='Meitu SVIP',
    tagline='✦ Phục chế ảnh AI 4K · Make-up tự nhiên · Full SVIP ✦',
    sticker='90k / 30 ngày · tiết kiệm ~64%',
    badges=['🛡️ bảo hành full', '👑 mở khóa 100% SVIP'],
    pkgs=[
        dict(icon='👑', name='Gói 30 ngày', small='Full SVIP · AI làm nét 4K · xuất sạch không watermark', price='90k', unit='/ 30 ngày'),
    ],
    cmp_rows=[
        ['Làm nét ảnh AI 4K', ('no', '🔒 Bị khóa'), ('yes', '✓ Nét từng sợi tóc')],
        ['Bộ lọc &amp; filter màu', ('no', 'Giới hạn'), ('yes', '✓ 100% SVIP')],
        ['Chỉnh dáng &amp; thon eo', ('no', 'Cơ bản'), ('yes', '✓ Chuẩn tỷ lệ vàng')],
        ['Xóa phông &amp; watermark', ('no', '🔒 Dính logo'), ('yes', '✓ Xuất sạch hoàn toàn')],
        ['Biên tập video cao cấp', ('no', '🔒 Bị khóa'), ('yes', '✓ Đầy đủ hiệu ứng Pro')],
        ['Quảng cáo', ('no', 'Hiện liên tục'), ('yes', '✓ Không quảng cáo')],
    ],
    receipt_rows=[('Giá chính hãng App Store / CH Play', '249.000đ / tháng', False),
                  ('Giá tại Sổ Acc Xwuan', '90.000đ / 30 ngày', True)],
    save='🔥 tiết kiệm ~64% — rẻ hơn 159.000đ mỗi tháng!',
    benefits=(['Phục hồi <b>ảnh cũ, mờ, nhòe</b> thành siêu nét 4K',
               'Trang điểm tự nhiên <b>chuẩn tỷ lệ vàng</b>',
               'Kéo chân, thon gọn <b>không biến dạng</b> bối cảnh'],
              ['Hàng ngàn <b>filter hot trend</b> TikTok &amp; Instagram',
               'Chỉnh màu điện ảnh <b>không watermark</b>',
               'Nhận tài khoản trong <b>2–5 phút</b> ⚡']),
    commit_l=['<b>Bảo hành full</b> trọn 30 ngày', 'Bàn giao tài khoản <b>2–5 phút</b>', 'Mượt trên <b>iPhone, iPad, Android</b>'],
    commit_r=['<b>1 đổi 1 ngay</b> nếu có sự cố', 'Hỗ trợ Zalo <b>24/7</b> nhiệt tình', 'Hướng dẫn sử dụng <b>tận tình</b>'],
    steps3=[('Nhắn Zalo', 'đặt mua Meitu SVIP qua %s.' % ZALO_TXT),
            ('Nhận tài khoản', 'acc kích hoạt sẵn SVIP trong 2–5 phút.'),
            ('Sáng tạo ngay', 'đăng nhập app Meitu và chỉnh ảnh thoải mái.')],
    selected='Meitu SVIP',
)


# ═══════════════════════════ LOCKET — 8 MẶT RIÊNG ═══════════════════════════
LOCKET_NAV = [
    (2, '💛 Gói giá'),
    (3, '🏆 So sánh'),
    (5, '🛡️ Cam kết'),
    (6, '❓ Hỏi đáp'),
    (7, '📞 Đặt Locket')
]

LOCKET_FACES = [
    cover_face('Locket <em>Gold</em>', '✦ Ghim khoảnh khắc · Kết nối người thương ✦',
               'từ 50k · có gói vĩnh viễn ♾️', 'chạm mở sổ xem giá ›',
               'an toàn iCloud · iOS & Android · BH tận tâm', icon='✨', nav=LOCKET_NAV, is_home=False),
    F(toc_face([(2, '💰 Gói giá Locket'), (3, '🏆 Gold vs Free'), (4, '💡 Mẹo hay khi dùng'),
                (5, '🛡️ Cam kết &amp; 3 bước'), (6, '❓ Hỏi – đáp'), (7, '📞 Liên hệ &amp; đặt acc')])),
    F('<h2 class="f-h"><span class="ico">💰</span>Gói giá Locket</h2>%s'
      '<div class="mini2">'
      '<div class="mini"><h4>🎥 Quay 5s</h4><ul class="p3"><li>6 tháng <b>50k</b></li><li>1 năm <b>80k</b></li><li>vĩnh viễn ♾️ <b>150k</b></li></ul></div>'
      '<div class="mini"><h4>🎬 Quay 15s</h4><ul class="p3"><li>6 tháng <b>60k</b></li><li>1 năm <b>100k</b></li><li>vĩnh viễn ♾️ <b>180k</b></li></ul></div>'
      '</div>%s'
      '<a class="btn btn-green" href="%s" target="_blank" rel="noopener" style="margin-top:.5em">💬 Chốt gói Locket qua Zalo</a>'
      % (SQ(), '<div style="text-align:center"><span class="warn-note">💡 gói vĩnh viễn hỗ trợ miễn phí kể cả khi đổi máy mới!</span></div>', ZALO)),
    F('<h2 class="f-h"><span class="ico">🏆</span>Locket Thường vs Gold</h2>%s%s'
      % (SQ('#4a7fb5'), cmp_face(['Tính năng', 'Free 😴', 'Gold ✨'], [
          ['Quảng cáo', ('no', 'Chèn quảng cáo'), ('yes', '✓ Không quảng cáo')],
          ['Video Locket', ('no', 'Giới hạn'), ('yes', '✓ Video 5s hoặc 15s')],
          ['Tải ảnh từ thư viện', ('no', 'Chỉ chụp trực tiếp'), ('yes', '✓ Tải mọi ảnh từ máy')],
          ['Biểu tượng App', ('no', 'Mặc định'), ('yes', '✓ Nhiều icon tùy chỉnh')],
          ['Huy hiệu Gold', ('no', 'Không có'), ('yes', '✓ Huy hiệu đặc quyền')],
      ]))),
    F('<h2 class="f-h"><span class="ico">💡</span>Mẹo hay khi dùng</h2>%s%s'
      % (SQ('#58a05f'), check_grid(
          ['<b>An toàn tuyệt đối</b> — không ảnh hưởng iCloud cá nhân',
           'Hỗ trợ cả <b>iOS &amp; Android</b>',
           'Ghim <b>ảnh + video 5s/15s</b> cho người thương'],
          ['<b>Đổi máy mới</b> vẫn hỗ trợ miễn phí',
           'Kích hoạt nhanh <b>2–5 phút</b>',
           'Tùy chỉnh <b>icon app</b> đẹp theo ý 🎨']))),
    F(commit_steps(
        ['<b>An toàn 100%</b> — không đụng iCloud của bạn',
         '<b>Bảo hành</b> trong thời gian sử dụng',
         'Kích hoạt <b>2–5 phút</b> sau chốt đơn'],
        ['Đổi máy mới <b>hỗ trợ miễn phí</b>',
         'Liên hệ <b>bất cứ lúc nào</b>, phản hồi nhanh',
         'Hướng dẫn cài <b>tận tình</b>'],
        [('Nhắn Zalo / Facebook', 'chọn gói Quay 5s / 15s + thời gian.'),
         ('Kích hoạt nhanh', 'xử lý Locket Gold trong 2–5 phút.'),
         ('Ghim ảnh thoải mái', 'tận hưởng Gold · BH suốt thời gian gói.')])),
    F(faq_face([
        ('Locket Gold là gì?', 'Widget ảnh đồng bộ từ người thương tới màn hình chính điện thoại — bản Gold cho gửi <b>video 5s/15s</b>, tải ảnh từ thư viện, không quảng cáo.'),
        ('Có an toàn với iCloud không?', '<b>An toàn tuyệt đối</b> — kích hoạt bằng tài khoản riêng, không đụng vào iCloud cá nhân của bạn.'),
        ('Đổi điện thoại mới dùng lại được không?', 'Có! <b>Hỗ trợ miễn phí</b> khi bạn đổi máy mới — chỉ cần nhắn Zalo là được xử lý.'),
    ], title='Hỏi – đáp về Locket')),
    back_cover('Locket Gold'),
]


# ═══════════════════════════ WINDOWS & OFFICE — 8 MẶT RIÊNG ═══════════════════════════
WIN_NAV = [
    (2, '🪟 Bảng giá'),
    (3, '🔥 Combo rẻ'),
    (4, '🤝 Cam kết'),
    (5, '🚀 3 bước'),
    (7, '📞 Đặt lịch')
]

WIN_FACES = [
    cover_face('Windows <em>&amp; Office</em>', '✦ Cài đặt kỹ thuật · Giá minh bạch · Giữ nguyên dữ liệu ✦',
               'từ 80k · BH lỗi phát sinh 6 tháng', 'chạm mở sổ xem giá ›',
               'ISO gốc Microsoft · xong 30–60 phút', icon='💻', nav=WIN_NAV, is_home=False),
    F(toc_face([(2, '💰 Bảng giá dịch vụ'), (3, '🔥 Combo gộp tiết kiệm'), (4, '🤝 Cam kết khi cài'),
                (5, '🚀 3 bước nhanh gọn'), (6, '❓ Hỏi – đáp'), (7, '📞 Liên hệ &amp; đặt lịch')])),
    F('<h2 class="f-h"><span class="ico">💰</span>Bảng giá dịch vụ</h2>%s%s%s%s'
      '<p class="f-note">💰 chọn <b>combo</b> ở trang sau sẽ rẻ hơn đó!</p>'
      % (SQ(),
         prow('🪟', 'Windows Chuẩn Microsoft', 'ISO gốc · driver đầy đủ · ổn định cao', '150k–180k', '/ lần cài'),
         prow('⚡', 'Windows Tối Ưu', 'nhẹ – mượt cho máy cũ / RAM 4GB', '100k–120k', '/ lần cài'),
         prow('📘', 'Microsoft Office', 'Word, Excel, PowerPoint · 365/2021/2019', '80k–120k', '/ lần cài'))),
    F('<h2 class="f-h"><span class="ico">🔥</span>Combo gộp — càng mua càng rẻ</h2>%s%s%s'
      % (SQ('#58a05f'),
         receipt_face([('Win Chuẩn + Office', '200k – 220k', True),
                       ('Win Tối Ưu + Office', '160k – 180k', True)],
                      '🔥 gộp combo tiết kiệm ~20k – 30k · bảo hành lỗi phát sinh!',
                      '<span class="warn-note">💾 cài xong trong 30–60 phút · giữ nguyên toàn bộ dữ liệu cũ!</span>'),
         '<a class="btn btn-green" href="%s" target="_blank" rel="noopener" style="margin-top:.5em">📞 Đặt lịch cài qua Zalo</a>' % ZALO)),
    F('<h2 class="f-h"><span class="ico">🤝</span>Cam kết khi cài</h2>%s%s'
      % (SQ('#d94f43'), check_grid(
          ['<b>Sao lưu dữ liệu an toàn</b> — giữ nguyên dữ liệu cũ',
           '<b>Bảo hành lỗi phát sinh 6 tháng</b>',
           'ISO <b>chuẩn gốc Microsoft</b>'],
          ['Không <b>bloatware</b>, không phần mềm rác',
           'Xong trong <b>30–60 phút</b>',
           'Hỗ trợ <b>sau cài đặt</b> tận tình 🤝']))),
    F('<h2 class="f-h"><span class="ico">🚀</span>Đặt lịch — 3 bước</h2>%s<ol class="steps">'
      '<li><span class="num">1</span><h4>Nhắn Zalo</h4><p>máy bạn đang dùng gì, muốn cài gói nào?</p></li>'
      '<li><span class="num">2</span><h4>Hẹn lịch cài</h4><p>hướng dẫn / hẹn giờ — xong trong 30–60 phút.</p></li>'
      '<li><span class="num">3</span><h4>Dùng kèm bảo hành</h4><p>BH lỗi phát sinh đến 6 tháng sau cài.</p></li>'
      '</ol>' % SQ('#58a05f')),
    F(faq_face([
        ('Cài win có mất dữ liệu không?', '<b>Không</b> — mình sao lưu dữ liệu an toàn trước khi cài, xong trả lại nguyên trạng. Bạn vẫn được dặn dò kiểm tra trước khi nghiệm thu.'),
        ('Cần chuẩn bị gì trước khi cài?', 'Chỉ cần máy sạc đầy pin / cắm điện + kết nối mạng. File, tài khoản quan trọng nên ghi chú lại password trước khi cài nha.'),
        ('Sau cài có được hỗ trợ không?', 'Có — <b>bảo hành lỗi phát sinh 6 tháng</b>, hỗ trợ cài lại driver, phần mềm cơ bản miễn phí qua Zalo.'),
    ], title='Hỏi – đáp khi cài Win')),
    back_cover('Windows / Office'),
]
WIN_NAV = [(2, 'BẢNG GIÁ'), (3, 'COMBO'), (4, 'CAM KẾT'), (7, 'LIÊN HỆ')]
