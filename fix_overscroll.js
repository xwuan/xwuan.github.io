const fs = require('fs');
const files = ['index.html', 'youtube.html', 'capcut.html', 'google-ai.html', 'meitu.html', 'netflix.html', 'canva.html', 'locket.html', 'windows-pricing.html'];

for (const file of files) {
    if (!fs.existsSync(file)) continue;
    let content = fs.readFileSync(file, 'utf8');
    
    // Add theme-color meta tag
    if (!content.includes('name="theme-color"')) {
        let themeColor = '#050505';
        if (file === 'locket.html') themeColor = '#0c0814';
        content = content.replace('<head>', '<head>\n  <meta name="theme-color" content="' + themeColor + '">');
    }
    
    // Fix HTML background for overscroll
    if (file === 'index.html') {
        content = content.replace('html { scroll-behavior: smooth; }', 'html { scroll-behavior: smooth; background-color: #050505; }');
    } else if (file === 'locket.html') {
        content = content.replace('/* APPLE OVERRIDE */', '/* APPLE OVERRIDE */\n  html { background-color: #0c0814 !important; }');
    } else if (file === 'windows-pricing.html') {
        content = content.replace('/* APPLE OVERRIDE */', '/* APPLE OVERRIDE */\n  html { background-color: #050505 !important; }');
    } else {
        // Detail pages (override.css is embedded in them, but I can also just inject it via regex)
        // Wait, override.css is a separate file? No, my previous script injected override.css into capcut.html, etc.?
        // Actually, earlier I used apply_override.js which copied override.css into the HTML files!
        // So I can just inject it right after /* APPLE OVERRIDE */
        content = content.replace('/* APPLE OVERRIDE */', '/* APPLE OVERRIDE */\n  html { background-color: #050505 !important; }');
    }
    
    fs.writeFileSync(file, content);
}

// Also update override.css itself just in case
if (fs.existsSync('override.css')) {
    let overrideContent = fs.readFileSync('override.css', 'utf8');
    if (!overrideContent.includes('html { background-color: #050505 !important; }')) {
        overrideContent = overrideContent.replace('/* APPLE OVERRIDE */', '/* APPLE OVERRIDE */\nhtml { background-color: #050505 !important; }');
        fs.writeFileSync('override.css', overrideContent);
    }
}

// Update handover.md as per workflow rules
let handover = fs.readFileSync('handover.md', 'utf8');
const bugFixEntry = "- [x] Fix loi overscroll hien nen trang tren Safari mobile va them meta theme-color dong bo thanh taskbar.";
if (!handover.includes('Fix loi overscroll')) {
    handover = handover.replace('## 8. QUY TAC', bugFixEntry + '\n\n## 8. QUY TAC');
    fs.writeFileSync('handover.md', handover);
}

console.log('Fixed overscroll and theme-color');