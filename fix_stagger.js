const fs = require('fs');

let content = fs.readFileSync('windows-pricing.html', 'utf8');

// 1. Update .fi to use var(--delay, 0s)
content = content.replace(/\.fi\s*\{\s*opacity:\s*0\s*!important;\s*transform:\s*scale\(0\.96\)\s*!important;\s*transition:\s*opacity\s*0\.6s\s*cubic-bezier\(0\.25,\s*1,\s*0\.5,\s*1\),\s*transform\s*0\.6s\s*cubic-bezier\(0\.25,\s*1,\s*0\.5,\s*1\)\s*!important;\s*\}/g, '.fi { opacity: 0 !important; transform: scale(0.96) !important; transition: opacity 0.6s cubic-bezier(0.25, 1, 0.5, 1) var(--delay, 0s), transform 0.6s cubic-bezier(0.25, 1, 0.5, 1) var(--delay, 0s) !important; }');

// 2. Add --delay inline instead of transition-delay
content = content.replace(/style="transition-delay:\s*0\.1s"/g, 'style="--delay: 0.1s"');
content = content.replace(/style="transition-delay:\s*0\.2s"/g, 'style="--delay: 0.2s"');
content = content.replace(/style="transition-delay:\s*0\.3s"/g, 'style="--delay: 0.3s"');
content = content.replace(/style="transition-delay:\.06s"/g, 'style="--delay: 0.06s"');
content = content.replace(/style="transition-delay:\.1s"/g, 'style="--delay: 0.1s"');
content = content.replace(/style="transition-delay:\.12s"/g, 'style="--delay: 0.12s"');
content = content.replace(/style="transition-delay:\.16s"/g, 'style="--delay: 0.16s"');
content = content.replace(/style="transition-delay:\.18s"/g, 'style="--delay: 0.18s"');
content = content.replace(/style="transition-delay:\.22s;margin-top:14px;"/g, 'style="--delay: 0.22s; margin-top:14px;"');
content = content.replace(/style="transition-delay:\.26s"/g, 'style="--delay: 0.26s"');
// For .repair which has margin-top
content = content.replace(/style="transition-delay:\s*0\.22s;\s*margin-top:14px;"/g, 'style="--delay: 0.22s; margin-top:14px;"');

fs.writeFileSync('windows-pricing.html', content, 'utf8');
console.log('Fixed CSS delays');