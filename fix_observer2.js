const fs = require('fs');

const oldScript = /const fadeObs = new IntersectionObserver\(entries => \{\s*entries\.forEach\(e => \{\s*if \(e\.isIntersecting\) \{\s*e\.target\.classList\.add\("in"\);\s*\} else \{\s*e\.target\.classList\.remove\("in"\);\s*\}\s*\}\);\s*\}, \{ threshold: 0\.1 \}\);/g;
const oldScriptIndex = /const fadeObs = new IntersectionObserver\(entries => \{\s*entries\.forEach\(e => \{\s*if \(e\.isIntersecting\) \{\s*e\.target\.classList\.add\('in'\);\s*\} else \{\s*e\.target\.classList\.remove\('in'\);\s*\}\s*\}\);\s*\}, \{ threshold: 0\.1 \}\);/g;

const newScript = 'const fadeObs = new IntersectionObserver(entries => { entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add("in"); } else if (e.boundingClientRect.top > 50) { e.target.classList.remove("in"); } }); }, { threshold: 0.15 });';

const files = ['index.html', 'youtube.html', 'capcut.html', 'google-ai.html', 'meitu.html', 'netflix.html', 'canva.html', 'locket.html', 'windows-pricing.html'];

for (const file of files) {
    if (!fs.existsSync(file)) continue;
    let content = fs.readFileSync(file, 'utf8');
    
    if (content.match(oldScript) || content.match(oldScriptIndex)) {
        content = content.replace(oldScript, newScript).replace(oldScriptIndex, newScript);
        fs.writeFileSync(file, content, 'utf8');
        console.log('Fixed observer loop in ' + file);
    }
}