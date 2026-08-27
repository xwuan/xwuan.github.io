/**
 * PRICING.JS — xwuan.github.io
 * Quản lý dữ liệu giá dịch vụ, chương trình SALE, thông tin liên hệ và banner thông báo.
 * Có thể chỉnh sửa trực tiếp từ file này hoặc thông qua trang quản trị admin.html
 */

(function () {
  const DEFAULT_CONFIG = {
    version: "2026.1",
    lastUpdated: "2026-08-27",
    announcement: {
      enabled: false,
      text: "",
      tag: "",
      link: ""
    },
    contact: {
      zalo: "0822307662",
      zaloLink: "https://zalo.me/0822307662",
      phone: "0822.307.662",
      facebook: "https://www.facebook.com/xwuan1/",
      tiktok: "https://www.tiktok.com/@xwuan2"
    },
    services: {
      capcut_7d: {
        id: "capcut_7d",
        name: "CapCut Pro 7 Ngày",
        price: "20k",
        unit: "/ 7 ngày",
        originalPrice: "",
        isSale: false,
        saleTag: "",
        warranty: "Bảo hành full thời gian",
        status: "available",
        detailUrl: "capcut.html"
      },
      capcut_30d: {
        id: "capcut_30d",
        name: "CapCut Pro 30 Ngày",
        price: "80k",
        unit: "/ 30 ngày",
        originalPrice: "",
        isSale: false,
        saleTag: "",
        warranty: "Bảo hành full thời gian",
        status: "available",
        detailUrl: "capcut.html"
      },
      youtube: {
        id: "youtube",
        name: "YouTube Premium",
        price: "40k",
        unit: "/ 30 ngày",
        originalPrice: "",
        isSale: false,
        saleTag: "",
        warranty: "Bảo hành full thời gian",
        status: "available",
        detailUrl: "youtube.html"
      },
      canva: {
        id: "canva",
        name: "Canva Pro 1 Năm",
        price: "130k",
        unit: "/ 1 năm",
        originalPrice: "",
        isSale: false,
        saleTag: "",
        warranty: "Bảo hành full thời gian",
        status: "available",
        detailUrl: "canva.html"
      },
      netflix: {
        id: "netflix",
        name: "Netflix 4K UHD",
        price: "45k",
        unit: "/ 30 ngày",
        originalPrice: "",
        isSale: false,
        saleTag: "",
        warranty: "Bảo hành full thời gian",
        status: "available",
        detailUrl: "netflix.html"
      },
      google_ai: {
        id: "google_ai",
        name: "Google AI Pro",
        price: "60k",
        unit: "/ 1 năm",
        originalPrice: "",
        isSale: false,
        saleTag: "",
        warranty: "Không bảo hành",
        status: "available",
        detailUrl: "google-ai.html"
      },
      meitu: {
        id: "meitu",
        name: "Meitu SVIP",
        price: "80k",
        unit: "/ 30 ngày",
        originalPrice: "",
        isSale: false,
        saleTag: "",
        warranty: "Bảo hành full thời gian",
        status: "available",
        detailUrl: "meitu.html"
      },
      locket_5s: {
        id: "locket_5s",
        name: "Locket Gold (Quay 5s)",
        p6m: "50k",
        p1y: "80k",
        pLife: "150k",
        status: "available",
        detailUrl: "locket.html"
      },
      locket_15s: {
        id: "locket_15s",
        name: "Locket Gold (Quay 15s)",
        p6m: "60k",
        p1y: "100k",
        pLife: "180k",
        status: "available",
        detailUrl: "locket.html"
      },
      win_std: {
        id: "win_std",
        name: "Windows Chuẩn Microsoft",
        price: "150k – 180k",
        status: "available",
        detailUrl: "windows-pricing.html"
      },
      win_opt: {
        id: "win_opt",
        name: "Windows Tối Ưu",
        price: "100k – 120k",
        status: "available",
        detailUrl: "windows-pricing.html"
      },
      office: {
        id: "office",
        name: "Microsoft Office",
        price: "80k – 120k",
        status: "available",
        detailUrl: "windows-pricing.html"
      },
      combo_std: {
        id: "combo_std",
        name: "Combo Win Chuẩn + Office",
        price: "200k – 220k",
        status: "available",
        detailUrl: "windows-pricing.html"
      },
      combo_opt: {
        id: "combo_opt",
        name: "Combo Win Tối Ưu + Office",
        price: "160k – 180k",
        status: "available",
        detailUrl: "windows-pricing.html"
      }
    },
    customProducts: []
  };

  // Dọn dẹp sạch sẽ bộ nhớ tạm từ các lần test trước (xóa sạch Google AI Pro)
  try {
    localStorage.removeItem("xwuan_site_config");
    localStorage.removeItem("xwuan_logged_in");
    localStorage.removeItem("xwuan_admin_auth");
    localStorage.removeItem("xwuan_admin_pass");
    localStorage.removeItem("xwuan_firebase_url");
    localStorage.removeItem("xwuan_firebase_secret");
    sessionStorage.clear();
  } catch (e) {}

  window.SITE_CONFIG = DEFAULT_CONFIG;
  window.DEFAULT_SITE_CONFIG = DEFAULT_CONFIG;

  /**
   * Tự động áp dụng giá và giao diện lên DOM
   */
  function applySitePricing() {
    const cfg = window.SITE_CONFIG;
    if (!cfg) return;

    // 1. Cập nhật Banner thông báo
    renderAnnouncementBanner(cfg.announcement);

    // 2. Cập nhật liên kết Liên hệ (Zalo, SĐT, Facebook)
    if (cfg.contact) {
      document.querySelectorAll('a[href*="zalo.me"]').forEach(el => {
        el.href = cfg.contact.zaloLink || `https://zalo.me/${cfg.contact.zalo}`;
      });
      document.querySelectorAll('a[href*="tel:"]').forEach(el => {
        el.href = `tel:${cfg.contact.zalo}`;
        const spanText = el.querySelector(".call-text") || el;
        if (spanText && spanText.innerHTML.includes("0822")) {
          spanText.innerHTML = spanText.innerHTML.replace(/0822[\.\s\d]+/, cfg.contact.phone || cfg.contact.zalo);
        }
      });
      document.querySelectorAll('a[href*="facebook.com"]').forEach(el => {
        if (cfg.contact.facebook) el.href = cfg.contact.facebook;
      });
      document.querySelectorAll('a[href*="tiktok.com"]').forEach(el => {
        if (cfg.contact.tiktok) el.href = cfg.contact.tiktok;
      });
    }

    // 3. Cập nhật các khối giá dịch vụ theo data-price-key
    const s = cfg.services;
    if (!s) return;

    // Helper cập nhật giá kèm sale
    function updatePriceElement(elem, svc) {
      if (!elem || !svc) return;
      let html = "";
      if (svc.isSale && svc.originalPrice) {
        html += `<span style="font-size:0.75rem;font-weight:600;color:#6b7280;text-decoration:line-through;">${svc.originalPrice}</span> `;
        html += `<span style="color:#ef4444;font-size:0.72rem;font-weight:700;margin-left:4px;padding:1px 6px;border-radius:10px;background:rgba(239,68,68,0.15);">${svc.saleTag || "SALE"}</span><br>`;
      }
      html += `${svc.price}`;
      
      // Chống trùng lặp đơn vị (/ 30 ngày / 30 ngày hoặc / 1 năm / 1 năm)
      const next = elem.nextElementSibling;
      const hasUnitSibling = next && (
        next.classList.contains("price-unit") ||
        next.classList.contains("price-month") ||
        next.classList.contains("price-period") ||
        next.classList.contains("cv-price-unit") ||
        next.classList.contains("yt-price-unit") ||
        next.textContent.trim().startsWith("/")
      );
      const isPriceOnly = elem.hasAttribute("data-price-only") || elem.classList.contains("price-val");
      
      if (svc.unit && !isPriceOnly && !hasUnitSibling) {
        html += ` <span style="font-size:0.8rem;font-weight:600;color:#9ca3af;">${svc.unit}</span>`;
      }
      elem.innerHTML = html;
    }

    // A. Netflix
    if (s.netflix) {
      document.querySelectorAll('[data-price-key="netflix"]').forEach(el => updatePriceElement(el, s.netflix));
      // Chi tiết trang netflix.html
      const nfCard = document.querySelector(".price-card .price-amount");
      if (nfCard && window.location.pathname.includes("netflix")) {
        const wrap = nfCard.parentElement;
        const strike = wrap.querySelector("span[style*='line-through']");
        const badge = wrap.querySelector("span[style*='SALE']");
        if (s.netflix.isSale && s.netflix.originalPrice) {
          if (strike) {
            strike.textContent = s.netflix.originalPrice;
            strike.style.display = "inline";
          }
          if (badge) {
            badge.textContent = s.netflix.saleTag || "SALE";
            badge.style.display = "inline";
          }
        } else {
          if (strike) strike.style.display = "none";
          if (badge) badge.style.display = "none";
        }
        nfCard.innerHTML = `${s.netflix.price} <span class="price-month">${s.netflix.unit || "/ tháng"}</span>`;
      }
    }

    // B. CapCut 30 ngày & 7 ngày
    if (s.capcut_30d) {
      document.querySelectorAll('[data-price-key="capcut_30d"]').forEach(el => updatePriceElement(el, s.capcut_30d));
      const ccCard30 = document.querySelector(".price-card.best");
      if (ccCard30 && window.location.pathname.includes("capcut")) {
        const strike = ccCard30.querySelector("div[style*='line-through']");
        const amount = ccCard30.querySelector(".price-amount");
        if (strike) {
          strike.textContent = s.capcut_30d.originalPrice || "";
          strike.style.display = s.capcut_30d.isSale ? "block" : "none";
        }
        if (amount) {
          let badgeHtml = s.capcut_30d.isSale
            ? `<span style="background:linear-gradient(135deg,#d946ef,#a855f7);color:#fff;font-size:10px;font-weight:700;padding:2px 7px;border-radius:12px;letter-spacing:.3px;">${s.capcut_30d.saleTag || "SALE"}</span>`
            : "";
          amount.innerHTML = `${s.capcut_30d.price} ${badgeHtml}`;
        }
      }
    }
    if (s.capcut_7d) {
      document.querySelectorAll('[data-price-key="capcut_7d"]').forEach(el => {
        el.textContent = s.capcut_7d.price;
      });
      const ccCards = document.querySelectorAll(".price-card");
      if (ccCards.length > 0 && window.location.pathname.includes("capcut")) {
        const ccCard7 = ccCards[0];
        const amt = ccCard7.querySelector(".price-amount");
        if (amt) amt.textContent = s.capcut_7d.price;
      }
    }

    // C. YouTube
    if (s.youtube) {
      document.querySelectorAll('[data-price-key="youtube"]').forEach(el => updatePriceElement(el, s.youtube));
      const ytAmt = document.querySelector(".yt-price-amount");
      if (ytAmt && window.location.pathname.includes("youtube")) {
        ytAmt.innerHTML = `${s.youtube.price} <span class="yt-price-unit">${s.youtube.unit || "/ tháng"}</span>`;
      }
    }

    // D. Canva
    if (s.canva) {
      document.querySelectorAll('[data-price-key="canva"]').forEach(el => updatePriceElement(el, s.canva));
      const cvAmt = document.querySelector(".cv-price-amount");
      if (cvAmt && window.location.pathname.includes("canva")) {
        cvAmt.innerHTML = `${s.canva.price} <span class="cv-price-unit">${s.canva.unit || "/ 1 năm"}</span>`;
      }
    }

    // E. Google AI & Meitu
    if (s.google_ai) {
      document.querySelectorAll('[data-price-key="google_ai"]').forEach(el => updatePriceElement(el, s.google_ai));
    }
    if (s.meitu) {
      document.querySelectorAll('[data-price-key="meitu"]').forEach(el => updatePriceElement(el, s.meitu));
    }

    // F. Locket Gold
    if (s.locket_5s) {
      document.querySelectorAll('[data-price-key="locket_5s_6m"]').forEach(el => (el.textContent = s.locket_5s.p6m));
      document.querySelectorAll('[data-price-key="locket_5s_1y"]').forEach(el => (el.textContent = s.locket_5s.p1y));
      document.querySelectorAll('[data-price-key="locket_5s_life"]').forEach(el => (el.textContent = s.locket_5s.pLife));
    }
    if (s.locket_15s) {
      document.querySelectorAll('[data-price-key="locket_15s_6m"]').forEach(el => (el.textContent = s.locket_15s.p6m));
      document.querySelectorAll('[data-price-key="locket_15s_1y"]').forEach(el => (el.textContent = s.locket_15s.p1y));
      document.querySelectorAll('[data-price-key="locket_15s_life"]').forEach(el => (el.textContent = s.locket_15s.pLife));
    }

    // F. Windows & Office
    if (s.win_std) {
      document.querySelectorAll('[data-price-key="win_std"]').forEach(el => (el.textContent = s.win_std.price));
    }
    if (s.win_opt) {
      document.querySelectorAll('[data-price-key="win_opt"]').forEach(el => (el.textContent = s.win_opt.price));
    }
    if (s.office) {
      document.querySelectorAll('[data-price-key="office"]').forEach(el => (el.textContent = s.office.price));
    }
    if (s.combo_std) {
      document.querySelectorAll('[data-price-key="combo_std"]').forEach(el => (el.textContent = s.combo_std.price));
    }
    if (s.combo_opt) {
      document.querySelectorAll('[data-price-key="combo_opt"]').forEach(el => (el.textContent = s.combo_opt.price));
    }

    // G. Thêm các sản phẩm tùy chỉnh (Custom Products) vào index.html nếu có
    if (cfg.customProducts && cfg.customProducts.length > 0) {
      renderCustomProducts(cfg.customProducts);
    }
  }

  /**
   * Tạo banner thông báo khuyến mãi trên đầu trang
   */
  function renderAnnouncementBanner(an) {
    if (!an || !an.enabled || !an.text) {
      const existing = document.getElementById("site-announcement-bar");
      if (existing) existing.remove();
      return;
    }

    let bar = document.getElementById("site-announcement-bar");
    if (!bar) {
      bar = document.createElement("div");
      bar.id = "site-announcement-bar";
      bar.style.cssText = `
        position: relative;
        z-index: 1000;
        background: linear-gradient(90deg, #ff0055, #ff5500, #9900ff);
        background-size: 200% auto;
        animation: bannerGradient 6s ease infinite;
        color: #fff;
        font-size: 13px;
        font-weight: 700;
        padding: 9px 14px;
        text-align: center;
        box-shadow: 0 4px 20px rgba(255, 0, 85, 0.3);
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 8px;
        flex-wrap: wrap;
      `;
      // Append keyframes if not exists
      if (!document.getElementById("banner-keyframes")) {
        const style = document.createElement("style");
        style.id = "banner-keyframes";
        style.textContent = `
          @keyframes bannerGradient { 
            0% { background-position: 0% 50%; } 
            50% { background-position: 100% 50%; } 
            100% { background-position: 0% 50%; } 
          }
        `;
        document.head.appendChild(style);
      }
      document.body.prepend(bar);
    }

    const tagHtml = an.tag
      ? `<span style="background:#fff;color:#ff0055;padding:2px 8px;border-radius:99px;font-size:10px;font-weight:900;letter-spacing:0.5px;">${an.tag}</span>`
      : "";
    const linkHtml = an.link
      ? `<a href="${an.link}" style="color:#fff;text-decoration:underline;margin-left:6px;font-weight:800;">Xem ngay →</a>`
      : "";

    bar.innerHTML = `${tagHtml} <span>${an.text}</span> ${linkHtml}`;
  }

  /**
   * Hiển thị danh sách sản phẩm mới thêm từ Admin vào trang chủ
   */
  function renderCustomProducts(products) {
    const entGrid = document.querySelector(".ent-grid");
    if (!entGrid) return;

    // Xóa custom cards cũ nếu có
    entGrid.querySelectorAll(".custom-ent-card").forEach(el => el.remove());

    products.forEach(p => {
      if (p.status === "disabled") return;
      const card = document.createElement("div");
      card.className = "ent-card custom-ent-card";
      card.style.cssText = `
        background: linear-gradient(180deg, rgba(20, 25, 45, 0.9), rgba(12, 16, 32, 0.95));
        border: 1px solid rgba(0, 212, 255, 0.25);
      `;
      const icon = p.icon || "images/avatar.png";
      const saleHtml = p.isSale && p.originalPrice
        ? `<span style="font-size:0.75rem;font-weight:600;color:#6b7280;text-decoration:line-through;">${p.originalPrice}</span>
           <span style="color:#00d4ff;font-size:0.72rem;font-weight:700;margin-left:4px;">${p.saleTag || "SALE"}</span><br>`
        : "";

      const featuresHtml = (p.features || [])
        .map(f => `<span>✨ ${f}</span>`)
        .join("");

      card.innerHTML = `
        <img src="${icon}" class="ent-icon" alt="${p.name}" onerror="this.src='images/avatar.png'">
        <div class="ent-title">${p.name}</div>
        <div class="ent-features">
          <span>🛡️ ${p.warranty || "Bảo hành uy tín"}</span>
          ${featuresHtml}
        </div>
        <div class="ent-price">
          ${saleHtml}
          ${p.price} <span style="font-size:0.8rem;font-weight:600;color:#9ca3af;">${p.unit || ""}</span>
        </div>
        <a href="${p.orderUrl || window.SITE_CONFIG.contact.zaloLink}" class="btn-ent" style="background:rgba(0,212,255,0.15);color:#00d4ff;border:1px solid rgba(0,212,255,0.4);margin-top:10px;">
          Mua ngay qua Zalo
        </a>
      `;
      entGrid.appendChild(card);
    });
  }

  // Tự động kích hoạt khi DOM đã sẵn sàng
  function initAll() {
    applySitePricing();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initAll);
  } else {
    initAll();
  }

  window.applySitePricing = applySitePricing;
})();
