const fs = require('fs');

const twemojiScript = 
<script src="https://cdn.jsdelivr.net/npm/@twemoji/api@14.1.0/dist/twemoji.min.js"></script>
<script>
  document.addEventListener("DOMContentLoaded", function() {
    twemoji.parse(document.body, { folder: 'svg', ext: '.svg' });
  });
</script>
<style>
  img.emoji {
    height: 1.2em;
    width: 1.2em;
    margin: 0 .05em 0 .1em;
    vertical-align: -0.2em;
  }
</style>
;

let content = fs.readFileSync('index.html', 'utf8');

if (!content.includes('twemoji')) {
    content = content.replace('</head>', twemojiScript + '</head>');
    fs.writeFileSync('index.html', content, 'utf8');
    console.log('Added twemoji to index.html');
} else {
    console.log('Already added.');
}