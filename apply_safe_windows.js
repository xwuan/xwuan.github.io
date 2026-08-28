const fs = require('fs');

let content = fs.readFileSync('windows-pricing.html', 'utf8');

// 1. Fix bounce loop
content = content.replace(/\.fi\s*\{\s*opacity:\s*0\s*!important;\s*transform:\s*translateY\(20px\)\s*!important;\s*transition:\s*opacity\s*0\.8s\s*cubic-bezier\(0\.25,\s*1,\s*0\.5,\s*1\),\s*transform\s*0\.8s\s*cubic-bezier\(0\.25,\s*1,\s*0\.5,\s*1\)\s*!important;\s*\}/g, '.fi { opacity: 0 !important; transform: scale(0.96) !important; transition: opacity 0.6s cubic-bezier(0.25, 1, 0.5, 1), transform 0.6s cubic-bezier(0.25, 1, 0.5, 1) !important; }');
content = content.replace(/0%\s*\{\s*opacity:\s*0;\s*transform:\s*translateY\(20px\);\s*\}/g, '0% { opacity: 0; transform: scale(0.96); }');
content = content.replace(/100%\s*\{\s*opacity:\s*1;\s*transform:\s*translateY\(0\);\s*\}/g, '100% { opacity: 1; transform: scale(1); }');

// 2. Fix CTA banner margin
if (!content.includes('.cta-banner { margin: 0 0 20px 0 !important; padding: 24px !important; }')) {
    content = content.replace('</style>', '.cta-banner { margin: 0 0 20px 0 !important; padding: 24px !important; }\n</style>');
}

// 3. Remove .html from links
const htmlLinks = ['index.html', 'windows-pricing.html', 'youtube.html', 'capcut.html', 'google-ai.html', 'meitu.html', 'netflix.html', 'canva.html', 'locket.html'];
for (const link of htmlLinks) {
    const replaceWith = link === 'index.html' ? './' : link.replace('.html', '');
    const regex = new RegExp('href="' + link + '"', 'g');
    if (content.match(regex)) {
        content = content.replace(regex, 'href="' + replaceWith + '"');
    }
}

fs.writeFileSync('windows-pricing.html', content, 'utf8');
console.log('Restored and applied fixes safely!');