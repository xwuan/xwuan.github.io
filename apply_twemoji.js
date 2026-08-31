const fs = require('fs');
const files = ['index.html', 'windows-pricing.html', 'youtube.html', 'capcut.html', 'netflix.html', 'canva.html', 'locket.html'];

const snippet = '<script src="https://cdn.jsdelivr.net/npm/@twemoji/api@14.1.0/dist/twemoji.min.js"></script>\n<script>\n  document.addEventListener("DOMContentLoaded", function() {\n    twemoji.parse(document.body, { folder: "svg", ext: ".svg" });\n  });\n</script>\n<style>\n  img.emoji {\n    height: 1.2em;\n    width: 1.2em;\n    margin: 0 .05em 0 .1em;\n    vertical-align: -0.2em;\n  }\n</style>\n';

for (const file of files) {
    if (!fs.existsSync(file)) continue;
    let content = fs.readFileSync(file, 'utf8');
    if (!content.includes('twemoji.min.js')) {
        content = content.replace('</head>', snippet + '</head>');
        fs.writeFileSync(file, content, 'utf8');
        console.log('Added to ' + file);
    }
}