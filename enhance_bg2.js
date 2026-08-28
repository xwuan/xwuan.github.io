const fs = require('fs');

const gridFix = '\n/* PREMIUM GRID BACKGROUND UNIFICATION */\n' +
'body { background-color: #0c0814 !important; background-image: radial-gradient(circle at 50% 50%, rgba(138, 43, 226, 0.1) 0%, transparent 60%), linear-gradient(rgba(255, 255, 255, 0.02) 1px, transparent 1px), linear-gradient(90deg, rgba(255, 255, 255, 0.02) 1px, transparent 1px) !important; background-size: 100% 100%, 20px 20px, 20px 20px !important; }\n';

const files = ['youtube.html', 'capcut.html', 'canva.html', 'locket.html'];

for (const file of files) {
    if (!fs.existsSync(file)) continue;
    let content = fs.readFileSync(file, 'utf8');
    
    // Remove old forced backgrounds that destroy grids
    content = content.replace(/body\s*\{\s*background:\s*linear-gradient[^!]+!important;\s*\}/g, '');
    
    if (!content.includes('PREMIUM GRID BACKGROUND UNIFICATION')) {
        content = content.replace('</style>', gridFix + '\n</style>');
        fs.writeFileSync(file, content, 'utf8');
        console.log('Applied premium grid to ' + file);
    }
}