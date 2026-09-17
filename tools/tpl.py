# -*- coding: utf-8 -*-
import os
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # repo root

CSS = """
:root{--blue:#4fc3f7;--green:#81c784;--orange:#ffb74d;--red:#e57373;--purple:#ce93d8;}
.reveal{font-family:'Segoe UI',system-ui,sans-serif;font-size:34px;}
.reveal h2{color:var(--blue);font-size:0.95em;}
.reveal h3{color:var(--green);margin-bottom:.3em;font-size:0.85em;}
.reveal p{font-size:.60em;line-height:1.5;}.reveal li{font-size:.68em;line-height:1.5;}
.reveal pre{font-size:.44em;width:100%;box-shadow:none;}
.reveal ul{text-align:left;margin-left:1em;}
.reveal table{font-size:.5em;}
.reveal table th{color:var(--blue);}
.reveal blockquote{width:100%;box-sizing:border-box;border-left:4px solid var(--blue);padding:.4em 1em;font-style:italic;color:#ccc;background:rgba(79,195,247,.06);margin:.5em 0;font-size:.60em;}
.lbl{font-size:.38em;letter-spacing:3px;text-transform:uppercase;color:#888;display:block;margin-bottom:.2em;}
.divider{width:40px;height:3px;background:var(--blue);margin:.3em auto .6em;}
.g2{display:grid;grid-template-columns:1fr 1fr;gap:12px;text-align:left;}
.g3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px;text-align:left;}
.card{background:rgba(255,255,255,.05);border-left:4px solid var(--blue);padding:8px 12px;border-radius:0 5px 5px 0;font-size:.65em;line-height:1.5;text-align:left;}
.card.g{border-left-color:var(--green);}
.card.o{border-left-color:var(--orange);}
.card.r{border-left-color:var(--red);}
.card.p{border-left-color:var(--purple);}
.card strong{display:block;margin-bottom:.15em;}
.plan{background:rgba(255,255,255,.04);border:1px solid rgba(79,195,247,.3);border-radius:10px;padding:16px 20px;text-align:left;max-width:860px;margin:0 auto;}
.plan-title{color:var(--blue);font-size:.8em;font-weight:700;margin-bottom:.6em;border-bottom:1px solid rgba(79,195,247,.2);padding-bottom:.4em;}
.plan-topics p{font-size:.68em;margin:.25em 0;color:#ddd;}
.plan-topics p span{color:var(--blue);font-weight:600;}
.plan-hw{background:rgba(79,195,247,.08);border:1px solid var(--blue);border-radius:6px;padding:8px 12px;font-size:.65em;margin-top:.7em;}
.plan-hw strong{color:var(--blue);}
.hw{background:rgba(79,195,247,.08);border:2px solid var(--blue);border-radius:10px;padding:14px 18px;text-align:left;}
.hw h3{color:var(--blue)!important;margin-top:0;}
.hw a{color:var(--orange);}
.teams{background:rgba(100,100,255,.08);border:2px solid #6264a7;border-radius:10px;padding:14px 18px;text-align:left;}
.teams h3{color:#9b9fe3!important;margin-top:0;}
.ai{background:linear-gradient(135deg,rgba(206,147,216,.10),rgba(79,195,247,.08));border:2px solid var(--purple);border-radius:12px;padding:14px 18px;text-align:left;}
.ai h3{color:var(--purple)!important;margin-top:0;}
.bio-grid{display:grid;grid-template-columns:1fr 2fr;gap:20px;text-align:left;}
.bio-left{background:rgba(255,255,255,.04);border-radius:8px;padding:12px;font-size:.65em;}
.bio-left .name{font-size:1.2em;font-weight:700;color:var(--blue);margin-bottom:.3em;}
.bio-left .role{color:var(--green);margin-bottom:.5em;}
.timeline{font-size:.62em;line-height:1.8;}
.timeline .year{color:var(--orange);font-weight:600;}
.chain{display:flex;align-items:center;gap:6px;justify-content:center;margin:.6em 0;flex-wrap:wrap;}
.chain .node{background:rgba(255,255,255,.07);border:1px solid var(--blue);border-radius:6px;padding:6px 10px;font-size:.62em;}
.chain .arr{color:var(--orange);}
.num{display:inline-block;width:20px;height:20px;background:var(--blue);color:#111;border-radius:50%;text-align:center;line-height:20px;font-size:.6em;font-weight:700;margin-right:5px;}
.bug-grid{display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px;}
.bug-card{background:rgba(229,115,115,.08);border:1px solid rgba(229,115,115,.3);border-radius:6px;padding:8px 10px;font-size:.62em;line-height:1.5;text-align:left;}
.bug-card .co{font-weight:700;color:var(--red);margin-bottom:.2em;}
.figure{text-align:center;margin:.5em 0;}
.figure img{max-width:100%;max-height:380px;border-radius:8px;background:#fff;padding:6px;box-shadow:0 4px 18px rgba(0,0,0,.4);}
.figure .cap{font-size:.42em;color:#888;margin-top:.35em;}
.g2 .figure img,.g3 .figure img{max-height:300px;}
.newsgrid{display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;align-items:start;}
.newsgrid img{width:100%;border-radius:6px;background:#fff;padding:3px;}
.newsgrid .n{font-size:.5em;color:#aaa;margin-top:.2em;text-align:left;line-height:1.4;}
.portrait{width:100%;border-radius:8px;}
.nav{position:fixed;top:12px;right:12px;z-index:999;font-size:.55em;display:flex;gap:8px;}
.nav a{color:#555;text-decoration:none;padding:3px 8px;border:1px solid #333;border-radius:5px;}
.nav a:hover{color:#fff;border-color:#fff;}
"""

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@4.6.1/dist/reveal.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@4.6.1/dist/theme/black.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@4.6.1/plugin/highlight/monokai.css">
<style>{css}</style>
</head>
<body>
<div class="nav">{nav}</div>
<div class="reveal"><div class="slides">
"""

FOOT = """
</div></div>
<script src="https://cdn.jsdelivr.net/npm/reveal.js@4.6.1/dist/reveal.js"></script>
<script src="https://cdn.jsdelivr.net/npm/reveal.js@4.6.1/plugin/highlight/highlight.js"></script>
<script>
Reveal.initialize({hash:true,progress:true,slideNumber:'c/t',transition:'slide',transitionSpeed:'fast',plugins:[RevealHighlight],keyboard:{27:null}});
document.addEventListener('keydown',function(e){if(e.key==='Escape'){e.preventDefault();e.stopPropagation();window.location.href='index.html';}},true);
</script>
</body>
</html>
"""

TOTAL = 13

BONUS = ["lesson-bonus-ai.html", "lesson-bonus-performance.html", "lesson-bonus-security.html"]

def nav_for(n):
    parts = []
    if n > 1:
        parts.append('<a href="lesson-%02d.html">&larr; L%d</a>' % (n-1, n-1))
    parts.append('<a href="index.html">&#8617; All lessons</a>')
    if n < TOTAL:
        parts.append('<a href="lesson-%02d.html">L%d &rarr;</a>' % (n+1, n+1))
    else:
        parts.append('<a href="lesson-bonus-ai.html">Bonus &rarr;</a>')
    return "".join(parts)

def nav_bonus(i):
    parts = []
    if i > 0:
        parts.append('<a href="%s">&larr; Bonus</a>' % BONUS[i-1])
    else:
        parts.append('<a href="lesson-13.html">&larr; L13</a>')
    parts.append('<a href="index.html">&#8617; All lessons</a>')
    if i < len(BONUS) - 1:
        parts.append('<a href="%s">Bonus &rarr;</a>' % BONUS[i+1])
    return "".join(parts)

def img(src, alt, width="72%", caption=None):
    cap = '<div class="cap">%s</div>' % caption if caption else ''
    return '<div class="figure"><img src="images/%s" alt="%s" style="width:%s">%s</div>' % (src, alt, width, cap)

def title_slide(n, title, sub):
    return """<section data-background-gradient="linear-gradient(135deg,#0f0c29,#302b63,#24243e)">
  <span class="lbl">Lesson %d of %d</span>
  <h2>%s</h2>
  <div class="divider"></div>
  <p style="font-size:.62em">%s</p>
  <p style="font-size:.5em;color:#555;margin-top:.8em">&rarr; next slide &nbsp;|&nbsp; ESC overview</p>
</section>""" % (n, TOTAL, title, sub)

def plan_slide(n, title, focus, topics, hw):
    t = "\n".join('        <p><span>%d.</span> %s</p>' % (i+1, x) for i, x in enumerate(topics))
    hwhtml = '      <div class="plan-hw"><strong>Homework:</strong> %s</div>' % hw if hw else ''
    return """<section>
  <span class="lbl">Lesson Plan</span>
  <div class="plan">
    <div class="plan-title">Lesson %d: %s<br>Focus: %s</div>
      <div class="plan-topics">
%s
      </div>
%s
  </div>
</section>""" % (n, title, focus, t, hwhtml)

def write_lesson(n, title, sub, focus, topics, hw_line, slides):
    body = [title_slide(n, title, sub), plan_slide(n, title, focus, topics, hw_line)] + slides
    html = HEAD.format(title="Lesson %d &ndash; %s" % (n, title), css=CSS, nav=nav_for(n)) \
           + "\n\n".join(body) + FOOT
    with open(os.path.join(OUT, "lesson-%02d.html" % n), "w") as f:
        f.write(html)
    print("wrote lesson-%02d.html (%d slides)" % (n, len(body)))
