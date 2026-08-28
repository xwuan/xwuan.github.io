const fs = require('fs');
const files = ['youtube.html', 'capcut.html', 'google-ai.html', 'meitu.html', 'netflix.html', 'canva.html', 'locket.html', 'windows-pricing.html'];

for (const file of files) {
    if (!fs.existsSync(file)) continue;
    let content = fs.readFileSync(file, 'utf8');
    
    // Remove all existing ' fi' or 'fi ' or 'fi' (carefully)
    // First, just remove ' fi' where it was appended by my script
    content = content.replace(/\s+fi"/g, '"');
    
    // Now apply it ONLY if the class list contains exactly 'card', 'ptier', 'pcard', 'combo', 'btn-group'
    content = content.replace(/class="([^"]+)"/g, (match, p1) => {
        const classes = p1.split(' ').map(s => s.trim());
        const shouldAddFi = classes.some(c => 
            c === 'card' || 
            c === 'ptier' || 
            c === 'pcard' || 
            c === 'combo' || 
            c === 'btn-group'
        );
        if (shouldAddFi && !classes.includes('fi')) {
            return 'class="' + p1 + ' fi"';
        }
        return match;
    });
    
    fs.writeFileSync(file, content);
    console.log('Fixed fi in ' + file);
}
