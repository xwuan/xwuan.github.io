const fs = require('fs');
const files = ['youtube.html', 'capcut.html', 'google-ai.html', 'meitu.html', 'netflix.html', 'canva.html'];
const ov = fs.readFileSync('override.css', 'utf8');

for (const file of files) {
    if (fs.existsSync(file)) {
        let content = fs.readFileSync(file, 'utf8');
        content = content.replace(/\/\* APPLE OVERRIDE \*\/[\s\S]*?<\/style>/, ov);
        fs.writeFileSync(file, content);
        console.log('Updated ' + file);
    }
}
