const fs = require('fs');

const cssFi = '\n/* FADE-IN ANIMATION */\n.fi { opacity: 0; transform: translateY(20px); transition: opacity 0.8s cubic-bezier(0.25, 1, 0.5, 1), transform 0.8s cubic-bezier(0.25, 1, 0.5, 1) !important; }\n.fi.in { opacity: 1; transform: none !important; }\n.card, .ptier, .pcard, .combo { animation: none !important; }\n';

const jsFi = '\n<script>\nconst fadeObs = new IntersectionObserver(entries => {\n  entries.forEach(e => {\n    if (e.isIntersecting) {\n      e.target.classList.add(\"in\");\n    } else {\n      e.target.classList.remove(\"in\");\n    }\n  });\n}, { threshold: 0.1 });\ndocument.querySelectorAll(\".fi\").forEach(el => fadeObs.observe(el));\n</script>\n';

const files = ['youtube.html', 'capcut.html', 'google-ai.html', 'meitu.html', 'netflix.html', 'canva.html', 'locket.html', 'windows-pricing.html'];

for (const file of files) {
    if (!fs.existsSync(file)) continue;
    let content = fs.readFileSync(file, 'utf8');
    
    if (!content.includes('/* FADE-IN ANIMATION */')) {
        content = content.replace('</style>', cssFi + '</style>');
    }
    
    if (!content.includes('fadeObs')) {
        content = content.replace('</body>', jsFi + '</body>');
    }
    
    content = content.replace(/class="card"/g, 'class="card fi"');
    content = content.replace(/class="btn-group d-4"/g, 'class="btn-group d-4 fi"');
    content = content.replace(/class="ptier"/g, 'class="ptier fi"');
    content = content.replace(/class="pcard"/g, 'class="pcard fi"');
    content = content.replace(/class="pcard featured"/g, 'class="pcard featured fi"');
    content = content.replace(/class="combo"/g, 'class="combo fi"');
    content = content.replace(/fi fi/g, 'fi');
    
    fs.writeFileSync(file, content);
    console.log('Added scroll animations to ' + file);
}
