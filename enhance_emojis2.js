const fs = require('fs');

const globalEnhancement = '\n/* GLOBAL EMOJI FLOAT & DECO ENHANCEMENT */\n' +
'.emoji-float, .deco { position: fixed !important; font-size: 2.2rem !important; opacity: 0.15 !important; animation: floatPremium 6s ease-in-out infinite !important; z-index: 0 !important; pointer-events: none !important; }\n' +
'.e-1, .d1 { top: 10% !important; left: 5% !important; animation-delay: 0s !important; }\n' +
'.e-2, .d2 { top: 25% !important; right: 5% !important; animation-delay: 1.5s !important; }\n' +
'.e-3, .d3 { top: 60% !important; left: 7% !important; animation-delay: 3s !important; }\n' +
'.e-4, .d4 { top: 75% !important; right: 8% !important; animation-delay: 4.5s !important; }\n' +
'@keyframes floatPremium { 0%, 100% { transform: translateY(0) rotate(0deg); } 50% { transform: translateY(-20px) rotate(12deg); } }\n';

const files = ['youtube.html', 'capcut.html', 'google-ai.html', 'meitu.html', 'netflix.html', 'canva.html', 'locket.html', 'windows-pricing.html'];

for (const file of files) {
    if (!fs.existsSync(file)) continue;
    let content = fs.readFileSync(file, 'utf8');
    
    if (!content.includes('GLOBAL EMOJI FLOAT & DECO ENHANCEMENT')) {
        content = content.replace('</style>', globalEnhancement + '\n</style>');
        fs.writeFileSync(file, content, 'utf8');
        console.log('Applied global emoji enhancements to ' + file);
    }
}