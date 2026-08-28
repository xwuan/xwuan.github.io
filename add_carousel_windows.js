const fs = require('fs');

const cssOverride = '\n/* MOBILE APP CAROUSEL UPGRADE */\n' +
'@media(max-width: 550px) {\n' +
'  .cards, .combos {\n' +
'    display: flex !important;\n' +
'    flex-wrap: nowrap !important;\n' +
'    overflow-x: auto !important;\n' +
'    scroll-snap-type: x mandatory !important;\n' +
'    -webkit-overflow-scrolling: touch !important;\n' +
'    margin: 0 -16px !important;\n' +
'    padding: 0 16px 20px 16px !important;\n' +
'    scroll-padding-left: 16px !important;\n' +
'  }\n' +
'  .cards::-webkit-scrollbar, .combos::-webkit-scrollbar { display: none !important; }\n' +
'  .pcard, .combo {\n' +
'    min-width: 85% !important;\n' +
'    max-width: 85% !important;\n' +
'    scroll-snap-align: center !important;\n' +
'    flex-shrink: 0 !important;\n' +
'  }\n' +
'}\n';

const file = 'windows-pricing.html';
let content = fs.readFileSync(file, 'utf8');
if (!content.includes('MOBILE APP CAROUSEL UPGRADE')) {
    content = content.replace('</style>', cssOverride + '</style>');
    fs.writeFileSync(file, content, 'utf8');
    console.log('Added mobile carousel to ' + file);
}