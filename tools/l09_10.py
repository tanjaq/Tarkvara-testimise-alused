# -*- coding: utf-8 -*-
from tpl import *

# ---------------- LESSON 9 ----------------
write_lesson(9,
 "Defect Management &amp; Exploratory Testing",
 "Error, defect, failure &middot; Bug reports &middot; Severity vs priority &middot; Lifecycle &middot; RCA &middot; Exploratory testing",
 "Finding defects without a script, and reporting them so they get fixed",
 ["Error, defect, failure &mdash; and why the words matter",
  "Exploratory testing &mdash; charters, tours and heuristics",
  "The fields of a good bug report",
  "Severity vs priority",
  "Bug lifecycle and root cause analysis"],
 "Run an exploratory session, then file a real defect as a GitHub issue in the Bug-Reporting repository.",
[
"""<section>
  <span class="lbl">Topic 1</span>
  <h3>Error, Defect, Failure</h3>
  <div class="g3">
    <div class="card"><strong>Error</strong>A human mistake &mdash; a wrong assumption, a misread requirement.<br><span style="color:#888">The developer read "age &ge; 18" as "age &gt; 18".</span></div>
    <div class="card o"><strong>Defect / bug</strong>The flaw in the code or document that results from the error.<br><span style="color:#888">The comparison is written as &gt; instead of &ge;.</span></div>
    <div class="card r"><strong>Failure</strong>The observable wrong behaviour when the defect is triggered.<br><span style="color:#888">An 18-year-old cannot register.</span></div>
  </div>
  <p style="font-size:.62em;margin-top:.5em">A defect is any deviation from the requirements &mdash; the actual result differs from the expected result. It does not have to crash anything.</p>
  <blockquote>Not every error causes a failure. A defect in code that never runs is still a defect &mdash; you only see the failure when that path is triggered. That is why edge cases matter.</blockquote>
</section>""",

"""<section>
  <span class="lbl">Topic 2</span>
  <h3>Exploratory Testing &mdash; What It Actually Is</h3>
  <p style="font-size:.64em">Simultaneous <strong>learning</strong>, <strong>test design</strong> and <strong>test execution</strong>. You design the next test based on what the last one just taught you.</p>
  <div class="g2">
    <div class="card g"><strong>It is</strong>
      &middot; Structured and time-boxed<br>
      &middot; Documented &mdash; notes, screenshots, questions<br>
      &middot; Driven by a stated mission<br>
      &middot; Reviewable: someone can read what you did</div>
    <div class="card r"><strong>It is not</strong>
      &middot; Random clicking<br>
      &middot; "Just have a play with it"<br>
      &middot; An excuse for having no test cases<br>
      &middot; Unrepeatable &mdash; your notes make it repeatable</div>
  </div>
  <p style="font-size:.58em;margin-top:.4em">Scripted testing checks what you already thought of. Exploratory testing finds what nobody thought of &mdash; which is where the interesting defects live.</p>
</section>""",

"""<section>
  <span class="lbl">Topic 2</span>
  <h3>Session-Based Test Management</h3>
  <div class="chain">
    <div class="node">Charter<br><span style="font-size:.85em;color:#888">what am I exploring, and why</span></div><span class="arr">&rarr;</span>
    <div class="node">Time box<br><span style="font-size:.85em;color:#888">45&ndash;90 minutes, uninterrupted</span></div><span class="arr">&rarr;</span>
    <div class="node">Notes<br><span style="font-size:.85em;color:#888">what you did, saw, questioned</span></div><span class="arr">&rarr;</span>
    <div class="node">Debrief<br><span style="font-size:.85em;color:#888">findings, defects, next charter</span></div>
  </div>
  <div class="card" style="margin-top:.6em"><strong>Charter format</strong>
    Explore <em>&lt;target&gt;</em> with <em>&lt;resources&gt;</em> to discover <em>&lt;information&gt;</em>.<br>
    <span style="color:#888">"Explore the checkout flow with an expired discount code to discover how the system handles invalid promotions."</span></div>
  <p style="font-size:.58em;margin-top:.4em">A charter turns an hour of clicking into a testable claim about the product. Without one, you cannot say afterwards what you covered.</p>
</section>""",

"""<section>
  <span class="lbl">Topic 2</span>
  <h3>Tours &mdash; Ways to Walk Through a Product</h3>
  <div class="g3">
    <div class="card"><strong>The guidebook tour</strong>Follow the user manual or the onboarding exactly. Does the documented path still work?</div>
    <div class="card g"><strong>The money tour</strong>Walk the features that make the money &mdash; checkout, subscription, upgrade. These are never allowed to break.</div>
    <div class="card o"><strong>The landmark tour</strong>Pick five key features and move between them in an unusual order.</div>
  </div>
  <div class="g3" style="margin-top:8px">
    <div class="card r"><strong>The back alley tour</strong>Deliberately test the least-used, least-loved features. Nobody has looked there in a year.</div>
    <div class="card p"><strong>The saboteur tour</strong>Actively try to break it: kill the network mid-request, submit twice, hit back, paste 5,000 characters.</div>
    <div class="card"><strong>The couch potato tour</strong>Do as little as possible &mdash; accept every default, submit every form empty, click straight to the end.</div>
  </div>
  <p style="font-size:.55em;color:#888;margin-top:.4em">Touring heuristics popularised by James Whittaker in <em>Exploratory Software Testing</em>.</p>
</section>""",

"""<section>
  <span class="lbl">Topic 2</span>
  <h3>Heuristics &mdash; Where to Point Your Attention</h3>
  <div class="g2">
    <div class="card"><strong>SFDIPOT &mdash; what to cover</strong>
      <strong style="display:inline;color:var(--blue)">S</strong>tructure &middot; <strong style="display:inline;color:var(--blue)">F</strong>unction &middot; <strong style="display:inline;color:var(--blue)">D</strong>ata &middot; <strong style="display:inline;color:var(--blue)">I</strong>nterfaces &middot; <strong style="display:inline;color:var(--blue)">P</strong>latform &middot; <strong style="display:inline;color:var(--blue)">O</strong>perations &middot; <strong style="display:inline;color:var(--blue)">T</strong>ime<br>
      <span style="color:#888">Ask of each: what could go wrong here?</span></div>
    <div class="card g"><strong>CRUD &mdash; for every entity</strong>&middot; Create it<br>&middot; Read it<br>&middot; Update it<br>&middot; Delete it &mdash; then read it again.<br>
      <span style="color:#888">Delete something that is referenced elsewhere. That is where the defects are.</span></div>
  </div>
  <div class="g2" style="margin-top:8px">
    <div class="card o"><strong>Goldilocks</strong>Too big, too small, just right. Zero items, one item, a thousand items. Empty string, one character, maximum length, maximum length + 1.</div>
    <div class="card p"><strong>Oracles &mdash; how do you know it is wrong?</strong>Compare against the requirement, a comparable product, the product's own past behaviour, user expectation, or plain internal consistency &mdash; the same action behaving differently in two screens is a defect even with no spec.</div>
  </div>
</section>""",

"""<section>
  <span class="lbl">Topic 2</span>
  <h3>When to Explore, and What to Write Down</h3>
  <div class="g2">
    <div class="card"><strong>Good moments for a session</strong>
      &middot; A new feature has just landed and there are no test cases yet<br>
      &middot; There is no specification and you need to write one<br>
      &middot; After a fix, to check the neighbourhood<br>
      &middot; Before release, as a time-boxed risk hunt<br>
      &middot; When the scripted suite keeps passing and you do not believe it</div>
    <div class="card g"><strong>Your session notes</strong>
      &middot; The charter and the time box<br>
      &middot; What you covered &mdash; areas, data, configurations<br>
      &middot; Defects found, with evidence<br>
      &middot; Questions and risks raised, for the analyst or product owner<br>
      &middot; What you did <em>not</em> get to &mdash; the next charter</div>
  </div>
  <blockquote>The output of an exploratory session is not just bugs. It is a map of the product and a list of better questions.</blockquote>
</section>""",

"""<section>
  <span class="lbl">Topic 3</span>
  <h3>Who Reads a Bug Report?</h3>
  <div class="g2">
    <div>
      <div class="card" style="margin-bottom:6px"><strong>Developer</strong>Needs exact steps to reproduce and environment details. The more precise, the faster the fix.</div>
      <div class="card g"><strong>Product manager</strong>Needs impact: how many users, which feature, how visible to customers. And an overview of quality level.</div>
    </div>
    <div>
      <div class="card o" style="margin-bottom:6px"><strong>Process manager</strong>Needs root-cause information: what process failure let this reach this stage?</div>
      <div class="card p"><strong>The whole team</strong>Needs clarity and a professional tone. Defects are system failures, not personal ones. Never write "you broke X".</div>
    </div>
  </div>
  <p style="font-size:.6em;margin-top:.4em">Always check for duplicates before filing. The same bug reported five times by five people wastes everyone's day.</p>
</section>""",

"""<section>
  <span class="lbl">Topic 3</span>
  <h3>Bug Report Fields (1/2)</h3>
  <div class="g2">
    <div>
      <div class="card" style="margin-bottom:6px"><strong>Summary / title</strong>A short summary of the defect, ideally naming the affected functionality.<br>Good: "[Search] Price filter shows products below $50 minimum"<br>Bad: "Filter broken" &mdash; unactionable and unsearchable.</div>
      <div class="card g"><strong>Environment</strong>&middot; Which environment (dev, QA, staging, production)<br>&middot; Which user role<br>&middot; Device and OS<br>&middot; Browser and version</div>
    </div>
    <div>
      <div class="card o" style="margin-bottom:6px"><strong>Severity</strong>How badly does this break the system?<br>&middot; Critical<br>&middot; Major<br>&middot; Minor<br>&middot; Trivial</div>
      <div class="card r"><strong>Priority</strong>How urgent is the fix?<br>&middot; P0 &mdash; core functionality unusable<br>&middot; P1 &mdash; key functions do not meet requirements<br>&middot; P2 &mdash; specific functions fail but the product is usable</div>
    </div>
  </div>
</section>""",

"""<section>
  <span class="lbl">Topic 3</span>
  <h3>Bug Report Fields (2/2)</h3>
  <div class="card" style="margin-bottom:6px"><strong>Steps to reproduce</strong>Numbered, exact, starting from a known state. Vague: "go to search and filter". Exact: "1. Open /search 2. Set min $50, max $200 3. Click Apply 4. Scroll results".</div>
  <div class="card g" style="margin-bottom:6px"><strong>Expected result</strong>What should happen at the final step &mdash; ideally with a link to the requirement that defines it.</div>
  <div class="card o" style="margin-bottom:6px"><strong>Actual result</strong>What actually happens, precisely. Not "it doesn't work" but "products priced $12, $32 and $41 appear in the results".</div>
  <div class="card p" style="margin-bottom:6px"><strong>Visuals</strong>Screenshots, recordings, files &mdash; anything that makes the failure obvious.</div>
  <div class="card r"><strong>Logs</strong>&middot; Browser console and network tab<br>&middot; Device logs<br>&middot; Server logs<br>If you cannot access logs, record the exact time it happened.</div>
</section>""",

"""<section>
  <span class="lbl">Topic 3</span>
  <h3>Evidence From the Browser</h3>
  <p style="font-size:.62em">Open DevTools (F12) <em>before</em> you reproduce the defect, not after.</p>
  <div class="g3">
    <div class="card"><strong>Console</strong>JavaScript errors and stack traces &mdash; often names the exact file and line.</div>
    <div class="card g"><strong>Network</strong>The failing request: URL, status code, request payload, response body. A 500 here saves the developer an hour.</div>
    <div class="card o"><strong>Elements / Application</strong>The rendered DOM, cookies, local storage &mdash; useful for state and session defects.</div>
  </div>
  <p style="font-size:.6em;margin-top:.4em">"The page showed an error" is a complaint. A console stack trace plus the failing request is a bug report.</p>
</section>""",

"""<section>
  <span class="lbl">Topic 3</span>
  <h3>A Complete Example</h3>
  <div class="card r">
    <strong>PRF-115 &middot; [Search] Price filter shows products below the minimum price</strong>
    <p style="font-size:.85em;margin:.2em 0">Environment: Chrome 124 &middot; macOS 14.4 &middot; QA env v2.3.1 &nbsp;&middot;&nbsp; Severity: Major &middot; Priority: P1</p>
    <p style="font-size:.85em;margin:.3em 0"><strong style="display:inline">Steps:</strong> 1. Log in as a registered user 2. Go to product search 3. Locate the "Price Range" filter 4. Enter min $50, max $200 5. Click Apply 6. Scroll the results</p>
    <p style="font-size:.85em;margin:.3em 0"><strong style="display:inline">Expected:</strong> all products in results are priced between $50 and $200 inclusive.</p>
    <p style="font-size:.85em;margin:.3em 0"><strong style="display:inline">Actual:</strong> products priced $12, $32 and $41 appear. The minimum price is not applied.</p>
  </div>
  <p style="font-size:.58em;margin-top:.4em">This is the defect that failed step 3 of test case TC-014 in Lesson 10. The actual result names specific prices, so the developer can reproduce the exact failure immediately.</p>
</section>""",

"""<section>
  <span class="lbl">Topic 4</span>
  <h3>Severity Is Not Priority</h3>
  <div class="g2">
    <div class="card r"><strong>High severity + high priority</strong>Checkout crashes for all users. Fix now &mdash; every minute costs money.</div>
    <div class="card o"><strong>Low severity + high priority</strong>The CEO's name is misspelled on the homepage. Nothing is broken &mdash; fix it before the morning press release.</div>
  </div>
  <div class="g2" style="margin-top:8px">
    <div class="card p"><strong>High severity + low priority</strong>Crash when exporting a legacy report used by two internal people once a year. A real crash, low business impact.</div>
    <div class="card"><strong>Low severity + low priority</strong>A pixel misalignment in the footer, Firefox only.</div>
  </div>
  <blockquote>QA sets severity from technical impact. Product sets priority from business context. If you are arguing about one number, you are probably arguing about two different things.</blockquote>
</section>""",

"""<section>
  <span class="lbl">Topic 5</span>
  <h3>Bug Lifecycle</h3>
  <div class="g2" style="align-items:center">
    <div class="figure" style="margin:0"><img src="images/bug-lifecycle.png" alt="Bug lifecycle from New to Closed with alternative paths" style="max-height:360px"></div>
    <div>
      <div class="card o"><strong>Alternative paths, all valid</strong>&middot; Re-opened &mdash; the fix did not work<br>&middot; Rejected / won't fix<br>&middot; Deferred<br>&middot; Duplicate<br>&middot; Not a bug<br>&middot; Cannot reproduce</div>
      <div class="card g" style="margin-top:8px"><strong>Why teams track this</strong>&middot; Progress and statistics<br>&middot; Prioritising and fixing<br>&middot; Trend analysis &mdash; is the defect count growing or shrinking, and do defects come from documentation or from code?</div>
      <p style="font-size:.55em;color:#888;margin-top:.4em">Tools: Jira &middot; GitHub Issues (used in this course) &middot; Linear &middot; YouTrack &middot; Azure DevOps</p>
    </div>
  </div>
</section>""",

"""<section>
  <span class="lbl">Topic 5</span>
  <h3>Defects That Reach Production</h3>
  <p style="font-size:.62em">The point of defect management is to fix the important ones before customers see them. Some still get through:</p>
  <ul style="font-size:.65em">
    <li>The defect could not be reproduced.</li>
    <li>It was found too late in the cycle.</li>
    <li>The team decided not to fix it.</li>
    <li>The fix failed, or the fix created new defects.</li>
    <li>It turned out to be a feature.</li>
  </ul>
</section>""",

"""<section>
  <span class="lbl">Topic 5</span>
  <h3>Root Cause Analysis</h3>
  <p style="font-size:.62em">Finding why the defect happened, not just fixing it and moving on. The team asks: why did this occur?</p>
  <div class="g3">
    <div class="card"><strong>Human cause</strong>A mistake by a person &mdash; misunderstood requirement, wrong assumption.<br><span style="color:#888">Fix: better requirements, more review.</span></div>
    <div class="card o"><strong>Organizational cause</strong>A process failure &mdash; no review, unclear spec, no test environment, unrealistic deadline.<br><span style="color:#888">Fix: improve the process, not the person.</span></div>
    <div class="card r"><strong>Physical / technical cause</strong>Infrastructure &mdash; server failure, network timeout, memory limit, third-party outage.<br><span style="color:#888">Fix: monitoring, redundancy.</span></div>
  </div>
  <blockquote>The goal of RCA is to improve the system, not to assign blame. The same defect happening twice means the process did not learn.</blockquote>
</section>""",

"""<section>
  <span class="lbl">In-Class Exercise</span>
  <div class="teams">
    <h3>One Exploratory Session, One Bug Report</h3>
    <ul style="font-size:.68em">
      <li>Write a charter for an application or website you use: <em>Explore &lt;target&gt; with &lt;resources&gt; to discover &lt;information&gt;.</em></li>
      <li>Time-box it: 20 minutes in class. Pick a tour &mdash; money, back alley, saboteur or couch potato.</li>
      <li>Take notes as you go: what you covered, what surprised you, what you could not check.</li>
      <li>Pick the most interesting defect you found and write the full bug report for it.</li>
      <li>File it as an issue: <a href="https://github.com/tanjaq/Bug-Reporting/issues" style="color:#9b9fe3">tanjaq/Bug-Reporting &middot; Issues</a> &mdash; use the bug report template; existing issues are worked examples.</li>
    </ul>
  </div>
</section>""",

"""<section>
  <span class="lbl">Self-Check</span>
  <h3>Can You Answer These?</h3>
  <ul style="font-size:.68em">
    <li>Explain error, defect and failure with one example of your own.</li>
    <li>Write a charter for exploring a password reset flow.</li>
    <li>Name three tours and say what kind of defect each is good at finding.</li>
    <li>A crash on a rarely used admin page &mdash; what severity, what priority, and why do they differ?</li>
    <li>Draw the bug lifecycle from memory, including two alternative paths.</li>
  </ul>
</section>""",

"""<section>
  <div class="hw">
    <h3>Homework 8 &mdash; Exploratory Session + Bug Report</h3>
    <p style="font-size:.68em">Run a time-boxed exploratory session with a written charter, then file one real defect as a GitHub issue in the Bug-Reporting repository, with your session notes attached.</p>
    <p style="font-size:.62em">Full brief: <a href="homework/hw-08.html">Homework 8</a></p>
  </div>
</section>""",
])

# ---------------- LESSON 10 ----------------
write_lesson(10,
 "Test Cases &amp; Documentation",
 "User story &rarr; requirement &rarr; test case &middot; Re-testing &middot; Regression &middot; Test management tools",
 "Writing test documentation that another person can actually execute",
 ["From user story to test case",
  "Anatomy of a test case and a worked example",
  "The role of test cases in development",
  "Confirmation testing and regression testing",
  "Best practices and test management tools"],
 "Write the test plan and the test cases for your own project, into the SRS document.",
[
"""<section>
  <span class="lbl">Topic 1</span>
  <h3>From User Story to Test Case</h3>
  <div class="card p" style="margin-bottom:6px"><strong>User story &mdash; the end-user need, from the user's point of view</strong>As an online shopper, I want to filter search results by price range, so that I can find products within my budget more easily.</div>
  <div class="card" style="margin-bottom:6px"><strong>Requirement &mdash; derived from the story</strong>The search results page shall support filtering by minimum and maximum price, showing only products within that range.</div>
  <div class="card g"><strong>Test case &mdash; derived from the requirement</strong>Verify that entering min $50 and max $200 in the price filter shows only products priced $50&ndash;$200.</div>
  <p style="font-size:.6em;margin-top:.4em">One user story &rarr; many requirements. One requirement &rarr; many test cases: happy path, negative cases, edge cases. When a test case fails, you write the bug report from Lesson 9.</p>
</section>""",

"""<section>
  <span class="lbl">Topic 2</span>
  <h3>Components of a Test Case</h3>
  <div class="g2">
    <div>
      <div class="card" style="margin-bottom:6px"><strong>ID / title</strong>Unique identifier plus a short name describing what is tested</div>
      <div class="card g" style="margin-bottom:6px"><strong>Description</strong>What this case verifies, and which requirement it covers</div>
      <div class="card o" style="margin-bottom:6px"><strong>Preconditions</strong>What must already be true &mdash; logged in? specific data present?</div>
      <div class="card r"><strong>Test steps</strong>Numbered actions, one thing per step</div>
    </div>
    <div>
      <div class="card p" style="margin-bottom:6px"><strong>Test data</strong>Exact values: which account, which input, which environment</div>
      <div class="card" style="margin-bottom:6px"><strong>Expected results</strong>What the system should do &mdash; specific and measurable</div>
      <div class="card g" style="margin-bottom:6px"><strong>Postconditions</strong>What state the system should be left in</div>
      <div class="card o"><strong>Status</strong>Pass / Fail / Blocked / Not executed, updated each run</div>
    </div>
  </div>
</section>""",

"""<section>
  <span class="lbl">Topic 2</span>
  <h3>What a Real Test Case Document Looks Like</h3>
  """ + img("test-case-template.png", "Test case template with scenario ID, priority, steps, expected and actual output", "76%",
            "Scenario ID, case ID, priority, pre- and post-requisites, then numbered steps with expected and actual output") + """
  <p style="font-size:.58em">Every column earns its place. The comments column with a timestamp and initials is what makes a result traceable weeks later.</p>
</section>""",

"""<section>
  <span class="lbl">Topic 2</span>
  <h3>A Test Case in Practice</h3>
  <p style="font-size:.55em"><strong>TC-014 &middot; Price filter shows results within range.</strong> Requirement: search results can be filtered by price range. Preconditions: site accessible, user logged in, on /search.</p>
  <table>
    <tr><th>#</th><th>Step</th><th>Expected result</th><th>Actual result</th></tr>
    <tr><td>1</td><td>Locate the "Price Range" filter</td><td>Filter is visible with min and max fields</td><td>Pass</td></tr>
    <tr><td>2</td><td>Enter 50 in min and 200 in max</td><td>Both fields accept the values</td><td>Pass</td></tr>
    <tr><td>3</td><td>Click "Apply"</td><td>Results reload; all products priced $50&ndash;$200</td><td>FAIL &mdash; products under $50 shown &rarr; PRF-115</td></tr>
    <tr><td>4</td><td>Click "Clear" to reset</td><td>All products shown again</td><td>Not executed (step 3 failed)</td></tr>
  </table>
  <p style="font-size:.55em;margin-top:.4em">The link between the failing step and the bug ID is what makes QA tracking work &mdash; anyone can go from a failed test to the report and back.</p>
</section>""",

"""<section>
  <span class="lbl">Topic 3</span>
  <h3>Why Test Cases Matter</h3>
  <ul style="font-size:.67em">
    <li>Test cases define the quality of the product &mdash; they are the agreed standard of "working".</li>
    <li>They demonstrate that the software conforms to the requirements.</li>
    <li>They reduce defects and raise reliability.</li>
    <li>They make confirmation testing and regression testing possible &mdash; you cannot re-run a test you never wrote down.</li>
    <li>They improve communication in the development team: a shared, unambiguous description of expected behaviour.</li>
  </ul>
</section>""",

"""<section>
  <span class="lbl">Topic 4</span>
  <h3>Confirmation Testing (Re-testing)</h3>
  <p style="font-size:.63em">A test failed because of a defect. The defect was reported and fixed in a new version. Now run the same test again.</p>
  <ul style="font-size:.66em">
    <li>Run it <strong>exactly</strong> as the first time: same inputs, same data, same environment.</li>
    <li>Only mark it fixed when it passes identically.</li>
    <li>Testing only the fixed spot is not enough &mdash; a fix often breaks something nearby.</li>
  </ul>
  <blockquote>"It works on my machine now" is not confirmation. Same steps, same data, same environment, written down.</blockquote>
</section>""",

"""<section>
  <span class="lbl">Topic 4</span>
  <h3>Regression Testing</h3>
  <p style="font-size:.62em">Every change or update to an application can bring surprises. After each change, check that the functionality that already worked still works &mdash; and that previously fixed defects have not returned.</p>
  <div class="g2">
    <div class="card"><strong>Four strategies</strong>
      1. <strong style="display:inline">Corrective</strong> &mdash; requirements unchanged, run the old tests as they are<br>
      2. <strong style="display:inline">Progressive</strong> &mdash; requirements changed, write new tests or update existing ones<br>
      3. <strong style="display:inline">Retest-all</strong> &mdash; run everything<br>
      4. <strong style="display:inline">Selective</strong> &mdash; run only the tests related to the changed functionality</div>
    <div class="card g"><strong>Why this gets automated</strong>Regression runs the same large set of tests after every change. Doing that by hand is slow and unreliable &mdash; not because it is impossible, but because humans cannot repeat it accurately at scale.<br><span style="color:#888">Regression tests also need maintaining as requirements change.</span></div>
  </div>
</section>""",

"""<section>
  <span class="lbl">Topic 5</span>
  <h3>Best Practices for Writing Test Cases</h3>
  <div class="g2">
    <div class="card g"><strong>Do</strong>
      &middot; Clear, precise description tied to a requirement<br>
      &middot; Exact, well-structured steps<br>
      &middot; Keep cases small and focused &mdash; one case, one scenario<br>
      &middot; Specific test data: environment, user, inputs<br>
      &middot; Prioritise by risk<br>
      &middot; Include negative and edge cases<br>
      &middot; Measurable, specific expected results<br>
      &middot; Automate repetitive and regression tests</div>
    <div class="card r"><strong>Don't</strong>
      &middot; Test login and price filtering in the same case &mdash; when it fails you will not know which broke<br>
      &middot; Write "works correctly" as an expected result<br>
      &middot; Chain dependent tests &mdash; one failure cascades<br>
      &middot; Name cases so vaguely that you must open them to know what failed</div>
  </div>
</section>""",

"""<section>
  <span class="lbl">Topic 5</span>
  <h3>Test Management Tools</h3>
  <div class="g3">
    <div class="card"><strong>Jira</strong>Atlassian's tool, widely used to manage development and testing. Create, manage and track cases and link them to development and defect tracking.</div>
    <div class="card g"><strong>Xray</strong>Test management inside Jira &mdash; integrates test case management with the Jira workflow.</div>
    <div class="card o"><strong>Zephyr</strong>Another popular Jira test management add-on.</div>
  </div>
  <div class="g3" style="margin-top:8px">
    <div class="card r"><strong>TestRail</strong>Purpose-built test case management: create cases, plan runs, track results, generate reports.</div>
    <div class="card p"><strong>TestLink</strong>Open-source test case management with reporting and test plans.</div>
    <div class="card"><strong>QMetry</strong>Test management platform covering case management, automation and quality management in one place.</div>
  </div>
</section>""",

"""<section>
  <span class="lbl">Self-Check</span>
  <h3>Can You Answer These?</h3>
  <ul style="font-size:.68em">
    <li>Write one positive and one negative test case for "users can search by product name".</li>
    <li>What is the difference between confirmation testing and regression testing?</li>
    <li>Which regression strategy fits a hotfix released the same afternoon?</li>
    <li>Why is "the page loads correctly" an unusable expected result?</li>
  </ul>
</section>""",

"""<section>
  <div class="hw">
    <h3>Homework 9 &mdash; Test Plan and Test Cases</h3>
    <p style="font-size:.68em">With your team, write your project&rsquo;s <strong>test plan</strong> into SRS section 7.1 &mdash; scope, what you will <em>not</em> test, approach, entry and exit criteria, environment, risks.</p>
    <p style="font-size:.68em">Then write the <strong>test cases</strong> into section 7.2, covering every functional requirement you wrote in Homework 3.</p>
    <p style="font-size:.62em">Full brief: <a href="homework/hw-09.html">Homework 9</a></p>
  </div>
</section>""",
])
