# -*- coding: utf-8 -*-
from tpl import *

# ---------------- LESSON 1 ----------------
write_lesson(1,
 "Testing Fundamentals &amp; the Quality Mindset",
 "Course intro &middot; Using AI in this course &middot; What is quality &middot; What can be tested",
 "Course introduction and what software quality actually means",
 ["Course introduction &mdash; structure, grading, prerequisites",
  "Using AI in this course &mdash; the ground rules",
  "Who is teaching this &mdash; and who are you",
  "What is quality? &mdash; car or code, and the seven aspects",
  "What is testing? What can be tested? Verification vs validation"],
 "",
[
"""<section>
  <span class="lbl">About Me</span>
  <div class="bio-grid">
    <div class="bio-left">
      <img class="portrait" src="images/instructor.jpg" alt="Tatjana Kirotar" style="margin-bottom:.5em">
      <div class="name">Tatjana Kirotar</div>
      <div class="role">Staff QA Engineer / QA Lead</div>
      <div style="font-size:.85em;color:#aaa">Teams &middot; Tatjana Kirotar<br>Tatjana.Kirotar@techno.ee<br>tatjana.kirotar@gmail.com</div>
    </div>
    <div class="timeline">
      <p><strong>Working experience:</strong></p>
      <p><span class="year">2025 &ndash;</span> &nbsp;<strong>DoorDash / Wolt / Deliveroo</strong> &mdash; Staff QA Engineer / Lead QA</p>
      <p><span class="year">2023 &ndash;</span> &nbsp;<strong>TPT</strong> &mdash; Visiting Lecturer</p>
      <p><span class="year">2020&ndash;25</span> <strong>CyberCube</strong> &mdash; QA Automation Engineer &rarr; Engineering Manager</p>
      <p><span class="year">2019</span> &nbsp;&nbsp;&nbsp;<strong>Testlio</strong> &mdash; Test Automation Specialist</p>
      <p><span class="year">2015&ndash;19</span> <strong>Evitec</strong> &mdash; QA Engineer &rarr; System Analyst</p>
      <p><span class="year">2016&ndash;19</span> <strong>TalTech</strong> &mdash; Assistant / Visiting Lecturer</p>
      <p style="margin-top:.4em"><strong>Education:</strong> &nbsp;<span class="year">MSc</span> Engineering, TalTech &nbsp;&middot;&nbsp; <span class="year">BSc</span> Engineering, TalTech</p>
      <p style="margin-top:.3em;color:#888">Languages: Estonian &middot; English &middot; Russian</p>
    </div>
  </div>
</section>""",

"""<section>
  <span class="lbl">About This Course</span>
  <h3>Course Overview</h3>
  <div class="g2">
    <div>
      <div class="card" style="margin-bottom:8px">
        <strong>Structure</strong>
        2 &times; 45 min &middot; TPT<br>
        New topic + in-class exercise
      </div>
      <div class="card g">
        <strong>Goal</strong>
        You can test the software you build yourself:<br>
        &middot; Requirements<br>&middot; Documentation<br>&middot; Techniques<br>&middot; Defects
      </div>
    </div>
    <div>
      <div class="card o" style="margin-bottom:8px">
        <strong>Grading</strong>
        Practical assignments, presented in class:<br>
        &middot; Group work<br>&middot; In-class exercises
      </div>
      <div class="card p">
        <strong>Prerequisites</strong>
        Programming Basics (any language)<br>
        Curiosity + willingness to break things
      </div>
    </div>
  </div>
  <p style="font-size:.65em;margin-top:.5em">Key references: ISTQB Foundation &middot; Agile Methodology &middot; <em>Clean Code</em> by Robert C. Martin &middot; BABOK</p>
</section>""",

"""<section>
  <span class="lbl">Where the Course Lives</span>
  <h3>Two Places &mdash; Teams and the Course Site</h3>
  <div class="g2">
    <div class="card"><strong>Teams</strong>
      &middot; Tarkvara testimise alused (2026)<br>
      &middot; Tarkvara testimine (2026)<br>
      <span style="color:#888">Announcements &middot; homework submissions &middot; questions between lessons</span></div>
    <div class="card g"><strong>The course site</strong>
      Every lesson, every assignment brief and all course materials on one page:<br>
      &middot; tanjaq.github.io/Tarkvara-testimise-alused<br>
      <span style="color:#888">Slides, homework briefs, worksheets and templates</span></div>
  </div>
  <div class="card o" style="margin-top:10px"><strong>Nothing to install</strong>Both work on a phone. Follow along during the lesson, and redo an exercise afterwards.</div>
</section>""",

"""<section>
  <span class="lbl">Topic 2</span>
  <div class="ai">
    <h3>Using AI in This Course</h3>
    <p style="font-size:.68em">AI tools &mdash; ChatGPT, Claude, Gemini, Copilot and the rest &mdash; are <strong>allowed and encouraged</strong> in my subjects. Using AI well is a real skill for both developers and testers today.</p>
    <div class="g2" style="margin-top:.4em">
      <div class="card g" style="border-left-color:var(--green)"><strong>The golden rule</strong>Use AI &mdash; but use it with your brain engaged.<br>You are always responsible for the result, not the AI. You must be able to explain and justify every piece of homework you submit.</div>
      <div class="card r"><strong>Trust, but verify</strong>AI can draft your first test cases, explain code and produce a documentation skeleton.<br>AI does not know your requirements, does not know your users, and does not know whether its own answer is correct.</div>
    </div>
    <p style="font-size:.6em;margin-top:.5em">Full treatment, with worked good and bad examples: <a href="lesson-bonus-ai.html" style="color:var(--orange)">bonus lesson on using AI responsibly</a>.</p>
  </div>
</section>""",

"""<section>
  <span class="lbl">Syllabus</span>
  <h3>What We Cover</h3>
  <div class="g3" style="font-size:.95em">
    <div class="card"><strong>Foundations</strong>1. Quality mindset<br>2. Purpose of testing<br>3. The testing process</div>
    <div class="card g"><strong>Design inputs</strong>4. Software requirements<br>5. Software architecture</div>
    <div class="card o"><strong>Techniques</strong>6. Static testing<br>7. Black box<br>8. White box</div>
    <div class="card r"><strong>Documentation</strong>9. Defects &amp; exploratory testing<br>10. Test cases &amp; documentation</div>
    <div class="card p"><strong>Specialised testing</strong>11. Database &amp; SQL<br>12. Accessibility<br>13. Mobile</div>
    <div class="card"><strong>Bonus lessons</strong>Using AI responsibly<br>Performance testing<br>Application security</div>
  </div>
  <p style="font-size:.55em;color:#888;margin-top:.6em">The topics and exercises are chosen for what the job market actually expects from a junior QA engineer or developer.</p>
</section>""",

"""<section>
  <div class="teams">
    <h3>👋 Your Turn &mdash; Let's Meet</h3>
    <p style="font-size:.63em">Speak up &mdash; we go round the room.</p>
    <div class="g2" style="margin-top:.5em">
      <div>
        <p style="font-size:.75em;color:var(--blue);font-weight:600">Questions:</p>
        <ul style="font-size:.70em;line-height:2">
          <li>What&rsquo;s your tech stack? (JS / Python / Java&hellip;)</li>
          <li>Projects you&rsquo;ve worked on?</li>
          <li>Testing experience so far?</li>
          <li>What do you want from this course?</li>
        </ul>
      </div>
      <div class="card" style="font-size:.50em">
        <strong>Why I'm asking:</strong>
        I'll adapt examples to your stack.<br>
        Your goals shape what we spend more time on.<br><br>
        No wrong answers &mdash; "zero experience" is a valid and welcome answer!
      </div>
    </div>
  </div>
</section>""",

"""<section>
  <span class="lbl">Topic 3</span>
  <h3>Quality is Quality &mdash; Car or Code, Same Standard</h3>
  <div class="g2" style="margin-top:.5em">
    <div style="background:rgba(255,255,255,.04);border-radius:10px;padding:14px;text-align:center;border:1px solid rgba(255,255,255,.12)">
      <div style="font-size:2em;margin-bottom:.2em">🚗</div>
      <div style="font-size:.58em;color:var(--orange);font-weight:700;margin-bottom:.5em;text-transform:uppercase;letter-spacing:2px">A quality car&hellip;</div>
      <ul style="text-align:left;font-size:.62em;line-height:1.9">
        <li>Starts every time you turn the key</li>
        <li>Does what the brochure says</li>
        <li>Doesn&rsquo;t break down unexpectedly</li>
        <li>Looks and feels consistent throughout</li>
        <li>Is easy to service and maintain</li>
        <li>Worth what you paid for it</li>
      </ul>
    </div>
    <div style="background:rgba(79,195,247,.05);border-radius:10px;padding:14px;text-align:center;border:1px solid rgba(79,195,247,.3)">
      <div style="font-size:2em;margin-bottom:.2em">🖥️</div>
      <div style="font-size:.58em;color:var(--blue);font-weight:700;margin-bottom:.5em;text-transform:uppercase;letter-spacing:2px">Quality software&hellip;</div>
      <ul style="text-align:left;font-size:.62em;line-height:1.9">
        <li>Works every time you run it</li>
        <li>Does what the requirements say</li>
        <li>Doesn&rsquo;t crash unexpectedly</li>
        <li>Behaves consistently across features</li>
        <li>Is easy to maintain and extend</li>
        <li>Worth what it cost to build</li>
      </ul>
    </div>
  </div>
  <blockquote>Quality is quality. The standard is the same &mdash; whether it rolls on four wheels or runs on a server.</blockquote>
</section>""",

"""<section>
  <span class="lbl">Topic 3</span>
  <h3>What Is (Software) Quality?</h3>
  <div class="g2">
    <div>
      <div class="card" style="margin-bottom:6px"><strong>Understandable design</strong>A user can figure out what to do without a manual</div>
      <div class="card g" style="margin-bottom:6px"><strong>Suitable functionality</strong>It does the job it was bought or built for</div>
      <div class="card o" style="margin-bottom:6px"><strong>Reliability</strong>It behaves the same way every time</div>
      <div class="card r"><strong>Consistency</strong>The same action produces the same result across the product</div>
    </div>
    <div>
      <div class="card p" style="margin-bottom:6px"><strong>Durability</strong>It keeps working as data, users and load grow</div>
      <div class="card" style="margin-bottom:6px"><strong>After-sales service</strong>Support, updates, bug fixes</div>
      <div class="card g"><strong>Value for money</strong>The cost is justified by what you get</div>
    </div>
  </div>
  <blockquote>Quality software is defect-free software, delivered on time and within budget, that meets requirements and expectations &mdash; and is maintainable.</blockquote>
</section>""",

"""<section>
  <span class="lbl">Topic 4</span>
  <h3>What Is Testing?</h3>
  <p style="font-size:.66em">The process of evaluating software quality and checking whether the product:</p>
  <div class="g2" style="margin-top:.4em">
    <div class="card"><strong>Meets requirements</strong>Both the business requirements and the technical ones</div>
    <div class="card g"><strong>Works as expected</strong>And is fit for the end user's actual purpose</div>
  </div>
  <blockquote>Software testing is the process of executing a program or application with the intent of finding software defects.</blockquote>
  <p style="font-size:.55em;color:#888">Note the two halves: <em>evaluating quality</em> (are we building the right thing?) and <em>finding defects</em> (are we building it right?).</p>
</section>""",

"""<section>
  <span class="lbl">Topic 4</span>
  <h3>What Can Be Tested? &mdash; Everything</h3>
  <div class="g2">
    <div>
      <div class="card" style="margin-bottom:6px"><strong>Business analysis document</strong>Describes end-user needs. Is it complete? Unambiguous?</div>
      <div class="card g" style="margin-bottom:6px"><strong>System analysis / design document</strong>Does it match the business analysis? Are FR and NFR both covered?</div>
      <div class="card o"><strong>Source code</strong>Does it meet the requirements? Readable, maintainable, testable?</div>
    </div>
    <div>
      <div class="card r" style="margin-bottom:6px"><strong>Installation guide</strong>Sufficient? Repeatable by someone new?</div>
      <div class="card p" style="margin-bottom:6px"><strong>Installed software</strong>Works as expected, meets requirements</div>
      <div class="card"><strong>User manual</strong>Understandable, traceable, repeatable</div>
    </div>
  </div>
  <p style="font-size:.58em;margin-top:.5em">Testing is not "clicking the app at the end". Every artefact in the project can be tested &mdash; and the earlier you test it, the cheaper the fix.</p>
</section>""",

"""<section>
  <span class="lbl">Topic 5</span>
  <h3>Two Words You Will Use Constantly</h3>
  <div class="g2">
    <div class="card"><strong>Verification</strong>Are we building the product <em>right</em>?<br>Does it match the specification, the design, the standard?<br><span style="color:#888">Reviews, static analysis, unit tests</span></div>
    <div class="card g"><strong>Validation</strong>Are we building the <em>right</em> product?<br>Does it solve the user's actual problem?<br><span style="color:#888">Acceptance testing, user feedback, demos</span></div>
  </div>
  <blockquote>A product can pass every verification check and still fail validation &mdash; it was built exactly as specified, and the specification was wrong.</blockquote>
</section>""",

"""<section>
  <span class="lbl">And One More Thing</span>
  <h3>Know What You Are Actually Claiming</h3>
  """ + img("fullstack-meme.png", "Everyone can do everything badly - full stack developer meme", "48%") + """
  <p style="font-size:.6em">"It works" is a claim. This course is about being able to say precisely <em>what</em> works, <em>under which conditions</em>, and <em>what you did not check</em>.</p>
</section>""",

"""<section>
  <span class="lbl">Self-Check</span>
  <h3>Can You Answer These?</h3>
  <ul style="font-size:.68em">
    <li>Name four aspects of software quality and give an example of each from an app you use.</li>
    <li>Give one artefact other than code that can be tested, and say what you would check in it.</li>
    <li>Explain verification vs validation in your own words.</li>
    <li>Why is "the software has no known bugs" not the same as "the software has quality"?</li>
    <li>What are you responsible for when you use AI on a homework submission?</li>
  </ul>
</section>""",

"""<section>
  <div class="hw">
    <h3>Something to Think About</h3>
    <p style="font-size:.68em">No homework for this lesson &mdash; but come to the next one ready to talk:</p>
    <ul style="font-size:.7em">
      <li>Think of <strong>one piece of software you consider high quality</strong>. Which of the seven aspects does it deliver on?</li>
      <li>Think of <strong>one you consider poor quality</strong>. What specifically fails?</li>
    </ul>
    <p style="font-size:.62em;margin-top:.4em">Everyday apps count &mdash; a bank app, a ticket site, a game. We start the next lesson with your examples.</p>
  </div>
</section>""",
])

# ---------------- LESSON 2 ----------------
write_lesson(2,
 "The Purpose of Testing",
 "Why we test &middot; Real-world failures &middot; Cost of defects &middot; Where bugs come from",
 "Why testing exists &mdash; what it costs not to do it",
 ["Why test? &mdash; famous software failures",
  "Consequences of software defects",
  "Where do defects come from?",
  "The cost of a defect over time",
  "The goals of software testing"],
 "Group work &mdash; pick a real software failure, analyse what happened and what testing would have caught it.",
[
"""<section>
  <span class="lbl">Topic 1</span>
  <h3>Testing Happens Everywhere, Not Only in Software</h3>
  """ + img("iihs-safety-ratings.png", "IIHS vehicle safety ratings table", "42%",
            "Independent crash-test ratings for midsize cars. Somebody defined the criteria, ran the tests and published the results &mdash; that is exactly what a test report is.") + """
  <p style="font-size:.6em">You already trust test results every day. The question is what happens when nobody runs them.</p>
</section>""",

"""<section>
  <span class="lbl">Topic 1</span>
  <h3>Users Tell You About Quality &mdash; Constantly</h3>
  <div class="g2">
    <div class="figure" style="margin:0"><img src="images/uber-reviews.png" alt="Uber app store reviews" style="max-height:320px"><div class="cap">Uber &mdash; 4.8</div></div>
    <div class="figure" style="margin:0"><img src="images/lyft-reviews.png" alt="Lyft app store reviews" style="max-height:320px"><div class="cap">Lyft &mdash; 4.9</div></div>
  </div>
  <p style="font-size:.58em;margin-top:.4em">App store reviews are unstructured defect reports written by your users. They arrive too late and cost you the customer &mdash; but they are still evidence of quality.</p>
</section>""",

"""<section>
  <span class="lbl">Topic 1</span>
  <h3>Why Test? &mdash; Real Failures</h3>
  <div class="newsgrid">
    <div><img src="images/uber-affair.png" alt="Uber notification bug headline"><div class="n"><strong>Uber, 2017</strong> &mdash; a man ordered a ride from his wife's phone and logged out. The app kept sending notifications to her phone, revealing his travel history. The couple divorced; he sued Uber for &euro;45m.</div></div>
    <div><img src="images/gangnam-style.png" alt="Gangnam Style broke YouTube view counter"><div class="n"><strong>YouTube, 2014</strong> &mdash; the view counter was a signed 32-bit integer. It broke past 2,147,483,647 views. A boundary value defect, live, in front of a billion people.</div></div>
    <div><img src="images/tesla-recall.png" alt="Tesla recall over computer memory failure"><div class="n"><strong>Tesla, 2021</strong> &mdash; 135,000 cars recalled. Flash memory in the touchscreen wore out, taking the rear-view camera and defroster controls with it.</div></div>
  </div>
</section>""",

"""<section>
  <span class="lbl">Topic 1</span>
  <h3>When Software Kills</h3>
  <div class="newsgrid">
    <div><img src="images/boeing-737max.png" alt="Boeing 737 MAX killer software headline"><div class="n"><strong>Boeing 737 MAX, 2018 &amp; 2019</strong> &mdash; the MCAS system relied on a single angle-of-attack sensor. Two crashes, 346 people dead. No redundancy, and pilots were not told the system existed.</div></div>
    <div><img src="images/starliner.png" alt="Boeing Starliner software errors headline"><div class="n"><strong>Boeing Starliner, 2020</strong> &mdash; two software defects in one flight: the spacecraft clock was 11 hours off, and the wrong thrusters fired. Investigators blamed the engineering culture, not one programmer.</div></div>
    <div><img src="images/crowdstrike-airport.jpg" alt="CrowdStrike outage blue screen at an airport"><div class="n"><strong>CrowdStrike, 2024</strong> &mdash; a faulty content update crashed ~8.5 million Windows machines worldwide. Airports, hospitals and banks stopped. Estimated damage: ~US$10 billion.</div></div>
  </div>
  <p style="font-size:.5em;color:#888;margin-top:.4em">Data breaches belong on the same list: T-Mobile 2022 (37M users) &middot; Juspay 2021 (card data) &middot; Yahoo 2014 (500M users).</p>
</section>""",

"""<section>
  <span class="lbl">Topic 1</span>
  <h3>It Happens Close to Home Too</h3>
  <div class="g2">
    <div class="card r"><strong>A national building register</strong>Municipalities missed statutory deadlines because of defects in a newly launched register &mdash; a government system where the deadline is written into law.</div>
    <div class="card o"><strong>A national social insurance system</strong>A large public IT project that failed after years of work. Requirements overloaded, multiple procurement disputes, deadlines missed, the system never delivered as specified.</div>
  </div>
  <blockquote>Most failures are not "someone wrote a bad line of code". They are requirements that were never clear, and testing that started too late.</blockquote>
</section>""",

"""<section>
  <span class="lbl">In-Class Exercise</span>
  <div class="teams">
    <h3>Group Work &mdash; Anatomy of a Failure</h3>
    <ul style="font-size:.72em">
      <li>Form groups of 3&ndash;4.</li>
      <li>Pick one example from the slides, or find your own software failure online.</li>
      <li>Answer together:
        <ul style="font-size:.95em">
          <li>What happened?</li>
          <li>What were the consequences?</li>
          <li>What testing should have been done to prevent it?</li>
        </ul>
      </li>
      <li>Time: 10&ndash;15 minutes. Each group gives a 2&ndash;3 minute summary.</li>
    </ul>
  </div>
</section>""",

"""<section>
  <span class="lbl">Topic 2</span>
  <h3>Consequences of Software Defects</h3>
  <div class="g2">
    <div>
      <div class="card o" style="margin-bottom:6px"><strong>Time and money to fix</strong>The defect itself, plus everything blocked behind it</div>
      <div class="card r" style="margin-bottom:6px"><strong>Loss of reputation</strong>The hardest one to buy back</div>
      <div class="card p"><strong>Direct financial loss</strong>Lost sales, refunds, contractual penalties, fines</div>
    </div>
    <div>
      <div class="card" style="margin-bottom:6px"><strong>Loss of human life</strong>Aviation, medical, automotive, industrial control</div>
      <div class="card g"><strong>Environmental damage</strong>Control systems for energy, water, chemicals</div>
    </div>
  </div>
</section>""",

"""<section>
  <span class="lbl">Topic 3</span>
  <h3>Where Do Defects Come From?</h3>
  <p style="font-size:.62em">Every step of development has a moment where a human mistake becomes a defect.</p>
  <ul style="font-size:.63em">
    <li><strong>The customer</strong> may not know exactly what they want, or forgets to state an important requirement.</li>
    <li><strong>The analyst</strong> may misinterpret the requirement, or never document it.</li>
    <li><strong>Design decisions</strong> made early create defects that only surface later.</li>
    <li><strong>Development</strong> introduces coding errors and misread specifications.</li>
    <li><strong>Testing</strong> misses defects because of time pressure, thin experience or incomplete documentation.</li>
    <li><strong>Acceptance testing</strong> does not cover everything, and the defect ships to production.</li>
  </ul>
  <blockquote>Notice how few of these are "the developer wrote bad code". Most defects are born before anyone starts typing.</blockquote>
</section>""",

"""<section>
  <span class="lbl">Topic 4</span>
  <h3>The Cost of a Defect Grows With Time</h3>
  <div class="chain">
    <div class="node">Requirements<br><strong style="color:var(--green)">1&times;</strong></div><span class="arr">&rarr;</span>
    <div class="node">Design<br><strong style="color:var(--green)">3&times;</strong></div><span class="arr">&rarr;</span>
    <div class="node">Development<br><strong style="color:var(--orange)">10&times;</strong></div><span class="arr">&rarr;</span>
    <div class="node">QA / Testing<br><strong style="color:var(--orange)">25&times;</strong></div><span class="arr">&rarr;</span>
    <div class="node">Production<br><strong style="color:var(--red)">100&times;</strong></div>
  </div>
  <div class="g2" style="margin-top:.5em">
    <div class="card r"><strong>Why defects escape to production</strong>&middot; Cannot be reproduced<br>&middot; Found too late<br>&middot; Team decided not to fix<br>&middot; The fix created a new defect<br>&middot; "It's not a bug, it's a feature"</div>
    <div class="card g"><strong>What this means for you</strong>A tester reviewing a requirements document is doing the single cheapest quality work available in the whole project.</div>
  </div>
</section>""",

"""<section>
  <span class="lbl">Topic 5</span>
  <h3>The Goals of Software Testing</h3>
  <div class="g2">
    <div>
      <div class="card" style="margin-bottom:6px"><strong>Find defects</strong>Introduced at any point in development</div>
      <div class="card g" style="margin-bottom:6px"><strong>Prevent defects</strong>By reviewing requirements and designs early</div>
      <div class="card o"><strong>Build confidence</strong>Give the business real information about quality level</div>
    </div>
    <div>
      <div class="card p" style="margin-bottom:6px"><strong>Prove conformance</strong>To business requirements and to the system specification</div>
      <div class="card r"><strong>Earn customer trust</strong>By shipping a product that behaves</div>
    </div>
  </div>
  <p style="font-size:.6em;margin-top:.5em">Coverage is the key metric: design test cases so that as much functionality as possible is exercised and as many problems as possible are found.</p>
</section>""",

"""<section>
  <span class="lbl">Self-Check</span>
  <h3>Can You Answer These?</h3>
  <ul style="font-size:.68em">
    <li>Pick one failure from this lesson. At which stage was the defect actually introduced?</li>
    <li>Why does a defect found in production cost roughly 100&times; a defect found in requirements?</li>
    <li>Give two reasons a known defect might still be shipped.</li>
    <li>Name three goals of testing beyond "find bugs".</li>
  </ul>
</section>""",

"""<section>
  <div class="hw">
    <h3>Homework 1 &mdash; Failure Case Analysis</h3>
    <p style="font-size:.68em">In your group, write up the failure you analysed in class: what happened, what the consequences were, which testing activity would have caught it, and at which stage the defect was introduced.</p>
    <p style="font-size:.62em">Full brief: <a href="homework/hw-01.html">Homework 1</a></p>
  </div>
</section>""",
])
