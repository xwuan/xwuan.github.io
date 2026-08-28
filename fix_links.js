const fs = require('fs');

const files = ['index.html', 'youtube.html', 'capcut.html', 'google-ai.html', 'meitu.html', 'netflix.html', 'canva.html', 'locket.html', 'windows-pricing.html'];

for (const file of files) {
    if (!fs.existsSync(file)) continue;
    let content = fs.readFileSync(file, 'utf8');
    
    let changed = false;
    
    // 1. Fix .cta-banner in windows-pricing.html
    if (file === 'windows-pricing.html') {
        if (!content.includes('.cta-banner { margin: 0 !important; }')) {
            content = content.replace('</style>', '.cta-banner { margin: 0 0 20px 0 !important; padding: 24px !important; }\n</style>');
            changed = true;
        }
    }
    
    // 2. Remove .html from links
    const htmlLinks = ['index.html', 'windows-pricing.html', 'youtube.html', 'capcut.html', 'google-ai.html', 'meitu.html', 'netflix.html', 'canva.html', 'locket.html'];
    
    for (const link of htmlLinks) {
        const replaceWith = link === 'index.html' ? './' : link.replace('.html', '');
        // We only want to replace href="something.html"
        const regex = new RegExp('href="' + link + '"', 'g');
        if (content.match(regex)) {
            content = content.replace(regex, 'href="' + replaceWith + '"');
            changed = true;
        }
    }
    
    if (changed) {
        fs.writeFileSync(file, content, 'utf8');
        console.log('Fixed links and banner in ' + file);
    }
}