const fs = require('fs');

const fixKeyframes = (file) => {
    if (!fs.existsSync(file)) return;
    let content = fs.readFileSync(file, 'utf8');
    
    // Completely remove any existing float1 and float2 definitions and their trailing garbage
    // We'll use a very greedy regex up to .wrap for index, or </style> for others
    
    // First, let's just strip out any float1 and float2 completely.
    // It's safer to just match @keyframes float1 up to the NEXT @keyframes or .wrap or </style>
    content = content.replace(/@keyframes float1[\s\S]*?(?=@keyframes float2)/g, '');
    content = content.replace(/@keyframes float2[\s\S]*?(?=\.wrap|<\/style>|\.card)/g, '');
    
    // Now insert the correct ones right before .wrap or </style> or .card
    const newAnims = 
@keyframes float1 {
  0% { transform: translate(0, 0) scale(1); opacity: 0.15; }
  33% { transform: translate(15vw, 10vh) scale(1.3); opacity: 0.25; }
  66% { transform: translate(-10vw, 15vh) scale(0.9); opacity: 0.1; }
  100% { transform: translate(0, 0) scale(1); opacity: 0.15; }
}
@keyframes float2 {
  0% { transform: translate(0, 0) scale(1); opacity: 0.1; }
  33% { transform: translate(-15vw, -15vh) scale(1.2); opacity: 0.2; }
  66% { transform: translate(10vw, -10vh) scale(0.8); opacity: 0.05; }
  100% { transform: translate(0, 0) scale(1); opacity: 0.1; }
}
;
    
    if (file === 'index.html') {
        content = content.replace(/\.wrap\s*\{/, newAnims + '\n.wrap {');
    } else if (file === 'override.css') {
        content = content.replace(/\.card\s*\{/, newAnims + '\n.card {');
    } else {
        // windows-pricing.html, locket.html
        content = content.replace(/<\/style>/, newAnims + '\n</style>');
    }
    
    fs.writeFileSync(file, content);
    console.log('Fixed ' + file);
}

const files = ['index.html', 'windows-pricing.html', 'locket.html', 'override.css'];
files.forEach(fixKeyframes);
