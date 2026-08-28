const fs = require('fs');

let content = fs.readFileSync('windows-pricing.html', 'utf8');

// 1. Add PREMIUM GRID BACKGROUND
if (!content.includes('PREMIUM GRID BACKGROUND UNIFICATION')) {
    const gridCSS = '\n/* PREMIUM GRID BACKGROUND UNIFICATION */\nbody { background-color: #0c0814 !important; background-image: radial-gradient(circle at 50% 50%, rgba(138, 43, 226, 0.1) 0%, transparent 60%), linear-gradient(rgba(255, 255, 255, 0.02) 1px, transparent 1px), linear-gradient(90deg, rgba(255, 255, 255, 0.02) 1px, transparent 1px) !important; background-size: 100% 100%, 20px 20px, 20px 20px !important; }\n';
    content = content.replace('</style>', gridCSS + '</style>');
}

// 2. Add .fi to repair and cta-banner
content = content.replace('<div class="repair"', '<div class="repair fi"');
content = content.replace('<div class="cta-banner"', '<div class="cta-banner fi"');

// 3. Remove duplicate observer
content = content.replace(/<script>\s*document\.getElementById\('yr'\)\.textContent = new Date\(\)\.getFullYear\(\);\s*const obs = new IntersectionObserver\(es => \{\s*es\.forEach\(e => \{ if\(e\.isIntersecting\)\{ e\.target\.classList\.add\('in'\); obs\.unobserve\(e\.target\); \}\}\);\s*\},\{threshold:\.08\}\);\s*document\.querySelectorAll\('\.fi'\)\.forEach\(el => obs\.observe\(el\)\);\s*<\/script>/, "<script>\ndocument.getElementById('yr').textContent = new Date().getFullYear();\n</script>");

// 4. Update floater classes
content = content.replace(/"emoji-float e-1"/g, '"floater f1"');
content = content.replace(/"emoji-float e-2"/g, '"floater f2"');
content = content.replace(/"emoji-float e-3"/g, '"floater f3"');
content = content.replace(/"emoji-float e-4"/g, '"floater f4"');

fs.writeFileSync('windows-pricing.html', content, 'utf8');
console.log('Fixed windows-pricing animations and background');