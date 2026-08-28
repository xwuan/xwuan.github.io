const fs = require('fs');

let content = fs.readFileSync('windows-pricing.html', 'utf8');

// The file was reverted to e632895.
// In e632895, .cta-banner has margin: 0 0 20px 0 !important; padding: 24px !important;
content = content.replace('.cta-banner { margin: 0 0 20px 0 !important; padding: 24px !important; }', '.cta-banner { margin: 14px 0 24px 0 !important; padding: 24px !important; }');

fs.writeFileSync('windows-pricing.html', content, 'utf8');
console.log('Fixed cta-banner margin using Node.js');