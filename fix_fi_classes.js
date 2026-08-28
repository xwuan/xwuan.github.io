const fs = require('fs');

const files = ['youtube.html', 'capcut.html', 'google-ai.html', 'meitu.html', 'netflix.html', 'canva.html', 'locket.html', 'windows-pricing.html'];

for (const file of files) {
    if (!fs.existsSync(file)) continue;
    let content = fs.readFileSync(file, 'utf8');
    
    content = content.replace(/class="([^"]*?(?:card\b|ptier\b|pcard\b|combo\b|btn-group\b)[^"]*?)"/g, (match, p1) => {
        if (!p1.includes('fi')) {
            return 'class="' + p1 + ' fi"';
        }
        return match;
    });
    
    fs.writeFileSync(file, content);
    console.log('Added fi to ' + file);
}
