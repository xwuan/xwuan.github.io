const fs = require('fs');
let content = fs.readFileSync('windows-pricing.html', 'utf8');

// Add transition-delay to pcards
content = content.replace('<div class="pcard featured fi">', '<div class="pcard featured fi" style="transition-delay: 0.1s">');
content = content.replace('<div class="pcard fi">', '<div class="pcard fi" style="transition-delay: 0.2s">');
content = content.replace('<div class="pcard fi">', '<div class="pcard fi" style="transition-delay: 0.3s">'); // This will match the second one

// Add transition-delay to combos
content = content.replace('<div class="combo fi">', '<div class="combo fi" style="transition-delay: 0.1s">');
content = content.replace('<div class="combo fi">', '<div class="combo fi" style="transition-delay: 0.2s">'); // Matches second combo

fs.writeFileSync('windows-pricing.html', content, 'utf8');
console.log('Added staggering to cards');