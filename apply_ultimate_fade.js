const fs = require('fs');

const cssOld = /\.fi\s*\{\s*opacity:\s*0;\s*transform:\s*translateY\(20px\);\s*transition:[^\}]+\}/g;
const cssNew = '.fi { opacity: 0; transform: scale(0.96); filter: blur(5px); transition: opacity 0.6s cubic-bezier(0.25, 1, 0.5, 1), transform 0.6s cubic-bezier(0.25, 1, 0.5, 1), filter 0.6s cubic-bezier(0.25, 1, 0.5, 1) !important; }';
const cssInOld = /\.fi\.in\s*\{\s*opacity:\s*1;\s*transform:\s*none;\s*\}/g;
const cssInNew = '.fi.in { opacity: 1; transform: scale(1); filter: blur(0); }';

const scriptOld = /const fadeObs = new IntersectionObserver\(entries => \{\s*entries\.forEach\(e => \{\s*if \(e\.isIntersecting\) \{\s*e\.target\.classList\.add\("in"\);\s*\} else if \(e\.boundingClientRect\.top > 50\) \{\s*e\.target\.classList\.remove\("in"\);\s*\}\s*\}\);\s*\}, \{ threshold: 0\.15 \}\);/g;
const scriptNew = 'const fadeObs = new IntersectionObserver(entries => { entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add("in"); } else { e.target.classList.remove("in"); } }); }, { threshold: 0.05 });';

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
    if (content.match(scriptOld)) {
        content = content.replace(scriptOld, scriptNew);
        changed = true;
    }
    
    if (changed) {
        fs.writeFileSync(file, content, 'utf8');
        console.log('Applied ultimate Apple blur-scale fade and restored bi-directional observer to ' + file);
    }
}