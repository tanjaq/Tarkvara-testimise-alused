# -*- coding: utf-8 -*-
from tpl import *

# ---------------- LESSON 6 ----------------
write_lesson(6,
 "Test Techniques I &mdash; Static Testing",
 "Reviews &middot; Walkthroughs &middot; Inspections &middot; Static code analysis &middot; PR review etiquette",
 "Finding defects without running a single line of code",
 ["Where static testing sits among the techniques",
  "Reviews, walkthroughs and inspections",
  "Static code analysis and the tools that do it",
  "How to review a pull request without starting a war",
  "In-class peer review of a real repository"],
 "Peer review the Rental-Car repository and write up every defect and inconsistency you find.",
[
"""<section>
  <span class="lbl">Topic 1</span>
  <h3>The Map of Testing Techniques</h3>
  """ + img("testing-taxonomy.png", "Testing split into dynamic and static; dynamic into functional and non-functional", "54%",
            "Static testing is one of the two families &mdash; and the one that runs first") + """
  <p style="font-size:.6em">Static testing examines the work product <strong>without executing it</strong>. Dynamic testing runs the software. Neither replaces the other.</p>
</section>""",

"""<section>
  <span class="lbl">Topic 1</span>
  <h3>Which Defect Is Easier to Fix?</h3>
  <div class="g2">
    <div class="card g"><strong>A typo in the documentation, before development starts</strong>One person, five minutes, no deployment.</div>
    <div class="card r"><strong>A broken SQL query, in production</strong>Incident, rollback, data repair, customer trust.</div>
  </div>
  <p style="font-size:.64em;margin-top:.5em">Static testing catches the first kind. It is the cheapest quality activity available &mdash; and the most often skipped.</p>
  <div class="g2" style="margin-top:.4em">
    <div class="card"><strong>Manual techniques</strong>&middot; Reviews<br>&middot; Peer reviews<br>&middot; Walkthroughs<br>&middot; Inspections</div>
    <div class="card o"><strong>Tool supported</strong>Static code analysis &mdash; automated scanning of source code for vulnerabilities and standard violations</div>
  </div>
</section>""",

"""<section>
  <span class="lbl">Topic 2</span>
  <h3>Peer Review</h3>
  <div class="card" style="margin-bottom:8px"><strong>What it is</strong>An informal technique where colleagues review each other's work. Focused on finding defects and improving quality.</div>
  <div class="card g"><strong>Example</strong>Mari reviews the test cases Jaan wrote. She notices that several tests have no "expected result" field and suggests fixing them before the CI pipeline runs.</div>
  <p style="font-size:.6em;margin-top:.5em">Informal does not mean careless &mdash; it means no moderator and no formal defect log. It is the most common form of static testing you will do in a real team.</p>
</section>""",

"""<section>
  <span class="lbl">Topic 2</span>
  <h3>Walkthroughs and Inspections</h3>
  <div class="g2">
    <div class="card o"><strong>Walkthrough</strong>A semi-formal session led by the author of the document. Participants ask questions and give feedback. Goal: shared understanding of the content.<br><span style="color:#888">Example: the author presents a new REST API design. A reviewer asks, "what happens if the client sends an empty request?"</span></div>
    <div class="card r"><strong>Inspection</strong>A formal, systematic review of documents by a team, led by a moderator. Defects are logged and reviewed for resolution.<br><span style="color:#888">Example: a code inspection meeting where a module is checked against the design document. Participants: developer, tester, moderator (architect or tech lead).</span></div>
  </div>
</section>""",

"""<section>
  <span class="lbl">Topic 2</span>
  <h3>Peer Review in Practice &mdash; a Requirements Document</h3>
  <p style="font-size:.62em"><strong>Objective:</strong> ensure the requirements are clear, complete and consistent.<br><strong>Participants:</strong> business analyst, project manager, developer, tester.</p>
  <div class="chain">
    <div class="node">Preparation<br><span style="font-size:.85em;color:#888">reviewers study the document individually</span></div><span class="arr">&rarr;</span>
    <div class="node">Meeting<br><span style="font-size:.85em;color:#888">discuss ambiguities and inconsistencies</span></div><span class="arr">&rarr;</span>
    <div class="node">Feedback<br><span style="font-size:.85em;color:#888">constructive, with suggestions</span></div><span class="arr">&rarr;</span>
    <div class="node">Follow-up<br><span style="font-size:.85em;color:#888">author revises</span></div>
  </div>
  <p style="font-size:.6em;margin-top:.4em"><strong>Outcome:</strong> clearer requirements, and far fewer defects in the phases that follow.</p>
</section>""",

"""<section>
  <span class="lbl">Topic 3</span>
  <h3>Static Code Analysis</h3>
  <p style="font-size:.62em">Analysing source code without running the program &mdash; checking standards, syntax and possible vulnerabilities. Mostly automated.</p>
  <div class="g3">
    <div class="card"><strong>Lint / ESLint</strong>Finds likely errors and code-style problems</div>
    <div class="card g"><strong>SonarQube / SonarLint</strong>Continuous code-quality review through static analysis</div>
    <div class="card o"><strong>Checkstyle</strong>Checks conformance to coding standards</div>
  </div>
  <p style="font-size:.6em;margin-top:.4em">Example: a developer runs SonarQube on a new module. The tool flags several potential security vulnerabilities and standard violations that must be fixed before the next stage.</p>
</section>""",

"""<section>
  <span class="lbl">Topic 3</span>
  <h3>What the Tool Actually Changes</h3>
  <div class="g2">
    <div>
      <p style="font-size:.6em;color:var(--red)">Before</p>
      <pre><code class="language-python">def calc_price(base, discount):
    finalPrice = base-discount
    print ("Price is: " + finalPrice)
    return finalPrice</code></pre>
    </div>
    <div>
      <p style="font-size:.6em;color:var(--green)">After</p>
      <pre><code class="language-python">def calculate_price(base: float, discount: float) -> float:
    final_price = base - discount
    print(f"Price is: {final_price}")
    return final_price</code></pre>
    </div>
  </div>
  <p style="font-size:.58em;margin-top:.4em">The analyser caught a real defect here, not just style: concatenating a float to a string raises a TypeError at runtime.</p>
</section>""",

"""<section>
  <span class="lbl">Topic 4</span>
  <h3>Review Size Decides Review Quality</h3>
  """ + img("code-review-tweet.png", "Ask a programmer to review 10 lines of code, he'll find 10 issues. Ask him to do 500 lines and he'll say it looks good.", "58%") + """
  <p style="font-size:.6em">This is the single most useful thing to know about reviews. If you want real feedback, send small changes.</p>
</section>""",

"""<section>
  <span class="lbl">Topic 4</span>
  <h3>Reviewing a Pull Request Without Starting a War</h3>
  <div class="g2">
    <div class="card g"><strong>Do</strong>
      &middot; Comment on the code, never the person<br>
      &middot; Ask questions when you are unsure: "what happens if this is null?"<br>
      &middot; Say what is good, not only what is wrong<br>
      &middot; Separate blocking issues from suggestions<br>
      &middot; Give a concrete alternative, not just "this is bad"
    </div>
    <div class="card r"><strong>Don't</strong>
      &middot; "You broke X" &mdash; write "X breaks when..."<br>
      &middot; Argue style that a linter should decide<br>
      &middot; Approve without reading because you trust the author<br>
      &middot; Bury a critical defect in fifteen nitpicks<br>
      &middot; Review 500 lines in one sitting &mdash; see the previous slide
    </div>
  </div>
  <blockquote>A review comment is a defect report with a smaller audience. The same rules apply: specific, reproducible, and about the work.</blockquote>
</section>""",

"""<section>
  <span class="lbl">In-Class Exercise</span>
  <div class="teams">
    <h3>Peer Review &mdash; Rental Car</h3>
    <p style="font-size:.64em"><strong>Goal:</strong> review the given code and documentation and identify every defect, problem or concern that needs fixing.</p>
    <p style="font-size:.66em"><strong>1) Read the documentation (README):</strong></p>
    <ul style="font-size:.64em"><li>Does it clearly describe what the application must do?</li><li>Are all requirements understandable and precise enough?</li></ul>
    <p style="font-size:.66em"><strong>2) Review the code:</strong></p>
    <ul style="font-size:.64em"><li>Is the code logical and easy to read?</li><li>Are function and variable names clear?</li><li>Does the code match the documented requirements?</li><li>Is any described function missing or implemented incorrectly?</li></ul>
    <p style="font-size:.6em">Repository: <a href="https://github.com/tanjaq/Rental-Car/tree/peer-review" style="color:#9b9fe3">tanjaq/Rental-Car &middot; peer-review branch</a></p>
  </div>
</section>""",

"""<section>
  <span class="lbl">Self-Check</span>
  <h3>Can You Answer These?</h3>
  <ul style="font-size:.68em">
    <li>What is the difference between a walkthrough and an inspection? Who leads each?</li>
    <li>Name two defects a static analysis tool can find and one it never will.</li>
    <li>Rewrite this review comment so it is usable: "this function is a mess".</li>
    <li>Why is static testing usually cheaper than dynamic testing?</li>
  </ul>
</section>""",

"""<section>
  <div class="hw">
    <h3>Homework 5 &mdash; Peer Review</h3>
    <p style="font-size:.68em">Write up every mismatch you found between the code and the documentation in the Rental-Car peer-review branch, and rank them by how serious they are.</p>
    <p style="font-size:.62em">Full brief: <a href="homework/hw-05.html">Homework 5</a></p>
  </div>
</section>""",
])

# ---------------- LESSON 7 ----------------
write_lesson(7,
 "Test Techniques II &mdash; Black Box",
 "Dynamic testing &middot; EP &middot; BVA &middot; Decision tables &middot; State transition &middot; Use cases",
 "Choosing the smallest set of tests that finds the most defects",
 ["Dynamic testing: black box vs white box",
  "Testing types and what drives them",
  "Equivalence partitioning and boundary value analysis",
  "Decision tables",
  "State transition and use-case testing"],
 "Decision table for the photo-ordering discounts.",
[
"""<section>
  <span class="lbl">Topic 1</span>
  <h3>Dynamic Testing</h3>
  <p style="font-size:.63em">Testing by actually executing the functionality: give the system inputs, evaluate the outputs.</p>
  <div class="g2">
    <div class="figure" style="margin:0"><img src="images/black-box.png" alt="Black box testing: input goes in, output comes out" style="max-height:230px"><div class="cap">Black box &mdash; input and output only</div></div>
    <div class="figure" style="margin:0"><img src="images/white-box.png" alt="White box testing approach through application code" style="max-height:230px"><div class="cap">White box &mdash; through the code itself</div></div>
  </div>
  <div class="g2" style="margin-top:.4em">
    <div class="card g"><strong>Black box (specification)</strong>Requirements based. Ignores internal workings. Measured by <em>test coverage</em>.<br><span style="color:#888">This lesson</span></div>
    <div class="card p"><strong>White box (structural)</strong>Tests the specific code. Used for unit and integration testing. Measured by <em>code coverage</em>.<br><span style="color:#888">Lesson 8</span></div>
  </div>
</section>""",

"""<section>
  <span class="lbl">Topic 2</span>
  <h3>Testing Types</h3>
  <p style="font-size:.62em">A test type is testing focused on a specific test objective. The objective might be to:</p>
  <ul style="font-size:.66em">
    <li>Validate non-functional characteristics, such as performance</li>
    <li>Review the structure or architecture of the product</li>
    <li>Validate that a defect has been fixed &mdash; <strong>re-testing</strong></li>
    <li>Check that recent changes broke nothing &mdash; <strong>regression testing</strong></li>
  </ul>
  <div class="g2" style="margin-top:.4em">
    <div class="card"><strong>Requirement-based functional testing</strong>Driven by requirement priority and risk analysis. The most critical functionality gets tested first.</div>
    <div class="card g"><strong>Business-process-based functional testing</strong>Driven by everyday use cases. The basis is knowledge of how the business actually works.</div>
  </div>
</section>""",

"""<section>
  <span class="lbl">Topic 3</span>
  <h3>Equivalence Partitioning</h3>
  <p style="font-size:.63em">Divide input data into groups (partitions) whose members should be handled identically. Test one value from each partition instead of all of them.</p>
  <div class="card o" style="margin-bottom:8px"><strong>Example: an age field accepting 18&ndash;65</strong>&middot; Invalid low: &lt;18<br>&middot; Valid: 18&ndash;65<br>&middot; Invalid high: &gt;65<br>&middot; Invalid type: letters, symbols, empty<br>
    Four tests instead of forty-eight &mdash; one per partition.</div>
  <blockquote>The technique only works if the partitions are drawn correctly. If two values in "your" partition are actually processed differently, the partition was wrong, not the technique.</blockquote>
</section>""",

"""<section>
  <span class="lbl">Topic 3</span>
  <h3>Boundary Value Analysis</h3>
  <p style="font-size:.63em">Most defects live at the edges of a partition. Test the values on the boundary and immediately around it.</p>
  <div class="card r" style="margin-bottom:8px"><strong>Same age field, 18&ndash;65</strong>
    Test: 17, 18, 19 &nbsp;&middot;&nbsp; 64, 65, 66<br>
    This is exactly the "age &ge; 18 written as age &gt; 18" defect from Lesson 9 &mdash; a one-character mistake that equivalence partitioning alone would miss.</div>
  <p style="font-size:.6em">Boundaries are not only numbers: first and last item in a list, empty and maximum-length strings, the first and last day of a month, midnight, the year boundary.</p>
</section>""",

"""<section>
  <span class="lbl">In-Class Exercise</span>
  <div class="teams">
    <h3>EP and BVA on a Live Form</h3>
    <p style="font-size:.66em">Open the <a href="materials/input-form-example.html" style="color:#9b9fe3">trip planner form</a> &mdash; the same one from Lesson 3, now as a target.</p>
    <ul style="font-size:.68em">
      <li>Define the equivalence partitions for <strong>number of travellers</strong> (1&ndash;8), <strong>budget</strong> (100&ndash;10000), <strong>email</strong> and <strong>promo code</strong> (4&ndash;10 characters).</li>
      <li>Write down the boundary values for each field.</li>
      <li>Run them. Note every case where the form's behaviour does not match its own stated rules.</li>
      <li>There are several real defects in there. How many did your partitions find, and which did only the boundaries catch?</li>
    </ul>
  </div>
</section>""",

"""<section>
  <span class="lbl">Topic 4</span>
  <h3>Decision Tables</h3>
  <p style="font-size:.62em">When several conditions combine to produce a result, a decision table shows every combination. Also called a cause-effect table.</p>
  <div class="g2" style="align-items:center">
    <div>
      <table>
        <tr><th>Condition</th><th>T1</th><th>T2</th><th>T3</th><th>T4</th></tr>
        <tr><td>Email</td><td>Valid</td><td>Valid</td><td>Invalid</td><td>Invalid</td></tr>
        <tr><td>Password</td><td>Valid</td><td>Invalid</td><td>Valid</td><td>Invalid</td></tr>
        <tr><td><strong>Output</strong></td><td>Login</td><td>Error</td><td>Error</td><td>Error</td></tr>
      </table>
    </div>
    <div class="figure" style="margin:0"><img src="images/login-form.png" alt="Login form with email and password" style="max-height:210px"></div>
  </div>
  <p style="font-size:.6em;margin-top:.4em">Two conditions give 2&sup2; = 4 combinations. Three give 8. The table makes the combination you forgot painfully visible.</p>
</section>""",

"""<section>
  <span class="lbl">Topic 5</span>
  <h3>State Transition Testing</h3>
  """ + img("state-diagram-pin.png", "State diagram for PIN entry with three attempts before the card is eaten", "58%",
            "PIN entry: the same input produces a different outcome depending on the state") + """
  <p style="font-size:.6em">A system behaves differently depending on its current state, and the state depends on what came before. Test the valid transitions first, then the invalid ones: what happens if a blocked account submits the <em>correct</em> password?</p>
</section>""",

"""<section>
  <span class="lbl">Topic 5</span>
  <h3>Use-Case Testing</h3>
  <p style="font-size:.62em">Test the scenarios a real user will actually run. Use cases have a main flow and alternative flows.</p>
  <table>
    <tr><th>Scenario</th><th>Steps</th><th>Result</th></tr>
    <tr><td>Valid login</td><td>User enters email and password</td><td>System validates input and logs the user in</td></tr>
    <tr><td>Invalid password</td><td>User enters email and wrong password</td><td>System shows an error message</td></tr>
    <tr><td>Blocked account</td><td>User enters wrong password three times</td><td>System shows an account-blocked error</td></tr>
  </table>
  <p style="font-size:.58em;margin-top:.4em">Specification-based techniques in one list: equivalence partitioning &middot; boundary value analysis &middot; decision tables &middot; state transition &middot; use-case testing. Experience-based testing &mdash; exploratory &mdash; comes in Lesson 9.</p>
</section>""",

"""<section>
  <span class="lbl">In-Class Exercise</span>
  <div class="teams">
    <h3>Decision Table &mdash; Photo Ordering</h3>
    <p style="font-size:.66em">A photo-printing site has the following business rules:</p>
    <ul style="font-size:.66em">
      <li>An unregistered regular user has no permanent discount.</li>
      <li>A registered user gets 5% off every purchase.</li>
      <li>Additional discounts:
        <ul style="font-size:.95em"><li>Ordering more than 10 photos adds 3%.</li><li>Ordering photo frames as well adds 3%.</li></ul>
      </li>
      <li>On a registered user's birthday, the usual 5% is replaced by 8%.</li>
    </ul>
    <p style="font-size:.66em">Build the decision table showing every combination of the business rules and the discount that applies to the user.</p>
  </div>
</section>""",

"""<section>
  <span class="lbl">Self-Check</span>
  <h3>Can You Answer These?</h3>
  <ul style="font-size:.68em">
    <li>A password field accepts 8&ndash;20 characters. List the EP partitions and the BVA values.</li>
    <li>Three independent conditions &mdash; how many rows does the full decision table have?</li>
    <li>Give an example where state transition testing finds a defect that EP and BVA cannot.</li>
    <li>When would you use business-process-based testing instead of requirement-based?</li>
  </ul>
</section>""",

"""<section>
  <div class="hw">
    <h3>Homework 6 &mdash; Decision Table</h3>
    <p style="font-size:.68em">Produce the complete decision table for the photo-ordering discount rules, mark the combinations you would test first and note any rule that is ambiguous as written.</p>
    <p style="font-size:.62em">Full brief: <a href="homework/hw-06.html">Homework 6</a></p>
  </div>
</section>""",
])

# ---------------- LESSON 8 ----------------
L08_CSS = """
.reveal pre{font-size:.52em;}
.cfg{width:100%;max-height:400px;}
.cfg text{font-family:'Segoe UI',system-ui,sans-serif;fill:#ddd;font-size:15px;}
.cfg .lab{font-size:13px;font-weight:700;}
.verdict{display:inline-block;font-weight:700;padding:1px 8px;border-radius:10px;font-size:.9em;}
.v-pass{background:rgba(129,199,132,.2);color:var(--green);}
.v-fail{background:rgba(227,115,115,.2);color:var(--red);}
.term{background:#1b1b1b;border:1px solid #333;border-radius:6px;padding:10px 14px;font-family:Consolas,Menlo,monospace;font-size:.42em;text-align:left;line-height:1.5;color:#ccc;white-space:pre;overflow-x:auto;}
.term .hl{color:var(--orange);font-weight:700;}
.term .ok{color:var(--green);}
.lbl.further{color:var(--orange);}
.reveal td.t{color:var(--green);} .reveal td.f{color:var(--red);}
"""

ARROW = '<defs><marker id="%s" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#888"/></marker></defs>'

def box(x, y, w, label):
    return ('<rect x="%d" y="%d" width="%d" height="32" rx="5" fill="rgba(79,195,247,.12)" stroke="#4fc3f7"/>'
            '<text x="180" y="%d" text-anchor="middle">%s</text>') % (x, y, w, y + 21, label)

def diamond(cy, label):
    return ('<polygon points="180,%d 262,%d 180,%d 98,%d" fill="rgba(255,183,77,.12)" stroke="#ffb74d"/>'
            '<text x="180" y="%d" text-anchor="middle">%s</text>') % (cy - 30, cy, cy + 30, cy, cy + 5, label)

def line(y1, y2, m, color="#888"):
    return '<line x1="180" y1="%d" x2="180" y2="%d" stroke="%s" stroke-width="2" marker-end="url(#%s)"/>' % (y1, y2, color, m)

def false_edge(cy, merge_y, m):
    return ('<polyline points="262,%d 325,%d 325,%d 186,%d" fill="none" stroke="#e57373" stroke-width="2" marker-end="url(#%s)"/>'
            '<text class="lab" x="276" y="%d" style="fill:#e57373">F</text>') % (cy, cy, merge_y, merge_y, m, cy - 8)

def true_label(y):
    return '<text class="lab" x="158" y="%d" style="fill:#81c784">T</text>' % y

CFG_FINAL = ('<svg class="cfg" viewBox="0 0 360 300" role="img" aria-label="Control flow graph of finalPrice">'
  + ARROW % "m1" + box(110, 4, 140, "let discount") + line(36, 58, "m1")
  + diamond(90, "isMember?") + line(120, 146, "m1", "#81c784") + true_label(139)
  + box(105, 148, 150, "discount = 0.1") + false_edge(90, 206, "m1")
  + line(180, 236, "m1") + box(60, 238, 240, "return price &minus; price &times; discount")
  + '</svg>')

CFG_DELIVERY = ('<svg class="cfg" viewBox="0 0 360 440" role="img" aria-label="Control flow graph of deliveryFee with four paths">'
  + ARROW % "m2" + box(115, 4, 130, "let fee = 5") + line(36, 58, "m2")
  + diamond(90, "isExpress?") + line(120, 146, "m2", "#81c784") + true_label(139)
  + box(120, 148, 120, "fee = 12") + false_edge(90, 206, "m2")
  + line(180, 226, "m2") + diamond(258, "total &ge; 50?")
  + line(288, 314, "m2", "#81c784") + true_label(307)
  + box(125, 316, 110, "fee = 0") + false_edge(258, 374, "m2")
  + line(348, 394, "m2") + box(120, 396, 120, "return fee")
  + '</svg>')

PASS = '<span class="verdict v-pass">PASS</span>'
FAIL = '<span class="verdict v-fail">FAIL</span>'

write_lesson(8,
 "Test Techniques III &mdash; White Box",
 "Function, statement and branch coverage &middot; Bugs that hide behind green coverage &middot; What coverage does and does not prove",
 "Testing the code itself &mdash; and reading a coverage report honestly",
 ["Black box vs white box, revisited",
  "Code coverage: function, statement, branch",
  "Reading code as a graph",
  "Worked examples &mdash; bugs hiding behind green coverage",
  "Going further: compound conditions, paths, complexity",
  "Live demo: a coverage report in Jest",
  "Why 100% coverage does not mean 100% tested"],
 "Boarding pass exercise &mdash; work out statement and branch coverage for two given test cases and add what is missing.",
[
"""<section>
  <span class="lbl">Topic 1</span>
  <h3>Two Kinds of Coverage</h3>
  """ + img("white-box.png", "White box testing approach: test case input through application code to output", "56%") + """
  <div class="g2">
    <div class="card g"><strong>Black box &rarr; test coverage</strong>How much of the <em>requirements</em> is covered. Did we test everything we promised to build?</div>
    <div class="card p"><strong>White box &rarr; code coverage</strong>How much of the <em>code</em> is executed. Did any test ever run this line?</div>
  </div>
  <p style="font-size:.56em;margin-top:.3em">Both numbers can be high while the product is still broken &mdash; and one being high tells you nothing about the other.</p>
</section>""",

"""<section>
  <span class="lbl">Topic 2</span>
  <h3>Three Levels of Code Coverage</h3>
  <div class="g3">
    <div class="card"><strong>Function coverage</strong>Was every function in the application called at least once?</div>
    <div class="card g"><strong>Statement coverage</strong>Was every line of code executed at least once?</div>
    <div class="card o"><strong>Branch coverage</strong>Was every branch &mdash; every true <em>and</em> false path &mdash; taken?</div>
  </div>
  <p style="font-size:.6em;margin-top:.5em">Each level is stricter than the one before it. 100% branch coverage implies 100% statement coverage; the reverse is not true.</p>
</section>""",

"""<section>
  <span class="lbl">Topic 3</span>
  <h3>Reading Code as a Graph</h3>
  <div class="g2" style="align-items:center">
    <div>
      <p style="font-size:.5em;color:#aaa;margin:0 0 .3em">Requirement: members get 10% off. Non-members pay the full price.</p>
      <pre><code class="language-javascript">function finalPrice(price, isMember) {
  let discount;
  if (isMember) {
    discount = 0.1;
  }
  return price - price * discount;
}</code></pre>
      <div class="card o" style="margin-top:.5em;font-size:.5em"><strong>Control flow graph</strong>Boxes = statements &middot; diamonds = decisions &middot; arrows = possible flow. Statement coverage visits every <em>box</em>; branch coverage walks every <em>arrow</em> out of a diamond.</div>
    </div>
    """ + CFG_FINAL + """
  </div>
</section>""",

"""<section>
  <span class="lbl">Topic 4</span>
  <h3>Example 1 &mdash; a Conditional</h3>
  <pre><code class="language-javascript">function calc(a, b) {
  let c = 0;
  if (a > b) {
    c = a;
  }
  return c;
}</code></pre>
  <div class="g3">
    <div class="card"><strong>Function coverage</strong>calc(1, 1)<br>The function ran &mdash; 100%.</div>
    <div class="card g"><strong>Statement coverage</strong>calc(2, 1)<br>Every line executed, including c = a.</div>
    <div class="card o"><strong>Branch coverage</strong>calc(2, 1) and calc(1, 3)<br>Both the true and the false path of the if.</div>
  </div>
  <p style="font-size:.58em;margin-top:.4em">Note that calc(1, 1) gives 100% function coverage while never executing the body of the if. This is why the metric you quote matters.</p>
</section>""",

"""<section>
  <span class="lbl">Topic 4</span>
  <h3>Example 2 &mdash; a Loop</h3>
  <pre><code class="language-javascript">function loop(a) {
  let c = 0;
  for (let i = 0; i &lt; a; i++) {
    c = c + 1;
  }
  return c;
}</code></pre>
  <div class="g2">
    <div class="card"><strong>Coverage</strong>&middot; Function: loop(1)<br>&middot; Statement: loop(1)<br>&middot; Branch: loop(2) and loop(0) &mdash; the loop body must both run and not run.</div>
    <div class="card r"><strong>Tests coverage will never suggest</strong>&middot; loop(-5)<br>&middot; loop(null)<br>&middot; loop("abs")<br>&middot; loop(300000000000)<br>These come from black-box thinking, not from the coverage report.</div>
  </div>
</section>""",

"""<section>
  <span class="lbl">Topic 4</span>
  <h3>Example 3 &mdash; 100% Statements, Still a Bug</h3>
  <div class="g2" style="align-items:start">
    <div>
      <p style="font-size:.5em;color:#aaa;margin:0 0 .3em">The <code>finalPrice</code> function from the graph, with one test:</p>
      <pre><code class="language-javascript">test('member gets 10% off', () => {
  expect(finalPrice(100, true)).toBe(90);
});</code></pre>
    </div>
    <div class="card g"><strong>Statement coverage: 100%</strong><code>let discount</code> &check;<br><code>if (isMember)</code> &check;<br><code>discount = 0.1</code> &check;<br><code>return &hellip;</code> &check;<br><br>Every line ran. Green. Ship it?</div>
  </div>
  <div class="card o" style="margin-top:.5em"><strong>Branch coverage: 50%</strong>The FALSE arrow out of <code>isMember?</code> was never walked. Branch coverage forces a second test: <code>finalPrice(100, false)</code>, expected 100.</div>
  <div class="card r fragment" style="margin-top:.5em"><strong>Actual result: NaN</strong>For non-members <code>discount</code> stays <code>undefined</code>. The bug lives on the arrow you can't see in the code &mdash; the missing <code>else</code>.</div>
</section>""",

"""<section>
  <span class="lbl">Topic 4</span>
  <h3>Example 4 &mdash; The Loop That Runs Zero Times</h3>
  <div class="g2" style="align-items:start">
    <div>
      <p style="font-size:.5em;color:#aaa;margin:0 0 .3em">Show the average star rating. A product with no ratings shows 0.</p>
      <pre><code class="language-javascript">function averageRating(ratings) {
  let sum = 0;
  for (const r of ratings) {
    sum += r;
  }
  return sum / ratings.length;
}</code></pre>
    </div>
    <div class="card o"><strong>Test every loop with</strong><span style="color:var(--red);font-weight:700">0</span> iterations &mdash; loop skipped entirely<br><span style="color:var(--orange);font-weight:700">1</span> iteration<br><span style="color:var(--green);font-weight:700">many</span> iterations<br><span style="color:var(--purple);font-weight:700">max</span> &mdash; if there is a limit<br><br>Sound familiar? It's boundary value analysis, applied to a loop.</div>
  </div>
  <table style="margin-top:.5em;width:100%">
    <tr><th>Iterations</th><th>Input</th><th>Expected</th><th>Actual</th><th>Result</th></tr>
    <tr><td>1</td><td>[3]</td><td>3</td><td>3</td><td>""" + PASS + """</td></tr>
    <tr><td>many</td><td>[4, 5, 3]</td><td>4</td><td>4</td><td>""" + PASS + """</td></tr>
    <tr class="fragment"><td>0</td><td>[ ]</td><td>0</td><td>NaN (0 &divide; 0)</td><td>""" + FAIL + """</td></tr>
  </table>
</section>""",

"""<section>
  <span class="lbl">Topic 4</span>
  <h3>Example 5 &mdash; Two Decisions, Four Paths</h3>
  <div class="g2" style="align-items:center">
    <div>
      <p style="font-size:.48em;color:#aaa;margin:0 0 .3em">Standard delivery 5 &euro;. Orders of 50 &euro; or more get free standard delivery. Express delivery <strong>always</strong> costs 12 &euro;.</p>
      <pre><code class="language-javascript">function deliveryFee(total, isExpress) {
  let fee = 5;
  if (isExpress) {
    fee = 12;
  }
  if (total >= 50) {
    fee = 0;
  }
  return fee;
}</code></pre>
      <p style="font-size:.5em;margin-top:.3em">Two decisions in a row &rarr; 2 &times; 2 = <strong>4 paths</strong> through the graph. Branch coverage only needs 2 of them.</p>
    </div>
    """ + CFG_DELIVERY + """
  </div>
</section>""",

"""<section>
  <span class="lbl">Topic 4</span>
  <h3>100% Branch Coverage &mdash; and Still a Bug</h3>
  <table style="width:100%">
    <tr><th>Path</th><th>Input</th><th>isExpress</th><th>total &ge; 50</th><th>Expected</th><th>Actual</th><th>Result</th></tr>
    <tr><td>A</td><td>(20, true)</td><td class="t">T</td><td class="f">F</td><td>12</td><td>12</td><td>""" + PASS + """</td></tr>
    <tr><td>B</td><td>(60, false)</td><td class="f">F</td><td class="t">T</td><td>0</td><td>0</td><td>""" + PASS + """</td></tr>
    <tr class="fragment"><td>C</td><td>(20, false)</td><td class="f">F</td><td class="f">F</td><td>5</td><td>5</td><td>""" + PASS + """</td></tr>
    <tr class="fragment"><td>D</td><td>(60, true)</td><td class="t">T</td><td class="t">T</td><td>12</td><td>0</td><td>""" + FAIL + """</td></tr>
  </table>
  <div class="g2" style="margin-top:.6em">
    <div class="card o"><strong>A + B = 100% branch coverage</strong>Each <code>if</code> was TRUE once and FALSE once. The coverage report is fully green.</div>
    <div class="card r"><strong>Path D: free delivery wipes out express</strong>The second <code>if</code> overwrites the first. Bugs love the <em>combination</em> of decisions &mdash; that's what <em>path coverage</em> targets.</div>
  </div>
</section>""",

"""<section>
  <span class="lbl further">Topic 5 &middot; Going further</span>
  <h3>Compound Conditions &mdash; the One-Character Bug</h3>
  <p style="font-size:.52em;margin:0 0 .3em">Requirement: you can rent a car if you are at least 21 <strong>and</strong> have a licence. The developer typed <code>||</code> instead of <code>&amp;&amp;</code>:</p>
  <pre><code class="language-javascript">if (age >= 21 || hasLicense) {   // should be &amp;&amp;
  return true;
}
return false;</code></pre>
  <table style="width:100%;margin-top:.3em">
    <tr><th>Test</th><th>Expected (&amp;&amp;)</th><th>Actual (||)</th><th>Branch-coverage tests</th><th>Each-condition tests</th></tr>
    <tr><td>(25, true)</td><td>true</td><td>true</td><td>""" + PASS + """</td><td>""" + PASS + """</td></tr>
    <tr><td>(18, false)</td><td>false</td><td>false</td><td>""" + PASS + """</td><td>&mdash;</td></tr>
    <tr><td>(18, true)</td><td>false</td><td>true</td><td>&mdash;</td><td>""" + FAIL + """</td></tr>
    <tr><td>(25, false)</td><td>false</td><td>true</td><td>&mdash;</td><td>""" + FAIL + """</td></tr>
  </table>
  <p style="font-size:.5em;margin-top:.4em">Two tests give 100% statement and branch coverage &mdash; and miss the bug. Fix: show that <em>each condition on its own</em> can flip the result. This is called <strong>MC/DC</strong> and is required for flight-critical aviation software.</p>
</section>""",

"""<section>
  <span class="lbl further">Topic 5 &middot; Going further</span>
  <h3>How Many Tests? Cyclomatic Complexity</h3>
  <div class="g2" style="align-items:start">
    <div class="card r"><strong>Why not test every path?</strong>2 <code>if</code>s &rarr; 4 paths<br>10 <code>if</code>s &rarr; 1&nbsp;024 paths<br>1 loop &rarr; potentially endless paths<br><br>Full path coverage is only realistic for small, critical functions.</div>
    <div class="card g"><strong>McCabe's rule of thumb</strong><span style="color:var(--green);font-size:1.15em">M = decisions + 1</span><br>Count every <code>if</code>, loop, <code>case</code>, <code>&amp;&amp;</code>, <code>||</code>, <code>?:</code>.<br><br>M = the number of <em>independent</em> paths &mdash; a good minimum number of tests.</div>
  </div>
  <table style="width:100%;margin-top:.6em">
    <tr><th>Function</th><th>Decisions</th><th>M</th><th>All paths</th></tr>
    <tr><td>finalPrice</td><td>1 if</td><td>2</td><td>2</td></tr>
    <tr><td>canRent</td><td>1 if + 1 &amp;&amp;</td><td>3</td><td>3</td></tr>
    <tr><td>deliveryFee</td><td>2 if</td><td>3</td><td>4</td></tr>
  </table>
  <p style="font-size:.5em;color:#aaa;margin-top:.4em">M above ~10 means the function is hard to test &mdash; refactor it. Static analysis (Lesson 6) can enforce this: ESLint <code>"complexity": ["warn", 10]</code>.</p>
</section>""",

"""<section>
  <span class="lbl">Topic 6</span>
  <h3>Live Demo &mdash; a Coverage Report in Jest</h3>
  <div class="g2" style="align-items:start">
    <div>
      <div class="term">$ npm install
$ npm run coverage

File                | % Stmts | % Branch
--------------------|---------|---------
01-finalPrice.js    |     100 |      <span class="hl">50</span>
02-canRent.js       |     100 |     <span class="ok">100</span>
03-deliveryFee.js   |     100 |     <span class="ok">100</span>
04-averageRating.js |     100 |     <span class="ok">100</span>
05-parkingFee.js    |   14.28 |        0

Tests: 1 todo, <span class="ok">7 passed</span></div>
      <p style="font-size:.48em;color:#aaa;margin-top:.4em">Open <code>coverage/index.html</code> &mdash; yellow and red mark code no test ever executed.</p>
    </div>
    <div class="card g"><strong>Demo script &mdash; White-Box-Examples</strong>1. Run coverage. Ask the class: <em>"Ship it?"</em><br>2. Open the HTML report on <code>01-finalPrice</code> &mdash; the missing else is highlighted.<br>3. Uncomment the <strong style="display:inline">STEP 2</strong> tests in each test file.<br>4. Run again &rarr; <span class="fragment"><strong style="display:inline;color:var(--red)">5 failing tests</strong> &mdash; three of the four files had 100% branch coverage.</span></div>
  </div>
</section>""",

"""<section>
  <span class="lbl">Topic 7</span>
  <h3>What Coverage Does Not Tell You</h3>
  <ul style="font-size:.67em">
    <li>100% code coverage does not mean a 100% tested product.</li>
    <li>Coverage only measures the behaviour of the code that <em>exists</em>.</li>
    <li>Missing code &mdash; a requirement nobody implemented &mdash; will never show up in a coverage report.</li>
    <li>A test that executes a line without asserting anything still counts towards coverage.</li>
  </ul>
  <blockquote>Recommendation: black box + white box together give higher test coverage <em>and</em> higher code coverage. Neither replaces the other.</blockquote>
</section>""",

"""<section>
  <span class="lbl">Warm-Up Exercise</span>
  <div class="teams">
    <h3>Parking Fee &mdash; Count Before You Test</h3>
    <div class="g2" style="gap:16px">
      <div>
        <p style="font-size:.5em;color:#aaa;margin:0 0 .3em">2 &euro; per hour; 0 hours costs nothing. Residents who park <strong>more than</strong> 3 hours get 50% off.</p>
        <pre><code class="language-javascript">function parkingFee(hours, isResident) {
  if (hours &lt;= 0) {
    return 0;
  }
  let fee = hours * 2;
  if (isResident &amp;&amp; hours > 3) {
    fee = fee / 2;
  }
  return fee;
}</code></pre>
      </div>
      <ol style="font-size:.85em;line-height:1.7;text-align:left;margin:0;padding-left:1.2em">
        <li>Draw the control flow graph</li>
        <li>Minimum tests for <strong>100% statement</strong> coverage?</li>
        <li>Minimum tests for <strong>100% branch</strong> coverage?</li>
        <li>Which black-box technique adds one more test here?</li>
        <li><span style="color:var(--orange)">Going further:</span> cyclomatic complexity? Which test proves <code>hours &gt; 3</code> matters on its own?</li>
      </ol>
    </div>
  </div>
</section>""",

"""<section>
  <span class="lbl">Warm-Up &middot; Answers</span>
  <h3>Parking Fee &mdash; Answers</h3>
  <table style="width:100%">
    <tr><th>Question</th><th>Answer</th><th>Tests</th></tr>
    <tr class="fragment"><td>100% statement</td><td><strong>2 tests</strong> (Jest: 100% statements, 83% branches)</td><td>(0, false) &rarr; 0 &middot; (5, true) &rarr; 5</td></tr>
    <tr class="fragment"><td>100% branch</td><td><strong>3 tests</strong> &mdash; add the FALSE outcome of the second if</td><td>+ (5, false) &rarr; 10</td></tr>
    <tr class="fragment"><td>Black box: BVA</td><td>"more than 3" &mdash; test the boundary</td><td>+ (3, true) &rarr; 6</td></tr>
    <tr class="fragment"><td>Cyclomatic complexity</td><td>2 if + 1 &amp;&amp; + 1 = <strong>4</strong></td><td>&mdash;</td></tr>
    <tr class="fragment"><td>hours &gt; 3 on its own</td><td>Resident, short stay &mdash; only <code>hours</code> changed vs (5, true)</td><td>+ (2, true) &rarr; 4</td></tr>
  </table>
  <p class="fragment" style="font-size:.52em;margin-top:.6em">After 3 tests Jest already shows <strong>100% branches</strong> &mdash; it cannot see the boundary or the single-condition case. The tool measures; <em>you</em> design.</p>
</section>""",

"""<section>
  <span class="lbl">In-Class Exercise</span>
  <div class="teams">
    <h3>Boarding Pass &mdash; Coverage Analysis</h3>
    <p style="font-size:.66em"><strong>Given test cases:</strong></p>
    <ul style="font-size:.68em">
      <li>Frequent flier is upgraded to Business class.</li>
      <li>Non-frequent flier gets an Economy ticket.</li>
    </ul>
    <p style="font-size:.66em"><strong>Questions:</strong></p>
    <ul style="font-size:.68em">
      <li>How many statements do these two tests cover?</li>
      <li>How many branches do they cover?</li>
      <li>Which tests must you add to reach 100% statement coverage?</li>
    </ul>
    <p style="font-size:.62em">Draw the flow diagram if it helps. Code: <a href="https://onecompiler.com/javascript/3yydc2m52" style="color:#9b9fe3">onecompiler.com/javascript/3yydc2m52</a></p>
  </div>
</section>""",

"""<section>
  <span class="lbl">Self-Check</span>
  <h3>Can You Answer These?</h3>
  <ul style="font-size:.68em">
    <li>Write a test that gives 100% statement coverage but not 100% branch coverage.</li>
    <li>A team reports 92% coverage and zero known bugs. What would you still ask them?</li>
    <li>Which coverage level would you require for a payment calculation, and why?</li>
    <li>Why can a coverage tool never find a missing requirement?</li>
  </ul>
</section>""",

"""<section>
  <div class="hw">
    <h3>Homework 7 &mdash; Boarding Pass Coverage</h3>
    <p style="font-size:.68em">Submit your statement and branch coverage analysis for the boarding pass code, the additional tests needed for 100% statement coverage, and a diagram if you drew one.</p>
    <p style="font-size:.62em">Full brief: <a href="homework/hw-07.html">Homework 7</a></p>
  </div>
</section>""",
], extra_css=L08_CSS)
