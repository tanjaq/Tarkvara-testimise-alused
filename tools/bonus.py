# -*- coding: utf-8 -*-
from tpl import *
import os

def write_bonus(i, fname, title, sub, slides):
    body = ["""<section data-background-gradient="linear-gradient(135deg,#0f0c29,#302b63,#24243e)">
  <span class="lbl">Bonus Lesson</span>
  <h2>%s</h2>
  <div class="divider"></div>
  <p style="font-size:.62em">%s</p>
  <p style="font-size:.5em;color:#555;margin-top:.8em">&rarr; next slide &nbsp;|&nbsp; ESC back to all lessons</p>
</section>""" % (title, sub)] + slides
    html = HEAD.format(title="Bonus &ndash; " + title, css=CSS, nav=nav_bonus(i)) + "\n\n".join(body) + FOOT
    open(os.path.join(OUT, fname), "w").write(html)
    print("wrote", fname, "(%d slides)" % len(body))


# ============ BONUS 1: AI ============
write_bonus(0, "lesson-bonus-ai.html",
 "Using AI Responsibly in Testing",
 "The rules &middot; Four things AI is good at &middot; Four ways it quietly fails &middot; Prompting &middot; Testing AI features",
[
"""<section>
  <span class="lbl">The Rules</span>
  <div class="ai">
    <h3>AI Is Allowed &mdash; and Encouraged</h3>
    <p style="font-size:.68em">ChatGPT, Claude, Gemini, Copilot and the rest are <strong>permitted in this course, and I recommend using them</strong>. Working well with AI is a real skill for developers and testers, and pretending otherwise helps nobody.</p>
    <div class="g2" style="margin-top:.5em">
      <div class="card g"><strong>The golden rule</strong>Use AI &mdash; but with your brain switched on.</div>
      <div class="card r"><strong>The consequence</strong>You are responsible for the result, not the AI. Every submitted homework must be something you can explain and defend out loud.</div>
    </div>
    <p style="font-size:.62em;margin-top:.5em">"The AI wrote it" is not an answer to "why does this test assert that?"</p>
  </div>
</section>""",

"""<section>
  <span class="lbl">Why It Fits This Course</span>
  <h3>Everything You Learn Here Is How You Supervise AI</h3>
  <div class="g2">
    <div class="card"><strong>Requirements (L4)</strong>AI does not know them. You supply them, and you notice when the output contradicts them.</div>
    <div class="card g"><strong>Techniques (L7, L8)</strong>EP, BVA, decision tables and coverage are how you audit a set of AI-generated tests in two minutes.</div>
  </div>
  <div class="g2" style="margin-top:8px">
    <div class="card o"><strong>Exploratory testing (L9)</strong>AI cannot be curious about your product. Charters and tours are yours.</div>
    <div class="card p"><strong>Bug reports (L9)</strong>AI can improve your writing. It cannot observe the failure for you.</div>
  </div>
  <blockquote>The people who get the most out of AI are the ones who could have done the work themselves &mdash; and therefore know when the answer is wrong.</blockquote>
</section>""",

"""<section>
  <span class="lbl">The Honest Summary</span>
  <h3>What AI Is and Is Not Good At</h3>
  <div class="g2">
    <div class="card g"><strong>Genuinely good at</strong>
      &middot; Boilerplate and scaffolding<br>
      &middot; A first draft of test cases from a requirement<br>
      &middot; Suggesting edge cases you did not think of<br>
      &middot; Explaining code, error messages and stack traces<br>
      &middot; Turning your rough notes into clear prose<br>
      &middot; Converting formats &mdash; a table into a checklist, notes into a report</div>
    <div class="card r"><strong>Quietly bad at</strong>
      &middot; Knowing your requirements<br>
      &middot; Knowing your system's context and history<br>
      &middot; Depth &mdash; generated tests are usually happy path only<br>
      &middot; Being wrong <em>visibly</em> &mdash; the code looks clean and the logic is subtly off<br>
      &middot; Saying "I don't know"<br>
      &middot; Anything requiring it to have actually run the software</div>
  </div>
  <p style="font-size:.6em;margin-top:.4em">AI-generated code compiles. It might even pass basic tests. That does not make it correct.</p>
</section>""",

"""<section>
  <span class="lbl">Good Example 1</span>
  <h3>First-Draft Test Cases From a Requirement</h3>
  <div class="card g" style="margin-bottom:8px"><strong>The prompt &mdash; note how much context it carries</strong>
    <p style="font-size:.88em;margin:.2em 0">"Here is a requirement: <em>Users must be able to book between 1 and 8 travellers per trip. Bookings above 8 must show the error 'Maximum 8 travellers per booking'.</em><br>
    Generate test cases using equivalence partitioning and boundary value analysis. For each case give the input, the technique it comes from, and the expected result. List any assumptions you had to make."</p></div>
  <div class="card" style="margin-bottom:8px"><strong>What comes back is useful</strong>&middot; 0, 1, 2, 7, 8, 9<br>&middot; Non-numeric input<br>&middot; Empty field<br>&middot; Negative<br>&middot; Decimal<br>A solid starting grid, in seconds.</div>
  <div class="card o"><strong>What you must still do</strong>Check the partitions against the <em>real</em> rule &middot; delete cases that duplicate each other &middot; add the ones only you know matter (what happens on the second booking? with a group discount?) &middot; read the "assumptions" list &mdash; that is where the requirement gaps are.</div>
</section>""",

"""<section>
  <span class="lbl">Bad Example 1</span>
  <h3>"Write Tests for This Function"</h3>
  <pre><code class="language-javascript">function applyDiscount(price, isMember) {
  if (isMember) return price * 0.95;
  return price;
}</code></pre>
  <div class="g2" style="margin-top:.3em">
    <div class="card r"><strong>What AI typically produces</strong>Two tests: member gets 5% off, non-member pays full. Both pass. Coverage: 100%.<br><span style="color:#888">Looks like a finished job.</span></div>
    <div class="card"><strong>What nobody tested</strong>&middot; A negative price, or a price of 0<br>&middot; <code>isMember</code> as the string "false" &mdash; which is truthy<br>&middot; Floating point: 19.99 &rarr; 18.9905<br>&middot; The birthday rule from the requirement, which is <em>not in this function at all</em></div>
  </div>
  <p style="font-size:.55em;margin-top:.35em;color:var(--red)">The last one is the real defect. AI cannot see a requirement you never gave it &mdash; and 100% coverage of the wrong logic is still the wrong logic.</p>
</section>""",

"""<section>
  <span class="lbl">Good Example 2</span>
  <h3>Explaining Code, Errors and Logs</h3>
  <div class="card g" style="margin-bottom:8px"><strong>Prompt</strong>
    "Explain what this function does, step by step, and list the inputs for which it would behave unexpectedly."<br>
    "Here is a stack trace from our test environment. What is the most likely cause, and what would you check first?"</div>
  <p style="font-size:.63em">This is the single highest-value use for a junior tester. You get a fast orientation in unfamiliar code, and a list of suspicious inputs to go and try yourself.</p>
  <div class="card o"><strong>Still your job</strong>Verify the explanation against the code. AI describing a function is a hypothesis, not documentation &mdash; and when it is wrong, it is wrong confidently and fluently.</div>
</section>""",

"""<section>
  <span class="lbl">Bad Example 2</span>
  <h3>"Is This Code Correct?"</h3>
  <div class="card r" style="margin-bottom:8px"><strong>Why this question cannot be answered</strong>
    Correct <em>against what</em>? Correctness is a relationship between code and a requirement. If you did not supply the requirement, the model invents a plausible one and then grades the code against its own invention.</div>
  <div class="g2">
    <div class="card"><strong>What you get</strong>"Yes, this looks correct and follows best practice." Delivered with total confidence, about code that computes VAT at the wrong rate.</div>
    <div class="card g"><strong>Ask this instead</strong>"Here is the requirement. Here is the code. List every case where the code's behaviour differs from the requirement, and say which requirement clause each one breaks."</div>
  </div>
  <p style="font-size:.6em;margin-top:.4em">The pattern generalises: never ask AI to <em>judge</em>. Ask it to <em>compare against something you provided</em>.</p>
</section>""",

"""<section>
  <span class="lbl">Good Example 3</span>
  <h3>Interrogating a Vague Requirement</h3>
  <div class="card g" style="margin-bottom:8px"><strong>Prompt</strong>
    "Here is a requirement from our SRS: <em>'The system should let users cancel their orders.'</em><br>
    Act as a tester reviewing this requirement. List every question that must be answered before it can be tested, and rewrite it as a SMART requirement once you have flagged the gaps."</div>
  <div class="card"><strong>What comes back</strong>Until when can an order be cancelled? What happens to a paid order &mdash; refund, credit, nothing? Partial cancellation? Who can cancel &mdash; the customer, support, both? What does the customer see? What if the order already shipped?</div>
  <p style="font-size:.62em;margin-top:.4em;color:var(--green)">Every one of those is a question <em>you</em> then take to the product owner. That is static testing (Lesson 6) with a very fast assistant.</p>
</section>""",

"""<section>
  <span class="lbl">Bad Example 3</span>
  <h3>Letting AI Write the Requirements</h3>
  <div class="card r" style="margin-bottom:8px"><strong>The prompt that ruins a project</strong>"Write the functional requirements for an online shop."</div>
  <p style="font-size:.63em">You will get forty confident, well-formatted requirements. They describe a generic shop that does not exist. Nobody in your team agreed to them, no user asked for them, and half of them contradict what you are actually building.</p>
  <div class="g2">
    <div class="card o"><strong>Then it compounds</strong>Test cases get written against invented requirements. The build gets judged against invented requirements. Real gaps stay invisible because the document looks complete.</div>
    <div class="card g"><strong>Use it the other way round</strong>Write your requirements yourself, then ask: "Here are our requirements. What is missing, ambiguous or contradictory? What would a tester be unable to verify?"</div>
  </div>
</section>""",

"""<section>
  <span class="lbl">Good Example 4</span>
  <h3>Polishing a Bug Report You Actually Observed</h3>
  <div class="g2">
    <div class="card"><strong>Your rough notes</strong>
      "price filter min 50 max 200, still shows 12 and 32 euro stuff, chrome, qa env, logged in as normal user, console clean, network shows the request goes out with min=50 so backend problem probably"</div>
    <div class="card g"><strong>Prompt</strong>
      "Turn these observations into a bug report with summary title, environment, severity, priority, numbered steps to reproduce, expected and actual result. Do not add any facts I did not give you. Mark anything you think is missing."</div>
  </div>
  <p style="font-size:.62em;margin-top:.4em">You supply every fact; the model supplies structure and clarity. The "do not add facts" clause is the important part of that prompt &mdash; and "mark anything missing" turns it into a checklist.</p>
</section>""",

"""<section>
  <span class="lbl">Bad Example 4</span>
  <h3>Inventing the Evidence</h3>
  <div class="card r" style="margin-bottom:8px"><strong>What goes wrong without that clause</strong>
    Ask for "a bug report about a broken price filter" and you will get plausible steps you never performed, an environment you never used, a log line that was never printed and an error code that does not exist in your system.</div>
  <div class="g2">
    <div class="card o"><strong>The cost</strong>A developer spends an afternoon chasing a reproduction path that was never real. Do that twice and your reports stop being trusted &mdash; which is the end of your usefulness as a tester.</div>
    <div class="card p"><strong>The rule</strong>Facts come from the product. AI may only rearrange facts you observed. Never paste an AI-written step you have not run yourself.</div>
  </div>
</section>""",

"""<section>
  <span class="lbl">Prompting</span>
  <h3>What Makes a Prompt Work for Testing</h3>
  <div class="g2">
    <div class="card g"><strong>Include</strong>
      &middot; The requirement, pasted in full<br>
      &middot; The code or the observation, pasted in full<br>
      &middot; The role: "act as a tester reviewing this"<br>
      &middot; The technique: "use equivalence partitioning and BVA"<br>
      &middot; The output shape: "a table with input, technique, expected result"<br>
      &middot; A constraint: "do not invent facts"<br>
      &middot; A request for uncertainty: "list your assumptions and anything you are unsure about"</div>
    <div class="card r"><strong>Avoid</strong>
      &middot; "Is this good?" &mdash; no yardstick<br>
      &middot; "Write tests" &mdash; no requirement<br>
      &middot; "Fix it" &mdash; you will not learn what was wrong<br>
      &middot; Pasting company code, customer data or credentials into a public tool<br>
      &middot; Accepting the first answer &mdash; ask it to critique its own output and it will often find the gap itself</div>
  </div>
</section>""",

"""<section>
  <span class="lbl">The Loop That Works</span>
  <h3>You Define Correct, Before AI Touches Anything</h3>
  <div class="chain">
    <div class="node" style="border-color:var(--red)"><strong>You write the test</strong><br><span style="font-size:.85em;color:#888">from the requirement &mdash; AI has no say here</span></div><span class="arr">&rarr;</span>
    <div class="node" style="border-color:var(--green)"><strong>AI writes the code</strong><br><span style="font-size:.85em;color:#888">let it draft &mdash; then read what it produced</span></div><span class="arr">&rarr;</span>
    <div class="node" style="border-color:var(--blue)"><strong>Tests judge the result</strong><br><span style="font-size:.85em;color:#888">trust the tests, not the model</span></div>
  </div>
  <p style="font-size:.63em;margin-top:.5em">If the tests come first, and the tests come from the requirements, then the model cannot quietly redefine what "working" means. This is why test-first thinking and AI fit together so well.</p>
</section>""",

"""<section>
  <span class="lbl">Ground Rules</span>
  <div class="ai">
    <h3>Do and Don't</h3>
    <div class="g2" style="margin-top:.4em">
      <div>
        <p style="font-size:.72em;color:var(--green);font-weight:600">Do</p>
        <ul style="font-size:.66em">
          <li>Use AI for boilerplate and first drafts</li>
          <li>Give it the requirement, always</li>
          <li>Ask it for edge cases you might have missed</li>
          <li>Read everything before you submit or commit it</li>
          <li>Run the full test suite against anything it produced</li>
          <li>Ask it to explain its reasoning &mdash; gaps appear fast</li>
          <li>Ask it what it is unsure about</li>
        </ul>
      </div>
      <div>
        <p style="font-size:.72em;color:var(--red);font-weight:600">Don't</p>
        <ul style="font-size:.66em">
          <li>Submit output you do not understand</li>
          <li>Treat generated tests as complete coverage</li>
          <li>Skip review because "AI wrote it"</li>
          <li>Accept a passing test as proof of correctness</li>
          <li>Let it define your requirements</li>
          <li>Paste confidential code or real user data into it</li>
          <li>Report a defect you did not personally reproduce</li>
        </ul>
      </div>
    </div>
    <p style="font-size:.62em;margin-top:.5em">AI is a fast junior colleague who never complains and never says "I'm not sure". Both halves of that need managing.</p>
  </div>
</section>""",

"""<section>
  <span class="lbl">The Other Direction</span>
  <h3>When the AI Is the Thing Being Tested</h3>
  <p style="font-size:.63em">More and more products have an AI feature in them. Testing those breaks some assumptions from this whole course:</p>
  <div class="g2">
    <div class="card o"><strong>What changes</strong>
      &middot; The same input can produce different output &mdash; there is no single expected result<br>
      &middot; "Correct" becomes a range of acceptable answers<br>
      &middot; Failures are not crashes; they are confident wrong answers<br>
      &middot; Behaviour changes when the underlying model is updated, without any code change on your side</div>
    <div class="card g"><strong>What you test instead</strong>
      &middot; Properties, not exact strings: is it in the right format? within the right bounds? does it refuse what it should refuse?<br>
      &middot; A fixed evaluation set of inputs with graded expectations, re-run on every change<br>
      &middot; The guard rails: prompt injection, leaking data, unsafe content<br>
      &middot; The fallback: what happens when the model is slow, down or returns nonsense</div>
  </div>
</section>""",

"""<section>
  <span class="lbl">In-Class Exercise</span>
  <div class="teams">
    <h3>Audit the Machine</h3>
    <ul style="font-size:.68em">
      <li>Take one functional requirement from your team's SRS.</li>
      <li>Ask an AI tool to write test cases for it. Save what it gives you.</li>
      <li>Now apply Lesson 7 to that output: are the equivalence partitions complete? Are the boundaries there? Any negative cases? Any case that contradicts the requirement?</li>
      <li>Count: how many cases did it miss, and how many did it invent?</li>
      <li>Write one paragraph on what the tool was actually useful for.</li>
    </ul>
    <p style="font-size:.62em;margin-top:.4em">Being able to say precisely what an AI missed is the skill. Anyone can paste a prompt.</p>
  </div>
</section>""",
])


# ============ BONUS 2: PERFORMANCE ============
write_bonus(1, "lesson-bonus-performance.html",
 "Performance Testing",
 "Response time &middot; Throughput &middot; Resource utilization &middot; Load, stress and endurance tests",
[
"""<section>
  <span class="lbl">Topic 1</span>
  <h3>Why Performance Matters</h3>
  <p style="font-size:.64em">Most performance problems come down to speed, response time, load time and poor scalability. A slow application loses users &mdash; performance testing makes sure it stays fast enough to keep their attention.</p>
  <div class="g2">
    <div class="card o"><strong>Long load time</strong>Load time is how long the application takes to start. Keep it to a minimum &mdash; ideally a few seconds.</div>
    <div class="card r"><strong>Poor response time</strong>The time from a user's input to the application's response. Wait too long and the user is gone.</div>
  </div>
</section>""",

"""<section>
  <span class="lbl">Topic 1</span>
  <h3>Scalability and Bottlenecks</h3>
  <div class="g2">
    <div class="card"><strong>Poor scalability</strong>The product cannot handle the expected number of users, or does not accommodate a wide enough range of them. Load testing tells you whether it can carry the anticipated user count.</div>
    <div class="card r"><strong>Bottlenecks</strong>Obstructions that degrade overall system performance &mdash; coding errors or hardware issues that reduce throughput under load.<br><span style="color:#888">Common ones: CPU utilization, memory utilization, network utilization, operating-system limits, disk usage.</span></div>
  </div>
  <p style="font-size:.6em;margin-top:.4em">Performance testing checks three things: <strong>speed</strong> (does it respond quickly), <strong>scalability</strong> (what user load can it carry), <strong>stability</strong> (is it stable under varying load).</p>
</section>""",

"""<section>
  <span class="lbl">Topic 2</span>
  <h3>Response Time</h3>
  <p style="font-size:.62em">The amount of time taken to respond to a request. There is more than one place to measure it:</p>
  <div class="g2">
    <div class="card"><strong>Latency at the server</strong>For serverless applications, one form is the duration of the function from start to finish of the computation.</div>
    <div class="card g"><strong>Latency at the client</strong>Measured from the user's perspective &mdash; includes the API gateway, request queue, computation and result queue.</div>
  </div>
  <p style="font-size:.6em;margin-top:.4em"><strong>Example requirement:</strong> small requests 1 second, heavy computation requests 5&ndash;7 seconds.</p>
  <blockquote>Always state which measurement point a number refers to. "200 ms" at the server and "200 ms" at the client are very different promises.</blockquote>
</section>""",

"""<section>
  <span class="lbl">Topic 2</span>
  <h3>Throughput and Resource Utilization</h3>
  <div class="g2">
    <div class="card o"><strong>Throughput</strong>The number of requests the application handles per second. Can be defined as transactions completed per second, or concurrent function executions.<br><span style="color:#888">Example: 10 requests per second sustained for at least 5 minutes.</span></div>
    <div class="card p"><strong>Resource utilization</strong>The cost in server and network resources:<br>&middot; CPU<br>&middot; Memory<br>&middot; Disk I/O<br>&middot; Network I/O.<br><span style="color:#888">Example: idle CPU usage 1&ndash;5%, heavy load 80&ndash;100%.</span></div>
  </div>
  <p style="font-size:.6em;margin-top:.4em">These three &mdash; response time, throughput, resource utilization &mdash; are the traditional performance indicators. Every performance NFR you write should be expressed in one of them.</p>
</section>""",

"""<section>
  <span class="lbl">Topic 3</span>
  <h3>Three Types of Performance Test</h3>
  <div class="g3">
    <div class="card"><strong>Load testing</strong>Measures performance under expected, production-like workload. The closest approximation to real usage. Main goal: make sure changes still meet the agreed non-functional requirements.</div>
    <div class="card r"><strong>Stress testing</strong>Measures the workload at which the application starts to fail. Shows the real capacity limits, which components break first, and how the system recovers.</div>
    <div class="card o"><strong>Endurance testing</strong>Load tests run for a long time with production-like workload, to find issues that only appear after extended running &mdash; memory leaks, log growth, connection exhaustion.</div>
  </div>
  <p style="font-size:.6em;margin-top:.4em">Performance tests should run regularly and eventually be part of the CI/CD pipeline &mdash; a performance test run once before release tells you nothing about the trend.</p>
</section>""",

"""<section>
  <span class="lbl">Topic 4</span>
  <h3>A Performance Testing Approach</h3>
  <table>
    <tr><th>Step</th><th>Description</th></tr>
    <tr><td>NFR capture</td><td>Gather performance NFRs from all stakeholders: performance targets, key use cases, data requirements</td></tr>
    <tr><td>Environment build</td><td>Make a close replica of production &mdash; at minimum reflect the production deployment and database size</td></tr>
    <tr><td>Use-case scripting</td><td>Identify key use cases and any components that need separate monitoring</td></tr>
    <tr><td>Scenario build</td><td>Choose the test type, volume and duration</td></tr>
    <tr><td>Execution</td><td>Run and monitor the tests</td></tr>
    <tr><td>Analysis &amp; reporting</td><td>Collect data from all runs, compare against requirements, write the report</td></tr>
  </table>
  <p style="font-size:.55em;color:#888;margin-top:.4em">Approach proposed by Ian Molyneaux, <em>The Art of Application Performance Testing</em></p>
</section>""",

"""<section>
  <span class="lbl">Topic 5</span>
  <h3>Tools</h3>
  <div class="g2">
    <div>
      <div class="card" style="margin-bottom:6px"><strong>JMeter</strong>Open source, load and performance testing across many servers and protocols. The usual starting point.</div>
      <div class="card g" style="margin-bottom:6px"><strong>k6</strong>Modern open-source load testing, tests written in JavaScript &mdash; fits well into a CI pipeline.</div>
      <div class="card o"><strong>BlazeMeter</strong>Scales load and performance testing; combines UX and load testing so you see what users see under load.</div>
    </div>
    <div>
      <div class="card r" style="margin-bottom:6px"><strong>LoadRunner</strong>Helps identify likely causes of performance issues in applications.</div>
      <div class="card p" style="margin-bottom:6px"><strong>LoadNinja</strong>Scriptless load test creation and playback; real-browser load execution at scale.</div>
      <div class="card"><strong>HeadSpin</strong>Mobile app performance optimisation across applications, devices and networks.</div>
    </div>
  </div>
</section>""",

"""<section>
  <span class="lbl">Exercise</span>
  <div class="teams">
    <h3>Performance Requirements for Your Project</h3>
    <ul style="font-size:.7em">
      <li>Discuss with your team and capture performance requirements for response time and throughput.</li>
      <li>How quickly should the main page load? How many concurrent users should the application hold? What would a stress test scenario look like?</li>
      <li>Express every requirement with a number, a unit and a measurement point.</li>
      <li>Write the requirements into your SRS document.</li>
    </ul>
  </div>
</section>""",

"""<section>
  <span class="lbl">Self-Check</span>
  <h3>Can You Answer These?</h3>
  <ul style="font-size:.68em">
    <li>Turn "the site should handle a lot of users" into a testable requirement using all three metrics.</li>
    <li>When would you run an endurance test rather than a load test?</li>
    <li>Your load test passes but users still complain the app is slow. Name two explanations.</li>
    <li>Why must the performance test environment resemble production?</li>
  </ul>
</section>""",
])


# ============ BONUS 3: SECURITY ============
write_bonus(2, "lesson-bonus-security.html",
 "Application Security",
 "CIA &middot; OWASP Top 10 and ASVS &middot; Injection, XSS, authentication, business logic",
[
"""<section>
  <span class="lbl">Topic 1</span>
  <h3>Three Components of Security</h3>
  <div class="g3">
    <div class="card"><strong>Confidentiality</strong>Information is accessible only by authorised users</div>
    <div class="card g"><strong>Integrity</strong>Information can be modified only by authorised users</div>
    <div class="card o"><strong>Availability</strong>Information is accessible to users whenever it is needed</div>
  </div>
  <blockquote>An attacker only needs to find one vulnerability. A developer has to fix all of them.</blockquote>
  <p style="font-size:.58em;color:#888">Meltdown, Spectre, HeartBleed, ShellShock, Ghostcat &mdash; and the endless stream of WordPress, Drupal and Joomla issues.</p>
</section>""",

"""<section>
  <span class="lbl">Topic 2</span>
  <h3>Where Vulnerabilities Come From</h3>
  <ul style="font-size:.66em">
    <li>The cost of doing security properly</li>
    <li>Short timelines</li>
    <li>Hoping the framework fixes it all</li>
    <li>Senior programmers who "know what they are doing"</li>
    <li>"It's only an internal web app"</li>
    <li>"It's a non-critical system"</li>
    <li>"Not my job"</li>
  </ul>
  <p style="font-size:.6em;margin-top:.4em">Every one of these is a process problem, not a technical one &mdash; which is exactly the organizational root cause from Lesson 9.</p>
</section>""",

"""<section>
  <span class="lbl">Topic 2</span>
  <h3>Where the Weaknesses Sit</h3>
  <div class="g3">
    <div class="card"><strong>Client&ndash;server communication</strong>HTTP in plain text &middot; HTTPS with weak encryption</div>
    <div class="card o"><strong>Client side</strong>Malware, hostile browser extensions, insecure storage</div>
    <div class="card r"><strong>Server side</strong>Storage issues, framework and component vulnerabilities, misconfiguration</div>
  </div>
  <p style="font-size:.62em;margin-top:.5em">Public leaks put the scale in perspective: LinkedIn &mdash; 167 million passwords offered for sale &middot; Tumblr &mdash; 65 million &middot; MySpace &mdash; 427 million.</p>
</section>""",

"""<section>
  <span class="lbl">Topic 3</span>
  <h3>OWASP</h3>
  <p style="font-size:.63em">The Open Web Application Security Project &mdash; rankings, manuals, cheat sheets, standards and tools, all free.</p>
  <div class="g3">
    <div class="card"><strong>OWASP Top 10</strong>The most common web application attacks. Start here.<br><a href="https://owasp.org/Top10/">owasp.org/Top10</a></div>
    <div class="card g"><strong>OWASP ASVS</strong>Application Security Verification Standard &mdash; a checklist of "verify that..." statements you can test against.</div>
    <div class="card o"><strong>OWASP WSTG</strong>Web Security Testing Guide &mdash; how to actually perform the tests.</div>
  </div>
  <p style="font-size:.58em;margin-top:.4em">ASVS v4 chapters: architecture &middot; authentication &middot; session management &middot; access control &middot; validation and encoding &middot; stored cryptography &middot; error handling and logging &middot; data protection &middot; communication &middot; malicious code &middot; business logic &middot; files and resources &middot; API and web services &middot; configuration</p>
</section>""",

"""<section>
  <span class="lbl">Topic 3</span>
  <h3>Where to Gather Information</h3>
  <div class="g2">
    <div class="card"><strong>Known vulnerabilities</strong><a href="https://cve.mitre.org/cve/">cve.mitre.org</a> &middot; <a href="https://seclists.org/">seclists.org</a><br>Security updates and fixes on vendor homepages</div>
    <div class="card o"><strong>Known exploits and community</strong><a href="https://www.exploit-db.com/">exploit-db.com</a><br>Communities &mdash; security accounts on social platforms, Reddit</div>
  </div>
</section>""",

"""<section>
  <span class="lbl">Topic 4</span>
  <h3>Exploiting User Input</h3>
  <p style="font-size:.62em">Anything a user can send, an attacker can craft. The entry points:</p>
  <ul style="font-size:.66em">
    <li>HTTP(S) POST and GET requests</li>
    <li>The browser itself &mdash; and its developer tools</li>
    <li>Plugins: cookie managers, user agent switchers, request tamperers</li>
    <li>The command line</li>
    <li>Program code calling your API directly</li>
  </ul>
  <blockquote>Client-side validation is a usability feature, not a security control. Everything must be validated again on the server.</blockquote>
</section>""",

"""<section>
  <span class="lbl">Topic 4</span>
  <h3>Web Content Injection and XSS</h3>
  <div class="g2">
    <div class="card"><strong>Injection points and defences</strong>
      HTML injection &rarr; verify HTML syntax, HTML-encode output<br>
      JavaScript injection &rarr; verify JS syntax, never eval user input<br>
      URL &rarr; allow-list protocols and URL patterns<br>
      Content-Type &rarr; verify response header and charset<br>
      Web content files &rarr; integrity checks; never include untrusted SVG as an object</div>
    <div class="card r"><strong>What XSS lets an attacker do</strong>&middot; Run scripts in the background<br>&middot; Change how the page looks<br>&middot; Modify the DOM, change links, steal input<br>&middot; Redirect to another site<br>&middot; Embed an iframe inside the page</div>
  </div>
</section>""",

"""<section>
  <span class="lbl">Topic 4</span>
  <h3>Authentication and Business Logic</h3>
  <div class="g2">
    <div class="card g"><strong>Authentication</strong>
      <span style="color:#888">User side:</span> avoid passwords where possible (Mobile-ID, Smart-ID, ID card) &middot; two-factor authentication &middot; unique passwords &middot; check <a href="https://haveibeenpwned.com/">haveibeenpwned.com</a><br>
      <span style="color:#888">Server side:</span> store passwords as hashes &middot; limit authentication attempts &middot; log attempts</div>
    <div class="card o"><strong>Business logic mistakes</strong>
      Problems caused by business rules that were never fully checked in the implementation: negative amounts in a shopping cart, steps that are not enforced, excessive requests, cancelling transactions at the wrong moment.<br>
      <span style="color:#888">Defence: discuss the logic with several parties, implement all controls server side, double-check inputs.</span></div>
  </div>
  <p style="font-size:.58em;margin-top:.4em">Business logic flaws are the ones you find with the black-box techniques from Lesson 7 &mdash; not with a scanner.</p>
</section>""",

"""<section>
  <span class="lbl">Topic 4</span>
  <h3>Components, Files and Injections</h3>
  <div class="g3">
    <div class="card"><strong>Frameworks, libraries, components</strong>&middot; Not enough background checks<br>&middot; Assuming the framework handles security<br>&middot; Publicly known issues.<br><span style="color:#888">Defence: identify and verify every component &mdash; OS, web server, languages, add-ons.</span></div>
    <div class="card o"><strong>Web server and files</strong>&middot; Public and private folders<br>&middot; Folder-based configuration<br>&middot; Server-side code exposure.<br><span style="color:#888">Defence: allow-lists and authorization &middot; never use user-supplied filenames &middot; read-only permissions. An uploaded evilimage.php.jpg can end up executed.</span></div>
    <div class="card r"><strong>Command and SQL injection</strong>Commands: running OS commands, remote shells, reading and writing files. SQL: queries built dynamically from input.<br><span style="color:#888">Defence: never build commands from user input &middot; do not let an attacker see or guess the database structure &middot; use prepared statements.</span></div>
  </div>
</section>""",

"""<section>
  <span class="lbl">Exercise</span>
  <div class="teams">
    <h3>Security Review of Your Own Project</h3>
    <ul style="font-size:.7em">
      <li>Capture every potentially problematic place in your application: user input fields, dropdowns, login, file uploads, payments.</li>
      <li>Write all the places where security testing should be conducted into your SRS document.</li>
      <li>Add <strong>GitHub Dependabot</strong> to your repository.</li>
      <li>Add <strong>SonarLint</strong> (or a similar static analysis tool) to your application.</li>
      <li>Report what the tools found in the first run.</li>
    </ul>
  </div>
</section>""",

"""<section>
  <span class="lbl">Self-Check</span>
  <h3>Can You Answer These?</h3>
  <ul style="font-size:.68em">
    <li>Give an example failure for each of confidentiality, integrity and availability.</li>
    <li>Why is client-side validation not a security control?</li>
    <li>Name a business logic flaw a security scanner would never find.</li>
    <li>What is the first thing you would check in your own project after this lesson?</li>
  </ul>
</section>""",
])
