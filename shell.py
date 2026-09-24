# -*- coding: utf-8 -*-
"""Khung QUYỂN SỔ LẬT TRANG dùng chung cho mọi trang.
Trang = danh sách các 'mặt giấy' (faces); engine JS gắp thành tờ (leaf):
 - desktop (>=860px): sổ mở 2 trang, lật tờ quanh gáy giữa
 - mobile  (<860px): sổ 1 trang, lật tờ quanh lò xo gáy trái
"""

FONT = open('fontface.css', encoding='utf-8').read()

CSS = FONT + """
:root{ --pw:460px; --ph:620px; }
*{box-sizing:border-box;margin:0;padding:0}
html,body{height:100%}
::selection{background:#ffd95e;color:#4a3410}
body{
  font-family:'Patrick Hand','Segoe Print','Comic Sans MS',cursive;
  color:#2e3d59; overflow-x:hidden;
  background:
    radial-gradient(1100px 500px at 50% -80px, rgba(255,233,190,.16), transparent 65%),
    url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='240' height='240'%3E%3Cg fill='none' stroke='%23ffe9c4' stroke-opacity='.055' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M18 44 q13 -20 26 0 q13 20 26 0'/%3E%3Ccircle cx='196' cy='36' r='11'/%3E%3Cpath d='M96 150 l8 16 18 3 -13 13 3 18 -16 -9 -16 9 3 -18 -13 -13 18 -3z'/%3E%3Cpath d='M150 210 h34 m-34 12 h22'/%3E%3Ccircle cx='52' cy='200' r='9'/%3E%3Cpath d='M180 120 q12 -16 24 0'/%3E%3Cpath d='M30 120 l12 -12 12 12 12 -12'/%3E%3C/g%3E%3C/svg%3E"),
    linear-gradient(160deg,#8f6f47,#63512f 55%,#4a3b21);

}
body::after{content:'';position:fixed;inset:0;pointer-events:none;z-index:90;box-shadow:inset 0 0 190px rgba(25,12,0,.5)}

/* ═══ THANH TRÊN ═══ */
.topbar{
  display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap;
  max-width:1200px;margin:0 auto;padding:14px 18px 4px;position:relative;z-index:5;
}
.brand{display:flex;align-items:center;gap:9px;text-decoration:none;color:#fdf3dd}
.brand-book{font-size:1.5rem;display:inline-block;transform:rotate(-6deg)}
.brand-name{font-family:'Shantell Sans',cursive;font-weight:700;font-size:1.3rem;letter-spacing:.5px;color:#fdf3dd}
.brand-tag{
  font-family:'Shantell Sans',cursive;font-size:.8rem;color:#5d4a12;background:var(--yellow,#ffdf6b);
  padding:1px 10px 3px;border-radius:8px;transform:rotate(-3deg);box-shadow:2px 2px 0 rgba(43,32,10,.3);
}
.top-note{color:#e4d3b2;font-style:italic;font-size:.98rem}

/* ═══ SÂN KHẤU SỔ ═══ */
.stage{
  min-height:calc(100vh - 76px);display:flex;flex-direction:column;align-items:center;
  justify-content:flex-start;gap:14px;padding:10px 12px 26px;position:relative;z-index:2;
}
.book-wrap{position:relative;perspective:2400px;-webkit-perspective:2400px;touch-action:pan-y}
.book{
  position:relative;width:calc(var(--pw)*2);height:var(--ph);
  transform-style:preserve-3d;-webkit-transform-style:preserve-3d;
}
.book-wrap.single .book{width:var(--pw)}
/* đế bìa */
.board{
  position:absolute;top:-7px;bottom:-9px;width:calc(var(--pw) + 7px);
  background:linear-gradient(150deg,#7a5c39,#5d4426 70%);
  border-radius:10px 14px 14px 10px;box-shadow:0 26px 60px rgba(30,16,2,.55), 0 4px 0 #46331c;
}
.board.l{left:-7px}
.board.r{right:-7px;border-radius:14px 10px 10px 14px}
.board::after{ /* vân bìa cứng */
  content:'';position:absolute;inset:0;border-radius:inherit;
  background:repeating-linear-gradient(115deg, rgba(255,235,200,.05) 0 3px, transparent 3px 9px);
}
.book-wrap.single .board.l{display:none}
.book-wrap.single .board.r{width:calc(var(--pw) + 14px);right:-7px}

/* chồng giấy kẹp dưới */
.book::after{
  content:'';position:absolute;left:3px;right:3px;top:6px;bottom:-4px;z-index:0;
  background:#e9dfc4;border-radius:6px;
  box-shadow:0 3px 0 #e2d7ba, 0 6px 0 #d8ccb0;
}

/* ═══ TỜ GIẤY ═══ */
.leaf{
  position:absolute;top:0;right:0;width:var(--pw);height:var(--ph);
  transform-origin:left center;transform-style:preserve-3d;-webkit-transform-style:preserve-3d;
  transition:transform .95s cubic-bezier(.42,.05,.32,1);will-change:transform;z-index:5;
}
.leaf.flipped{transform:rotateY(-180deg)}
.book-wrap.single .leaf{transition:transform .95s cubic-bezier(.42,.05,.32,1), opacity .3s ease .68s}
.book-wrap.single .leaf.flipped{opacity:0}
.book.noanim .leaf{transition:none!important}
.book-wrap{transition:opacity .17s ease}
.book-wrap.jumping{opacity:0}
.book-wrap.idle .book{animation:breathe 2.8s ease-in-out infinite}
@keyframes breathe{0%,100%{transform:scale(1)}50%{transform:scale(1.014) rotate(.15deg)}}
.sparkle{position:absolute;font-size:1.35em;pointer-events:none;z-index:80;animation:spark 1.5s ease-out forwards}
@keyframes spark{0%{opacity:0;transform:translateY(8px) scale(.4) rotate(0)}18%{opacity:1}100%{opacity:0;transform:translateY(-48px) scale(1.25) rotate(26deg)}}
.face{
  position:absolute;inset:0;overflow:hidden;
  backface-visibility:hidden;-webkit-backface-visibility:hidden;
  background:
    linear-gradient(90deg, rgba(58,38,12,.10) 0 3px, transparent 30px),
    repeating-linear-gradient(180deg, transparent 0 31px, rgba(120,164,196,.30) 31px 33px),
    linear-gradient(180deg,#fdf9ee,#f7f1de);
  border-radius:4px 12px 12px 4px;
  box-shadow:inset 0 0 46px rgba(88,58,20,.10);
}
.face.back{
  transform:rotateY(180deg);border-radius:12px 4px 4px 12px;
  background:
    linear-gradient(-90deg, rgba(58,38,12,.10) 0 3px, transparent 30px),
    repeating-linear-gradient(180deg, transparent 0 31px, rgba(120,164,196,.30) 31px 33px),
    linear-gradient(180deg,#f9f3e0,#fdf9ee);
}
/* bóng gáy khi lật */
.leaf.flipping{box-shadow:0 0 34px rgba(30,16,2,.4)}
.face.front::before,.face.back::before{
  content:'';position:absolute;top:0;bottom:0;pointer-events:none;z-index:3;
}
.face.front::before{left:0;width:38px;background:linear-gradient(90deg,rgba(80,52,18,.16),transparent)}
.face.back::before{right:0;width:38px;background:linear-gradient(-90deg,rgba(80,52,18,.16),transparent)}
.face-in{position:absolute;inset:0;padding:1.15em 1.35em .9em;overflow:hidden}
.face-in.blank-in{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:.5em;color:#a89a78;font-style:italic;text-align:center}
.blank-in .b-doodle{font-size:2.4em;transform:rotate(-8deg)}

/* gáy giữa (chỉ sổ mở) */
.spine{
  display:none;position:absolute;top:-4px;bottom:-6px;left:50%;width:52px;transform:translateX(-50%);
  z-index:60;pointer-events:none;
  background:linear-gradient(90deg,transparent,rgba(60,38,12,.20) 30% 70%,transparent);
}
.spine::after{
  content:'';position:absolute;top:8px;bottom:8px;left:50%;width:0;transform:translateX(-50%);
  border-left:3px dashed rgba(94,70,40,.5);
}
.book-wrap.spread .spine{display:block}
/* lò xo gáy trái (chỉ sổ 1 trang) */
.spiral-edge{
  display:none;position:absolute;top:-8px;bottom:-10px;left:-13px;width:58px;z-index:61;pointer-events:none;
  background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='58' height='56'%3E%3Cg fill='none' stroke-linecap='round'%3E%3Cg stroke='%232a2a30' stroke-opacity='.16' stroke-width='4.4' transform='translate(-2 3)'%3E%3Cpath d='M6 27 C 6 11 42 9 52 21'/%3E%3Cpath d='M6 31 C 6 47 46 49 52 36'/%3E%3C/g%3E%3Cg stroke='%23878795' stroke-width='4.4'%3E%3Cpath d='M6 27 C 6 11 42 9 52 21'/%3E%3Cpath d='M6 31 C 6 47 46 49 52 36'/%3E%3C/g%3E%3Cg stroke='%23dcdce4' stroke-width='1.5'%3E%3Cpath d='M6 26 C 6 12 40 10 50 19'/%3E%3Cpath d='M6 30 C 6 44 43 47 50 35'/%3E%3C/g%3E%3C/g%3E%3Cellipse cx='56' cy='28.5' rx='3.8' ry='5.4' fill='%23ded0b2' stroke='%23a8987b' stroke-width='1.3'/%3E%3C/svg%3E") repeat-y;
  background-size:58px 56px;
}
.book-wrap.single .spiral-edge{display:block}

/* vùng chạm lật trang */
.flip-zone{position:absolute;top:0;bottom:0;width:15%;z-index:70;cursor:pointer;background:transparent;border:none;padding:0;touch-action:none}
.leaf.dragging{transition:none!important;box-shadow:0 0 40px rgba(30,16,2,.45)}
.book-wrap.dragging{cursor:grabbing}
.flip-zone.next{right:0}
.flip-zone.prev{left:0}
.flip-zone:focus-visible{outline:3px dashed #d94f43;outline-offset:-6px}
.flip-hint{
  position:absolute;bottom:10px;font-family:'Shantell Sans',cursive;font-size:.8em;color:#8a8172;
  opacity:.65;transition:.25s;pointer-events:none;
}
.flip-zone.next .flip-hint{right:10px}
.flip-zone.prev .flip-hint{left:10px}
.flip-zone:hover .flip-hint{opacity:1;transform:scale(1.15)}

/* tab dán cạnh phải (chỉ sổ mở) */
.edge-tabs{display:none;position:absolute;top:0;right:-26px;height:100%;z-index:65}
.book-wrap.spread .edge-tabs{display:block}
.edge-tabs button{
  position:absolute;right:0;transform:translateX(52%);width:34px;padding:12px 0 14px;
  font-family:'Shantell Sans',cursive;font-size:.72rem;color:#2e3d59;border:2px solid rgba(46,61,89,.28);
  border-left:none;border-radius:0 10px 10px 0;cursor:pointer;box-shadow:3px 3px 0 rgba(60,35,10,.28);
  writing-mode:vertical-rl;letter-spacing:1px;transition:.2s;
}
.edge-tabs button:hover{transform:translateX(72%)}
.edge-tabs button:nth-child(1){top:9%;background:#ffc9d8}
.edge-tabs button:nth-child(2){top:24%;background:#c9e6f7}
.edge-tabs button:nth-child(3){top:39%;background:#ffdf6b}
.edge-tabs button:nth-child(4){top:54%;background:#cfeec2}
.edge-tabs button:nth-child(5){top:69%;background:#ffb3a0}

/* ═══ ĐIỀU KHIỂN DƯỚI ═══ */
.controls{display:flex;align-items:center;gap:14px;position:relative;z-index:5}
.nav-btn{
  font-family:'Shantell Sans',cursive;font-size:1rem;color:#5d4a12;background:#ffdf6b;
  border:2px solid rgba(46,61,89,.25);border-radius:12px;padding:.42em 1em .5em;cursor:pointer;
  box-shadow:3px 4px 0 rgba(43,32,10,.32);transition:.18s;
}
.nav-btn:hover:not(:disabled){transform:translateY(-3px) rotate(-1.5deg)}
.nav-btn:active:not(:disabled){transform:translate(1px,2px);box-shadow:1px 1px 0 rgba(43,32,10,.32)}
.nav-btn:disabled{opacity:.45;cursor:default}
.counter{
  min-width:120px;text-align:center;font-family:'Shantell Sans',cursive;font-size:.95rem;
  color:#fdf3dd;background:rgba(43,28,8,.4);border-radius:999px;padding:.35em 1em .45em;
}
.dots{display:flex;gap:6px;position:relative;z-index:5}
.dots i{width:10px;height:10px;border-radius:50%;background:rgba(253,243,221,.38);border:1.5px solid rgba(80,55,20,.4);transition:.25s}
.dots i.past{background:#ffdf6b}
.dots i.cur{background:#e2574c;transform:scale(1.3)}
.chips-nav{display:flex;flex-wrap:wrap;gap:9px;justify-content:center;position:relative;z-index:5;max-width:900px}
.chips-nav button{
  font-family:'Shantell Sans',cursive;font-size:.85rem;color:#2e3d59;text-decoration:none;cursor:pointer;
  background:#fdf6e4;border:2px dashed rgba(46,61,89,.32);border-radius:999px;padding:.32em 1em .42em;
  box-shadow:2px 2px 0 rgba(43,32,10,.18);transition:.18s;
}
.chips-nav button:hover{transform:translateY(-2px) rotate(1.5deg);border-style:solid;background:#fff8e1}

/* ═══ ══════════ NỘI DUNG TRANG GIẤY (em-based) ══════════ ═══ */
.f-kick{
  display:inline-block;font-family:'Shantell Sans',cursive;font-size:.82em;color:#5d4a12;
  background:#ffdf6b;padding:.18em .9em .28em;border-radius:999px;transform:rotate(-1.6deg);
  box-shadow:2px 2px 0 rgba(43,32,10,.22);margin-bottom:.7em;
}
.f-h{font-family:'Shantell Sans',cursive;font-weight:700;font-size:1.5em;line-height:1.2}
.f-h .ico{display:inline-block;transform:rotate(-6deg);margin-right:.25em}
.f-squig{display:block;margin:.1em 0 .5em;width:150px}
.f-lead{color:#42527a;font-size:1.02em;margin:.5em 0 .8em}
.f-note{color:#8a8172;font-style:italic;font-size:.92em;margin-top:.6em}
.hl{
  display:inline-block;color:#b03a30;
  background:linear-gradient(104deg, rgba(255,223,107,0) .8%, #ffdf6b 3%, #ffdf6b 96%, rgba(255,223,107,0) 98%);
  border-radius:.3em;padding:.02em .22em .06em;transform:rotate(-.8deg);
}
.btn{
  display:inline-block;font-family:'Shantell Sans',cursive;font-size:.95em;line-height:1.2;
  padding:.5em 1em .6em;border-radius:11px;text-decoration:none;cursor:pointer;border:none;
  box-shadow:2px 3px 0 rgba(43,32,10,.35);transition:.18s;
}
.btn:hover{transform:translateY(-2px) rotate(-1deg)}
.btn:active{transform:translate(1px,2px);box-shadow:1px 1px 0 rgba(43,32,10,.35)}
.btn-red{background:#d94f43;color:#fff8e7}
.btn-line{background:transparent;color:#2e3d59;border:2px solid #2e3d59;box-shadow:2px 3px 0 rgba(43,32,10,.25)}
.btn-green{background:#3c6e46;color:#fff8e7}

/* mục lục */
.toc{list-style:none;margin-top:.6em}
.toc li{
  display:flex;align-items:baseline;gap:.5em;padding:.42em .2em;cursor:pointer;border-radius:8px;
  font-size:1.02em;transition:.15s;
}
.toc li:hover{background:#fff3d6;transform:translateX(4px)}
.toc .t{white-space:nowrap}
.toc .dots{flex:1;border-bottom:2px dotted rgba(46,61,89,.35);margin:0 .2em;transform:translateY(-4px)}
.toc b{font-family:'Shantell Sans',cursive;color:#b03a30;white-space:nowrap;font-weight:700}

/* hàng giá trong sổ */
.prow{
  display:flex;align-items:center;gap:.7em;background:#fffdf4;border:2px solid rgba(46,61,89,.13);
  border-radius:12px;padding:.5em .7em;margin-bottom:.55em;box-shadow:2px 3px 0 rgba(43,32,10,.12);
  transition:.18s;
}
.prow:nth-child(odd){transform:rotate(-.4deg)}
.prow:nth-child(even){transform:rotate(.3deg)}
.prow:hover{transform:translateY(-2px);box-shadow:2px 5px 0 rgba(43,32,10,.16)}
.prow .ic{
  flex:0 0 auto;width:2.6em;height:2.6em;display:grid;place-items:center;font-size:1.05em;
  border:2.5px solid #2e3d59;border-radius:48% 52% 55% 45%/52% 48% 58% 42%;background:#fff8e1;transform:rotate(-3deg);
}
.prow .tx{flex:1;min-width:0}
.prow .tx b{font-family:'Shantell Sans',cursive;font-size:.98em;display:block;line-height:1.15}
.prow .tx small{color:#5a6a88;font-size:.82em;line-height:1.2;display:block}
.prow .pr{text-align:right;white-space:nowrap}
.prow .pr b{font-family:'Shantell Sans',cursive;color:#b03a30;font-size:1.12em;display:block;line-height:1.1}
.prow .pr small{color:#8a8172;font-size:.72em}
.prow .pr a{display:inline-block;margin-top:.15em;font-family:'Shantell Sans',cursive;font-size:.78em;color:#b03a30;text-decoration:underline dashed;text-underline-offset:3px}

/* bảng so sánh */
.cmp{width:100%;border-collapse:collapse;margin-top:.4em;background:#fffdf4;border:2px solid rgba(46,61,89,.14);border-radius:12px;overflow:hidden;box-shadow:0 8px 18px rgba(60,35,10,.13)}
.cmp th,.cmp td{padding:.4em .6em;border-bottom:2px dashed rgba(46,61,89,.15);text-align:left;font-size:.88em;vertical-align:top}
.cmp thead th{font-family:'Shantell Sans',cursive;font-size:.9em;background:#fff3d6;border-bottom:2px solid rgba(46,61,89,.25)}
.cmp tbody tr:last-child td{border-bottom:none}
.cmp td:first-child{font-family:'Shantell Sans',cursive;font-size:.84em;width:33%;color:#42527a}
.cmp .no{color:#9a6a5a}
.cmp .yes{color:#2f7a3d}
.cmp tr.hot td{background:#fff6dd}
.cmp tr.hot td:last-child{font-family:'Shantell Sans',cursive;color:#b03a30}

/* hoá đơn giá */
.receipt{background:#fffdf4;border:2.5px dashed rgba(46,61,89,.32);border-radius:14px;padding:.8em 1.1em .7em;margin-top:.7em;transform:rotate(-.4deg);box-shadow:0 8px 18px rgba(60,35,10,.13)}
.receipt h3{font-family:'Shantell Sans',cursive;font-size:1.05em;margin-bottom:.15em}
.r-row{display:flex;justify-content:space-between;align-items:baseline;gap:.8em;padding:.4em .1em;border-bottom:2px dashed rgba(46,61,89,.14);font-size:.95em;color:#3c4c70}
.r-row .val{font-family:'Shantell Sans',cursive;white-space:nowrap;color:#2e3d59}
.r-row s{color:#8a8172;text-decoration-color:#d94f43;text-decoration-thickness:2px}
.r-row.big .val{color:#b03a30;font-size:1.3em}
.r-save{display:inline-block;font-family:'Shantell Sans',cursive;font-size:.85em;background:#cfeec2;color:#2f5c37;border:2px solid rgba(46,61,89,.22);border-radius:999px;padding:.25em .9em .35em;transform:rotate(-1.5deg);box-shadow:2px 2px 0 rgba(43,32,10,.18);margin-top:.5em}
.warn-note{display:inline-block;background:#ffe97a;border:2px solid rgba(46,61,89,.2);border-radius:10px;padding:.4em .9em;font-family:'Shantell Sans',cursive;font-size:.88em;color:#5d4a12;transform:rotate(-.8deg);box-shadow:2px 2px 0 rgba(43,32,10,.16);margin-top:.6em}

/* checklist */
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:.1em 1.4em;margin-top:.5em}
.checklist{list-style:none}
.checklist li{display:flex;gap:.6em;padding:.32em 0;align-items:flex-start;font-size:.95em;color:#3c4c70}
.cbx{
  flex:0 0 auto;width:1.6em;height:1.6em;margin-top:.15em;display:grid;place-items:center;
  border:2px solid #2e3d59;border-radius:42% 58% 50% 50%/55% 45% 55% 45%;
  color:#b03a30;font-family:'Shantell Sans',cursive;font-size:.95em;background:#fffdf4;
  transform:rotate(-2deg);box-shadow:1px 1px 0 rgba(43,32,10,.18);
}
.checklist b{color:#b03a30}

/* 3 bước */
.steps{display:flex;gap:.8em;list-style:none;margin-top:.7em}
.steps li{flex:1;position:relative;text-align:center;padding:0 .2em}
.steps li:not(:last-child)::after{content:'➜';position:absolute;right:-.75em;top:1.1em;color:#d94f43;font-size:1.1em;transform:rotate(8deg)}
.num{
  display:inline-grid;place-items:center;width:2.2em;height:2.2em;margin-bottom:.3em;
  font-family:'Shantell Sans',cursive;font-weight:700;font-size:1.15em;color:#2e3d59;
  border:2.5px solid #2e3d59;border-radius:47% 53% 52% 48%/55% 47% 53% 45%;
  background:#ffdf6b;transform:rotate(-4deg);box-shadow:2px 2px 0 rgba(43,32,10,.22);
}
.steps li:nth-child(2) .num{background:#ffc9d8;transform:rotate(3deg)}
.steps li:nth-child(3) .num{background:#cfeec2;transform:rotate(-3deg)}
.steps h4{font-family:'Shantell Sans',cursive;font-size:.95em;margin-bottom:.1em}
.steps p{font-size:.85em;color:#42527a;line-height:1.35}

/* sticky note */
.notes{display:grid;grid-template-columns:1fr 1fr;gap:1em .9em;margin-top:.7em}
.note{position:relative;padding:1.2em .9em .7em;border-radius:3px;min-height:7.2em;box-shadow:3px 6px 14px rgba(40,22,2,.22);display:flex;flex-direction:column;gap:.4em}
.n-yellow{background:#ffe97a;transform:rotate(-1.6deg)}
.n-pink{background:#ffc9d8;transform:rotate(1.2deg)}
.n-blue{background:#bfe3f2;transform:rotate(-1deg)}
.note blockquote{font-style:italic;font-size:.88em;line-height:1.4;color:#4a3d20}
.n-pink blockquote{color:#7c3a4b}.n-blue blockquote{color:#2f5068}
.note figcaption{margin-top:auto;font-family:'Shantell Sans',cursive;font-size:.8em}
.note figcaption small{display:block;font-family:'Patrick Hand',cursive;color:rgba(40,30,10,.55);font-size:.85em}
.note-empty{border:2.5px dashed rgba(90,80,60,.5);background:transparent;box-shadow:none;align-items:center;justify-content:center;text-align:center;color:#8a8172;font-style:italic;font-size:.9em;transform:rotate(1.5deg);display:flex;flex-direction:column;gap:.4em}

/* FAQ */
.faq details{border-bottom:2px dashed rgba(46,61,89,.22);padding:.28em .1em}
.faq summary{list-style:none;cursor:pointer;display:flex;align-items:center;gap:.7em;font-family:'Shantell Sans',cursive;font-size:.95em;padding:.2em 0;user-select:none}
.faq summary::-webkit-details-marker{display:none}
.faq summary .plus{
  flex:0 0 auto;width:1.55em;height:1.55em;display:grid;place-items:center;
  font-size:.95em;color:#fff8e7;background:#d94f43;border-radius:46% 54% 50% 50%/52% 48% 55% 45%;
  box-shadow:1px 1px 0 rgba(43,32,10,.25);transition:transform .25s;
}
.faq details[open] summary .plus{transform:rotate(45deg);background:#3c6e46}
.faq details p{padding:.1em .2em .45em 2.3em;color:#42527a;font-size:.9em;line-height:1.4}

/* bìa sau / liên hệ */
.backcover-in{background:transparent}
.bc-title{font-family:'Shantell Sans',cursive;font-size:1.3em;color:#ffe9b8}
.bc-lead{color:#e4d3b2;font-size:.95em;margin:.3em 0 .7em}
.contact-row{display:flex;flex-direction:column;gap:.5em;align-items:flex-start}
.contact{
  display:inline-block;font-family:'Shantell Sans',cursive;font-size:.92em;color:#3c3a33;text-decoration:none;
  background:#fdf6e4;padding:.45em 1em .55em;border-radius:10px;box-shadow:2px 3px 0 rgba(0,0,0,.35);transition:.18s;
}
.contact:hover{transform:translateY(-2px) rotate(-1deg)}
.pay-row{display:flex;flex-wrap:wrap;gap:.45em;margin-top:.8em;align-items:center}
.pay-label{font-size:.85em;color:#d8c5a0;font-style:italic}
.pay{font-size:.78em;font-family:'Shantell Sans',cursive;color:#5c4a2e;background:#f3e3bd;padding:.2em .7em .32em;border-radius:999px;transform:rotate(-1deg)}
.order{margin-top:.8em;background:rgba(253,246,228,.09);border:2px dashed rgba(243,231,207,.4);border-radius:12px;padding:.8em .9em}
.order h3{font-family:'Shantell Sans',cursive;font-size:1em;color:#ffe9b8;margin-bottom:.5em}
.order .row{display:flex;gap:.7em;flex-wrap:wrap;margin-bottom:.6em}
.order input,.order select{
  flex:1;min-width:9em;font-family:'Patrick Hand',cursive;font-size:.9em;
  background:transparent;border:none;border-bottom:2px dashed rgba(253,246,228,.55);
  padding:.3em .1em;outline:none;color:#fdf6e4;
}
.order select option{color:#3c3a33}
.order input::placeholder{color:#cdbb96}
.order input:focus,.order select:focus{border-bottom-color:#ffdf6b}
.fineprint{margin-top:.7em;color:#c9b58f;font-size:.78em;font-style:italic;line-height:1.35}

/* bìa trước */
.face.cover-face{border-radius:6px 14px 14px 6px;background:linear-gradient(155deg,#9a7648,#6b5130 60%,#59422a)}
.face.cover-face::before{display:none}
.cov-in{display:flex;flex-direction:column;align-items:center;text-align:center;padding:2em 1.5em 1.4em;position:relative;height:100%}
.cov-band{position:absolute;top:0;bottom:0;right:11%;width:1.6em;background:linear-gradient(90deg,#b03a30,#8f2c24);opacity:.85;box-shadow:0 0 8px rgba(0,0,0,.25)}
.cov-kicker{font-family:'Shantell Sans',cursive;color:#f3e3bd;font-size:.9em;letter-spacing:2px}
.cov-title{font-family:'Shantell Sans',cursive;font-weight:700;font-size:2.6em;line-height:1.05;color:#fff3dc;text-shadow:2px 3px 0 rgba(43,28,8,.45);margin:.15em 0 .05em}
.cov-title em{font-style:normal;color:#ffdf6b}
.cov-sub{color:#e8d8b8;font-size:.95em;margin:.6em 0 .4em;max-width:15em;line-height:1.5}
.cov-sticker{
  display:inline-block;font-family:'Shantell Sans',cursive;font-size:1em;color:#5d4a12;background:#ffdf6b;
  padding:.4em 1.1em .55em;border-radius:12px;transform:rotate(-3deg);box-shadow:3px 4px 0 rgba(30,16,2,.4);margin-top:.2em;
}
.cov-burst{width:7.2em;margin:.9em auto .2em;filter:drop-shadow(0 6px 10px rgba(30,16,2,.35))}
.cov-hint{
  margin-top:auto;font-family:'Shantell Sans',cursive;color:#f3e3bd;font-size:.9em;opacity:.9;
  animation:nudge 1.6s ease-in-out infinite alternate;
}
@keyframes nudge{from{transform:translateX(0)}to{transform:translateX(8px)}}
.cov-foot{margin-top:.7em;font-size:.78em;color:#cdbb96;font-style:italic}

/* board khi hết sổ */
.end-cover{position:absolute;inset:0;z-index:1;display:none;align-items:center;justify-content:center;text-align:center;padding:2em;transform:translateZ(-40px);pointer-events:none}
.end-cover .btn{pointer-events:auto}
.book-wrap.spread .end-cover.l{display:flex}
.book-wrap.single .end-cover.r{display:none;background:linear-gradient(150deg,#7a5c39,#5d4426 70%);border-radius:10px}
.book-wrap.single.done .end-cover.r{display:flex}
.end-in{color:#f3e3bd}
.end-in .big{font-family:'Shantell Sans',cursive;font-size:1.6em;font-weight:700;text-shadow:2px 3px 0 rgba(43,28,8,.4)}
.end-in p{color:#e8d8b8;margin:.4em 0 .8em;font-size:.95em}

/* reveal nhẹ */
.face-in>*{animation:fadeUp .5s ease both}
@keyframes fadeUp{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}

.nav-btn.snd{padding:.42em .55em .5em;font-size:.95rem}
.controls .nav-btn{white-space:nowrap}
@media (max-width:480px){
  .nav-btn{padding:.38em .7em .48em;font-size:.92rem}
  .counter{min-width:98px;font-size:.85rem}
}
.toast{position:fixed;left:50%;bottom:18px;transform:translateX(-50%);background:#2e2010;color:#ffe9b8;font-family:'Shantell Sans',cursive;font-size:.9em;padding:.5em 1.1em .6em;border-radius:999px;box-shadow:0 8px 20px rgba(0,0,0,.4);z-index:100}
.toast[hidden]{display:none}

a:focus-visible,button:focus-visible,summary:focus-visible,input:focus-visible,select:focus-visible{outline:3px dashed #d94f43;outline-offset:2px;border-radius:6px}

/* polaroid feedback */
.fb-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:.6em;margin-top:.5em}
.fb-pol{position:relative;margin:0;background:#fffdf6;padding:.45em .45em .3em;border-radius:4px;box-shadow:3px 6px 14px rgba(40,22,2,.22);transform:rotate(-2deg)}
.fb-pol.r2{transform:rotate(1.7deg)}
.fb-pol.r3{transform:rotate(-1deg)}
.fb-pol img,.fb-pol .fb-ph{width:100%;height:6.4em;object-fit:cover;border-radius:2px;display:block}
.fb-pol .fb-ph{display:none;border:2px dashed rgba(90,80,60,.5);flex-direction:column;align-items:center;justify-content:center;text-align:center;color:#a89a78;font-size:.6em;line-height:1.35;font-style:italic}
.fb-pol figcaption{font-family:'Shantell Sans',cursive;font-size:.68em;text-align:center;padding-top:.3em;color:#3c3a33}

/* nút Zalo nổi (mobile) */
.zalo-float{
  display:none;position:fixed;right:11px;bottom:132px;width:54px;height:54px;border-radius:50%;
  background:linear-gradient(160deg,#2f8fff,#0068ff);z-index:95;align-items:center;justify-content:center;
  box-shadow:0 7px 18px rgba(0,45,130,.45), inset 0 -2px 4px rgba(0,0,0,.18);
  animation:zpulse 2.2s ease-in-out infinite;text-decoration:none;
}
.zalo-float svg{width:27px;height:27px;display:block}
.zalo-float::after{
  content:'Nhắn Zalo!';position:absolute;top:-1.7em;left:50%;transform:translateX(-50%) rotate(-2deg);
  font-family:'Shantell Sans',cursive;font-size:.62em;color:#5d4a12;background:#ffdf6b;
  padding:.1em .6em .25em;border-radius:999px;white-space:nowrap;box-shadow:1px 2px 0 rgba(43,32,10,.25);
}
@keyframes zpulse{0%,100%{transform:scale(1)}50%{transform:scale(1.09)}}
@media (max-width:859px){.zalo-float{display:flex}}

@media (prefers-reduced-motion:reduce){
  .leaf,.leaf.flipped{transition-duration:.01s}
  .face-in>*{animation:none}
  .cov-hint{animation:none}
  .book-wrap.idle .book{animation:none}
  .sparkle{display:none}
}

/* pool ẩn (dùng noscript thì hiện dạng cuộn) */
#pool{display:none}
.no-js #pool{display:block;max-width:720px;margin:0 auto;padding:10px}
.no-js #pool > .face-pad{min-height:320px;margin-bottom:14px;border-radius:8px;overflow:hidden;box-shadow:0 8px 18px rgba(60,35,10,.2)}
.no-js .stage,.no-js .topbar{display:none}
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
<script>document.documentElement.className='js';</script>
<header class="topbar">
  <a class="brand" href="index.html"><span class="brand-book">📓</span><span class="brand-name">Sổ Acc</span><span class="brand-tag">xwuan</span></a>
  <span class="top-note">nhanh · sạch · uy tín ✏️</span>
</header>

<div class="stage" id="stage">
  <div class="book-wrap spread" id="bookWrap">
    <div class="board l"></div><div class="board r"></div>
    <div class="end-cover l"><div class="end-in"></div></div>
    <div class="end-cover r"><div class="end-in"><div class="big">📓 Sổ Acc Xwuan</div><p>hết sổ rồi — nhắn Zalo để được tư vấn tiếp nha!</p><a class="btn btn-red" href="https://zalo.me/0822307662" target="_blank" rel="noopener">💬 Zalo: 0822.307.662</a></div></div>
    <div class="book noanim" id="book"></div>
    <div class="spine" aria-hidden="true"></div>
    <div class="spiral-edge" aria-hidden="true"></div>
    <nav class="edge-tabs" aria-label="Đi nhanh tới mục">@@EDGETABS@@</nav>
    <button class="flip-zone prev" id="zonePrev" aria-label="Trang trước"><span class="flip-hint">‹ kéo lật lại</span></button>
    <button class="flip-zone next" id="zoneNext" aria-label="Trang sau"><span class="flip-hint">kéo lật trang ›</span></button>
  </div>

  <div class="controls">
    <button class="nav-btn" id="btnPrev">‹ trước</button>
    <span class="counter" id="counter">bìa sổ</span>
    <button class="nav-btn" id="btnNext">sau ›</button>
    <button class="nav-btn snd" id="btnSnd" aria-label="Bật/tắt âm thanh lật trang">🔊</button>
  </div>
  <div class="dots" id="dots" aria-hidden="true"></div>
  <nav class="chips-nav" aria-label="Đi tới mục">@@CHIPS@@</nav>
</div>

<a class="zalo-float" href="https://zalo.me/0822307662" target="_blank" rel="noopener" aria-label="Nhắn Zalo ngay: 0822.307.662">
  <svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M12 3C7.03 3 3 6.58 3 11c0 2.24 1.04 4.27 2.73 5.72-.09.95-.48 2.32-1.5 3.33 1.66-.19 3.05-.85 3.95-1.46.94.31 1.96.48 3.02.48 4.97 0 9-3.58 9-8.07S16.97 3 12 3z" fill="#fff"/><circle cx="8.6" cy="10.6" r="1.15" fill="#0068ff"/><circle cx="12" cy="10.6" r="1.15" fill="#0068ff"/><circle cx="15.4" cy="10.6" r="1.15" fill="#0068ff"/></svg>
</a>

<div class="toast" id="toast" hidden>📖 đã mở lại trang bạn đọc dở</div>

<div id="pool">
@@FACES@@
</div>

<noscript><style>#pool{display:block}</style></noscript>

<script>
@@JS@@
</script>
</body>
</html>
"""

ENGINE_JS = """
(function(){
  'use strict';
  var poolEls = Array.prototype.slice.call(document.querySelectorAll('#pool > .face-pad'));
  var N = poolEls.length;
  var book = document.getElementById('book');
  var wrapEl = document.getElementById('bookWrap');
  var stageEl = document.getElementById('stage');
  var counterEl = document.getElementById('counter');
  var dotsEl = document.getElementById('dots');
  var prevBtn = document.getElementById('btnPrev');
  var nextBtn = document.getElementById('btnNext');
  var mode = 'spread', leaves = [], flipped = 0;

  function el(t, c, h){ var e = document.createElement(t); if (c) e.className = c; if (h != null) e.innerHTML = h; return e; }
  var BLANK = '<div class="face-in blank-in"><span class="b-doodle">✏️</span><p>trang để dành…<br>ghi chú của bạn vào đây nha!</p></div>';

  function build(m){
    mode = m;
    wrapEl.classList.toggle('single', m === 'single');
    wrapEl.classList.toggle('spread', m === 'spread');
    Array.prototype.slice.call(book.querySelectorAll('.leaf')).forEach(function(l){ l.parentNode.removeChild(l); });
    leaves = [];
    if (m === 'spread'){
      for (var i = 0; i < N; i += 2){
        var leaf = el('div', 'leaf');
        var f = el('div', 'face front'); f.appendChild(poolEls[i]);
        if (poolEls[i].hasAttribute('data-cover')) f.classList.add('cover-face');
        var b = el('div', 'face back');
        var backContent = poolEls[i+1];
        if (!backContent){ backContent = el('div', 'face-pad'); backContent.innerHTML = BLANK; }
        if (backContent.hasAttribute && backContent.hasAttribute('data-cover')) b.classList.add('cover-face');
        b.appendChild(backContent);
        leaf.appendChild(f); leaf.appendChild(b); book.appendChild(leaf); leaves.push(leaf);
      }
    } else {
      poolEls.forEach(function(pf){
        var leaf = el('div', 'leaf');
        var f = el('div', 'face front'); f.appendChild(pf);
        if (pf.hasAttribute('data-cover')) f.classList.add('cover-face');
        var b = el('div', 'face back blank-back'); b.innerHTML = '<div class="face-in blank-in"><span class="b-doodle">✏️</span></div>';
        leaf.appendChild(f); leaf.appendChild(b); book.appendChild(leaf); leaves.push(leaf);
      });
    }
    leaves.forEach(function(l){
      l.addEventListener('transitionend', function(){ l.classList.remove('flipping'); applyZ(); });
    });
    flipped = 0;
    leaves.forEach(function(l){ l.classList.remove('flipped'); });
    applyZ(); updateUI();
  }

  function applyZ(){
    leaves.forEach(function(l, i){
      if (l.classList.contains('flipping')) return;
      l.style.zIndex = l.classList.contains('flipped') ? (i + 1) : (leaves.length - i + 5);
    });
  }

  function next(){
    if (flipped >= leaves.length) return;
    var leaf = leaves[flipped];
    leaf.classList.add('flipping');
    leaf.style.zIndex = leaves.length + 20;
    void leaf.offsetWidth;
    leaf.classList.add('flipped');
    flipped++;
    flipSound();
    if (flipped === 1 && !introDone){ introDone = true; sparkles(); }
    updateUI();
  }
  function prev(){
    if (flipped <= 0) return;
    var leaf = leaves[flipped - 1];
    leaf.classList.add('flipping');
    leaf.style.zIndex = leaves.length + 20;
    void leaf.offsetWidth;
    leaf.classList.remove('flipped');
    flipped--;
    flipSound();
    updateUI();
  }

  function updateUI(){
    var L = leaves.length;
    prevBtn.disabled = flipped <= 0;
    nextBtn.disabled = flipped >= L;
    var label;
    if (mode === 'spread'){
      label = flipped === 0 ? '📗 bìa sổ' : (flipped >= L ? '📙 bìa sau' : 'tờ ' + flipped + '/' + L);
    } else {
      label = flipped === 0 ? 'trang 1/' + N : (flipped >= N ? 'hết sổ 📙' : 'trang ' + (flipped + 1) + '/' + N);
    }
    counterEl.textContent = label;
    wrapEl.classList.toggle('done', flipped >= leaves.length);
    wrapEl.classList.toggle('idle', flipped === 0);
    savePos();
    dotsEl.innerHTML = '';
    for (var i = 0; i < L; i++){
      var d = document.createElement('i');
      if (i < flipped) d.className = 'past';
      if (i === flipped) d.className = 'cur';
      dotsEl.appendChild(d);
    }
  }

  function targetFlipped(k){
    return mode === 'single' ? k : Math.ceil(k / 2);
  }
  function goTo(k){
    k = Math.max(0, Math.min(k, N - 1));
    var t = Math.min(targetFlipped(k), leaves.length);
    var steps = Math.abs(t - flipped);
    if (steps === 0) return;
    if (steps <= 2){
      /* lật thật từng tờ */
      var forward = t > flipped, d = 0;
      for (var i = 0; i < steps; i++){
        (function(dd, fwd){ setTimeout(function(){ if (fwd) next(); else prev(); }, dd); })(d, forward);
        d += 430;
      }
    } else {
      /* nhảy xa: nháy nhẹ rồi đặt vị trí — nhẹ máy, không ghép nhiều lớp 3D */
      wrapEl.classList.add('jumping');
      setTimeout(function(){
        book.classList.add('noanim');
        leaves.forEach(function(l, i){ l.classList.toggle('flipped', i < t); });
        flipped = t;
        void book.offsetWidth;
        book.classList.remove('noanim');
        applyZ(); updateUI(); flipSound(0.5);
        requestAnimationFrame(function(){ requestAnimationFrame(function(){ wrapEl.classList.remove('jumping'); }); });
      }, 170);
    }
  }
  function goToInstant(k){
    var t = Math.max(0, Math.min(targetFlipped(k), leaves.length));
    book.classList.add('noanim');
    leaves.forEach(function(l, i){ l.classList.toggle('flipped', i < t); });
    flipped = t;
    void book.offsetWidth;
    book.classList.remove('noanim');
    applyZ(); updateUI();
  }

  /* ── kích thước & co giãn nội dung ── */
  function layout(){
    var vw = window.innerWidth, vh = window.innerHeight;
    var chrome = 0;
    ['.topbar', '.controls', '.dots', '.chips-nav'].forEach(function(s){
      var e = document.querySelector(s); if (e) chrome += e.offsetHeight;
    });
    chrome += 74;
    var availW = Math.min(vw - 28, 1180);
    var availH = Math.max(380, vh - chrome);
    var pw, ph;
    if (mode === 'spread'){
      pw = Math.min(availW / 2 - 4, 505, availH / 1.28);
      ph = Math.min(pw * 1.32, availH);
      pw = Math.min(pw, ph / 1.2);
    } else {
      pw = Math.min(availW - 16, 480, availH / 1.38);
      ph = Math.min(pw * 1.42, availH);
      pw = Math.min(pw, ph / 1.3);
    }
    pw = Math.max(240, Math.round(pw)); ph = Math.max(330, Math.round(ph));
    document.documentElement.style.setProperty('--pw', pw + 'px');
    document.documentElement.style.setProperty('--ph', ph + 'px');
    book.style.fontSize = Math.max(12.5, Math.min(17.5, pw * (mode === 'spread' ? 0.0365 : 0.042))) + 'px';
    fitAll();
  }

  function fitAll(){
    Array.prototype.forEach.call(book.querySelectorAll('.face'), function(face){
      var fn = face.querySelector('.face-in');
      if (!fn) return;
      fn.style.transform = ''; fn.style.width = '';
      var ch = face.clientHeight, sh = fn.scrollHeight;
      if (sh > ch + 2){
        var s = Math.max(0.52, (ch - 3) / sh);
        fn.style.transform = 'scale(' + s + ')';
        fn.style.width = (100 / s) + '%';
      }
    });
  }

  /* ── âm thanh lật giấy (Web Audio, không cần file) ── */
  var actx = null, sndOn = true;
  try { sndOn = localStorage.getItem('soacc_snd') !== '0'; } catch(e){}
  function flipSound(vol){
    if (!sndOn) return;
    try {
      var AC = window.AudioContext || window.webkitAudioContext;
      if (!AC) return;
      if (!actx) actx = new AC();
      if (actx.state === 'suspended') actx.resume();
      var dur = 0.22 + Math.random() * 0.08;
      var buf = actx.createBuffer(1, Math.floor(actx.sampleRate * dur), actx.sampleRate);
      var d = buf.getChannelData(0);
      for (var i = 0; i < d.length; i++){
        var t = i / d.length;
        d[i] = (Math.random() * 2 - 1) * Math.pow(1 - t, 1.4) * (0.35 + 0.65 * Math.sin(t * Math.PI));
      }
      var src = actx.createBufferSource(); src.buffer = buf;
      var bp = actx.createBiquadFilter(); bp.type = 'bandpass';
      bp.frequency.value = 1900 + Math.random() * 900; bp.Q.value = 0.55;
      var g = actx.createGain();
      g.gain.value = (0.15 + Math.random() * 0.05) * (vol || 1);
      src.connect(bp); bp.connect(g); g.connect(actx.destination);
      src.start();
    } catch(e){}
  }
  var introDone = false;
  function sparkles(){
    if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    var em = ['✨', '⭐', '📖', '💌', '💫'];
    for (var i = 0; i < 8; i++){
      (function(i){
        setTimeout(function(){
          var s = document.createElement('span');
          s.className = 'sparkle';
          s.textContent = em[i % em.length];
          s.style.left = (12 + Math.random() * 76) + '%';
          s.style.top = (28 + Math.random() * 42) + '%';
          wrapEl.appendChild(s);
          setTimeout(function(){ if (s.parentNode) s.parentNode.removeChild(s); }, 1600);
        }, i * 90);
      })(i);
    }
  }
  var posReady = false;
  function savePos(){ if (!posReady) return; try { localStorage.setItem('soacc_pos_' + location.pathname, String(flipped)); } catch(e){} }

  /* ── điều khiển ── */
  document.getElementById('zoneNext').addEventListener('click', next);
  document.getElementById('zonePrev').addEventListener('click', prev);
  nextBtn.addEventListener('click', next);
  prevBtn.addEventListener('click', prev);
  document.addEventListener('keydown', function(e){
    if (e.target && /INPUT|SELECT|TEXTAREA/.test(e.target.tagName)) return;
    if (e.key === 'ArrowRight') next();
    if (e.key === 'ArrowLeft') prev();
  });
  var sndBtn = document.getElementById('btnSnd');
  function syncSnd(){ sndBtn.textContent = sndOn ? '🔊' : '🔇'; }
  sndBtn.addEventListener('click', function(){
    sndOn = !sndOn;
    try { localStorage.setItem('soacc_snd', sndOn ? '1' : '0'); } catch(e){}
    syncSnd();
    if (sndOn) flipSound(0.8);
  });
  syncSnd();

  document.addEventListener('click', function(e){
    var g = e.target.closest('[data-goto]');
    if (g){ e.preventDefault(); goTo(parseInt(g.getAttribute('data-goto'), 10)); }
  });
  /* ── KÉO GÓC TRANG ĐỂ LẬT (chuột + cảm ứng) ── */
  var drag = null, suppressClickUntil = 0;
  var tx = 0, ty = 0;

  function coverTap(e){
    if (flipped !== 0 || !leaves.length) return false;
    var t = e.target;
    if (t.closest && t.closest('a,button,input,select,textarea,details,summary')) return false;
    var leaf0 = book.firstElementChild;
    if (!leaf0 || !leaf0.classList.contains('leaf')) return false;
    var front = leaf0.querySelector('.face.front');
    return !!(front && front.contains(t));
  }

  wrapEl.addEventListener('pointerdown', function(e){
    if (drag || (e.button && e.button !== 0)) return;
    var t = e.target;
    var zNext = t.closest && t.closest('.flip-zone.next');
    var zPrev = t.closest && t.closest('.flip-zone.prev');
    var onCover = !zNext && !zPrev && coverTap(e);
    if (!zNext && !zPrev && !onCover) return;
    if (t.closest && t.closest('a,input,select,textarea,details,summary')) return;
    var dir = null;
    if ((zNext || onCover) && flipped < leaves.length) dir = 'next';
    else if (zPrev && flipped > 0) dir = 'prev';
    if (!dir) return;
    drag = {mode: dir, startX: e.clientX, startY: e.clientY, lastX: e.clientX, lastT: e.timeStamp,
            p: 0, active: false, leaf: null, w: book.clientWidth / (mode === 'spread' ? 2 : 1)};
    wrapEl.classList.remove('idle');
    if (e.pointerType === 'touch') e.preventDefault();
  });

  window.addEventListener('pointermove', function(e){
    if (!drag) return;
    var dx = e.clientX - drag.startX;
    if (!drag.active){
      if (Math.abs(dx) < 7) return;
      drag.leaf = leaves[drag.mode === 'next' ? flipped : flipped - 1];
      if (!drag.leaf){ drag = null; return; }
      drag.active = true;
      drag.leaf.classList.add('dragging');
      drag.leaf.classList.add('flipping');
      drag.leaf.style.zIndex = leaves.length + 20;
      suppressClickUntil = Date.now() + 600;
      wrapEl.classList.add('dragging');
    }
    var p = Math.max(-1, Math.min(1, dx / drag.w));
    if (drag.mode === 'next' && p > 0) p = 0;
    if (drag.mode === 'prev' && p < 0) p = 0;
    drag.p = p;
    var base = drag.mode === 'next' ? 0 : -180;
    var ang = base + (drag.mode === 'next' ? -1 : 1) * Math.abs(p) * 180;
    drag.leaf.style.transform = 'rotateY(' + ang.toFixed(2) + 'deg)';
    drag.lastX = e.clientX; drag.lastT = e.timeStamp;
  });

  function endDrag(e, cancel){
    if (!drag) return;
    var d = drag; drag = null;
    wrapEl.classList.remove('dragging');
    if (!d.active || !d.leaf) return;   /* chỉ là tap — để sự kiện click xử lý */
    var vx = (e.clientX - d.lastX) / Math.max(1, e.timeStamp - d.lastT);
    var p = cancel ? 0 : (d.p || 0);
    var complete;
    if (d.mode === 'next') complete = (p < -0.42) || (vx < -0.35 && p < -0.06);
    else complete = (p > 0.42) || (vx > 0.35 && p > 0.06);
    var leaf = d.leaf;
    leaf.style.transition = 'transform .5s cubic-bezier(.3,.05,.3,1)';
    requestAnimationFrame(function(){
      if (d.mode === 'next'){
        if (complete){ leaf.classList.add('flipped'); flipped++; flipSound(); }
      } else {
        if (complete){ leaf.classList.remove('flipped'); flipped--; flipSound(); }
      }
      leaf.style.transform = '';
      updateUI();
    });
    setTimeout(function(){
      leaf.style.transition = '';
      leaf.classList.remove('dragging');
      leaf.classList.remove('flipping');
      applyZ();
    }, 560);
  }
  window.addEventListener('pointerup', function(e){ endDrag(e, false); });
  window.addEventListener('pointercancel', function(e){ endDrag(e, true); });
  wrapEl.addEventListener('click', function(e){
    if (Date.now() < suppressClickUntil){ e.preventDefault(); e.stopPropagation(); return; }
    if (coverTap(e)) next();
  }, true);
  wrapEl.addEventListener('dragstart', function(e){ e.preventDefault(); });

  /* vuốt nhanh mọi nơi (cảm ứng) */
  wrapEl.addEventListener('touchstart', function(e){
    if (drag) return;
    if (e.target.closest && e.target.closest('input,select,textarea,a,button,details')) return;
    tx = e.changedTouches[0].clientX; ty = e.changedTouches[0].clientY;
  }, {passive: true});
  wrapEl.addEventListener('touchend', function(e){
    if (drag) return;
    if (e.target.closest && e.target.closest('input,select,textarea,a,button,details')) return;
    var dx = e.changedTouches[0].clientX - tx, dy = e.changedTouches[0].clientY - ty;
    if (Math.abs(dx) > 46 && Math.abs(dx) > Math.abs(dy) * 1.4){ if (dx < 0) next(); else prev(); }
  }, {passive: true});

  /* ── form đặt hàng ── */
  var form = document.getElementById('orderForm');
  if (form){
    form.addEventListener('submit', function(e){
      e.preventDefault();
      var f = e.target;
      var msg = 'Xin chào Sổ Acc Xwuan! 📓\\n'
        + 'Mình là ' + f.ten.value.trim() + '\\n'
        + 'Muốn mua: ' + f.acc.value
        + (f.ghi.value.trim() ? '\\nGhi chú: ' + f.ghi.value.trim() : '')
        + '\\nLiên hệ: ' + f.sdt.value.trim();
      var hint = document.getElementById('formHint');
      var done = function(){ if (hint){ hint.hidden = false; setTimeout(function(){ hint.hidden = true; }, 8000); } };
      if (navigator.clipboard && navigator.clipboard.writeText){ navigator.clipboard.writeText(msg).then(done, done); } else { done(); }
      window.open('https://zalo.me/0822307662', '_blank');
    });
  }

  /* ── khởi động + resize ── */
  function restoreFlipped(cnt){
    var t = Math.max(0, Math.min(cnt, leaves.length));
    book.classList.add('noanim');
    leaves.forEach(function(l, i){ l.classList.toggle('flipped', i < t); });
    flipped = t;
    void book.offsetWidth;
    book.classList.remove('noanim');
    applyZ(); updateUI();
  }
  function desiredMode(){ return window.innerWidth >= 860 ? 'spread' : 'single'; }
  build(desiredMode());
  layout();
  var savedPos = 0;
  try { savedPos = parseInt(localStorage.getItem('soacc_pos_' + location.pathname) || '0', 10) || 0; } catch(e){}
  posReady = true;
  if (savedPos > 0){
    restoreFlipped(savedPos);
    var toastEl = document.getElementById('toast');
    if (toastEl){ toastEl.hidden = false; setTimeout(function(){ toastEl.hidden = true; }, 2400); }
  }
  window.addEventListener('resize', function(){
    var m = desiredMode();
    if (m !== mode){
      var pos = (mode === 'spread') ? (flipped === 0 ? 0 : Math.min(2 * flipped - 1, N - 1)) : Math.min(flipped, N - 1);
      build(m); layout(); goToInstant(pos);
    } else {
      layout();
    }
  });
  if (document.fonts && document.fonts.ready){ document.fonts.ready.then(function(){ layout(); }); }
  window.addEventListener('load', function(){ layout(); });
})();
"""


def edge_tabs(items):
    return '\n      '.join('<button data-goto="%d" aria-label="%s">%s</button>' % (k, lbl, lbl) for k, lbl in items)


def chips(items):
    return '\n    '.join('<button data-goto="%d">%s</button>' % (k, lbl) for k, lbl in items)


def render_page(fname, title, desc, faces, nav, end_note=None):
    """faces: list chuỗi HTML (mỗi cái là 1 <div class="face">). nav: [(face_idx, nhãn)]"""
    etabs = edge_tabs([(k, lbl) for k, lbl in nav])
    chps = chips(nav)
    faces_html = '\n'.join(faces)
    html = (HEAD
            .replace('@@TITLE@@', title)
            .replace('@@DESC@@', desc)
            .replace('@@CSS@@', CSS)
            .replace('@@EDGETABS@@', etabs)
            .replace('@@CHIPS@@', chps)
            .replace('@@FACES@@', faces_html)
            .replace('@@JS@@', ENGINE_JS))
    if end_note:
        default_r = '<div class="end-cover r"><div class="end-in"><div class="big">📓 Sổ Acc Xwuan</div><p>hết sổ rồi — nhắn Zalo để được tư vấn tiếp nha!</p><a class="btn btn-red" href="https://zalo.me/0822307662" target="_blank" rel="noopener">💬 Zalo: 0822.307.662</a></div></div>'
        html = html.replace(default_r, '<div class="end-cover r"><div class="end-in">%s</div></div>' % end_note)
    open(fname, 'w', encoding='utf-8').write(html)
    print('→ %s (%.0f KB)' % (fname, len(html) / 1024))
