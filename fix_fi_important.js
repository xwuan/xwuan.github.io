const fs = require('fs');
const files = ['youtube.html', 'capcut.html', 'google-ai.html', 'meitu.html', 'netflix.html', 'canva.html', 'locket.html', 'windows-pricing.html'];

for (const file of files) {
    if (!fs.existsSync(file)) continue;
    let content = fs.readFileSync(file, 'utf8');
    
    content = content.replace(/\.fi \{ opacity: 0; transform: translateY\(20px\);/g, '.fi { opacity: 0 !important; transform: translateY(20px) !important;');
    content = content.replace(/\.fi\.in \{ opacity: 1;/g, '.fi.in { opacity: 1 !important;');
    
    fs.writeFileSync(file, content);
}
