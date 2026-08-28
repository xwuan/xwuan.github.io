const fs = require('fs');
const files = ['windows-pricing.html', 'index.html', 'youtube.html', 'capcut.html', 'google-ai.html', 'meitu.html', 'netflix.html', 'canva.html', 'locket.html'];

for (const file of files) {
    if (!fs.existsSync(file)) continue;
    let content = fs.readFileSync(file, 'utf8');

    // Restore translateY(20px) instead of scale(0.96)
    content = content.replace(/transform:\s*scale\(0\.96\)/g, 'transform: translateY(20px)');
    
    // Fix bounce loop by adding rootMargin to the observer
    content = content.replace(/\{ threshold:\s*0\.05\s*\}/g, '{ threshold: 0.05, rootMargin: "50px 0px" }');
    content = content.replace(/\{ threshold:\s*0\.1\s*\}/g, '{ threshold: 0.1, rootMargin: "50px 0px" }');
    content = content.replace(/\{ threshold:\s*0\.08\s*\}/g, '{ threshold: 0.08, rootMargin: "50px 0px" }');
    
    // Also tone down the emojis just in case they were too big
    content = content.replace(/font-size:\s*2\.2rem\s*!important/g, 'font-size: 1.8rem !important');

    fs.writeFileSync(file, content, 'utf8');
    console.log('Restored slideUp and fixed observer in ' + file);
}