# -*- coding: utf-8 -*-
import os
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # repo root
os.makedirs(os.path.join(OUT, "homework"), exist_ok=True)

PAGE_CSS = """
*{box-sizing:border-box;margin:0;padding:0;}
body{background:#0f0c29;color:#e0e0e0;font-family:'Segoe UI',system-ui,sans-serif;min-height:100vh;padding:40px 20px;line-height:1.65;}
.wrap{max-width:820px;margin:0 auto;}
a{color:#4fc3f7;}
.crumb{font-size:.8em;color:#666;margin-bottom:1.5em;}
.crumb a{color:#888;text-decoration:none;}
.crumb a:hover{color:#4fc3f7;}
h1{color:#4fc3f7;font-size:1.5em;margin-bottom:.2em;}
.meta{color:#888;font-size:.85em;margin-bottom:2em;}
.meta span{display:inline-block;border:1px solid #333;border-radius:10px;padding:2px 10px;margin-right:6px;font-size:.9em;}
h2{color:#81c784;font-size:1.02em;margin:1.8em 0 .5em;border-bottom:1px solid rgba(255,255,255,.08);padding-bottom:.3em;}
ul,ol{margin:.4em 0 .4em 1.4em;}
li{margin:.35em 0;font-size:.95em;}
p{margin:.5em 0;font-size:.95em;}
.box{background:rgba(255,255,255,.05);border-left:4px solid #4fc3f7;border-radius:0 6px 6px 0;padding:12px 16px;margin:.8em 0;font-size:.95em;}
.box.g{border-left-color:#81c784;} .box.o{border-left-color:#ffb74d;} .box.r{border-left-color:#e57373;}
table{border-collapse:collapse;width:100%;margin:.8em 0;font-size:.9em;}
th,td{border:1px solid rgba(255,255,255,.12);padding:7px 10px;text-align:left;vertical-align:top;}
th{color:#4fc3f7;background:rgba(255,255,255,.03);}
code{background:rgba(255,255,255,.08);padding:1px 5px;border-radius:3px;font-size:.9em;}
footer{margin-top:3em;padding-top:1em;border-top:1px solid rgba(255,255,255,.08);color:#555;font-size:.8em;}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:16px;margin-top:1.5em;}
.hwcard{background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.1);border-radius:10px;padding:18px;text-decoration:none;color:inherit;display:block;transition:all .2s;border-left:4px solid #4fc3f7;}
.hwcard:hover{background:rgba(79,195,247,.1);border-color:#4fc3f7;transform:translateY(-2px);}
.hwcard .n{font-size:.72em;letter-spacing:2px;text-transform:uppercase;color:#888;}
.hwcard .t{font-weight:600;color:#fff;margin:.25em 0;font-size:1em;}
.hwcard .d{font-size:.85em;color:#aaa;}
.esc{font-size:.75em;color:#555;margin-top:2em;}
"""

ESC = """<script>
document.addEventListener('keydown',function(e){if(e.key==='Escape'){e.preventDefault();window.location.href='../index.html';}},true);
</script>"""

def page(title, body, crumb):
    return """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>%s</title>
<style>%s</style>
</head>
<body>
<div class="wrap">
<div class="crumb">%s</div>
%s
<footer>Software Testing Fundamentals &middot; Tatjana Kirotar &middot; <span class="esc">press ESC to go back to all lessons</span></footer>
</div>
%s
</body>
</html>
""" % (title, PAGE_CSS, crumb, body, ESC)

HW = [
 dict(n=1, lesson=2, title="Failure Case Analysis",
   short="Analyse a real software failure and the testing that would have prevented it.",
   type="Group of 3&ndash;4", submit="Teams",
   objective="Connect a real-world failure to a specific, missing testing activity.",
   steps=["Pick one failure from the lesson (Uber, YouTube, Tesla, Boeing 737 MAX, Starliner, CrowdStrike, or one of the public-sector examples) or find your own online.",
          "Answer as a group: What happened? What were the consequences (money, reputation, safety, environment)?",
          "At which stage was the defect introduced &mdash; requirements, design, development, testing, acceptance?",
          "What testing should have been done to prevent it? Be specific: which technique, at which stage, checking what.",
          "Prepare a 2&ndash;3 minute summary for the class."],
   deliverable="A one-page write-up per group, plus the in-class summary.",
   criteria=[["Accuracy","The facts of the incident are right and sourced"],["Root cause","You identify the stage where the defect was introduced, not just where it was noticed"],["Prevention","The proposed testing is specific and would actually have caught it"]],
   resources=[["Lesson 2 &mdash; The Purpose of Testing","../lesson-02.html"]]),

 dict(n=2, lesson=3, title="Test Process Worksheet &mdash; Calculator",
   short="Run all five ISTQB test process steps on a simple web calculator.",
   type="Group of 3&ndash;4", submit="Teams",
   objective="Experience the full test process end to end on something small enough to finish in one session.",
   steps=["The system under test: a simple web calculator that takes two numbers, offers four operations (add, subtract, multiply, divide) and shows a result.",
          "<strong>1. Planning and control</strong> &mdash; define the scope of testing. What are the risks? (division by zero, negative numbers, empty fields, very large numbers, decimal separators)",
          "<strong>2. Analysis and design</strong> &mdash; identify test conditions. Choose which conditions matter most, based on risk, frequency and criticality.",
          "<strong>3. Test creation</strong> &mdash; write at least three test cases with inputs, steps and expected result.",
          "<strong>4. Test execution</strong> &mdash; assume the calculator is built (you may use your OS or phone calculator). Mark each test PASS or FAIL. For a FAIL, write a short defect description.",
          "<strong>5. Closure</strong> &mdash; was the testing sufficient? What was left uncovered? What would you improve next round?",
          "<strong>Filling it in</strong> &mdash; either download the <a href=\"../materials/testing-process-worksheet.docx\">Word version</a> and type into it, or type straight into the <a href=\"testing-process-worksheet.html\">worksheet page</a> and use its Print button to save a PDF. Hand the finished file in through Teams.",
          "Present to the class and discuss whether the testing was enough."],
   deliverable="The completed worksheet with all five sections filled in.",
   criteria=[["Completeness","All five process steps are filled in, not just the test cases"],["Risk thinking","Risks named are real and specific to a calculator"],["Test cases","At least three cases with concrete inputs and a single, measurable expected result"],["Honest closure","You can name what you did not cover"]],
   resources=[["Worksheet &mdash; Word version (.docx)","../materials/testing-process-worksheet.docx"],["Worksheet &mdash; fill in on the page","testing-process-worksheet.html"],["Lesson 3 &mdash; The Testing Process","../lesson-03.html"]]),

 dict(n=3, lesson=4, title="Requirements for Your Project",
   short="Write the SRS requirements for your own project: functional and non-functional.",
   type="Group project", submit="Teams",
   objective="Produce requirements you can actually build and test against for the rest of the course.",
   steps=["Start from the SRS template.",
          "Write the <strong>functional requirements</strong> &mdash; what the software must do. Derive them from user stories; do not submit the user stories as requirements.",
          "Write the <strong>non-functional requirements</strong> &mdash; how the software must behave. Cover at least: performance, security, usability, availability and accessibility.",
          "Check every requirement against SMART: specific, measurable, achievable, realistic, timely.",
          "Review each other's requirements inside the team before submitting &mdash; that is a peer review, and it counts."],
   deliverable="An SRS document with FR and NFR sections completed.",
   criteria=[["Testable","Every requirement could be turned into a test case with one expected result"],["Measurable","NFRs contain numbers and a measurement point, not adjectives"],["Complete","The requirements cover the whole scope you intend to build"],["Not user stories","Requirements are written as system behaviour, not as \"as a user I want...\""]],
   resources=[["SRS document template (.docx)","../materials/Software Requirements Specification (SRS) Document Template.docx"],["SRS example 1","../materials/srs_example_1.pdf"],["SRS example 2","../materials/srs_example_2.pdf"],["ISO/IEC/IEEE 29148 SRS example","https://www.reqview.com/doc/iso-iec-ieee-29148-srs-example/"],["Lesson 4 &mdash; Software Requirements","../lesson-04.html"]]),

 dict(n=4, lesson=5, title="Project Architecture",
   short="Draw the architecture of your project and justify the style you chose.",
   type="Group project", submit="Teams",
   objective="Make the structure of your system explicit, so you can reason about where to test it.",
   steps=["As a team, decide which architecture style fits your project best: monolithic, layered, microservices, event-driven, serverless, modular or monorepo.",
          "Draw the diagram: components, the relationships between them, and the communication channels.",
          "Add comments explaining why this architecture is the right choice for your project &mdash; consider project size and complexity, team size and experience, scalability and maintainability needs, budget and schedule, technology constraints.",
          "Add one paragraph on testing: given this architecture, where will most defects appear, and how will you test the connections between components?",
          "Present the diagram to the class: why you chose it and what challenges you expect."],
   deliverable="Architecture diagram plus justification, added to the SRS document.",
   criteria=[["Correctness","The diagram matches what you are actually building"],["Justification","The choice is argued against real constraints, not fashion"],["Testing angle","You identify where this architecture makes testing harder"]],
   resources=[["Lesson 5 &mdash; Software Architecture","../lesson-05.html"]]),

 dict(n=5, lesson=6, title="Peer Review &mdash; Rental Car",
   short="Review a real repository and report every defect and inconsistency you find.",
   type="Individual or pair", submit="Teams",
   objective="Practise static testing: find defects by reading, before anything is executed.",
   steps=["Open the repository: <a href=\"https://github.com/tanjaq/Rental-Car/tree/peer-review\">tanjaq/Rental-Car, peer-review branch</a>",
          "<strong>Read the documentation (README)</strong> &mdash; does it clearly describe what the application must do? Are all requirements understandable and precise enough?",
          "<strong>Review the code</strong> &mdash; is it logical and easy to read? Are function and variable names clear? Does the code match the documented requirements? Is any described function missing or implemented incorrectly?",
          "Write down every problem or discrepancy you find between the code and the documentation.",
          "Rank your findings: which are defects that would break the product, which are maintainability concerns, which are style preferences.",
          "Phrase every finding the way you would in a real pull request review &mdash; about the code, not the person."],
   deliverable="A list of findings, each with: where it is, what is wrong, why it matters, and how serious it is.",
   criteria=[["Coverage","You reviewed both the documentation and the code"],["Real defects","Actual mismatches found, not only formatting opinions"],["Ranking","Blocking issues separated from suggestions"],["Tone","Comments are constructive and specific"]],
   resources=[["Rental-Car peer-review branch","https://github.com/tanjaq/Rental-Car/tree/peer-review"],["Lesson 6 &mdash; Static Testing","../lesson-06.html"]]),

 dict(n=6, lesson=7, title="Decision Table + EP/BVA",
   short="Build the discount decision table, and run EP and BVA against the trip planner form.",
   type="Individual or pair", submit="Teams",
   objective="Apply specification-based techniques to a rule set complex enough that intuition fails, and to a real form that really is broken.",
   steps=["<strong>Part 1 &mdash; decision table.</strong> A user wants to print holiday photos. The business rules are:",
          "&bull; An unregistered regular user has no permanent discount.<br>&bull; A registered user gets a 5% discount on every purchase.<br>&bull; Additional discounts: ordering more than 10 photos adds 3%; ordering photo frames as well adds 3%.<br>&bull; On a registered user's birthday, the standard 5% is replaced by 8%.",
          "Build the decision table showing every possible combination of the business rules and the discount that applies.",
          "Mark which combinations you would test first, and why. Note any rule that is ambiguous as written &mdash; that is a defect in the requirement.",
          "<strong>Part 2 &mdash; EP and BVA on a live form.</strong> Open the <a href=\"../materials/input-form-example.html\">trip planner form</a>.",
          "Define the equivalence partitions and boundary values for: number of travellers (1&ndash;8), budget (100&ndash;10000), email, and promo code (4&ndash;10 characters).",
          "Run them. Record every case where the form's behaviour does not match its own stated rules &mdash; there are several real defects in it.",
          "For each defect say which technique found it: would equivalence partitioning alone have caught it, or did you need the boundary values?"],
   deliverable="The complete decision table with prioritisation, plus your EP/BVA table and the list of defects found in the form.",
   criteria=[["Completeness","Every combination of conditions appears in the table"],["Correct outcomes","The discount for each row is calculated correctly"],["Partitions and boundaries","Both are defined for every field, and the boundary values are the right ones"],["Defects found","Real mismatches between the form's rules and its behaviour, with evidence"],["Technique awareness","You can say which technique caught which defect"]],
   resources=[["Trip planner form","../materials/input-form-example.html"],["Lesson 7 &mdash; Black Box Techniques","../lesson-07.html"]]),

 dict(n=7, lesson=8, title="Boarding Pass &mdash; Coverage Analysis",
   short="Work out statement and branch coverage for two given tests, and add what is missing.",
   type="Individual or pair", submit="Teams",
   objective="Read code coverage honestly &mdash; and see what it does not tell you.",
   steps=["Open the code example: <a href=\"https://onecompiler.com/javascript/3yydc2m52\">onecompiler.com/javascript/3yydc2m52</a>",
          "Given test cases: (1) a frequent flier is upgraded to Business class; (2) a non-frequent flier gets an Economy ticket.",
          "How many statements do these two tests cover? (statement coverage)",
          "How many branches do they cover? (branch coverage)",
          "Which tests must you add to reach 100% statement coverage?",
          "Draw a flow diagram if it helps &mdash; it usually does.",
          "Finally: name one defect this code could contain that 100% statement coverage would still not find."],
   deliverable="Your coverage numbers, the additional tests needed, the diagram if drawn, and the answer to the last question.",
   criteria=[["Correct counting","Statement and branch counts are right"],["Additional tests","The added tests genuinely reach the uncovered code"],["Understanding limits","You can name what coverage cannot detect"]],
   resources=[["Code example","https://onecompiler.com/javascript/3yydc2m52"],["Lesson 8 &mdash; White Box Techniques","../lesson-08.html"]]),

 dict(n=8, lesson=9, title="Exploratory Session + Bug Report",
   short="Run a charter-driven exploratory session, then file a real defect in the Bug-Reporting repo.",
   type="Individual", submit="GitHub &mdash; Bug-Reporting repo",
   objective="Find a defect nobody scripted a test for, and report it so a developer can reproduce it without asking you anything.",
   steps=["<strong>Write a charter</strong> before you touch the product: <em>Explore &lt;target&gt; with &lt;resources&gt; to discover &lt;information&gt;.</em> Choose any application or website you use regularly.",
          "<strong>Pick a tour</strong> &mdash; money, back alley, saboteur, couch potato or guidebook &mdash; and say why that one fits your charter.",
          "<strong>Time-box the session</strong> to 45&ndash;60 minutes. Take notes as you go: what you covered, what surprised you, questions raised, what you did not get to.",
          "Use the heuristics from the lesson: CRUD every entity you can, try Goldilocks values (zero, one, far too many), and check SFDIPOT for areas you have not touched.",
          "<strong>Pick your most interesting defect</strong> &mdash; a broken feature, a wrong error message, a missing validation, a UI glitch, a data problem.",
          "Write the full bug report: summary title, environment, severity, priority, numbered steps to reproduce, expected result, actual result, visuals and logs. Open DevTools before reproducing so you have the console and network evidence.",
          "File it as an issue: <a href=\"https://github.com/tanjaq/Bug-Reporting/issues\">tanjaq/Bug-Reporting &middot; Issues</a>. Use the Bug Report template &mdash; it has all the fields pre-filled. The existing issues in that repo are worked examples using the same template.",
          "Attach your session notes to the issue, and explain in two sentences why you chose this defect and what severity and priority you assigned."],
   deliverable="One GitHub issue in the Bug-Reporting repository with all fields completed, your charter and session notes, and the severity/priority justification.",
   criteria=[["Charter","A real charter was written before exploring, and the session stayed on mission"],["Reproducible","Someone else can follow your steps and see the same failure"],["Specific actual result","Names what actually happens, with values &mdash; not \"it doesn't work\""],["Evidence","Screenshot, console error or network response included"],["Severity vs priority","The two are assigned separately and both justified"],["Notes","Your notes say what you covered and what you did not"]],
   resources=[["Bug-Reporting repository","https://github.com/tanjaq/Bug-Reporting"],["File a new issue","https://github.com/tanjaq/Bug-Reporting/issues"],["Lesson 9 &mdash; Defect Management &amp; Exploratory Testing","../lesson-09.html"]]),

 dict(n=9, lesson=10, title="Test Plan and Test Cases for Your Project",
   short="Write your project's test plan, and the test cases that cover every functional requirement.",
   type="Group project", submit="Teams",
   objective="Close the loop: the requirements you wrote in Homework 3, now verified by a plan that says how you will test them and by cases that actually do it.",
   steps=["<strong>Part 1 &mdash; the test plan.</strong> Write it into your SRS document, section 7.1 Test Plan. Keep it to one page. It must contain:",
          "&bull; <strong>Scope</strong> &mdash; which parts of the system the plan covers, and at which test level<br>&bull; <strong>Features to be tested</strong> &mdash; listed explicitly and traceable to the functional requirements in section 3<br>&bull; <strong>Features not to be tested</strong> &mdash; and why<br>&bull; <strong>Test approach</strong> &mdash; which techniques from Lessons 7 and 8 you will use, and what you will test manually<br>&bull; <strong>Entry and exit criteria</strong> &mdash; when testing can start, and when it is finished<br>&bull; <strong>Test environment and test data</strong> &mdash; which environment, which accounts, which data<br>&bull; <strong>Risks and mitigations</strong> &mdash; what could stop testing, and what you will do<br>&bull; <strong>Deliverables and schedule</strong>",
          "Write the exit criteria so that someone outside your team could look at your project and answer yes or no. \"Testing is done when it works\" is not an exit criterion.",
          "Writing the plan usually finds requirement defects &mdash; a behaviour nobody has decided yet. Note those; they count in your favour.",
          "<strong>Part 2 &mdash; the test cases.</strong> Add them to your SRS document, section 7.2 Test Cases.",
          "The test cases must cover <strong>all</strong> of your functional requirements &mdash; check them off one by one against section 3.",
          "Each test case needs: ID and title, description and the requirement it covers, preconditions, numbered steps, test data, expected results, and a status column.",
          "Include negative and edge cases, not only the happy path. Use equivalence partitioning and boundary value analysis to decide which values to test.",
          "Keep each case focused on one scenario, and make sure no case depends on the output of another."],
   deliverable="Your SRS document with section 7.1 Test Plan and section 7.2 Test Cases completed.",
   criteria=[["Plan is complete","All eight parts of the test plan are filled in, including what will <em>not</em> be tested"],
             ["Exit criteria are checkable","Someone else could decide from them whether testing is finished"],
             ["Approach matches the product","The chosen techniques fit what your system actually does"],
             ["Traceability","Every functional requirement has at least one test case, and every case names its requirement"],
             ["Executable","Another team could run your cases without asking questions"],
             ["Measurable expected results","No \"works correctly\""],
             ["Negative coverage","Invalid input and edge cases are included"]],
   resources=[["SRS document template (.docx)","../materials/Software Requirements Specification (SRS) Document Template.docx"],["Lesson 3 &mdash; planning and control","../lesson-03.html"],["Lesson 10 &mdash; Test Cases &amp; Documentation","../lesson-10.html"]]),

 dict(n=10, lesson=11, title="SQL Verification &mdash; Shop Database",
   short="Verify requirements with SQL and find the data defects hiding in a sample database.",
   type="Individual or pair", submit="Teams",
   objective="Prove things about data instead of trusting the screen &mdash; and see which defects a missing constraint lets through.",
   steps=["Open <a href=\"https://sqliteonline.com\">sqliteonline.com</a> (or any SQLite client). Paste <a href=\"../materials/shop-database.sql\">shop-database.sql</a> and run it.",
          "The nine requirements the application is supposed to guarantee are listed in comments at the top of the file.",
          "<strong>Write one query per requirement</strong> that checks whether the data actually honours it. A good check returns zero rows when everything is fine, and the offending rows when it is not.",
          "Run the join comparison suggested at the bottom of the file: <code>JOIN</code> versus <code>LEFT JOIN</code> on orders and customers. Explain the difference in the row count.",
          "<strong>Find the defects.</strong> There are at least six. For each one record: the query that found it, the rows returned, which requirement it breaks, and the severity you would assign.",
          "For each defect, name the <strong>database constraint</strong> that would have prevented it &mdash; <code>NOT NULL</code>, <code>UNIQUE</code>, <code>FOREIGN KEY</code> or <code>CHECK</code>.",
          "Finally: one of the requirements is about money. Look at how prices and totals are stored and say what you would change, and why."],
   deliverable="Your queries, the defects found with evidence, the constraint that would have prevented each, and your note on the money storage.",
   criteria=[["Query per requirement","Each requirement has a check that returns rows only when it is violated"],["Defects found","At least six, correctly mapped to the requirement they break"],["Constraints","The right constraint is named for each defect"],["Join understanding","You can explain the row-count difference between JOIN and LEFT JOIN"],["Severity","Assigned and justified per defect"]],
   resources=[["shop-database.sql","../materials/shop-database.sql"],["SQLite Online","https://sqliteonline.com"],["Lesson 11 &mdash; Database &amp; SQL Testing","../lesson-11.html"]]),

 dict(n=11, lesson=12, title="Accessibility Audit",
   short="Audit one public site and your own project against WCAG 2.2 level AA.",
   type="Individual or pair", submit="Teams",
   objective="Find real accessibility defects with a keyboard, your eyes and one scanner &mdash; and see how much the scanner misses.",
   steps=["Pick <strong>one public site</strong> (a shop, a bank, a public service, a news site) and <strong>your own project</strong>.",
          "<strong>Keyboard-only walkthrough.</strong> Put the mouse away. Complete one real task using only Tab, Shift+Tab, Enter, Space and the arrow keys. Record: anything unreachable, any point where the focus indicator disappeared, any keyboard trap, any order that made no sense.",
          "<strong>Zoom.</strong> Take the page to 200% and then 400%. Does content reflow, or is text cut off and overlapping?",
          "<strong>Contrast.</strong> Check body text, placeholder text, buttons and disabled states. Normal text needs at least 4.5:1, large text and UI components 3:1.",
          "<strong>Colour only.</strong> Find at least one place where information is conveyed by colour alone &mdash; or confirm there is none.",
          "<strong>Structure.</strong> Check headings (one h1, no skipped levels), image alt text, form labels (a placeholder is not a label), link text out of context, and error messages.",
          "<strong>Automated scan.</strong> Run axe DevTools, WAVE or Lighthouse on the same pages.",
          "<strong>Optional but recommended:</strong> turn on VoiceOver, NVDA or TalkBack and try one flow with your eyes closed.",
          "<strong>Report.</strong> One row per finding: page, what is wrong, the WCAG success criterion it breaks (e.g. 1.4.3 Contrast, 2.1.1 Keyboard, 2.4.7 Focus Visible, 3.3.2 Labels), severity, and how you would fix it.",
          "Finish with a comparison: how many findings came from the automated scan, and how many only from your manual checks?"],
   deliverable="An audit report for both sites with findings mapped to WCAG criteria, plus the manual-versus-automated comparison and a fix for at least one finding in your own project.",
   criteria=[["Manual work","The keyboard, zoom, contrast and structure checks were actually done, not just a scan"],["WCAG mapping","Findings reference specific success criteria"],["Severity","Assigned by user impact, and justified"],["Comparison","You can say what the scanner missed"],["Your own project","At least one accessibility defect in your own project is found and fixed"]],
   resources=[["WCAG 2.2 quick reference","https://www.w3.org/WAI/WCAG22/quickref/"],["axe DevTools","https://www.deque.com/axe/devtools/"],["WAVE","https://wave.webaim.org/"],["Lesson 12 &mdash; Accessibility Testing","../lesson-12.html"]]),

 dict(n=12, lesson=13, title="Mobile Test Charter",
   short="Build a device matrix, then break an app on a real phone with interruptions and bad network.",
   type="Individual or pair", submit="Teams",
   objective="Test the conditions that only exist once the software is in someone's hand.",
   steps=["<strong>Part 1 &mdash; device matrix.</strong> For your own project (or a chosen app), decide which devices you would test on. Give five rows: device or class, OS version, screen size, why it is on the list, and what you would prioritise testing there. Include one deliberately old, small and slow device.",
          "Say where each row would be tested: real device, emulator, or device cloud &mdash; and why.",
          "<strong>Part 2 &mdash; the session.</strong> Write a charter: <em>Explore &lt;app&gt; under interruption and poor network to discover state-loss defects.</em>",
          "Time-box it to 45 minutes on a <strong>real phone</strong>. Start a real flow &mdash; a search, a booking, a multi-step form, a checkout.",
          "During the flow, apply the conditions from the lesson: rotate the device &middot; switch to another app and come back &middot; turn on airplane mode mid-request &middot; switch WiFi to mobile data &middot; let the screen lock &middot; deny a permission and retry &middot; tap the submit button twice quickly &middot; use a very large system font.",
          "Record what happens each time: state lost, duplicate submission, frozen screen, silent failure, unreadable layout, unreachable button.",
          "<strong>Part 3 &mdash; report.</strong> Write up your findings as defects with severity, and pick the single worst one to write as a full bug report.",
          "Note which conditions found the most defects &mdash; that is your priority list for next time."],
   deliverable="A five-row device matrix with justification, your session notes, the defect list with severities, and one full bug report.",
   criteria=[["Matrix reasoning","Devices are chosen from real usage considerations, not at random"],["Real device","The session was run on an actual phone, not only an emulator"],["Condition coverage","Interruption, network, orientation and permission conditions were all tried"],["Defects","Real findings with enough detail to reproduce"],["Prioritisation","You can say which conditions were most productive and why"]],
   resources=[["Lesson 13 &mdash; Mobile Testing","../lesson-13.html"],["Lesson 9 &mdash; charters and tours","../lesson-09.html"]]),
]

for h in HW:
    steps = "\n".join("  <li>%s</li>" % s for s in h["steps"])
    crit = "\n".join("  <tr><td><strong>%s</strong></td><td>%s</td></tr>" % (a, b) for a, b in h["criteria"])
    res = ""
    if h["resources"]:
        res = "<h2>Resources</h2>\n<ul>\n" + "\n".join('  <li><a href="%s">%s</a></li>' % (u, t) for t, u in h["resources"]) + "\n</ul>"
    body = """<h1>Homework %d &mdash; %s</h1>
<div class="meta"><span>%s</span><span>Lesson %d</span><span>Submit: %s</span></div>

<h2>Objective</h2>
<p>%s</p>

<h2>Task</h2>
<ol>
%s
</ol>

<h2>Deliverable</h2>
<div class="box g">%s</div>

<h2>Assessment criteria</h2>
<table>
  <tr><th>Criterion</th><th>What we look for</th></tr>
%s
</table>

%s
""" % (h["n"], h["title"], h["type"], h["lesson"], h["submit"], h["objective"], steps, h["deliverable"], crit, res)
    crumb = '<a href="../index.html">Course</a> &rsaquo; <a href="index.html">Homework</a> &rsaquo; Homework %d' % h["n"]
    open(os.path.join(OUT, "homework", "hw-%02d.html" % h["n"]), "w").write(
        page("Homework %d &ndash; %s" % (h["n"], h["title"]), body, crumb))

cards = "\n".join("""  <a href="hw-%02d.html" class="hwcard">
    <div class="n">Homework %d &middot; Lesson %d</div>
    <div class="t">%s</div>
    <div class="d">%s</div>
  </a>""" % (h["n"], h["n"], h["lesson"], h["title"], h["short"]) for h in HW)
rows = "\n".join("  <tr><td>%d</td><td><a href=\"hw-%02d.html\">%s</a></td><td>%s</td><td>%s</td></tr>" % (h["lesson"], h["n"], h["title"], h["type"], h["submit"]) for h in HW)
body = """<h1>Homework</h1>
<div class="meta">12 assignments &middot; group work, pair work and individual exercises</div>
<p>Each assignment has a full brief with the task, what to hand in and how it is assessed. The group project runs through the whole course: requirements (Lesson 4) &rarr; architecture (Lesson 5) &rarr; test cases (Lesson 10) all land in the same SRS document. Lesson 1 has no homework &mdash; just something to think about.</p>

<h2>Course materials used by the assignments</h2>
<ul>
  <li>Testing process worksheet &mdash; Homework 2: <a href="../materials/testing-process-worksheet.docx">Word version</a> or <a href="testing-process-worksheet.html">fill in on the page</a></li>
  <li><a href="../materials/Software Requirements Specification (SRS) Document Template.docx">SRS document template</a> &mdash; Homework 3 and 9</li>
  <li><a href="../materials/input-form-example.html">Trip planner form</a> &mdash; Homework 6</li>
  <li><a href="../materials/shop-database.sql">shop-database.sql</a> &mdash; Homework 10</li>
</ul>

<h2>Overview</h2>
<table>
  <tr><th>Lesson</th><th>Assignment</th><th>Format</th><th>Where to submit</th></tr>
%s
</table>

<h2>All assignments</h2>
<div class="grid">
%s
</div>
""" % (rows, cards)
open(os.path.join(OUT, "homework", "index.html"), "w").write(
    page("Homework &ndash; Software Testing Fundamentals", body, '<a href="../index.html">Course</a> &rsaquo; Homework'))
print("wrote %d homework pages + index" % len(HW))
