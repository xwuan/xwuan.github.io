# -*- coding: utf-8 -*-
"""Build toàn bộ website Sổ Acc Xwuan bản LẬT TRANG — chạy: python3 build.py"""
from shell import render_page
import pages_data as D

def build_acc(fname, cfg, extra_title):
    render_page(
        fname,
        '%s giá rẻ — %s | Sổ Acc Xwuan' % (cfg['name'].replace('&amp;', '&'), extra_title),
        '%s giá học sinh tại Xwuan: kích hoạt 2–5 phút, bảo hành full, hỗ trợ 24/24. Zalo 0822.307.662.' % cfg['name'].replace('&amp;', '&'),
        D.acc_faces(**cfg), D.ACC_NAV,
    )

# 1. TRANG CHỦ
render_page('index.html',
            'Sổ Acc Xwuan 📓 | Acc rẻ chỉ 2–5/10 giá gốc — lật sổ xem giá',
            'Quyển sổ giá acc: CapCut, Canva, Netflix, YouTube, Gemini, Meitu, Locket, Win/Office — giá 2–5/10 giá gốc, kích hoạt 2–5 phút, bảo hành full.',
            D.HOME_FACES, D.HOME_NAV, end_note=D.HOME_END)

# 2–7. CÁC TRANG ACC
build_acc('capcut.html', D.CAPCUT, '20k/7 ngày · 80k/30 ngày')
build_acc('canva.html', D.CANVA, '130k/năm tiết kiệm ~90%')
build_acc('youtube.html', D.YOUTUBE, '40k/tháng không quảng cáo')
build_acc('netflix.html', D.NETFLIX, '45k/tháng 4K HDR')
build_acc('google-ai.html', D.GEMINI, '60k/năm Gemini 3.1 Pro')
build_acc('meitu.html', D.MEITU, '90k/30 ngày full SVIP')

# 8. LOCKET
render_page('locket.html',
            'Locket Gold từ 50k — quay 5s/15s, gói vĩnh viễn | Sổ Acc Xwuan',
            'Locket Gold: video 5s/15s, không quảng cáo, tải ảnh từ thư viện. An toàn iCloud, iOS & Android, kích hoạt 2–5 phút. Zalo 0822.307.662.',
            D.LOCKET_FACES, D.LOCKET_NAV)

# 9. WINDOWS & OFFICE
render_page('windows-pricing.html',
            'Cài Windows & Office từ 80k — bảo hành 6 tháng | Sổ Acc Xwuan',
            'Cài Windows chuẩn Microsoft / tối ưu máy yếu / Office 365-2021-2019. Giá minh bạch, giữ nguyên dữ liệu, xong 30–60 phút, bảo hành 6 tháng.',
            D.WIN_FACES, D.WIN_NAV)

print('✅ Xong! 9 trang bản lật trang đã được tạo.')
