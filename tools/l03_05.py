# -*- coding: utf-8 -*-
from tpl import *

# ---------------- LESSON 3 ----------------
write_lesson(3,
 "The Testing Process",
 "SDLC &middot; Waterfall, V-model, Agile &middot; The ISTQB test process &middot; 7 principles",
 "How testing is organised as a process, not a single activity",
 ["Software Development Life Cycle and its models",
  "The ISTQB test process &mdash; five steps",
  "Planning, analysis and design",
  "Execution, exit criteria and closure",
  "The seven principles of testing"],
 "Group work &mdash; run the full five-step test process on a simple web calculator, using the worksheet.",
[
"""<section>
  <span class="lbl">Topic 1</span>
  <h3>Software Development Life Cycle</h3>
  <p style="font-size:.6em">A set of processes used to build and deliver quality software. There are many models &mdash; but almost all of them contain the same phases.</p>
  <table>
    <tr><th>Phase</th><th>Entry criteria</th><th>Exit criteria</th></tr>
    <tr><td>Kickoff / planning</td><td>Requirements gathered from stakeholders</td><td>Project accepted and planned</td></tr>
    <tr><td>Analysis &amp; requirements</td><td>Requirements, change requests</td><td>SRS document</td></tr>
    <tr><td>Design</td><td>SRS document</td><td>Design specification</td></tr>
    <tr><td>Development</td><td>SRS + design spec</td><td>Build, unit tests, environment set up</td></tr>
    <tr><td>Testing</td><td>SRS, deployed build, test cases</td><td>System tested, defects closed</td></tr>
    <tr><td>Deployment</td><td>No high-priority defects</td><td>Build in production</td></tr>
    <tr><td>Operation &amp; maintenance</td><td>Real users reporting issues</td><td>Fixes deployed</td></tr>
  </table>
</section>""",

"""<section>
  <span class="lbl">Topic 1</span>
  <h3>Waterfall</h3>
  """ + img("waterfall.png", "Waterfall model phases", "58%",
            "Each phase finishes before the next begins &mdash; testing is a phase near the end") + """
  <p style="font-size:.6em">Predictable and well documented, but changing direction late is expensive, and a requirements defect is not discovered until verification.</p>
</section>""",

"""<section>
  <span class="lbl">Topic 1</span>
  <h3>V-Model</h3>
  """ + img("v-model.png", "V-model linking development phases to test levels", "62%",
            "Every development phase has a matching test level, defined at the same time") + """
  <p style="font-size:.6em">Requirements analysis pairs with system testing, high-level design with integration testing, detailed design with unit testing. Test design starts early, even though execution comes later.</p>
</section>""",

"""<section>
  <span class="lbl">Topic 1</span>
  <h3>Agile</h3>
  <div class="g2">
    <div class="figure" style="margin:0"><img src="images/agile.png" alt="Agile cycle" style="max-height:310px"></div>
    <div>
      <div class="card"><strong>Short iterations</strong>Plan, develop, test, release, feedback &mdash; then again</div>
      <div class="card g" style="margin-top:8px"><strong>Testing is continuous</strong>It is not a phase, and it is not one person's job</div>
      <div class="card o" style="margin-top:8px"><strong>Working software each sprint</strong>Which means something must be testable each sprint</div>
    </div>
  </div>
  <blockquote>The model changes <em>when</em> you test. It does not change <em>what</em> good testing is.</blockquote>
</section>""",

"""<section>
  <span class="lbl">Topic 1</span>
  <h3>And Where This Ends Up: DevOps</h3>
  """ + img("devops-lifecycle.png", "DevOps lifecycle loop", "58%",
            "Plan &rarr; code &rarr; build &rarr; test &rarr; release &rarr; deploy &rarr; operate &rarr; monitor") + """
  <p style="font-size:.58em">Testing sits in the middle of the loop and runs automatically on every change. You meet this again in the CI section of the automation course.</p>
</section>""",

"""<section>
  <span class="lbl">Topic 2</span>
  <h3>Testing Is a Process &mdash; ISTQB</h3>
  <div class="chain">
    <div class="node">1. Planning<br>&amp; control</div><span class="arr">&rarr;</span>
    <div class="node">2. Analysis<br>&amp; design</div><span class="arr">&rarr;</span>
    <div class="node">3. Implementation<br>&amp; execution</div><span class="arr">&rarr;</span>
    <div class="node">4. Exit criteria<br>&amp; reporting</div><span class="arr">&rarr;</span>
    <div class="node">5. Test closure</div>
  </div>
  <p style="font-size:.6em;margin-top:.5em">These five steps are the spine of this course. Every technique and document we cover later plugs into one of them.</p>
</section>""",

"""<section>
  <span class="lbl">Step 1</span>
  <h3>Planning and Control</h3>
  <div class="g2">
    <div class="card"><strong>Test planning</strong>&middot; Define the scope and assess risks<br>&middot; Choose the test approach<br>&middot; Create the test strategy<br>&middot; Assign resources (people, environments, tools)<br>&middot; Build the schedule<br>&middot; Define exit criteria</div>
    <div class="card g"><strong>Test control</strong>Track progress against the plan and report it. This runs continuously through the whole project, not once at the start.</div>
  </div>
  <p style="font-size:.6em;margin-top:.4em">Planning is not paperwork for its own sake: it is where you decide what you will <em>not</em> test, and say so out loud. The output is a document &mdash; the <strong>test plan</strong>. You write one for your own project in <a href="homework/hw-09.html" style="color:var(--orange)">Homework 9</a>.</p>
</section>""",

"""<section>
  <span class="lbl">Step 2</span>
  <h3>Analysis and Design</h3>
  <ul style="font-size:.66em">
    <li>Review the test basis: requirements, design documents, risk analysis, architecture.</li>
    <li>Identify test conditions &mdash; what needs to be verified.</li>
    <li>Design test cases against those conditions.</li>
    <li>Evaluate testability of the requirements and of the system.</li>
    <li>Define test environment requirements and select tools.</li>
  </ul>
  <blockquote>If a requirement cannot be tested, that is a defect in the requirement. Say so now, not in the last sprint.</blockquote>
</section>""",

"""<section>
  <span class="lbl">Step 3</span>
  <h3>Implementation and Execution</h3>
  <div class="g2">
    <div class="card o"><strong>Test implementation</strong>&middot; Write and prioritise test cases<br>&middot; Create test data<br>&middot; Group cases into test suites<br>&middot; Prepare the test environment</div>
    <div class="card r"><strong>Test execution</strong>&middot; Run the suites<br>&middot; Compare actual to expected results<br>&middot; Report defects found<br>&middot; Run regression tests<br>&middot; Log what was run, in what order, and pass/fail</div>
  </div>
  <p style="font-size:.58em;margin-top:.4em">The log matters: a result you cannot reproduce or trace back to a version and environment is not evidence.</p>
</section>""",

"""<section>
  <span class="lbl">Steps 4 &amp; 5</span>
  <h3>Exit Criteria and Closure</h3>
  <div class="g2">
    <div class="card p"><strong>Evaluating exit criteria</strong>Different applications need different exit strategies, based on risk. For example:<br>&middot; A planned number of test cases executed with a defined pass rate<br>&middot; Defect rate below an agreed level<br>&middot; Deadlines reached.<br>Then decide: do we test more, or do we change the criteria?</div>
    <div class="card"><strong>Test closure</strong>&middot; Check the delivered software has the required functionality<br>&middot; Confirm the most important problems are resolved<br>&middot; Tidy up testware (documents, automated tests) for reuse<br>&middot; Hold a retrospective on the testing process itself</div>
  </div>
</section>""",

"""<section>
  <span class="lbl">Topic 5</span>
  <h3>The Seven Principles (1/2)</h3>
  <div class="card" style="margin-bottom:8px"><strong>1. Testing shows the presence of defects</strong>It can never prove their absence. "All tests passed" means "we found nothing with these tests".</div>
  <div class="card g" style="margin-bottom:8px"><strong>2. Exhaustive testing is impossible</strong>You cannot test every combination &mdash; we prove this on the next slide.</div>
  <div class="card o"><strong>3. Early testing saves time and money</strong>Start as early in the life cycle as possible. See the 1&times;&rarr;100&times; curve from Lesson 2.</div>
</section>""",

"""<section>
  <span class="lbl">In-Class Exercise</span>
  <div class="teams">
    <h3>Prove It &mdash; the Trip Planner</h3>
    <p style="font-size:.68em">Open the <a href="materials/input-form-example.html" style="color:#9b9fe3">trip planner form</a>. It has five dropdowns, each with five options.</p>
    <ul style="font-size:.7em">
      <li>How many different trip combinations exist from the dropdowns alone?</li>
      <li>Now add the free-text fields: travellers, budget, email, promo code. How many test cases would exhaustive testing need?</li>
      <li>At 30 seconds per manual test, how long would that take?</li>
      <li>So which combinations <em>would</em> you actually test &mdash; and on what basis?</li>
    </ul>
    <p style="font-size:.62em;margin-top:.4em">That last question is the whole of Lesson 7.</p>
  </div>
</section>""",

"""<section>
  <span class="lbl">Topic 5</span>
  <h3>The Seven Principles (2/2)</h3>
  <div class="card r" style="margin-bottom:8px"><strong>4. Defect clustering</strong>The most-used and most-complex functionality usually contains most of the defects. Follow the clusters.</div>
  <div class="card p" style="margin-bottom:8px"><strong>5. The pesticide paradox</strong>The same tests stop finding new bugs. Review and refresh your test set.</div>
  <div class="card" style="margin-bottom:8px"><strong>6. Testing is context dependent</strong>A banking system, a game and an internal admin tool are tested very differently.</div>
  <div class="card g"><strong>7. Absence-of-errors fallacy</strong>If the software does not meet the user's needs, finding and fixing defects will not make it a good product.</div>
</section>""",

"""<section>
  <span class="lbl">In-Class Exercise</span>
  <div class="teams">
    <h3>The Test Process in Real Life &mdash; Calculator</h3>
    <p style="font-size:.64em">In groups of 3&ndash;4, take a simple web calculator (two numbers, four operations, one result) and walk it through all five steps using the worksheet:</p>
    <ul style="font-size:.66em">
      <li>Planning and control &mdash; scope and risks (division by zero, negative numbers, empty fields)</li>
      <li>Analysis and design &mdash; test conditions and their priority</li>
      <li>Test creation &mdash; at least three test cases with inputs, steps and expected result</li>
      <li>Execution &mdash; mark PASS/FAIL, describe any failure</li>
      <li>Closure &mdash; was the testing sufficient? What was left uncovered?</li>
    </ul>
    <p style="font-size:.6em">Worksheet: <a href="materials/testing-process-worksheet.docx" style="color:#9b9fe3">Word version</a> &middot; <a href="homework/testing-process-worksheet.html" style="color:#9b9fe3">or fill it in on the page</a></p>
  </div>
</section>""",

"""<section>
  <span class="lbl">Self-Check</span>
  <h3>Can You Answer These?</h3>
  <ul style="font-size:.68em">
    <li>Name the five steps of the ISTQB test process in order.</li>
    <li>Why is it worth writing down the features you will <em>not</em> test?</li>
    <li>Write one entry criterion and one exit criterion for testing a login feature.</li>
    <li>Which principle explains why a regression suite that always passes might be worthless?</li>
    <li>In the V-model, which test level pairs with requirements analysis?</li>
  </ul>
</section>""",

"""<section>
  <div class="hw">
    <h3>Homework 2 &mdash; Test Process Worksheet</h3>
    <p style="font-size:.68em">Complete the five-step worksheet for the calculator and be ready to present it: what you covered, what you did not, and what you would improve in the next round.</p>
    <p style="font-size:.62em">Full brief: <a href="homework/hw-02.html">Homework 2</a></p>
  </div>
</section>""",
])

# ---------------- LESSON 4 ----------------
write_lesson(4,
 "Software Requirements",
 "Business vs system requirements &middot; FR and NFR &middot; SMART &middot; SRS",
 "What we test against &mdash; and how to tell a good requirement from a bad one",
 ["Business requirements vs system requirements",
  "Functional requirements &mdash; and why they are not user stories",
  "Non-functional requirements and their categories",
  "SMART &mdash; what makes a requirement testable",
  "The SRS document"],
 "Group project &mdash; write the requirements document for your own project (FR + NFR) using the SRS template.",
[
"""<section>
  <span class="lbl">Topic 1</span>
  <h3>From Business Need to a Testable Requirement</h3>
  """ + img("requirements-hierarchy.png", "Business requirements to user, product, functional and non-functional requirements", "80%",
            "High level on the left, detailed on the right") + """
  <p style="font-size:.6em">A requirement is a documented need that the product must satisfy. Business requirements say <em>why</em>; system requirements say <em>what</em>, in enough detail to build and to test.</p>
</section>""",

"""<section>
  <span class="lbl">Topic 1</span>
  <h3>The Chain You Will Use All Course</h3>
  <div class="chain">
    <div class="node">Business need</div><span class="arr">&rarr;</span>
    <div class="node">Business requirement</div><span class="arr">&rarr;</span>
    <div class="node">System requirement<br>(FR / NFR)</div><span class="arr">&rarr;</span>
    <div class="node">Test case</div><span class="arr">&rarr;</span>
    <div class="node">Bug report</div>
  </div>
  <div class="g2" style="margin-top:.5em">
    <div class="card"><strong>Functional requirements (FR)</strong>Describe <em>what</em> the software must do</div>
    <div class="card g"><strong>Non-functional requirements (NFR)</strong>Describe <em>how</em> the software must behave</div>
  </div>
  <p style="font-size:.58em;margin-top:.4em">Both must be SMART: specific, measurable, achievable, realistic, timely.</p>
</section>""",

"""<section>
  <span class="lbl">Topic 2</span>
  <h3>Functional Requirements Are Not User Stories</h3>
  <div class="card p" style="margin-bottom:8px"><strong>User story</strong>As a registered user, I want to be able to log into my account.</div>
  <div class="card g"><strong>Functional requirements derived from it</strong>
    &middot; The system must allow users to log in by entering their email and password.<br>
    &middot; The system must allow users to log in with a social account (Google, Facebook, LinkedIn).<br>
    &middot; The system must allow users to reset their password by clicking "I forgot my password" and receiving a link at their verified email address.
  </div>
  <blockquote>One user story becomes several functional requirements. Each functional requirement becomes several test cases. That chain is what makes testing traceable.</blockquote>
</section>""",

"""<section>
  <span class="lbl">Topic 2</span>
  <h3>Good and Bad Functional Requirements</h3>
  <table>
    <tr><th>Bad requirement</th><th>Good requirement</th></tr>
    <tr><td>The system should allow users to post jobs.</td><td>Employers must be able to post job listings by providing job title, job description, location, salary range and job type.</td></tr>
    <tr><td>Users should be able to search for jobs.</td><td>Users must be able to search for jobs by keyword and filter results by location, salary range and job type. Results are shown as a list and can be sorted by relevance, date posted or salary.</td></tr>
  </table>
  <p style="font-size:.6em;margin-top:.5em">Test the requirement before you test the code: can you write a test case from it that has exactly one expected result? If not, it is not finished.</p>
</section>""",

"""<section>
  <span class="lbl">Topic 3</span>
  <h3>Non-Functional Requirements (1/2)</h3>
  <table>
    <tr><th>Category</th><th>Meaning</th></tr>
    <tr><td>Availability</td><td>System is accessible when required</td></tr>
    <tr><td>Compatibility</td><td>System operates with other components</td></tr>
    <tr><td>Maintainability</td><td>System is easily modified for new needs</td></tr>
    <tr><td>Performance</td><td>System responds in time with minimum resource consumption</td></tr>
    <tr><td>Portability</td><td>System can be moved between environments</td></tr>
    <tr><td>Reliability</td><td>System performs its functions for a specified period</td></tr>
    <tr><td>Scalability</td><td>System grows with increased workload</td></tr>
    <tr><td>Security</td><td>System is protected against malicious access or use</td></tr>
    <tr><td>Usability</td><td>System is easy for a user to learn</td></tr>
  </table>
</section>""",

"""<section>
  <span class="lbl">Topic 3</span>
  <h3>Non-Functional Requirements (2/2)</h3>
  <table>
    <tr><th>Category</th><th>Meaning</th></tr>
    <tr><td>Certification</td><td>System meets necessary standards or conventions</td></tr>
    <tr><td>Compliance</td><td>System meets regulatory or legal constraints</td></tr>
    <tr><td>Localization</td><td>System supports several locales &mdash; languages, laws, currencies, cultures</td></tr>
    <tr><td>Service level agreements</td><td>System follows the formally agreed rules</td></tr>
    <tr><td>Extensibility</td><td>System can be updated with new functionality easily</td></tr>
  </table>
  <p style="font-size:.58em;margin-top:.4em">Several of these get a whole lesson later: accessibility and usability in Lesson 12, and performance and security in the bonus lessons.</p>
</section>""",

"""<section>
  <span class="lbl">Topic 3</span>
  <h3>Writing NFRs That Can Be Tested</h3>
  <div class="card p" style="margin-bottom:8px"><strong>User story</strong>As a user, I want to be able to use the website at any time.</div>
  <div class="card g" style="margin-bottom:8px"><strong>Requirements derived from it</strong>&middot; The system must be available 99% of the time each month during business hours.<br>&middot; The system must support at least 100 concurrent users.</div>
  <table>
    <tr><th>Bad</th><th>Good</th></tr>
    <tr><td>The system must respond quickly.</td><td>Each request must be processed within 3 seconds with 10,000 concurrent users.</td></tr>
    <tr><td>The system should be secure.</td><td>User data, including CVs, must be encrypted with industry-standard TLS in transit. Passwords must be hashed and salted. Access to applications and CVs is restricted to authorised personnel.</td></tr>
  </table>
</section>""",

"""<section>
  <span class="lbl">Topic 4</span>
  <h3>SMART Requirements</h3>
  <div class="g3">
    <div class="card"><strong>Specific</strong>One unambiguous behaviour, not a wish</div>
    <div class="card g"><strong>Measurable</strong>You can state a number or a clear yes/no</div>
    <div class="card o"><strong>Achievable</strong>Possible with the team, budget and technology</div>
    <div class="card r"><strong>Realistic</strong>Justified by real user need, not gold-plating</div>
    <div class="card p"><strong>Timely</strong>Has a defined time frame or release</div>
  </div>
  <blockquote>SMART is not paperwork. A requirement that is not measurable cannot fail a test &mdash; which means it cannot pass one either.</blockquote>
  <p style="font-size:.55em;color:#888">Source: BABOK, International Institute of Business Analysis</p>
</section>""",

"""<section>
  <span class="lbl">Topic 5</span>
  <h3>The SRS Document</h3>
  <p style="font-size:.63em">A Software Requirements Specification collects everything the team agreed to build: scope, functional requirements, non-functional requirements, interfaces, constraints &mdash; and later in this course, your test cases.</p>
  <div class="g2">
    <div class="card"><strong>Template</strong><a href="materials/Software Requirements Specification (SRS) Document Template.docx">SRS document template (.docx)</a></div>
    <div class="card g"><strong>Real examples</strong><a href="materials/srs_example_1.pdf">Example 1</a> &middot; <a href="materials/srs_example_2.pdf">Example 2</a><br><a href="https://www.reqview.com/doc/iso-iec-ieee-29148-srs-example/">ISO/IEC/IEEE 29148 example</a></div>
  </div>
  <p style="font-size:.58em;margin-top:.4em">Your SRS grows through the course: requirements now, architecture in Lesson 5, test cases in Lesson 10, and it gets peer reviewed by another team afterwards.</p>
</section>""",

"""<section>
  <span class="lbl">Self-Check</span>
  <h3>Can You Answer These?</h3>
  <ul style="font-size:.68em">
    <li>Turn "the app should be fast" into a testable non-functional requirement.</li>
    <li>Write one user story and derive three functional requirements from it.</li>
    <li>Which SMART letter does "the system should be user friendly" fail on?</li>
    <li>Name four NFR categories that apply to a public job-search site.</li>
  </ul>
</section>""",

"""<section>
  <div class="hw">
    <h3>Homework 3 &mdash; Requirements for Your Project</h3>
    <p style="font-size:.68em">In your team, write the requirements document for your own project using the SRS template. It must contain functional requirements and non-functional requirements, all of them SMART.</p>
    <p style="font-size:.63em">You will build the product against these requirements and test against them later &mdash; write them properly now.</p>
    <p style="font-size:.62em">Full brief: <a href="homework/hw-03.html">Homework 3</a></p>
  </div>
</section>""",
])

# ---------------- LESSON 5 ----------------
write_lesson(5,
 "Software Architecture",
 "Monolith &middot; Layered &middot; Microservices &middot; Event-driven &middot; Serverless &middot; Modular &middot; Monorepo",
 "How the system is put together &mdash; and what that means for testing it",
 ["What software architecture is and why a tester cares",
  "Seven architecture styles, with pros and cons",
  "How to choose an architecture",
  "What each style changes about testing"],
 "Group work &mdash; draw the architecture of your own project and justify the style you chose.",
[
"""<section>
  <span class="lbl">Topic 1</span>
  <h3>What Is Software Architecture?</h3>
  <p style="font-size:.64em">Architecture describes the structure of a system: which components exist, and how they work together. A good architecture gives the system scalability, maintainability and the ability to adapt.</p>
  <blockquote>For a tester, architecture answers a practical question: <em>where can I observe this behaviour, and where can I break it?</em> The same defect in a monolith and across microservices needs completely different test setups.</blockquote>
</section>""",

"""<section>
  <span class="lbl">Topic 2</span>
  <h3>Monolithic Architecture</h3>
  <div class="g2">
    <div class="card"><strong>What it is</strong>One single application where all parts of the system are tightly coupled &mdash; user interface, business logic and data access ship together as one deployable unit.</div>
    <div class="card g"><strong>Advantages</strong>Simple to develop, run locally and deploy for smaller applications. One place to look when something breaks.</div>
  </div>
  <div class="g2" style="margin-top:8px">
    <div class="card r"><strong>Disadvantages</strong>Hard to maintain and scale as the system grows. One change means redeploying everything.</div>
    <div class="card o"><strong>Example</strong>Early web applications and early e-commerce platforms.</div>
  </div>
  <p style="font-size:.58em;margin-top:.4em"><strong>Testing angle:</strong> easy to spin up end to end &mdash; but every change needs a full regression run.</p>
</section>""",

"""<section>
  <span class="lbl">Topic 2</span>
  <h3>Layered Architecture</h3>
  <div class="g2">
    <div class="figure" style="margin:0"><img src="images/arch-layered.png" alt="Layered architecture: presentation, business, persistence, database" style="max-height:320px"></div>
    <div>
      <div class="card"><strong>What it is</strong>The application is split into layers &mdash; presentation, business, persistence, database. Each layer talks only to the one below it.</div>
      <div class="card g" style="margin-top:6px"><strong>Advantages</strong>Clear separation of concerns; straightforward to develop and maintain.</div>
      <div class="card r" style="margin-top:6px"><strong>Disadvantages</strong>Can become rigid once layers start depending on each other.</div>
    </div>
  </div>
  <p style="font-size:.56em;margin-top:.4em"><strong>Testing angle:</strong> the layers give you natural test levels &mdash; unit tests in the business layer, integration tests at the persistence layer, UI tests at the top.</p>
</section>""",

"""<section>
  <span class="lbl">Topic 2</span>
  <h3>Microservices Architecture</h3>
  """ + img("arch-microservices.png", "Microservices with separate databases behind a user interface", "62%",
            "Independent services, each with its own database, talking over APIs") + """
  <p style="font-size:.58em">+ scalability, independent deployments, technology flexibility per service &nbsp;&middot;&nbsp; &ndash; more complex to deploy and operate; the network becomes a failure mode. Examples: Netflix, Amazon.</p>
  <p style="font-size:.56em;color:#888"><strong>Testing angle:</strong> most defects live <em>between</em> services, not inside them. API and contract testing matter more than clicking the UI.</p>
</section>""",

"""<section>
  <span class="lbl">Topic 2</span>
  <h3>Event-Driven Architecture</h3>
  """ + img("arch-event-driven.png", "Event sources publishing to an event broker with subscribers", "64%",
            "Event sources publish; an event broker routes; subscribers react to what they subscribed to") + """
  <p style="font-size:.58em">+ excellent for dynamic and distributed systems &nbsp;&middot;&nbsp; &ndash; harder to trace and debug, because there is no single call stack. Examples: real-time data systems, financial applications.</p>
  <p style="font-size:.56em;color:#888"><strong>Testing angle:</strong> ordering, duplicate and lost events are the classic defects. Expect asynchronous tests, waits and correlation IDs.</p>
</section>""",

"""<section>
  <span class="lbl">Topic 2</span>
  <h3>Serverless Architecture</h3>
  """ + img("arch-serverless.png", "Serverless architecture with an API gateway and functions", "68%",
            "Clients reach an API gateway; each piece of logic is a separate managed function") + """
  <p style="font-size:.58em">+ no infrastructure to manage, scales automatically &nbsp;&middot;&nbsp; &ndash; best suited to smaller, self-contained tasks; cold starts and vendor limits are real. Examples: AWS Lambda, Google Cloud Functions.</p>
  <p style="font-size:.56em;color:#888"><strong>Testing angle:</strong> you cannot attach a debugger to production. Logging, tracing and testing each function in isolation carry the load.</p>
</section>""",

"""<section>
  <span class="lbl">Topic 2</span>
  <h3>Modular Architecture and Monorepo</h3>
  <div class="g2">
    <div>
      <div class="figure" style="margin:0"><img src="images/arch-modular.png" alt="Modular architecture with plugins merged into one output" style="max-height:260px"><div class="cap">Modular &mdash; plugins added and removed independently</div></div>
      <p style="font-size:.55em">+ flexible and easy to extend &nbsp;&middot;&nbsp; &ndash; module dependencies get tangled. Example: browsers and their plugins.</p>
    </div>
    <div>
      <div class="figure" style="margin:0"><img src="images/arch-monorepo.png" alt="Monorepo with apps and libraries in one dependency graph" style="max-height:260px"><div class="cap">Monorepo &mdash; every app and library in one code base</div></div>
      <p style="font-size:.55em">+ faster builds and tests through dependency tracking, shared code, one workflow &nbsp;&middot;&nbsp; &ndash; the graph gets complex at scale. Examples: Google, Uber, Airbnb.</p>
    </div>
  </div>
</section>""",

"""<section>
  <span class="lbl">Topic 3</span>
  <h3>How to Choose an Architecture</h3>
  <ul style="font-size:.68em">
    <li>Size and complexity of the project</li>
    <li>Size and experience of the team</li>
    <li>Scalability and maintainability requirements</li>
    <li>Budget and schedule</li>
    <li>Technology constraints and where the product is heading</li>
  </ul>
  <blockquote>There is no best architecture. There is the one whose trade-offs you can live with &mdash; and that you can afford to test.</blockquote>
</section>""",

"""<section>
  <span class="lbl">In-Class Exercise</span>
  <div class="teams">
    <h3>Draw Your Project's Architecture</h3>
    <ul style="font-size:.7em">
      <li>As a team, draw the software architecture of your own project.</li>
      <li>Decide which of the styles above fits your project best &mdash; and why.</li>
      <li>Draw a simple diagram: components, the relationships between them, and the communication channels.</li>
      <li>Add notes explaining why this architecture is the right choice for your project.</li>
      <li>Present to the class: why you chose it, and what challenges you expect.</li>
    </ul>
  </div>
</section>""",

"""<section>
  <span class="lbl">Self-Check</span>
  <h3>Can You Answer These?</h3>
  <ul style="font-size:.68em">
    <li>Give one advantage and one disadvantage of microservices compared to a monolith.</li>
    <li>Your project has 3 developers and 4 months. Which style would you argue for, and why?</li>
    <li>Which architecture makes a defect hardest to trace, and what would you do about it as a tester?</li>
    <li>Where would you place an integration test in a layered architecture?</li>
  </ul>
</section>""",

"""<section>
  <div class="hw">
    <h3>Homework 4 &mdash; Project Architecture</h3>
    <p style="font-size:.68em">Add an architecture diagram and a short justification to your team's SRS document.</p>
    <p style="font-size:.62em">Full brief: <a href="homework/hw-04.html">Homework 4</a></p>
  </div>
</section>""",
])
