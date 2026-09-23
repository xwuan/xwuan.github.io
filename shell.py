# -*- coding: utf-8 -*-
"""Khung sổ tay dùng chung cho mọi trang (CSS + masthead + footer + JS)."""

FONT = open('fontface.css', encoding='utf-8').read()

CSS = FONT + """
:root{
  --marker:'Shantell Sans','Segoe Print','Comic Sans MS',cursive;
  --hand:'Patrick Hand','Segoe Print','Comic Sans MS',cursive;
  --ink:#2e3d59;
  --ink-soft:#5a6a88;
  --pencil:#8a8172;
  --red:#d94f43;
  --red-dark:#b03a30;
  --paper:#fbf6e8;
  --card:#fffdf4;
  --yellow:#ffdf6b;
  --pink:#ffc9d8;
  --blue:#c9e6f7;
  --green:#cfeec2;
  --orange:#ffb3a0;
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
::selection{background:#ffd95e;color:#4a3410}

body{
  font-family:var(--hand);
  font-size:18.5px;
  line-height:1.6;
  color:var(--ink);
  background:
    radial-gradient(1100px 500px at 50% -80px, rgba(255,233,190,.16), transparent 65%),
    url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='240' height='240'%3E%3Cg fill='none' stroke='%23ffe9c4' stroke-opacity='.055' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M18 44 q13 -20 26 0 q13 20 26 0'/%3E%3Ccircle cx='196' cy='36' r='11'/%3E%3Cpath d='M96 150 l8 16 18 3 -13 13 3 18 -16 -9 -16 9 3 -18 -13 -13 18 -3z'/%3E%3Cpath d='M150 210 h34 m-34 12 h22'/%3E%3Ccircle cx='52' cy='200' r='9'/%3E%3Cpath d='M180 120 q12 -16 24 0'/%3E%3Cpath d='M30 120 l12 -12 12 12 12 -12'/%3E%3C/g%3E%3C/svg%3E"),
    linear-gradient(160deg,#8f6f47,#63512f 55%,#4a3b21);
  background-attachment:fixed,fixed,fixed;
}
body::after{
  content:'';position:fixed;inset:0;pointer-events:none;z-index:60;
  box-shadow:inset 0 0 200px rgba(25,12,0,.5);
}

/* ══════════ QUYỂN SỔ ══════════ */
.wrap{max-width:1140px;margin:46px auto 90px;padding:0 18px;position:relative;z-index:1}
.notebook{
  position:relative;
  border-left:26px solid #7d5b35;
  border-radius:16px 22px 22px 16px;
  background:
    linear-gradient(90deg, rgba(58,38,12,.20) 0 4px, rgba(58,38,12,.06) 14px, transparent 42px),
    repeating-linear-gradient(180deg, transparent 0 33px, rgba(120,164,196,.34) 33px 35px),
    linear-gradient(180deg,#fdf9ee,#f9f3e0);
  box-shadow:
    0 34px 70px rgba(35,20,4,.5),
    0 6px 0 #5c4527,
    0 12px 0 #46331c;
}
.notebook::before{
  content:'';position:absolute;top:0;bottom:0;left:106px;width:2.5px;z-index:0;
  background:linear-gradient(rgba(217,79,67,.6),rgba(217,79,67,.32));
}
.notebook::after{
  content:'';position:absolute;inset:0;z-index:0;border-radius:inherit;pointer-events:none;
  box-shadow:inset 0 0 110px rgba(88,58,20,.13), inset 0 -34px 70px rgba(88,58,20,.08);
}
.spiral{
  position:absolute;top:12px;bottom:12px;left:-18px;width:96px;z-index:6;pointer-events:none;
  background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='96' height='64'%3E%3Cg fill='none' stroke-linecap='round'%3E%3Cg stroke='%232a2a30' stroke-opacity='.16' stroke-width='5' transform='translate(-2 3)'%3E%3Cpath d='M8 31 C 8 12 52 10 64 24'/%3E%3Cpath d='M8 35 C 8 54 58 56 65 41'/%3E%3C/g%3E%3Cg stroke='%23878795' stroke-width='5'%3E%3Cpath d='M8 31 C 8 12 52 10 64 24'/%3E%3Cpath d='M8 35 C 8 54 58 56 65 41'/%3E%3C/g%3E%3Cg stroke='%23dcdce4' stroke-width='1.7'%3E%3Cpath d='M8 30 C 8 13 50 11 61 22'/%3E%3Cpath d='M8 34 C 8 51 55 54 63 40'/%3E%3C/g%3E%3C/g%3E%3Cellipse cx='70' cy='32.5' rx='4.2' ry='6' fill='%23ded0b2' stroke='%23a8987b' stroke-width='1.4'/%3E%3Cellipse cx='70' cy='32.5' rx='2' ry='3.8' fill='%2333304a' opacity='.5'/%3E%3C/svg%3E") repeat-y;
  background-size:96px 64px;
}
.page{position:relative;z-index:2;padding:30px 46px 0 142px}
section{scroll-margin-top:16px}

.tape{
  position:absolute;width:112px;height:30px;z-index:3;pointer-events:none;
  background:repeating-linear-gradient(45deg, rgba(233,110,98,.75) 0 10px, rgba(255,252,240,.6) 10px 20px);
  opacity:.9;top:-14px;left:50%;transform:translateX(-50%) rotate(-3deg);
  box-shadow:0 2px 5px rgba(60,35,10,.18);
}
.tape-plain{background:rgba(255,252,238,.55);box-shadow:0 2px 5px rgba(60,35,10,.12)}

/* ─── tab mục lục ─── */
.tabs{position:absolute;top:0;right:-30px;height:0;z-index:8}
.tabs a{
  position:absolute;right:0;width:150px;padding:13px 6px 15px;text-align:center;
  font-family:var(--marker);font-size:.95rem;color:var(--ink);text-decoration:none;
  border-radius:0 12px 12px 0;border:2px solid rgba(46,61,89,.26);border-left:none;
  box-shadow:3px 3px 0 rgba(60,35,10,.28);
  transform:translateX(var(--tx,0)) rotate(var(--r,0deg));transition:.25s;
}
.tabs a:hover{--tx:9px}
.tabs a:nth-child(1){top:118px;background:var(--pink);--r:.6deg}
.tabs a:nth-child(2){top:203px;background:var(--blue);--r:-.7deg}
.tabs a:nth-child(3){top:288px;background:var(--yellow);--r:.5deg}
.tabs a:nth-child(4){top:373px;background:var(--green);--r:-.5deg}
.tabs a:nth-child(5){top:458px;background:var(--orange);--r:.7deg}
.mobile-tabs{display:none}

.masthead{display:flex;align-items:flex-end;justify-content:space-between;gap:18px;flex-wrap:wrap;padding-bottom:8px}
.brand{display:flex;align-items:center;gap:10px;text-decoration:none;color:var(--ink)}
.brand-book{font-size:1.9rem;display:inline-block;transform:rotate(-6deg)}
.brand:hover .brand-book{animation:wiggle .5s ease-in-out infinite}
.brand-name{font-family:var(--marker);font-weight:700;font-size:1.85rem;letter-spacing:.5px}
.brand-tag{
  font-family:var(--marker);font-size:.95rem;color:#fff6e3;background:var(--red);
  padding:2px 12px 4px;border-radius:8px;transform:rotate(-3deg);
  box-shadow:2px 3px 0 rgba(43,32,10,.3);margin-left:2px;
}
.mast-note{color:var(--pencil);font-style:italic;font-size:1.02rem}
@keyframes wiggle{0%,100%{transform:rotate(-6deg)}50%{transform:rotate(4deg) scale(1.06)}}

/* ══════════ HERO ══════════ */
.hero{display:flex;gap:40px;align-items:center;padding:44px 0 40px}
.hero-text{flex:1.15;min-width:0}
.hero-art{flex:.85;position:relative;min-height:360px}
.pill{
  display:inline-block;font-family:var(--marker);font-size:.95rem;color:#5d4a12;
  background:var(--yellow);padding:5px 16px 7px;border-radius:999px;transform:rotate(-1.6deg);
  box-shadow:2px 3px 0 rgba(43,32,10,.22);margin-bottom:20px;
}
h1{font-family:var(--marker);font-weight:700;line-height:1.14;font-size:clamp(2rem,4.4vw,3.1rem)}
h1 .small-line{display:block;font-family:var(--hand);font-size:.62em;color:var(--ink-soft);margin-bottom:8px}
.hl{
  display:inline-block;color:var(--red-dark);
  background:linear-gradient(104deg, rgba(255,223,107,0) .8%, #ffdf6b 3%, #ffdf6b 96%, rgba(255,223,107,0) 98%);
  border-radius:.35em;padding:.02em .28em .06em;transform:rotate(-.8deg);
}
.lead{margin:20px 0 26px;font-size:1.16rem;color:#42527a;max-width:34em}
.cta{display:flex;gap:16px;flex-wrap:wrap;align-items:center}
.btn{
  display:inline-block;font-family:var(--marker);font-size:1.03rem;line-height:1.25;
  padding:.7em 1.2em .8em;border-radius:13px;text-decoration:none;cursor:pointer;border:none;
  box-shadow:3px 4px 0 rgba(43,32,10,.35);transition:transform .18s, box-shadow .18s;
}
.btn:hover{transform:translateY(-3px) rotate(-1deg);box-shadow:4px 6px 0 rgba(43,32,10,.35)}
.btn:active{transform:translate(2px,3px);box-shadow:1px 1px 0 rgba(43,32,10,.35)}
.btn-red{background:var(--red);color:#fff8e7}
.btn-red:hover{background:#e2604f}
.btn-line{background:transparent;color:var(--ink);border:2.5px solid var(--ink);box-shadow:3px 4px 0 rgba(43,32,10,.25)}
.btn-green{background:#3c6e46;color:#fff8e7}
.btn-green:hover{background:#4a8156}
.hero-stats{display:flex;gap:12px;list-style:none;margin-top:34px;flex-wrap:wrap}
.hero-stats li{
  background:var(--card);border:2px solid rgba(46,61,89,.16);border-radius:12px;
  padding:8px 18px 10px;text-align:center;transform:rotate(-1deg);
  box-shadow:2px 3px 0 rgba(43,32,10,.14);
}
.hero-stats li:nth-child(2){transform:rotate(1.2deg);background:#fff8e1}
.hero-stats li:nth-child(3){transform:rotate(-.6deg)}
.hero-stats b{display:block;font-family:var(--marker);font-size:1.35rem;color:var(--red-dark)}
.hero-stats span{font-size:.95rem;color:var(--ink-soft)}

.polaroid{
  position:relative;background:#fffdf6;padding:14px 14px 12px;border-radius:4px;
  box-shadow:0 16px 32px rgba(40,22,2,.35);transform:rotate(3deg);width:min(320px,86%);margin:10px auto 0;
}
.ph-img{
  height:190px;border-radius:2px;display:grid;place-items:center;font-size:3.4rem;letter-spacing:.12em;
  background:
    radial-gradient(140px 90px at 70% 22%, rgba(255,255,255,.5), transparent 70%),
    repeating-linear-gradient(0deg, transparent 0 26px, rgba(255,255,255,.16) 26px 28px),
    linear-gradient(150deg,#f6c453,#e2574c 78%);
}
.ph-cap{font-family:var(--marker);text-align:center;padding-top:10px;font-size:1.12rem;color:#3c3a33}
.burst{
  position:absolute;top:-26px;right:-4px;width:138px;z-index:4;
  filter:drop-shadow(0 8px 12px rgba(40,22,2,.3));animation:floaty 3.8s ease-in-out infinite alternate;
}
@keyframes floaty{from{transform:rotate(9deg) translateY(0)}to{transform:rotate(12deg) translateY(-8px)}}
.mini-sticker{
  position:absolute;font-family:var(--marker);font-size:.95rem;background:var(--card);
  border:2px solid rgba(46,61,89,.2);border-radius:999px;padding:5px 14px 7px;
  box-shadow:2px 3px 0 rgba(43,32,10,.2);white-space:nowrap;
}
.s1{bottom:52px;left:-14px;transform:rotate(-5deg);color:var(--red-dark)}
.s2{bottom:0;left:96px;transform:rotate(2.4deg);color:#3c6e46}
.hero-arrow{position:absolute;left:-40px;bottom:-16px;width:130px;opacity:.75;transform:rotate(6deg)}
.arrow-note{position:absolute;right:6px;bottom:-42px;font-family:var(--hand);font-style:italic;color:#5c4a2e;font-size:.98rem}

.h-scrap{font-family:var(--marker);font-weight:700;font-size:clamp(1.55rem,3.1vw,2.25rem);line-height:1.2}
.h-scrap .ico{display:inline-block;transform:rotate(-6deg);margin-right:6px}
.squig{display:block;margin:4px 0 0 4px}
.squig.blue path{stroke:#4a7fb5}
.squig.green path{stroke:#58a05f}
.sec{padding:64px 0 8px}

/* ══════════ THẺ GIÁ ══════════ */
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(255px,1fr));gap:40px 28px;margin-top:44px}
.card{
  position:relative;background:var(--card);border:2px solid rgba(46,61,89,.1);border-radius:14px;
  padding:34px 24px 26px;text-align:center;box-shadow:0 16px 30px rgba(60,35,10,.16);
  transition:transform .22s, box-shadow .22s;display:flex;flex-direction:column;
}
.card.r-a{transform:rotate(-.7deg)} .card.r-b{transform:rotate(.55deg)} .card.r-c{transform:rotate(-.4deg)}
.card:hover{transform:translateY(-9px) rotate(0);box-shadow:0 24px 42px rgba(60,35,10,.22)}
.badge{
  position:absolute;top:-16px;right:-10px;z-index:4;font-family:var(--marker);font-size:.86rem;color:#5d4a12;
  background:var(--yellow);border:2px solid rgba(46,61,89,.2);border-radius:999px;padding:4px 13px 6px;
  transform:rotate(6deg);box-shadow:2px 3px 0 rgba(43,32,10,.2);
}
.badge.b-blue{background:var(--blue);color:#274a68;transform:rotate(-5deg)}
.badge.b-green{background:var(--green);color:#2f5c37}
.badge.b-gray{background:#e8e2d2;color:#6a6152}
.badge.b-pink{background:var(--pink);color:#8c3a55;transform:rotate(-4deg)}
.p-icon{
  width:78px;height:78px;margin:2px auto 12px;display:grid;place-items:center;font-size:2.3rem;
  border:3px solid var(--ink);border-radius:48% 52% 55% 45% / 52% 48% 58% 42%;
  background:#fff8e1;transform:rotate(-3deg);
}
.card h3{font-family:var(--marker);font-size:1.42rem;margin-bottom:2px}
.card .desc{color:var(--ink-soft);font-size:1rem;line-height:1.4}
.old-price{color:var(--pencil);margin-top:12px;font-size:1rem}
.old-price s{text-decoration-color:var(--red);text-decoration-thickness:2.5px}
.price{font-family:var(--marker);font-weight:700;color:var(--red-dark);font-size:2.15rem;line-height:1.1;margin:2px 0 4px}
.price small{font-family:var(--hand);font-size:1rem;color:var(--ink-soft);font-weight:400}
.deal-note{color:var(--red-dark);font-size:1rem;margin-bottom:2px}
.feat{list-style:none;text-align:left;margin:16px auto 20px;max-width:260px}
.feat li{
  padding:3px 0 3px 30px;position:relative;font-size:1.02rem;color:#3c4c70;
  background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='18' height='18' viewBox='0 0 18 18'%3E%3Cpath d='M3 10 l4 5 8 -11' fill='none' stroke='%23d94f43' stroke-width='3.2' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") no-repeat 2px 7px;
}
.btn-card{width:100%;background:var(--red);color:#fff8e7}
.btn-card:hover{background:#e2604f}
.zalo-mini{display:block;text-align:center;margin-top:12px;font-size:.98rem;color:#42527a;text-decoration:underline dashed;text-underline-offset:4px}
.zalo-mini:hover{color:var(--red-dark)}

.more-accs{display:flex;flex-wrap:wrap;gap:14px 16px;align-items:center;margin-top:38px}
.more-label{font-family:var(--marker);font-size:1.1rem;color:#5c4a2e;transform:rotate(-1deg)}
.chip{
  font-family:var(--marker);font-size:.95rem;color:var(--ink);text-decoration:none;background:var(--card);
  border:2px dashed rgba(46,61,89,.32);border-radius:999px;padding:6px 16px 8px;
  box-shadow:2px 3px 0 rgba(43,32,10,.15);transition:.18s;
}
.chip:hover{transform:translateY(-3px) rotate(1.5deg)!important;border-style:solid;background:#fff8e1}
.chip:nth-child(odd){transform:rotate(-1.2deg)}
.chip:nth-child(even){transform:rotate(1.1deg)}
.disclaimer{margin-top:16px;color:var(--pencil);font-style:italic;font-size:.98rem}

/* ══════════ KHỐI RỘNG (LOCKET / WIN) ══════════ */
.wide-card{position:relative;margin-top:46px;border-radius:16px;padding:30px 30px 26px;box-shadow:0 16px 30px rgba(60,35,10,.16);transform:rotate(-.35deg)}
.wide-card.w-pink{background:var(--pink);border:2px solid rgba(46,61,89,.14)}
.wide-card.w-blue{background:var(--blue);border:2px solid rgba(46,61,89,.14)}
.wide-card h3{font-family:var(--marker);font-size:1.5rem}
.wide-card .w-sub{color:#42527a;margin-top:2px}
.wide-grid{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:20px}
.wide-col{background:rgba(255,253,244,.8);border-radius:12px;padding:16px 20px 14px;box-shadow:2px 3px 0 rgba(43,32,10,.1)}
.wide-col h4{font-family:var(--marker);font-size:1.12rem;margin-bottom:2px}
.price3{list-style:none;margin:10px 0 6px}
.price3 li{display:flex;justify-content:space-between;align-items:baseline;gap:12px;border-bottom:2px dashed rgba(46,61,89,.16);padding:7px 2px;font-size:1.04rem;color:#3c4c70}
.price3 li:last-child{border-bottom:none}
.price3 b{font-family:var(--marker);color:var(--red-dark);white-space:nowrap}
.svc-list{list-style:none;margin-top:20px;max-width:860px}
.svc-row{display:flex;justify-content:space-between;align-items:center;gap:16px;background:var(--card);border:2px solid rgba(46,61,89,.14);border-radius:12px;padding:13px 20px;margin-bottom:12px;box-shadow:2px 4px 0 rgba(43,32,10,.12)}
.svc-row:nth-child(odd){transform:rotate(-.4deg)}
.svc-row:nth-child(even){transform:rotate(.35deg)}
.svc-row span{font-family:var(--marker);font-size:1.02rem;color:#3c4c70}
.svc-row span small{display:block;font-family:var(--hand);color:var(--ink-soft);font-size:.95rem}
.svc-row b{font-family:var(--marker);color:var(--red-dark);white-space:nowrap;font-size:1.1rem}
.save-stamp{
  display:inline-block;font-family:var(--marker);font-size:.9rem;background:var(--green);color:#2f5c37;
  border:2px solid rgba(46,61,89,.22);border-radius:999px;padding:2px 12px 4px;transform:rotate(-2deg);margin-left:10px;
}

/* ══════════ CAM KẾT + BƯỚC ══════════ */
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:6px 46px;margin-top:26px}
.checklist{list-style:none}
.checklist li{display:flex;gap:12px;padding:8px 0;align-items:flex-start}
.cbx{
  flex:0 0 auto;width:30px;height:30px;margin-top:4px;display:grid;place-items:center;
  border:2.5px solid var(--ink);border-radius:42% 58% 50% 50% / 55% 45% 55% 45%;
  color:var(--red-dark);font-family:var(--marker);font-size:1.1rem;background:var(--card);
  transform:rotate(-2deg);box-shadow:1.5px 2px 0 rgba(43,32,10,.18);
}
.checklist b{color:var(--red-dark)}
.steps{display:flex;gap:44px;list-style:none;margin-top:40px;counter-reset:step}
.steps li{flex:1;position:relative;text-align:center;padding:0 6px}
.steps li:not(:last-child)::after{
  content:'➜';position:absolute;right:-34px;top:26px;color:var(--red);
  font-size:1.7rem;transform:rotate(8deg);
}
.num{
  display:inline-grid;place-items:center;width:58px;height:58px;margin-bottom:12px;
  font-family:var(--marker);font-weight:700;font-size:1.7rem;color:var(--ink);
  border:3px solid var(--ink);border-radius:47% 53% 52% 48% / 55% 47% 53% 45%;
  background:var(--yellow);transform:rotate(-4deg);box-shadow:2.5px 3px 0 rgba(43,32,10,.22);
}
.steps li:nth-child(2) .num{background:var(--pink);transform:rotate(3deg)}
.steps li:nth-child(3) .num{background:var(--green);transform:rotate(-3deg)}
.steps h4{font-family:var(--marker);font-size:1.18rem;margin-bottom:4px}
.steps p{font-size:1.02rem;color:#42527a}

/* ══════════ TRANG CHI TIẾT ══════════ */
.crumb{
  display:inline-flex;align-items:center;gap:8px;font-family:var(--marker);font-size:1rem;color:#5c4a2e;
  text-decoration:none;background:var(--card);border:2px solid rgba(46,61,89,.18);border-radius:999px;
  padding:6px 18px 8px;box-shadow:2px 3px 0 rgba(43,32,10,.15);transform:rotate(-1deg);margin-top:26px;transition:.18s;
}
.crumb:hover{transform:translateY(-2px) rotate(0);color:var(--red-dark)}
.d-hero{display:flex;gap:38px;align-items:center;padding:30px 0 6px}
.d-icon{
  flex:0 0 auto;width:122px;height:122px;display:grid;place-items:center;font-size:3.5rem;
  border:3.5px solid var(--ink);border-radius:48% 52% 55% 45% / 52% 48% 58% 42%;
  background:#fff8e1;transform:rotate(-4deg);box-shadow:3px 4px 0 rgba(43,32,10,.2);
}
.d-title{font-size:clamp(2.1rem,4.6vw,3rem)}
.d-tag{font-style:italic;color:var(--ink-soft);font-size:1.15rem;margin-top:10px;max-width:30em}

.cmp{width:100%;max-width:880px;border-collapse:collapse;margin-top:34px;background:var(--card);border:2px solid rgba(46,61,89,.14);border-radius:14px;overflow:hidden;box-shadow:0 14px 28px rgba(60,35,10,.14)}
.cmp th,.cmp td{padding:12px 16px;border-bottom:2px dashed rgba(46,61,89,.16);text-align:left;font-size:1.02rem;vertical-align:top}
.cmp thead th{font-family:var(--marker);font-size:1.05rem;background:#fff3d6;border-bottom:2.5px solid rgba(46,61,89,.28)}
.cmp tbody tr:last-child td{border-bottom:none}
.cmp td:first-child{font-family:var(--marker);font-size:.98rem;width:34%;color:#42527a}
.cmp .no{color:#9a6a5a}
.cmp .yes{color:#2f7a3d;font-family:var(--hand)}
.cmp tr.hot td{background:#fff6dd}
.cmp tr.hot td:last-child{font-family:var(--marker);color:var(--red-dark)}

.receipt{position:relative;max-width:620px;background:var(--card);border:2.5px dashed rgba(46,61,89,.32);border-radius:16px;padding:24px 30px 20px;margin-top:38px;transform:rotate(-.5deg);box-shadow:0 14px 28px rgba(60,35,10,.14)}
.receipt h3{font-family:var(--marker);font-size:1.3rem;margin-bottom:6px}
.r-row{display:flex;justify-content:space-between;align-items:baseline;gap:14px;padding:10px 2px;border-bottom:2px dashed rgba(46,61,89,.14);font-size:1.06rem;color:#3c4c70}
.r-row .val{font-family:var(--marker);white-space:nowrap;color:var(--ink)}
.r-row s{color:var(--pencil);text-decoration-color:var(--red);text-decoration-thickness:2.5px}
.r-row.big .val{color:var(--red-dark);font-size:1.55rem}
.r-save{display:inline-block;font-family:var(--marker);background:var(--green);color:#2f5c37;border:2px solid rgba(46,61,89,.22);border-radius:999px;padding:5px 16px 7px;transform:rotate(-1.5deg);box-shadow:2px 3px 0 rgba(43,32,10,.18);margin-top:10px}
.warn-note{
  display:inline-block;background:#ffe97a;border:2px solid rgba(46,61,89,.2);border-radius:12px;
  padding:10px 18px;font-family:var(--marker);font-size:1rem;color:#5d4a12;transform:rotate(-.8deg);
  box-shadow:2px 3px 0 rgba(43,32,10,.16);margin-top:16px;
}

/* ══════════ STICKY NOTE ══════════ */
.notes{display:grid;grid-template-columns:repeat(auto-fit,minmax(228px,1fr));gap:34px 26px;margin-top:44px}
.note{
  position:relative;padding:34px 20px 18px;border-radius:3px;min-height:190px;
  box-shadow:4px 8px 18px rgba(40,22,2,.24);display:flex;flex-direction:column;gap:10px;
  transition:transform .22s;
}
.note:hover{transform:scale(1.04) rotate(0)!important}
.n-yellow{background:#ffe97a;transform:rotate(-2deg)}
.n-pink{background:#ffc9d8;transform:rotate(1.6deg)}
.n-blue{background:#bfe3f2;transform:rotate(-1.2deg)}
.note blockquote{font-style:italic;font-size:1.05rem;line-height:1.45;color:#4a3d20}
.n-pink blockquote{color:#7c3a4b}.n-blue blockquote{color:#2f5068}
.note figcaption{margin-top:auto;font-family:var(--marker);font-size:.98rem}
.note figcaption small{display:block;font-family:var(--hand);color:rgba(40,30,10,.55);font-size:.9rem}
.note-empty{
  border:2.5px dashed rgba(90,80,60,.5);background:transparent;box-shadow:none;
  align-items:center;justify-content:center;text-align:center;color:var(--pencil);
  font-style:italic;font-size:1.05rem;transform:rotate(2deg);
}

/* ══════════ FAQ ══════════ */
.faq{margin-top:26px;max-width:820px}
.faq details{border-bottom:2px dashed rgba(46,61,89,.24);padding:10px 6px}
.faq summary{
  list-style:none;cursor:pointer;display:flex;align-items:center;gap:14px;
  font-family:var(--marker);font-size:1.12rem;padding:6px 0;user-select:none;
}
.faq summary::-webkit-details-marker{display:none}
.faq summary .plus{
  flex:0 0 auto;width:30px;height:30px;display:grid;place-items:center;
  font-family:var(--marker);font-size:1.2rem;color:#fff8e7;background:var(--red);
  border-radius:46% 54% 50% 50% / 52% 48% 55% 45%;box-shadow:1.5px 2px 0 rgba(43,32,10,.25);
  transition:transform .25s;
}
.faq details[open] summary .plus{transform:rotate(45deg);background:#3c6e46}
.faq details p{padding:2px 6px 10px 46px;color:#42527a;font-size:1.05rem}

/* ══════════ FOOTER — BÌA SAU ══════════ */
.footer{
  margin:78px -46px 0 -142px;background:linear-gradient(170deg,#5f4a2e,#4c3a20);
  border-radius:0 0 22px 16px;padding:52px 54px 30px 148px;color:#f3e7cf;
  box-shadow:inset 0 14px 26px -16px rgba(0,0,0,.55);position:relative;
  background-image:
    radial-gradient(500px 200px at 85% 0%, rgba(255,224,170,.08), transparent 70%),
    linear-gradient(170deg,#5f4a2e,#4c3a20);
}
.footer h2{font-family:var(--marker);font-size:clamp(1.5rem,3vw,2rem);color:#ffe9b8}
.footer .f-lead{margin:8px 0 24px;color:#e4d3b2;font-size:1.08rem;max-width:44em}
.contact-row{display:flex;flex-wrap:wrap;gap:16px}
.contact{
  display:inline-block;font-family:var(--marker);font-size:1rem;color:#3c3a33;text-decoration:none;
  background:#fdf6e4;padding:10px 20px 12px;border-radius:12px;
  box-shadow:3px 4px 0 rgba(0,0,0,.35);transition:.18s;
}
.contact:hover{transform:translateY(-3px) rotate(-1deg)}
.contact.zalo{transform:rotate(-1.2deg)}
.contact.fb{transform:rotate(.8deg)}
.contact.tt{transform:rotate(-.6deg)}
.pay-row{display:flex;flex-wrap:wrap;gap:10px;margin-top:22px;align-items:center}
.pay-label{font-size:1rem;color:#d8c5a0;font-style:italic}
.pay{
  font-size:.92rem;font-family:var(--marker);color:#5c4a2e;background:#f3e3bd;
  padding:3px 13px 5px;border-radius:999px;transform:rotate(-1deg);
}
.order{margin-top:34px;background:rgba(253,246,228,.09);border:2px dashed rgba(243,231,207,.4);border-radius:16px;padding:24px 24px 26px;max-width:660px}
.order h3{font-family:var(--marker);font-size:1.25rem;color:#ffe9b8;margin-bottom:14px}
.order .row{display:flex;gap:14px;flex-wrap:wrap;margin-bottom:14px}
.order input,.order select{
  flex:1;min-width:180px;font-family:var(--hand);font-size:1.05rem;
  background:transparent;border:none;border-bottom:2.5px dashed rgba(253,246,228,.55);
  padding:7px 4px;outline:none;color:#fdf6e4;
}
.order select option{color:#3c3a33}
.order input::placeholder{color:#cdbb96}
.order input:focus,.order select:focus{border-bottom-color:var(--yellow)}
.form-hint{margin-top:14px;color:#ffe9b8;font-size:1rem}
.form-hint[hidden]{display:none}
.fineprint{margin-top:30px;color:#c9b58f;font-size:.95rem;font-style:italic}

/* ══════════ REVEAL ══════════ */
.reveal{opacity:0;transform:translateY(18px) rotate(var(--rr,0deg));transition:opacity .6s ease var(--d,0s), transform .6s ease var(--d,0s)}
.reveal.in{opacity:1;transform:translateY(0) rotate(var(--rr,0deg))}
.r-a.reveal{--rr:-.7deg}.r-b.reveal{--rr:.55deg}.r-c.reveal{--rr:-.4deg}
.n-yellow.reveal{--rr:-2deg}.n-pink.reveal{--rr:1.6deg}.n-blue.reveal{--rr:-1.2deg}
.wide-card.reveal{--rr:-.35deg}

a:focus-visible,button:focus-visible,summary:focus-visible,input:focus-visible,select:focus-visible{
  outline:3px dashed var(--red);outline-offset:3px;border-radius:6px;
}

/* ══════════ RESPONSIVE ══════════ */
@media (max-width:1010px){
  .tabs{display:none}
  .mobile-tabs{display:flex;flex-wrap:wrap;gap:10px;width:100%;margin-top:18px}
  .mobile-tabs a{
    font-family:var(--marker);font-size:.92rem;color:var(--ink);text-decoration:none;
    padding:6px 15px 8px;border-radius:999px;border:2px solid rgba(46,61,89,.24);
    box-shadow:2px 2px 0 rgba(60,35,10,.2);
  }
  .mobile-tabs a:nth-child(1){background:var(--pink)}
  .mobile-tabs a:nth-child(2){background:var(--blue)}
  .mobile-tabs a:nth-child(3){background:var(--yellow)}
  .mobile-tabs a:nth-child(4){background:var(--green)}
  .mobile-tabs a:nth-child(5){background:var(--orange)}
}
@media (max-width:860px){
  body{font-size:17.5px}
  .wrap{margin-top:24px;padding:0 10px}
  .notebook{border-left-width:14px}
  .spiral{left:-10px;width:64px;background-size:64px 44px}
  .notebook::before{left:64px}
  .page{padding:24px 22px 0 82px}
  .footer{margin:64px -22px 0 -82px;padding:40px 26px 26px 88px;border-radius:0 0 22px 0}
  .hero{flex-direction:column;gap:14px;padding-top:30px}
  .hero-art{width:100%;min-height:330px}
  .hero-arrow{left:auto;right:30px}
  .d-hero{flex-direction:column;text-align:center;gap:16px;padding-top:24px}
  .d-icon{width:96px;height:96px;font-size:2.7rem}
  .d-tag{margin-left:auto;margin-right:auto}
  .grid2{grid-template-columns:1fr}
  .steps{flex-direction:column;gap:34px;max-width:420px;margin-left:auto;margin-right:auto}
  .steps li:not(:last-child)::after{right:auto;left:50%;top:auto;bottom:-40px;transform:rotate(96deg)}
  .burst{width:112px;top:-18px;right:-2px}
  .wide-grid{grid-template-columns:1fr}
}
@media (max-width:480px){
  .page{padding:20px 14px 0 64px}
  .notebook::before{left:50px}
  .footer{margin:56px -14px 0 -64px;padding:34px 18px 24px 68px}
  .brand-name{font-size:1.5rem}
  .polaroid{width:94%}
  .s2{left:60px}
  .cmp th,.cmp td{padding:8px 9px;font-size:.92rem}
  .cmp td:first-child{width:37%;font-size:.88rem;padding-right:6px}
  .r-row{flex-wrap:wrap}
  .r-row.big .val{font-size:1.3rem}
  .svc-row{flex-wrap:wrap;padding:11px 14px}
  .wide-card{padding:24px 18px 20px}
}
"""

MASTHEAD = """<header class="masthead">
        <a class="brand" href="index.html">
          <span class="brand-book">📓</span>
          <span class="brand-name">Sổ Acc</span>
          <span class="brand-tag">xwuan</span>
        </a>
        <p class="mast-note">“nhanh · sạch · uy tín — ghi trong sổ này hết ✏️”</p>
        <nav class="mobile-tabs" aria-label="Mục lục">@@MTABS@@</nav>
      </header>"""

FOOTER = """<footer class="footer" id="lienhe">
        <h2>📞 Sổ tay liên hệ</h2>
        <p class="f-lead">Nhắn ngay để được báo giá + tư vấn acc phù hợp. Kích hoạt trong 2–5 phút, hỗ trợ hỏi đáp 24/24 🎉</p>
        <div class="contact-row">
          <a class="contact zalo" href="https://zalo.me/0822307662" target="_blank" rel="noopener">💬 Zalo: 0822.307.662</a>
          <a class="contact fb" href="https://www.facebook.com/xwuan1/" target="_blank" rel="noopener">📘 Facebook: Xwuan</a>
          <a class="contact tt" href="https://www.tiktok.com/@xwuan2" target="_blank" rel="noopener">🎵 TikTok: @xwuan2</a>
        </div>
        <div class="pay-row">
          <span class="pay-label">cam kết trong sổ:</span>
          <span class="pay">⚡ Kích hoạt 2–5 phút</span>
          <span class="pay">🕐 Hỗ trợ 24/24</span>
          <span class="pay">🛡️ Bảo hành theo gói</span>
        </div>
        <form class="order" id="orderForm">
          <h3>✍️ Đặt nhanh — ghi vào sổ:</h3>
          <div class="row">
            <input name="ten" placeholder="Tên của bạn…" required>
            <input name="sdt" placeholder="SĐT / Zalo…" required>
          </div>
          <div class="row">
            <select name="acc" aria-label="Chọn acc">@@OPTIONS@@</select>
            <input name="ghi" placeholder="Ghi chú (thời gian, số lượng…)">
          </div>
          <button class="btn btn-red" type="submit">📨 Gửi đơn qua Zalo</button>
          <p class="form-hint" id="formHint" hidden>Đã chép nội dung đơn vào bộ nhớ tạm — dán vào khung chat Zalo là xong nha! 💜</p>
        </form>
        <p class="fineprint">© <span id="year">2026</span> Sổ Acc Xwuan · Nhanh · Sạch · Uy tín · Made with 📓✏️</p>
      </footer>"""

JS = """
// ── hiệu ứng các mẩu giấy hiện dần khi cuộn ──
const io = new IntersectionObserver(entries => {
  entries.forEach(e => {
    if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
  });
}, { threshold: .14 });
document.querySelectorAll('.reveal').forEach(el => io.observe(el));

// ── gửi đơn: chép tin nhắn + mở Zalo ──
const ZALO = '0822307662';
document.getElementById('orderForm').addEventListener('submit', e => {
  e.preventDefault();
  const f = e.target;
  const msg = 'Xin chào Sổ Acc Xwuan! 📓\\n'
    + 'Mình là ' + f.ten.value.trim() + '\\n'
    + 'Muốn mua: ' + f.acc.value
    + (f.ghi.value.trim() ? '\\nGhi chú: ' + f.ghi.value.trim() : '')
    + '\\nLiên hệ: ' + f.sdt.value.trim();
  const hint = document.getElementById('formHint');
  const done = () => { hint.hidden = false; setTimeout(() => hint.hidden = true, 8000); };
  if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(msg).then(done).catch(done);
  } else { done(); }
  window.open('https://zalo.me/' + ZALO, '_blank');
});

// ── năm tự động ──
document.getElementById('year').textContent = new Date().getFullYear();
"""

HEAD = """<!doctype html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>@@TITLE@@</title>
<meta name="description" content="@@DESC@@">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ctext y='.9em' font-size='88'%3E%F0%9F%93%93%3C/text%3E%3C/svg%3E">
<style>
@@CSS@@
</style>
</head>
<body>

<div class="wrap">
  <div class="notebook">
    <div class="spiral" aria-hidden="true"></div>

    <nav class="tabs" aria-label="Mục lục">@@TABS@@</nav>

    <div class="page">
"""

TAIL = """
    </div><!-- /.page -->
  </div><!-- /.notebook -->
</div><!-- /.wrap -->

<script>@@JS@@</script>
</body>
</html>
"""


def tabs_html(items):
    return '\n      '.join('<a href="%s">%s</a>' % (h, l) for h, l in items)


def options_html(selected=None):
    accs = ['ChatGPT Plus', 'CapCut Pro', 'Canva Pro', 'YouTube Premium', 'Netflix 4K UHD',
            'Google AI Pro (Gemini)', 'Meitu SVIP', 'Locket Gold', 'Windows / Office', 'Khác (tư vấn giúp)']
    out = []
    for a in accs:
        sel = ' selected' if a == selected else ''
        out.append('<option%s>%s</option>' % (sel, a))
    return '\n              '.join(out)


def render_page(fname, title, desc, tabs, content, selected_acc=None):
    t = tabs_html(tabs)
    html = (HEAD
            .replace('@@TITLE@@', title)
            .replace('@@DESC@@', desc)
            .replace('@@CSS@@', CSS)
            .replace('@@TABS@@', t))
    html = html.replace(HEAD_MARK, '')  # no-op safety
    body = (MASTHEAD.replace('@@MTABS@@', t) + '\n\n      ' + content + '\n\n      ' +
            FOOTER.replace('@@OPTIONS@@', options_html(selected_acc)))
    html += body
    html += TAIL.replace('@@JS@@', JS)
    open(fname, 'w', encoding='utf-8').write(html)
    print('→ %s (%.0f KB)' % (fname, len(html) / 1024))


HEAD_MARK = '@@HEADMARK@@'
