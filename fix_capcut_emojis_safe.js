const fs = require('fs');

const files = ['youtube.html', 'capcut.html', 'google-ai.html', 'meitu.html', 'netflix.html', 'canva.html', 'locket.html', 'windows-pricing.html'];

for (const file of files) {
    if (!fs.existsSync(file)) continue;
    let content = fs.readFileSync(file, 'utf8');
    
    let changed = false;
    
    // Fix CSS selectors to include floater and f1..f4
    if (content.includes('.emoji-float, .deco {')) {
        content = content.replace('.emoji-float, .deco {', '.emoji-float, .deco, .floater {');
        content = content.replace('.e-1, .d1 {', '.e-1, .d1, .f1 {');
        content = content.replace('.e-2, .d2 {', '.e-2, .d2, .f2 {');
        content = content.replace('.e-3, .d3 {', '.e-3, .d3, .f3 {');
        content = content.replace('.e-4, .d4 {', '.e-4, .d4, .f4 {');
        changed = true;
    }
    
    // Inject emojis into windows-pricing.html
    if (file === 'windows-pricing.html' && !content.includes('emoji-float e-1')) {
        const emojisHtml = '\n<div class="emoji-float e-1">💻</div>\n<div class="emoji-float e-2">⚙️</div>\n<div class="emoji-float e-3">🛠️</div>\n<div class="emoji-float e-4">🔥</div>\n';
        content = content.replace('<body>', '<body>' + emojisHtml);
        changed = true;
    }
    
    if (changed) {
        fs.writeFileSync(file, content, 'utf8');
        console.log('Fixed emojis safely in ' + file);
    }
}