const fs = require('fs');

const files = ['youtube.html', 'capcut.html', 'google-ai.html', 'meitu.html', 'netflix.html', 'canva.html', 'locket.html'];

for (const file of files) {
    if (!fs.existsSync(file)) continue;
    let content = fs.readFileSync(file, 'utf8');
    
    // Replace the !important version of .fi
    content = content.replace(/\.fi\s*\{\s*opacity:\s*0\s*!important;\s*transform:\s*translateY\(20px\)\s*!important;\s*transition:\s*opacity\s*0\.8s\s*cubic-bezier\(0\.25,\s*1,\s*0\.5,\s*1\),\s*transform\s*0\.8s\s*cubic-bezier\(0\.25,\s*1,\s*0\.5,\s*1\)\s*!important;\s*\}/g, '.fi { opacity: 0 !important; transform: scale(0.96) !important; transition: opacity 0.6s cubic-bezier(0.25, 1, 0.5, 1), transform 0.6s cubic-bezier(0.25, 1, 0.5, 1) !important; }');
    
    // Also replace the @keyframes slideUp which uses translateY(20px) just in case
    content = content.replace(/0%\s*\{\s*opacity:\s*0;\s*transform:\s*translateY\(20px\);\s*\}/g, '0% { opacity: 0; transform: scale(0.96); }');
    content = content.replace(/100%\s*\{\s*opacity:\s*1;\s*transform:\s*translateY\(0\);\s*\}/g, '100% { opacity: 1; transform: scale(1); }');
    
    // Some static elements might have inline transform: translateY(20px), but let's be careful.
    
    fs.writeFileSync(file, content, 'utf8');
    console.log('Fixed .fi translateY loop in ' + file);
}