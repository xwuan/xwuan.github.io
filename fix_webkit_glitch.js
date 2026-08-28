const fs = require('fs');

const cssOld = /\.fi\s*\{\s*opacity:\s*0;\s*transform:\s*scale\(0\.96\);\s*filter:\s*blur\(5px\);\s*transition:[^\}]+\}/g;
const cssNew = '.fi { opacity: 0; transform: scale(0.96); transition: opacity 0.6s cubic-bezier(0.25, 1, 0.5, 1), transform 0.6s cubic-bezier(0.25, 1, 0.5, 1) !important; }';

const cssInOld = /\.fi\.in\s*\{\s*opacity:\s*1;\s*transform:\s*scale\(1\);\s*filter:\s*blur\(0\);\s*\}/g;
const cssInNew = '.fi.in { opacity: 1; transform: scale(1); }';

const files = ['index.html', 'youtube.html', 'capcut.html', 'google-ai.html', 'meitu.html', 'netflix.html', 'canva.html', 'locket.html', 'windows-pricing.html'];

for (const file of files) {
    if (!fs.existsSync(file)) continue;
    let content = fs.readFileSync(file, 'utf8');
    
    let changed = false;
    if (content.match(cssOld)) {
        content = content.replace(cssOld, cssNew);
        changed = true;
    }
    if (content.match(cssInOld)) {
        content = content.replace(cssInOld, cssInNew);
        changed = true;
    }
    
    // Also add .locket-card to the premium hover list
    if (content.includes('.svc-card, .card, .pcard, .ptier, .combo {') && !content.includes('.locket-card { transition: transform 0.4s')) {
        content = content.replace('.svc-card, .card, .pcard, .ptier, .combo {', '.svc-card, .card, .pcard, .ptier, .combo, .locket-card, .ent-card {');
        content = content.replace('.svc-card:hover, .card:hover, .pcard:hover, .ptier:hover, .combo:hover {', '.svc-card:hover, .card:hover, .pcard:hover, .ptier:hover, .combo:hover, .locket-card:hover, .ent-card:hover {');
        changed = true;
    }
    
    if (changed) {
        fs.writeFileSync(file, content, 'utf8');
        console.log('Fixed webkit glitch and upgraded Locket card hover in ' + file);
    }
}