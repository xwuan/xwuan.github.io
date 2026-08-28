const fs = require('fs');

const files = ['youtube.html', 'capcut.html', 'google-ai.html', 'meitu.html', 'netflix.html', 'canva.html', 'locket.html'];

for (const file of files) {
    if (!fs.existsSync(file)) continue;
    let content = fs.readFileSync(file, 'utf8');
    
    // Make visible observer bidirectional
    content = content.replace(/if\s*\(entry\.isIntersecting\)\s*\{\s*entry\.target\.classList\.add\('visible'\);\s*\}/, "if (entry.isIntersecting) {\n                    entry.target.classList.add('visible');\n                } else {\n                    entry.target.classList.remove('visible');\n                }");
    
    fs.writeFileSync(file, content, 'utf8');
    console.log('Made visible observer bidirectional in ' + file);
}