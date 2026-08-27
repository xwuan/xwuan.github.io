#!/usr/bin/env bash
echo "============================================="
echo "  Xwuan - Push code lên GitHub"
echo "  URL: https://github.com/xwuan/xwuan.github.io"
echo "============================================="
git status
git add .
git commit -m "feat: them admin.html quan ly gia/sale va module pricing.js dong bo" || true
git push -u https://github.com/xwuan/xwuan.github.io main
echo ""
echo "============================================="
read -p "Nhan Enter de thoat..."
