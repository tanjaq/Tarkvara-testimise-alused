# -*- coding: utf-8 -*-
import os
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # repo root

LESSONS = [
 (1,"Testing Fundamentals &amp; the Quality Mindset",["Quality","Terminology","V&amp;V","AI ground rules"],"l1","",""),
 (2,"The Purpose of Testing",["Why test","Real failures","Cost of defects"],"l2","HW 1",""),
 (3,"The Testing Process",["SDLC","ISTQB process","Waterfall / V / Agile","7 principles"],"l3","HW 2",""),
 (4,"Software Requirements",["FR / NFR","SMART","User stories","SRS"],"l4","HW 3",""),
 (5,"Software Architecture",["Monolith","Microservices","Event-driven","Monorepo"],"l5","HW 4",""),
 (6,"Test Techniques I &mdash; Static Testing",["Reviews","Inspections","Static analysis","PR review"],"l6","HW 5",""),
 (7,"Test Techniques II &mdash; Black Box",["EP","BVA","Decision tables","State transition"],"l7","HW 6",""),
 (8,"Test Techniques III &mdash; White Box",["Statement","Branch","Coverage limits"],"l8","HW 7",""),
 (9,"Defect Management &amp; Exploratory Testing",["Charters","Tours","Bug reports","RCA"],"l9","HW 8",""),
 (10,"Test Cases &amp; Documentation",["Test cases","Regression","SRS review"],"l1","HW 9",""),
 (11,"Database &amp; SQL Testing",["SQL","Integrity","Migrations","Test data"],"l2","HW 10",""),
 (12,"Accessibility Testing",["WCAG","POUR","Keyboard","Contrast"],"l3","HW 11",""),
 (13,"Mobile Testing",["Devices","Interruptions","Network","Stores"],"l4","HW 12"," &middot; Last lesson"),
]
COLORS = {"l1":"#4fc3f7","l2":"#81c784","l3":"#ffb74d","l4":"#e57373","l5":"#ce93d8",
          "l6":"#4fc3f7","l7":"#81c784","l8":"#ffb74d","l9":"#e57373"}

cards = []
for n, title, tags, cls, hw, sub in LESSONS:
    c = COLORS[cls]
    tg = "".join('\n      <span class="tag" style="color:%s">%s</span>' % (c, t) for t in tags)
    badge = '\n    <div class="hw-badge">%s</div>' % hw if hw else ''
    cards.append("""  <a href="lesson-%02d.html" class="card %s">%s
    <div class="lesson-num">Lesson %d%s</div>
    <div class="lesson-title">%s</div>
    <div class="topics">%s
    </div>
  </a>""" % (n, cls, badge, n, sub, title, tg))

BONUS = [
 ("lesson-bonus-ai.html", "Using AI Responsibly in Testing", ["Good uses","Silent failures","Prompting","Testing AI"], "#ce93d8"),
 ("lesson-bonus-performance.html", "Performance Testing", ["Response time","Throughput","Load / stress"], "#4fc3f7"),
 ("lesson-bonus-security.html", "Application Security", ["CIA","OWASP","Injection","XSS"], "#81c784"),
]
bcards = []
for href, title, tags, c in BONUS:
    tg = "".join('\n      <span class="tag" style="color:%s">%s</span>' % (c, t) for t in tags)
    bcards.append("""  <a href="%s" class="card" style="--accent:%s">
    <div class="lesson-num">Bonus Lesson</div>
    <div class="lesson-title">%s</div>
    <div class="topics">%s
    </div>
  </a>""" % (href, c, title, tg))

html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Software Testing Fundamentals</title>
<style>
*{box-sizing:border-box;margin:0;padding:0;}
body{background:#0f0c29;color:#e0e0e0;font-family:'Segoe UI',system-ui,sans-serif;min-height:100vh;padding:40px 20px;}
h1{color:#4fc3f7;font-size:1.6em;text-align:center;margin-bottom:.3em;}
.subtitle{text-align:center;color:#888;font-size:.80em;margin-bottom:1.6em;}
.track{text-align:center;font-size:.72em;color:#888;margin:-1em 0 1.6em;}
.track a{color:#4fc3f7;text-decoration:none;border-bottom:1px solid rgba(79,195,247,.35);}
.track a:hover{border-color:#4fc3f7;}
.cta{max-width:1100px;margin:2.8em auto 0;display:flex;justify-content:center;}
.cta a{display:flex;align-items:center;gap:14px;background:linear-gradient(135deg,rgba(79,195,247,.18),rgba(129,199,132,.12));border:2px solid #4fc3f7;border-radius:14px;padding:16px 30px;text-decoration:none;color:inherit;transition:all .2s;}
.cta a:hover{background:linear-gradient(135deg,rgba(79,195,247,.3),rgba(129,199,132,.2));transform:translateY(-2px);}
.cta .big{font-size:1.05em;font-weight:700;color:#4fc3f7;}
.cta .sm{font-size:.72em;color:#aaa;margin-top:2px;}
.cta .arrow{font-size:1.3em;color:#4fc3f7;}
.sechead{max-width:1100px;margin:2.8em auto 1em;font-size:.72em;letter-spacing:3px;text-transform:uppercase;color:#666;border-bottom:1px solid rgba(255,255,255,.08);padding-bottom:.5em;}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:20px;max-width:1100px;margin:0 auto;}
.card{background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.1);border-radius:12px;padding:24px;text-decoration:none;color:inherit;transition:all .2s;position:relative;overflow:hidden;}
.card:hover{background:rgba(79,195,247,.1);border-color:#4fc3f7;transform:translateY(-2px);}
.card::before{content:'';position:absolute;top:0;left:0;width:4px;height:100%;background:var(--accent,#4fc3f7);}
.lesson-num{font-size:.58em;letter-spacing:3px;text-transform:uppercase;color:#888;margin-bottom:.4em;}
.lesson-title{font-size:.92em;font-weight:600;color:#fff;margin-bottom:.5em;}
.topics{font-size:.62em;color:#aaa;line-height:1.6;}
.tag{display:inline-block;padding:2px 8px;border-radius:10px;font-size:.55em;border:1px solid currentColor;margin:2px;}
.hw-badge{position:absolute;top:16px;right:16px;font-size:.53em;background:rgba(79,195,247,.15);color:#4fc3f7;border:1px solid #4fc3f7;padding:2px 8px;border-radius:10px;}
.l1{--accent:#4fc3f7;} .l2{--accent:#81c784;} .l3{--accent:#ffb74d;}
.l4{--accent:#e57373;} .l5{--accent:#ce93d8;} .l6{--accent:#4fc3f7;}
.l7{--accent:#81c784;} .l8{--accent:#ffb74d;} .l9{--accent:#e57373;}
.materials{max-width:1100px;margin:1.2em auto 0;font-size:.68em;color:#888;text-align:center;}
.materials a{color:#4fc3f7;text-decoration:none;margin:0 10px;}
.materials a:hover{text-decoration:underline;}
footer{text-align:center;color:#555;font-size:.65em;margin-top:3.4em;line-height:1.9;}
</style>
</head>
<body>
<h1>Software Testing Fundamentals</h1>
<p class="subtitle">13 lessons + 3 bonus lessons &middot; manual testing, from the quality mindset to mobile</p>
<p class="track">Meeting every other week? <a href="compact/index.html">Compact track &mdash; the same course in 6 sessions &rarr;</a></p>

<div class="sechead">Lessons</div>
<div class="grid">

@@CARDS@@

</div>

<div class="sechead">Bonus lessons</div>
<div class="grid">

@@BONUS@@

</div>

<div class="cta">
  <a href="homework/index.html">
    <div>
      <div class="big">Homework &mdash; all 12 assignments</div>
      <div class="sm">Task, deliverable and assessment criteria for every assignment</div>
    </div>
    <div class="arrow">&rarr;</div>
  </a>
</div>

<div class="materials">
  Course materials:
  <a href="materials/Software Requirements Specification (SRS) Document Template.docx">SRS template</a>
  <a href="materials/input-form-example.html">Trip planner form</a>
  <a href="materials/shop-database.sql">Shop database</a>
  <a href="homework/testing-process-worksheet.html">Testing process worksheet</a>
</div>

<footer>
  Software Testing Fundamentals &middot; Tatjana Kirotar<br>
  Open any lesson to begin &middot; use &rarr; to move between slides, ESC to come back here
</footer>
</body>
</html>
""".replace("@@CARDS@@", "\n\n".join(cards)).replace("@@BONUS@@", "\n\n".join(bcards))

open(os.path.join(OUT, "index.html"), "w").write(html)
print("wrote index.html")
