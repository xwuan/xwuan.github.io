# -*- coding: utf-8 -*-
"""Build toàn bộ website Sổ Acc Xwuan — chạy: python3 build.py"""
from shell import render_page
import pages_data as D

# ═══════════════════════════ 1. TRANG CHỦ ═══════════════════════════
render_page(
    'index.html',
    'Sổ Acc Xwuan 📓 | Acc rẻ chỉ 2–5/10 giá gốc — CapCut, Canva, Netflix, Gemini…',
    'Acc premium giá học sinh: CapCut Pro 20k, Canva Pro 130k/năm, Netflix 4K 45k, YouTube 40k, Gemini 60k/năm. Kích hoạt 2–5 phút, bảo hành full, hỗ trợ 24/24.',
    D.INDEX_TABS,
    D.INDEX_CONTENT,
    selected_acc=None,
)

# ═══════════════════════════ 2. CAPCUT ═══════════════════════════
c = D.d_hero('🎬', '🛡️ Bảo hành full thời gian', 'CapCut Pro', '✦ Mở khóa toàn bộ tính năng chỉnh sửa chuyên nghiệp ✦')
c += """
      <section class="sec" id="goigoi">
        <h2 class="h-scrap"><span class="ico">💰</span>Gói giá trong sổ</h2>
        """ + D.SQUIG_RED + """
        <div class="cards" style="grid-template-columns:repeat(auto-fit,minmax(240px,330px));justify-content:center">
          """ + D.pkg_card('b-blue', '✨ THỬ NHẸ TRƯỚC', 'Gói 7 ngày', '20k', '7 ngày',
                           ['Full tính năng Pro', 'Không watermark', 'Bảo hành full thời gian']) + """
          """ + D.pkg_card('b-pink', '🔥 PHỔ BIẾN NHẤT', 'Gói 30 ngày', '80k', '30 ngày',
                           ['Full tính năng Pro', 'Xuất 4K + cloud 100GB', 'Bảo hành full thời gian'],
                           deal='tiết kiệm ~68% so với giá hãng') + """
        </div>
      </section>
      <section class="sec" id="sosanh">
        <h2 class="h-scrap"><span class="ico">⚖️</span>So sánh: Free vs Pro</h2>
        """ + D.SQUIG_BLUE + """
        """ + D.cmp_table(
            ['Tính năng', 'Free 😐', 'Pro ✨'],
            [
                ['Watermark CapCut', ('no', '❌ Có watermark'), ('yes', '✓ Không watermark')],
                ['Hiệu ứng cao cấp', ('no', '🔒 Bị khóa'), ('yes', '✓ Mở khóa toàn bộ')],
                ['Font chữ Premium', ('no', 'Giới hạn'), ('yes', '✓ 500+ font chữ')],
                ['Nhạc bản quyền', ('no', 'Giới hạn'), ('yes', '✓ Kho nhạc không giới hạn')],
                ['Bộ lọc &amp; sticker Pro', ('no', '🔒 Bị khóa'), ('yes', '✓ Toàn bộ bộ lọc Pro')],
                ['Xuất video', ('no', '1080p max'), ('yes', '✓ Xuất 4K chất lượng cao')],
                ['Dung lượng đám mây', ('no', '500MB'), ('yes', '✓ 100GB cloud')],
            ]) + """
        """ + D.receipt(
            [('Giá chính hãng CapCut Pro', '~250.000đ / tháng', False),
             ('Giá tại Sổ Acc Xwuan (30 ngày)', '80.000đ', True)],
            '🔥 Tiết kiệm ~68% · hoặc thử 7 ngày chỉ 20.000đ!') + """
      </section>
      <section class="sec" id="aine">
        <h2 class="h-scrap"><span class="ico">🙋</span>Ai nên dùng CapCut Pro?</h2>
        """ + D.SQUIG_GREEN + """
        """ + D.check2col(
            ['<b>Làm video TikTok</b>, Reels, YouTube Shorts',
             'Chỉnh ảnh, edit video <b>cho công việc</b>',
             'Sinh viên làm <b>bài thuyết trình</b>, video project'],
            ['Freelancer, <b>content creator</b> cần công cụ chuyên nghiệp',
             'Bất kỳ ai muốn video <b>đẹp và chuẩn</b> hơn',
             'Bạn từng phát điên với <b>watermark</b> bản Free 😅']) + """
      </section>"""
c += D.camket_section(
    'Cam kết từ Xwuan', D.SQUIG_RED,
    D.check2col(['<b>Bảo hành full</b> thời gian sử dụng',
                 'Kích hoạt trong <b>2–5 phút</b>',
                 'Hỗ trợ cả <b>điện thoại và máy tính</b>'],
                ['Hỗ trợ <b>đổi mới nếu có lỗi</b>',
                 'Liên hệ <b>bất cứ lúc nào</b> — phản hồi nhanh',
                 'Hướng dẫn cài đặt <b>tận tình miễn phí</b>']),
    D.steps(('Nhắn Zalo / Facebook', 'Chọn gói 7 ngày hoặc 30 ngày, chốt đơn ngay.'),
            ('Xwuan kích hoạt', 'Nâng cấp CapCut Pro cho bạn trong 2–5 phút.'),
            ('Sáng tạo thôi!', 'Edit video thỏa thích · bảo hành suốt thời gian gói.')))
render_page('capcut.html',
            'CapCut Pro giá rẻ — chỉ 20k/7 ngày, 80k/30 ngày | Sổ Acc Xwuan',
            'CapCut Pro không watermark, hiệu ứng Premium, xuất 4K. Giá hãng ~250k/tháng, tại Xwuan chỉ 80k/30 ngày — bảo hành full thời gian.',
            D.DET_TABS, c, selected_acc='CapCut Pro')

# ═══════════════════════════ 3. CANVA ═══════════════════════════
c = D.d_hero('🎨', '✨ 100+ triệu mẫu Pro · AI Magic Studio', 'Canva Pro', '✦ 100+ Triệu Mẫu · Xóa Phông 1 Chạm · AI Magic Studio ✦')
c += """
      <section class="sec" id="goigoi">
        <h2 class="h-scrap"><span class="ico">💰</span>Gói giá trong sổ</h2>
        """ + D.SQUIG_RED + """
        <div class="cards" style="grid-template-columns:repeat(auto-fit,minmax(240px,330px));justify-content:center">
          """ + D.pkg_card('b-blue', '🌿 THỬ TRƯỚC', 'Gói 30 ngày', '20k', '30 ngày',
                           ['Full tính năng Pro', 'Xóa phông 1 chạm', 'Bảo hành full thời gian']) + """
          """ + D.pkg_card('b-pink', '🔥 TIẾT KIỆM NHẤT', 'Gói 1 Năm', '130k', '1 năm',
                           ['Full Pro trọn 12 tháng', 'Nâng cấp trên email cá nhân', 'Giữ 100% thiết kế cũ'],
                           deal='tiết kiệm ~90% (~1,16 triệu)') + """
        </div>
      </section>
      <section class="sec" id="sosanh">
        <h2 class="h-scrap"><span class="ico">⚖️</span>So sánh: Miễn phí vs Canva Pro</h2>
        """ + D.SQUIG_BLUE + """
        """ + D.cmp_table(
            ['Tính năng', 'Bản Thường 😐', 'Canva Pro ✨'],
            [
                ['Kho mẫu &amp; hình ảnh', ('no', 'Giới hạn'), ('yes', '✓ 100M+ mẫu &amp; ảnh Pro')],
                ['Xóa phông (Background Remover)', ('no', '🔒 Bị khóa'), ('yes', '✓ Xóa nền 1 click')],
                ['Đổi cỡ Magic Switch', ('no', '🔒 Bị khóa'), ('yes', '✓ Đổi cỡ đa nền tảng')],
                ['AI Magic Studio', ('no', 'Giới hạn lượt dùng'), ('yes', '✓ Trọn bộ AI không giới hạn')],
                ['Brand Kit (thương hiệu)', ('no', '🔒 Không có'), ('yes', '✓ Lưu logo, font, màu sắc')],
                ['Dung lượng lưu trữ', ('no', '5GB'), ('yes', '✓ 1TB cloud')],
            ]) + """
        """ + D.receipt(
            [('Giá mua chính hãng Canva Pro', '~1.299.000đ / 1 năm', False),
             ('Giá tại Sổ Acc Xwuan', '130.000đ / 1 năm', True)],
            '🔥 Tiết kiệm ~90% — rẻ hơn 1,16 triệu đồng!') + """
      </section>
      <section class="sec" id="loiich">
        <h2 class="h-scrap"><span class="ico">🌟</span>Lợi ích Canva Pro</h2>
        """ + D.SQUIG_GREEN + """
        """ + D.check2col(
            ['Nâng cấp <b>trực tiếp trên email của bạn</b>, giữ 100% thiết kế cũ',
             'Mở khóa toàn bộ <b>ảnh stock, video, đồ họa</b> và font Pro',
             '<b>Xóa phông</b> ảnh &amp; video chỉ 1 click, chuẩn xác'],
            ['Tự động <b>đổi kích thước</b> sang Story, Banner, Post Facebook, TikTok',
             '<b>Đồng bộ thời gian thực</b> trên điện thoại, iPad, máy tính',
             'Kích hoạt qua email trong <b>2–5 phút</b> ⚡']) + """
      </section>"""
c += D.camket_section(
    'Cam kết từ Xwuan', D.SQUIG_RED,
    D.check2col(['<b>Bảo hành full</b> suốt 12 tháng sử dụng',
                 'Kích hoạt &amp; gửi lời mời qua email <b>2–5 phút</b>',
                 '<b>1 đổi 1 ngay</b> nếu gặp bất kỳ gián đoạn nào'],
                ['Hỗ trợ kỹ thuật qua Zalo <b>24/7</b> nhiệt tình',
                 'Dùng được trên <b>web + điện thoại + iPad</b>',
                 'Hướng dẫn tận tình <b>miễn phí</b>']),
    D.steps(('Nhắn Zalo / Facebook', 'Gửi email cần nâng cấp Canva Pro.'),
            ('Nhận lời mời Pro', 'Xwuan gửi lời mời kích hoạt trong 2–5 phút.'),
            ('Thiết kế thoải mái', '1TB lưu trữ · AI Magic · bảo hành 1 năm.')))
render_page('canva.html',
            'Canva Pro 1 năm chỉ 130k — tiết kiệm ~90% | Sổ Acc Xwuan',
            'Canva Pro: 100M+ mẫu Premium, xóa phông 1 chạm, AI Magic Studio, 1TB cloud. Giá hãng ~1.299k/năm, tại Xwuan chỉ 130k/năm hoặc 20k/30 ngày.',
            D.DET_TABS, c, selected_acc='Canva Pro')

# ═══════════════════════════ 4. YOUTUBE ═══════════════════════════
c = D.d_hero('▶️', '🛡️ Bảo hành full thời gian', 'YouTube Premium', '✦ Xem không giới hạn · Không quảng cáo · Nghe nhạc nền ✦')
c += """
      <section class="sec" id="goigoi">
        <h2 class="h-scrap"><span class="ico">💰</span>Gói giá trong sổ</h2>
        """ + D.SQUIG_RED + """
        <div class="cards" style="grid-template-columns:minmax(0,360px);justify-content:center">
          """ + D.pkg_card('b-pink', '🎵 KÈM YT MUSIC', 'Gói 30 ngày', '40k', '30 ngày',
                           ['Chặn 100% quảng cáo', 'Tắt màn hình vẫn nghe nhạc', 'Kèm YouTube Music Premium'],
                           deal='tiết kiệm ~50% mỗi tháng so với giá hãng') + """
        </div>
      </section>
      <section class="sec" id="sosanh">
        <h2 class="h-scrap"><span class="ico">⚖️</span>So sánh: Free vs Premium</h2>
        """ + D.SQUIG_BLUE + """
        """ + D.cmp_table(
            ['Tính năng', 'Free 😢', 'Premium ✨'],
            [
                ['Quảng cáo', ('no', 'Liên tục 😫'), ('yes', '✓ Không quảng cáo')],
                ['Phát nền', ('no', 'Không hỗ trợ'), ('yes', '✓ Tắt màn hình vẫn nghe nhạc')],
                ['Tải offline', ('no', 'Không'), ('yes', '✓ Xem không cần mạng')],
                ['YT Music', ('no', 'Có quảng cáo'), ('yes', '✓ Miễn phí Premium')],
                ['Chất lượng', ('no', 'Tối đa 1080p'), ('yes', '✓ 4K + HDR')],
            ]) + """
        """ + D.receipt(
            [('Giá chính hãng', '79.000đ / tháng', False),
             ('Giá tại Sổ Acc Xwuan', '40.000đ / tháng', True)],
            '🔥 Tiết kiệm ~50% mỗi tháng!') + """
      </section>"""
c += D.camket_section(
    'Cam kết từ Xwuan', D.SQUIG_RED,
    D.check2col(['<b>Bảo hành full</b> thời gian sử dụng',
                 'Kích hoạt trong <b>2–5 phút</b>',
                 'Hỗ trợ mọi thiết bị: <b>điện thoại, máy tính, TV</b>'],
                ['Hỗ trợ <b>đổi tài khoản</b> nếu có lỗi',
                 'Liên hệ bất cứ lúc nào, <b>phản hồi nhanh</b>',
                 'Hướng dẫn cài đặt <b>tận tình miễn phí</b>']),
    D.steps(('Nhắn Zalo / Facebook', 'Chọn gói YouTube Premium 30 ngày.'),
            ('Xwuan kích hoạt', 'Kích hoạt Premium cho bạn trong 2–5 phút.'),
            ('Xem thả ga', 'Không quảng cáo · phát nền · kèm YT Music.')))
render_page('youtube.html',
            'YouTube Premium chỉ 40k/tháng — không quảng cáo | Sổ Acc Xwuan',
            'YouTube Premium: chặn 100% quảng cáo, phát nền, tải offline, kèm YT Music Premium, 4K HDR. Giá hãng 79k/tháng, tại Xwuan chỉ 40k/tháng.',
            D.DET_TABS, c, selected_acc='YouTube Premium')

# ═══════════════════════════ 5. NETFLIX ═══════════════════════════
c = D.d_hero('🍿', '🛡️ Bảo hành full thời gian', 'Netflix 4K UHD', '✦ Xem phim không giới hạn · Chuẩn 4K HDR · Mọi thiết bị ✦')
c += """
      <section class="sec" id="goigoi">
        <h2 class="h-scrap"><span class="ico">💰</span>Gói giá trong sổ</h2>
        """ + D.SQUIG_RED + """
        <div class="cards" style="grid-template-columns:minmax(0,360px);justify-content:center">
          """ + D.pkg_card('b-pink', '🔥 GÓI CAO CẤP NHẤT', 'Netflix 4K UHD', '45k', '30 ngày',
                           ['Chất lượng 4K UHD + HDR', 'Profile riêng + mã PIN bảo mật', 'Xem trên TV, laptop, điện thoại'],
                           deal='chỉ trả 45k cho gói trị giá 273.000đ!') + """
        </div>
      </section>
      <section class="sec" id="sosanh">
        <h2 class="h-scrap"><span class="ico">⚖️</span>So sánh: các gói Netflix</h2>
        """ + D.SQUIG_BLUE + """
        """ + D.cmp_table(
            ['Gói', 'Chất lượng', 'Giá'],
            [
                ['Di động', ('no', '480p SD'), ('no', '74.000đ')],
                ['Cơ bản', ('no', '720p HD'), ('no', '114.000đ')],
                ['Tiêu chuẩn', ('no', '1080p FHD'), ('no', '231.000đ')],
                ['Cao cấp (4K)', ('yes', '4K HDR'), ('yes', '45.000đ 🔥 tại sổ')],
            ], hot_row=3) + """
        """ + D.receipt(
            [('Giá gốc Netflix Premium (Cao cấp)', '273.000đ / tháng', False),
             ('Giá tại Sổ Acc Xwuan', '45.000đ / 30 ngày', True)],
            '🔥 Tiết kiệm ~83% — rẻ hơn 228.000đ mỗi tháng!') + """
      </section>
      <section class="sec" id="loiich">
        <h2 class="h-scrap"><span class="ico">🌟</span>Lợi ích Netflix Premium</h2>
        """ + D.SQUIG_GREEN + """
        """ + D.check2col(
            ['Xem trọn <b>bom tấn &amp; series</b> chất lượng 4K UHD + HDR',
             'Xem mượt trên <b>Smart TV, laptop, điện thoại, tablet</b>',
             '<b>Profile cá nhân riêng</b> + mã PIN bảo mật 100%'],
            ['<b>Tải phim offline</b> xem mọi lúc không cần mạng',
             'Không quảng cáo, âm thanh vòm <b>Dolby Atmos</b> như rạp phim',
             'Nhận tài khoản trong <b>2–5 phút</b> ⚡']) + """
      </section>"""
c += D.camket_section(
    'Cam kết từ Xwuan', D.SQUIG_RED,
    D.check2col(['<b>Bảo hành full</b> suốt 30 ngày sử dụng',
                 'Nhận <b>profile + mã PIN</b> trong 2–5 phút',
                 '<b>1 đổi 1 ngay</b> nếu gặp lỗi'],
                ['Hỗ trợ kỹ thuật qua Zalo <b>24/7</b> nhiệt tình',
                 'Hỗ trợ <b>đổi profile</b> bất kỳ lúc nào',
                 'Hướng dẫn đăng nhập <b>tận tình</b>']),
    D.steps(('Nhắn Zalo', 'Bấm nút đặt mua hoặc nhắn 0822.307.662.'),
            ('Nhận tài khoản', 'Nhận profile + mã PIN đăng nhập trong 2–5 phút.'),
            ('Bật phim thôi!', 'Đăng nhập Netflix và thưởng thức phim 4K thỏa thích.')))
render_page('netflix.html',
            'Netflix 4K UHD chỉ 45k/tháng — tiết kiệm ~83% | Sổ Acc Xwuan',
            'Netflix Premium 4K HDR giá hãng 273k/tháng, tại Xwuan chỉ 45k/30 ngày. Profile riêng, mã PIN riêng, xem mọi thiết bị, bảo hành full.',
            D.DET_TABS, c, selected_acc='Netflix 4K UHD')

# ═══════════════════════════ 6. GOOGLE AI ═══════════════════════════
c = D.d_hero('🤖', '⚡ Gói siêu tiết kiệm cho HSSV', 'Google AI Pro', '✦ Gemini 3.1 Pro Siêu Thông Minh · 1 Triệu Token · Google One 2TB ✦')
c += """
      <section class="sec" id="goigoi">
        <h2 class="h-scrap"><span class="ico">💰</span>Gói giá trong sổ</h2>
        """ + D.SQUIG_RED + """
        <div class="cards" style="grid-template-columns:minmax(0,360px);justify-content:center">
          """ + D.pkg_card('b-gray', '⚠️ KHÔNG BẢO HÀNH', 'Gói 1 Năm', '60k', '1 năm',
                           ['Gemini 3.1 Pro trọn năm', 'Google One 2TB', 'Kích hoạt sẵn trong 2–5 phút'],
                           deal='rẻ hơn ~5,74 triệu so với giá hãng 🤯') + """
        </div>
        <p class="warn-note">⚠️ Gói giá siêu rẻ phi lợi nhuận cho học sinh, sinh viên — không bảo hành nha!</p>
      </section>
      <section class="sec" id="sosanh">
        <h2 class="h-scrap"><span class="ico">⚖️</span>So sánh: Miễn phí vs AI Pro</h2>
        """ + D.SQUIG_BLUE + """
        """ + D.cmp_table(
            ['Tính năng', 'Bản Thường 😐', 'Google AI Pro ✨'],
            [
                ['Mô hình cốt lõi', ('no', 'Gemini Flash'), ('yes', '✓ Gemini 3.1 Pro')],
                ['Ngữ cảnh Token', ('no', '32.000 tokens'), ('yes', '✓ 1.000.000 tokens')],
                ['Phân tích video &amp; PDF', ('no', '🔒 Bị giới hạn'), ('yes', '✓ Tải file 1.500 trang')],
                ['Google Workspace', ('no', '🔒 Không có'), ('yes', '✓ Tích hợp Docs, Gmail')],
                ['Vẽ ảnh AI Imagen 3', ('no', 'Chất lượng cơ bản'), ('yes', '✓ Ultra HD không giới hạn')],
                ['Lập trình &amp; Debug', ('no', 'Mức độ vừa'), ('yes', '✓ Chuyên sâu đa ngôn ngữ')],
            ]) + """
        """ + D.receipt(
            [('Giá chính hãng Google One AI', '~5.800.000đ / năm', False),
             ('Giá tại Sổ Acc Xwuan', '60.000đ / 1 năm', True)],
            '🔥 Tiết kiệm ~99% — rẻ hơn 5,7 triệu đồng!') + """
      </section>
      <section class="sec" id="loiich">
        <h2 class="h-scrap"><span class="ico">🌟</span>Lợi ích Google AI Pro</h2>
        """ + D.SQUIG_GREEN + """
        """ + D.check2col(
            ['Mô hình <b>Gemini 3.1 Pro</b> — tư duy &amp; phân tích vượt trội',
             'Xử lý tài liệu khổng lồ, <b>đọc cả sách giáo trình</b> trong vài giây',
             'Viết luận, báo cáo khoa học, <b>lập kế hoạch</b> kinh doanh'],
            ['Viết &amp; sửa lỗi code <b>Python, JS, C++, SQL</b> chính xác cao',
             'Tạo ảnh minh họa nghệ thuật bằng <b>Imagen 3</b>',
             'Kèm <b>Google One 2TB</b> lưu trữ cloud 🗄️']) + """
      </section>"""
c += D.camket_section(
    'Cam kết từ Xwuan', D.SQUIG_RED,
    D.check2col(['Kích hoạt &amp; bàn giao tài khoản trong <b>2–5 phút</b>',
                 'Hỗ trợ mọi thiết bị: <b>máy tính, điện thoại, tablet</b>',
                 'Hướng dẫn sử dụng tận tình qua <b>Zalo 24/7</b>'],
                ['Gói <b>phi lợi nhuận</b> cho học sinh, sinh viên',
                 'Không bảo hành — <b>giá siết sát nhất</b> có thể',
                 'Mua nhiều được <b>xem giá tốt hơn</b> 🤝']),
    D.steps(('Nhắn Zalo', 'Đăng ký gói Google AI Pro 1 năm.'),
            ('Nhận tài khoản', 'Nhận acc kích hoạt sẵn Gemini 3.1 Pro sau 2–5 phút.'),
            ('Sử dụng ngay', 'Đăng nhập gemini.google.com và trải nghiệm trọn 1 năm.')))
render_page('google-ai.html',
            'Google AI Pro (Gemini 3.1 Pro) chỉ 60k/năm — tiết kiệm ~99% | Sổ Acc Xwuan',
            'Gemini 3.1 Pro, ngữ cảnh 1 triệu token, Imagen 3, Google One 2TB. Giá hãng ~5,8 triệu/năm, tại Xwuan chỉ 60k/năm — gói siêu rẻ cho học sinh sinh viên.',
            D.DET_TABS, c, selected_acc='Google AI Pro (Gemini)')

# ═══════════════════════════ 7. MEITU ═══════════════════════════
c = D.d_hero('📸', '🛡️ Bảo hành full thời gian', 'Meitu SVIP', '✦ Phục chế ảnh AI 4K · Make-up tự nhiên · Mở khóa 100% SVIP ✦')
c += """
      <section class="sec" id="goigoi">
        <h2 class="h-scrap"><span class="ico">💰</span>Gói giá trong sổ</h2>
        """ + D.SQUIG_RED + """
        <div class="cards" style="grid-template-columns:minmax(0,360px);justify-content:center">
          """ + D.pkg_card('b-pink', '👑 FULL SVIP', 'Gói 30 ngày', '90k', '30 ngày',
                           ['Mở khóa 100% tính năng SVIP', 'AI làm nét &amp; phục chế 4K', 'Xuất ảnh sạch, không watermark'],
                           deal='tiết kiệm ~64% so với giá App Store/CH Play') + """
        </div>
      </section>
      <section class="sec" id="sosanh">
        <h2 class="h-scrap"><span class="ico">⚖️</span>So sánh: Miễn phí vs Meitu SVIP</h2>
        """ + D.SQUIG_BLUE + """
        """ + D.cmp_table(
            ['Tính năng', 'Bản Thường 😐', 'Meitu SVIP ✨'],
            [
                ['Làm nét ảnh AI 4K', ('no', '🔒 Bị khóa'), ('yes', '✓ Nét từng sợi tóc')],
                ['Bộ lọc &amp; filter màu', ('no', 'Giới hạn'), ('yes', '✓ Mở khóa 100% SVIP')],
                ['Chỉnh dáng &amp; thon eo', ('no', 'Cơ bản'), ('yes', '✓ Chuẩn tỷ lệ vàng')],
                ['Xóa phông &amp; watermark', ('no', '🔒 Dính logo'), ('yes', '✓ Xuất sạch hoàn toàn')],
                ['Biên tập video cao cấp', ('no', '🔒 Bị khóa'), ('yes', '✓ Đầy đủ hiệu ứng Pro')],
                ['Quảng cáo phiền toái', ('no', 'Hiện liên tục'), ('yes', '✓ Không quảng cáo')],
            ]) + """
        """ + D.receipt(
            [('Giá mua chính hãng App Store/CH Play', '249.000đ / tháng', False),
             ('Giá tại Sổ Acc Xwuan', '90.000đ / 30 ngày', True)],
            '🔥 Tiết kiệm ~64% — rẻ hơn 159.000đ mỗi tháng!') + """
      </section>
      <section class="sec" id="loiich">
        <h2 class="h-scrap"><span class="ico">🌟</span>Lợi ích Meitu SVIP</h2>
        """ + D.SQUIG_GREEN + """
        """ + D.check2col(
            ['Phục hồi <b>ảnh cũ, mờ, nhòe</b> thành ảnh siêu nét 4K',
             'Trang điểm tự nhiên, chỉnh nét mặt <b>chuẩn tỷ lệ vàng</b>',
             'Kéo chân, thon gọn <b>không biến dạng</b> bối cảnh'],
            ['Hàng ngàn <b>filter hot trend</b> TikTok &amp; Instagram',
             'Biên tập video, chỉnh màu điện ảnh <b>không watermark</b>',
             'Nhận tài khoản trong <b>2–5 phút</b> ⚡']) + """
      </section>"""
c += D.camket_section(
    'Cam kết từ Xwuan', D.SQUIG_RED,
    D.check2col(['<b>Bảo hành full</b> trọn vẹn 30 ngày',
                 'Kích hoạt &amp; bàn giao tài khoản <b>2–5 phút</b>',
                 'Mượt trên cả <b>iPhone, iPad, Android</b>'],
                ['<b>1 đổi 1 ngay</b> nếu có sự cố',
                 'Hỗ trợ kỹ thuật Zalo <b>24/7</b> nhiệt tình',
                 'Hướng dẫn sử dụng <b>tận tình</b>']),
    D.steps(('Nhắn Zalo', 'Đặt mua Meitu SVIP qua Zalo 0822.307.662.'),
            ('Nhận tài khoản', 'Nhận acc kích hoạt sẵn SVIP trong 2–5 phút.'),
            ('Sáng tạo ngay', 'Đăng nhập app Meitu và chỉnh ảnh thỏa sức.')))
render_page('meitu.html',
            'Meitu SVIP chỉ 90k/30 ngày — full tính năng SVIP | Sổ Acc Xwuan',
            'Meitu SVIP: AI làm nét 4K, filter hot trend, chỉnh dáng tỷ lệ vàng, không watermark. Giá hãng 249k/tháng, tại Xwuan chỉ 90k/30 ngày, bảo hành full.',
            D.DET_TABS, c, selected_acc='Meitu SVIP')

# ═══════════════════════════ 8. LOCKET ═══════════════════════════
c = D.d_hero('✨', '🛡️ Bảo hành tận tâm · iOS &amp; Android', 'Locket Gold', '✦ Ghim khoảnh khắc · Kết nối người thương ✦')
c += """
      <section class="sec" id="goigoi">
        <h2 class="h-scrap"><span class="ico">💰</span>Gói giá trong sổ</h2>
        """ + D.SQUIG_RED + """
        <div class="cards" style="grid-template-columns:repeat(auto-fit,minmax(240px,330px));justify-content:center">
          """ + D.pkg_card('b-blue', '🎥 QUAY 5S', 'Gói Quay 5s', '50k', '6 tháng',
                           ['1 năm: 80k', 'Vĩnh viễn ♾️: 150k', 'Bảo hành trong thời gian sử dụng']) + """
          """ + D.pkg_card('b-pink', '🎬 QUAY 15S', 'Gói Quay 15s', '60k', '6 tháng',
                           ['1 năm: 100k', 'Vĩnh viễn ♾️: 180k', 'Bảo hành trong thời gian sử dụng']) + """
        </div>
        <p class="warn-note">💡 Gói vĩnh viễn dùng mãi mãi — hỗ trợ miễn phí kể cả khi đổi máy mới!</p>
      </section>
      <section class="sec" id="sosanh">
        <h2 class="h-scrap"><span class="ico">🏆</span>Locket Thường vs Locket Gold</h2>
        """ + D.SQUIG_BLUE + """
        """ + D.cmp_table(
            ['Tính năng', 'Free 😴', 'Gold ✨'],
            [
                ['Quảng cáo', ('no', 'Chèn quảng cáo'), ('yes', '✓ Không quảng cáo')],
                ['Video Locket', ('no', 'Giới hạn'), ('yes', '✓ Video 5s hoặc 15s')],
                ['Tải ảnh từ thư viện', ('no', 'Chỉ chụp trực tiếp'), ('yes', '✓ Tải mọi ảnh từ máy')],
                ['Biểu tượng App', ('no', 'Mặc định'), ('yes', '✓ Nhiều icon tùy chỉnh')],
                ['Huy hiệu Gold', ('no', 'Không có'), ('yes', '✓ Huy hiệu đặc quyền')],
            ]) + """
      </section>"""
c += D.camket_section(
    'Cam kết từ Xwuan', D.SQUIG_RED,
    D.check2col(['<b>An toàn tuyệt đối</b> — không ảnh hưởng iCloud cá nhân',
                 '<b>Bảo hành</b> trong thời gian sử dụng',
                 'Hỗ trợ cả <b>iOS &amp; Android</b>'],
                ['Hỗ trợ miễn phí kể cả khi <b>đổi máy mới</b>',
                 'Kích hoạt nhanh chóng chỉ trong <b>2–5 phút</b>',
                 'Liên hệ bất cứ lúc nào, <b>phản hồi nhanh</b>']),
    D.steps(('Nhắn Zalo / Facebook', 'Cho Xwuan biết gói Quay 5s / 15s + thời gian.'),
            ('Kích hoạt nhanh', 'Xử lý kích hoạt Locket Gold trong 2–5 phút.'),
            ('Ghim ảnh thoải mái', 'Tận hưởng Gold · bảo hành suốt thời gian gói.')))
render_page('locket.html',
            'Locket Gold từ 50k — quay 5s/15s, có gói vĩnh viễn | Sổ Acc Xwuan',
            'Locket Gold: widget ảnh với video 5s/15s, không quảng cáo, tải ảnh từ thư viện, huy hiệu Gold. An toàn cho iCloud, hỗ trợ iOS & Android, kích hoạt 2–5 phút.',
            D.LOCKET_TABS, c, selected_acc='Locket Gold')

# ═══════════════════════════ 9. WINDOWS & OFFICE ═══════════════════════════
c = D.d_hero('💻', '🛡️ Bảo hành lỗi phát sinh 6 tháng', 'Windows &amp; Office', '✦ Cài đặt kỹ thuật · Giá minh bạch · Không phát sinh · Giữ nguyên dữ liệu ✦')
c += """
      <section class="sec" id="quickfact">
        <div class="more-accs reveal" style="margin-top:26px">
          <span class="chip">⚡ Xong trong 30–60 phút</span>
          <span class="chip">🛡️ Bảo hành 6 tháng</span>
          <span class="chip">✅ ISO gốc Microsoft</span>
          <span class="chip">💾 Giữ nguyên dữ liệu</span>
        </div>
      </section>
      <section class="sec" id="goigoi">
        <h2 class="h-scrap"><span class="ico">💰</span>Bảng giá đơn lẻ</h2>
        """ + D.SQUIG_RED + """
        <div class="cards" style="grid-template-columns:repeat(auto-fit,minmax(230px,320px));justify-content:center">
          """ + D.pkg_card('b-pink', '⭐ ỔN ĐỊNH NHẤT', 'Windows Chuẩn Microsoft', '150k – 180k', 'lúc cài',
                           ['Cài sạch từ ISO gốc Microsoft', 'Driver đầy đủ, không thiếu', 'Ổn định, ít lỗi vặt', 'Không bloatware, không rác']) + """
          """ + D.pkg_card('b-blue', '⚡ CHO MÁY YẾU / CŨ', 'Windows Tối Ưu Hiệu Năng', '100k – 120k', 'lúc cài',
                           ['Tắt service ngầm dư thừa', 'Tối ưu RAM &amp; CPU', 'Khởi động nhanh hơn rõ rệt', 'Phù hợp máy RAM 4GB trở xuống']) + """
          """ + D.pkg_card('', '📘 FULL BỘ OFFICE', 'Microsoft Office', '80k – 120k', 'lúc cài',
                           ['Word, Excel, PowerPoint đầy đủ', 'Outlook, OneNote tùy chọn', 'Office 365 hoặc 2021/2019', 'Bản offline hoặc 365']) + """
        </div>
      </section>
      <section class="sec" id="combo">
        <h2 class="h-scrap"><span class="ico">🔥</span>Combo gộp — càng mua càng rẻ</h2>
        """ + D.SQUIG_GREEN + """
        """ + D.receipt(
            [('Win Chuẩn + Office', '200k – 220k', True),
             ('Win Tối Ưu + Office', '160k – 180k', True)],
            '🔥 Gộp combo tiết kiệm ~20k – 30k · bảo hành lỗi phát sinh!') + """
      </section>"""
c += D.camket_section(
    'Cam kết từ Xwuan', D.SQUIG_RED,
    D.check2col(['<b>Sao lưu dữ liệu an toàn</b> — giữ nguyên dữ liệu cũ',
                 '<b>Bảo hành lỗi phát sinh 6 tháng</b>',
                 'ISO <b>chuẩn gốc Microsoft</b>, không sửa đổi'],
                ['Không <b>bloatware</b>, không phần mềm rác',
                 'Xong trong <b>30–60 phút</b>',
                 'Hỗ trợ <b>sau cài đặt</b> tận tình 🤝']),
    D.steps(('Nhắn Zalo / Facebook', 'Máy bạn đang dùng gì, muốn cài gói nào?'),
            ('Hẹn lịch cài đặt', 'Xwuan hướng dẫn / hẹn giờ — xong trong 30–60 phút.'),
            ('Dùng kèm bảo hành', 'Bảo hành lỗi phát sinh đến 6 tháng sau cài.')))
render_page('windows-pricing.html',
            'Báo giá Windows & Office — cài win từ 100k, bảo hành 6 tháng | Sổ Acc Xwuan',
            'Cài đặt Windows chuẩn Microsoft / tối ưu máy yếu / Office 365-2021-2019. Giá minh bạch 80k–220k, giữ nguyên dữ liệu, xong 30–60 phút, bảo hành 6 tháng.',
            D.WIN_TABS, c, selected_acc='Windows / Office')

print('✅ Xong! 9 trang đã được tạo.')
