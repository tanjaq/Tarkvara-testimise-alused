# -*- coding: utf-8 -*-
from tpl import *

# ---------------- LESSON 11 ----------------
write_lesson(11,
 "Database &amp; SQL Testing",
 "Why data hides defects &middot; SQL for testers &middot; Integrity &middot; Migrations &middot; Test data",
 "Checking what the application actually stored, not what the screen claims",
 ["Why a tester needs SQL",
  "The SQL you actually need &mdash; SELECT, WHERE, JOIN, GROUP BY",
  "Verifying a UI action against the database",
  "Data integrity defects and where they hide",
  "Migrations and test data management"],
 "Load the sample shop database, verify the requirements with SQL and find the data defects hiding in it.",
[
"""<section>
  <span class="lbl">Topic 1</span>
  <h3>The Screen Is Not the Truth</h3>
  <p style="font-size:.64em">The user interface shows you what the application <em>says</em> happened. The database shows you what actually happened. These are not always the same thing.</p>
  <div class="g2">
    <div class="card r"><strong>Defects the UI will happily hide</strong>
      &middot; The order was saved twice<br>
      &middot; The amount was rounded to 2 decimals for display but stored with 6<br>
      &middot; The "deleted" record is still there, just flagged<br>
      &middot; The timestamp was stored in the wrong timezone<br>
      &middot; The cancel button updated the screen and nothing else</div>
    <div class="card g"><strong>What SQL gives you</strong>
      &middot; Proof, not inference<br>
      &middot; The ability to set up exactly the test data you need<br>
      &middot; A way to check 10,000 rows instead of 3 screens<br>
      &middot; Evidence to attach to a bug report</div>
  </div>
</section>""",

"""<section>
  <span class="lbl">Topic 2</span>
  <h3>The SQL You Actually Need</h3>
  <pre><code class="language-sql">-- 1. Look at a table
SELECT * FROM orders LIMIT 20;

-- 2. Filter
SELECT id, total, status FROM orders WHERE status = 'PAID' AND total > 100;

-- 3. Count and group
SELECT status, COUNT(*) FROM orders GROUP BY status;

-- 4. Join two tables
SELECT o.id, c.email, o.total
FROM orders o
JOIN customers c ON c.id = o.customer_id
WHERE o.created_at >= '2026-01-01';

-- 5. Find what should not exist
SELECT * FROM orders WHERE customer_id NOT IN (SELECT id FROM customers);</code></pre>
  <p style="font-size:.58em;margin-top:.3em">Five patterns cover most of a tester's day. Query 5 is the one that finds real defects.</p>
</section>""",

"""<section>
  <span class="lbl">Topic 2</span>
  <h3>JOIN Types &mdash; and the Defect They Cause</h3>
  <div class="g2">
    <div class="card"><strong>INNER JOIN</strong>Only rows that match on both sides. Silently <em>drops</em> anything unmatched.</div>
    <div class="card g"><strong>LEFT JOIN</strong>All rows from the left table, matched or not. Unmatched right-hand columns come back NULL.</div>
  </div>
  <blockquote>A report that "lost" 40 orders overnight is very often an INNER JOIN against a table where some rows have a NULL foreign key. Swap it to LEFT JOIN and count again &mdash; if the number changes, you have found the defect.</blockquote>
  <p style="font-size:.6em">Same trap with <code>NULL</code>: <code>WHERE status != 'PAID'</code> does <strong>not</strong> return rows where status is NULL. You need <code>OR status IS NULL</code>.</p>
</section>""",

"""<section>
  <span class="lbl">Topic 3</span>
  <h3>Verifying a UI Action Against the Database</h3>
  <div class="chain">
    <div class="node">1. Note the state<br><span style="font-size:.85em;color:#888">query before</span></div><span class="arr">&rarr;</span>
    <div class="node">2. Do the action<br><span style="font-size:.85em;color:#888">in the UI</span></div><span class="arr">&rarr;</span>
    <div class="node">3. Query again<br><span style="font-size:.85em;color:#888">what changed?</span></div><span class="arr">&rarr;</span>
    <div class="node">4. Compare<br><span style="font-size:.85em;color:#888">against the requirement</span></div>
  </div>
  <div class="card" style="margin-top:.6em"><strong>Example &mdash; "cancelling an order refunds the customer"</strong>
    <p style="font-size:.9em;margin:.2em 0">Before: <code>SELECT status, refunded_at FROM orders WHERE id = 4711;</code> &rarr; PAID, NULL</p>
    <p style="font-size:.9em;margin:.2em 0">Action: click Cancel in the UI. Screen says "Order cancelled, refund issued".</p>
    <p style="font-size:.9em;margin:.2em 0">After: status = CANCELLED, <strong>refunded_at still NULL</strong>, and no row in <code>refunds</code>.</p>
    <p style="font-size:.9em;margin:.2em 0;color:var(--red)">That is a Critical defect the UI told you was a success.</p></div>
</section>""",

"""<section>
  <span class="lbl">Topic 4</span>
  <h3>Where Data Defects Hide</h3>
  <div class="g3">
    <div class="card"><strong>Orphan records</strong>A child row whose parent no longer exists. Deleting a customer should not leave their orders pointing at nothing.</div>
    <div class="card g"><strong>Duplicates</strong>The same customer created twice because the unique constraint is on the wrong column &mdash; or missing.</div>
    <div class="card o"><strong>NULL where NULL is not allowed</strong>An email, a price or a status that the requirement says is mandatory.</div>
  </div>
  <div class="g3" style="margin-top:8px">
    <div class="card r"><strong>Money and rounding</strong>Prices stored as floating point. 0.1 + 0.2 is not 0.3. Use integers (cents) or a decimal type.</div>
    <div class="card p"><strong>Dates and timezones</strong>Stored in local time, displayed in UTC &mdash; or the other way round. Test around midnight and across a DST change.</div>
    <div class="card"><strong>Encoding and length</strong>Names with &otilde;, &auml;, emoji or 300 characters. Silent truncation is a real and common defect.</div>
  </div>
</section>""",

"""<section>
  <span class="lbl">Topic 4</span>
  <h3>Constraints Are Tests the Database Runs for You</h3>
  <div class="g2">
    <div class="card"><strong>Check they exist</strong>
      &middot; <code>PRIMARY KEY</code> &mdash; every row identifiable<br>
      &middot; <code>FOREIGN KEY</code> &mdash; references stay valid<br>
      &middot; <code>UNIQUE</code> &mdash; no duplicate emails<br>
      &middot; <code>NOT NULL</code> &mdash; mandatory fields<br>
      &middot; <code>CHECK</code> &mdash; quantity &gt; 0, status in a known set</div>
    <div class="card g"><strong>Then test them</strong>
      Try to break each one deliberately: insert a duplicate email, an order for a customer that does not exist, a negative quantity.<br>
      If the database accepts it, the constraint is missing &mdash; and sooner or later the application will write that row.</div>
  </div>
  <p style="font-size:.58em;margin-top:.4em">Application-side validation is not enough: data also arrives through imports, admin tools, migrations and other services.</p>
</section>""",

"""<section>
  <span class="lbl">Topic 5</span>
  <h3>Migrations and Test Data</h3>
  <div class="g2">
    <div class="card o"><strong>Testing a migration</strong>
      &middot; Does it run on a copy of production-sized data, not just an empty schema?<br>
      &middot; How long does it take &mdash; and does it lock the table?<br>
      &middot; Is existing data preserved and correctly transformed?<br>
      &middot; Does the rollback work?<br>
      &middot; Does the old application version still run against the new schema during deployment?</div>
    <div class="card p"><strong>Test data management</strong>
      &middot; Fixtures &mdash; a known, versioned data set you can reset to<br>
      &middot; Generated data for volume testing<br>
      &middot; Copies of production data must be anonymised &mdash; real names, emails and payment data in a test environment is a data protection incident waiting to happen<br>
      &middot; Every test should leave the database in a state the next test can rely on</div>
  </div>
</section>""",

"""<section>
  <span class="lbl">Topic 5</span>
  <h3>Tools</h3>
  <div class="g3">
    <div class="card"><strong>DBeaver</strong>Free, cross-platform desktop client. Connects to almost anything.</div>
    <div class="card g"><strong>pgAdmin / MySQL Workbench</strong>The official clients for PostgreSQL and MySQL.</div>
    <div class="card o"><strong>sqliteonline.com / DB Fiddle</strong>Browser-based &mdash; nothing to install. We use these in class.</div>
  </div>
  <p style="font-size:.6em;margin-top:.5em">In a real job you will usually be given read-only access to a test database. Ask for it on day one &mdash; it is the difference between reporting "the screen looks wrong" and "row 4711 has refunded_at NULL after a successful cancel".</p>
</section>""",

"""<section>
  <span class="lbl">In-Class Exercise</span>
  <div class="teams">
    <h3>Find the Defects in the Shop Database</h3>
    <ul style="font-size:.68em">
      <li>Open <a href="https://sqliteonline.com" style="color:#9b9fe3">sqliteonline.com</a> and load <a href="materials/shop-database.sql" style="color:#9b9fe3">shop-database.sql</a> (paste it and run).</li>
      <li>The schema has customers, products, orders and order_items, with the requirements written in comments at the top of the file.</li>
      <li>Write a query for each requirement to check whether the data honours it.</li>
      <li>There are <strong>at least six data defects</strong> in there. Find them, and for each one say which requirement it breaks and what severity you would give it.</li>
    </ul>
  </div>
</section>""",

"""<section>
  <span class="lbl">Self-Check</span>
  <h3>Can You Answer These?</h3>
  <ul style="font-size:.68em">
    <li>Write a query that finds order items pointing at a product that no longer exists.</li>
    <li>Why does <code>WHERE status != 'PAID'</code> miss rows, and how do you fix it?</li>
    <li>A total on screen is &euro;19.99 and in the database it is 19.989999. Is that a defect? What would you check first?</li>
    <li>Name two things you must test about a migration besides "it ran".</li>
    <li>Why must production data be anonymised before it goes into a test environment?</li>
  </ul>
</section>""",

"""<section>
  <div class="hw">
    <h3>Homework 10 &mdash; SQL Verification</h3>
    <p style="font-size:.68em">Submit one query per requirement, the defects you found with the evidence, and a short note on which constraint would have prevented each one.</p>
    <p style="font-size:.62em">Full brief: <a href="homework/hw-10.html">Homework 10</a></p>
  </div>
</section>""",
])

# ---------------- LESSON 12 ----------------
write_lesson(12,
 "Accessibility Testing",
 "WCAG &middot; POUR &middot; Keyboard &middot; Contrast &middot; Screen readers &middot; Automated vs manual",
 "Testing that the product works for everyone, not just for you",
 ["Who accessibility is for &mdash; and why it is now the law",
  "WCAG and the four POUR principles",
  "The checks you can run today",
  "Screen readers and keyboard-only operation",
  "What automation catches, and what it never will"],
 "Run an accessibility audit of your own project and one public site, mapped to WCAG criteria.",
[
"""<section>
  <span class="lbl">Topic 1</span>
  <h3>Who Is This For?</h3>
  <div class="g3">
    <div class="card"><strong>Permanent</strong>Blind, low vision, colour blind, deaf, motor impairment, cognitive differences.<br><span style="color:#888">Roughly 1 in 6 people worldwide.</span></div>
    <div class="card g"><strong>Temporary</strong>A broken arm, an eye infection, a lost pair of glasses, an ear infection.</div>
    <div class="card o"><strong>Situational</strong>Bright sunlight on a phone screen, a noisy train, holding a baby, a slow connection, a trackpad that just died.</div>
  </div>
  <blockquote>Accessibility is not a minority feature. Everybody is temporarily or situationally impaired several times a week &mdash; accessible products are simply better products.</blockquote>
</section>""",

"""<section>
  <span class="lbl">Topic 1</span>
  <h3>And It Is Now a Legal Requirement</h3>
  <div class="g2">
    <div class="card"><strong>The standards</strong>
      &middot; <strong style="display:inline">WCAG</strong> &mdash; Web Content Accessibility Guidelines, currently 2.2. The reference everyone uses.<br>
      &middot; <strong style="display:inline">EN 301 549</strong> &mdash; the European standard, which points at WCAG.<br>
      &middot; <strong style="display:inline">European Accessibility Act</strong> &mdash; applies to a wide range of consumer digital products and services.</div>
    <div class="card o"><strong>Conformance levels</strong>
      &middot; <strong style="display:inline">A</strong> &mdash; the absolute minimum<br>
      &middot; <strong style="display:inline">AA</strong> &mdash; the level almost every law and contract requires<br>
      &middot; <strong style="display:inline">AAA</strong> &mdash; aspirational; not required for whole sites<br>
      <span style="color:#888">When someone says "we need to be accessible", they mean WCAG 2.2 level AA.</span></div>
  </div>
  <p style="font-size:.58em;margin-top:.4em">Accessibility is a non-functional requirement, exactly like performance and security &mdash; and it belongs in your SRS with a stated conformance target.</p>
</section>""",

"""<section>
  <span class="lbl">Topic 2</span>
  <h3>POUR &mdash; the Four Principles</h3>
  <div class="g2">
    <div>
      <div class="card" style="margin-bottom:6px"><strong>Perceivable</strong>Users can perceive the content. Text alternatives for images, captions for video, sufficient contrast, content that does not rely on colour alone.</div>
      <div class="card g"><strong>Operable</strong>Users can operate the interface. Everything reachable by keyboard, enough time to act, no content that flashes dangerously, clear focus indication.</div>
    </div>
    <div>
      <div class="card o" style="margin-bottom:6px"><strong>Understandable</strong>Content and behaviour are predictable. Readable language, consistent navigation, clear labels, helpful error messages that say how to fix the problem.</div>
      <div class="card p"><strong>Robust</strong>It works with assistive technology now and later. Valid semantic HTML, correct roles and names, no custom widget that only a mouse understands.</div>
    </div>
  </div>
</section>""",

"""<section>
  <span class="lbl">Topic 3</span>
  <h3>Checks You Can Run in Ten Minutes</h3>
  <div class="g2">
    <div class="card"><strong>Unplug the mouse</strong>
      Tab through the whole page. Can you reach every control? Activate it with Enter or Space? Can you always <em>see</em> where the focus is? Can you get out of every component again &mdash; or is there a keyboard trap?</div>
    <div class="card g"><strong>Zoom to 200%</strong>
      Does the content reflow, or does text get cut off and overlap? Try 400% too &mdash; WCAG asks for it.</div>
  </div>
  <div class="g2" style="margin-top:8px">
    <div class="card o"><strong>Check the contrast</strong>
      Normal text needs a ratio of at least <strong style="display:inline">4.5:1</strong> against its background; large text and UI components, <strong style="display:inline">3:1</strong>. Grey-on-grey placeholder text fails almost every time.</div>
    <div class="card r"><strong>Turn off the colour</strong>
      Is any information conveyed only by colour? A red border with no error text. A green dot with no label. Both fail.</div>
  </div>
</section>""",

"""<section>
  <span class="lbl">Topic 3</span>
  <h3>The Structural Checks</h3>
  <ul style="font-size:.66em">
    <li><strong>Images</strong> &mdash; does every meaningful image have an <code>alt</code> that describes its purpose? Is every decorative image marked <code>alt=""</code> so it is skipped?</li>
    <li><strong>Headings</strong> &mdash; is there exactly one <code>h1</code>, and do heading levels descend without skipping? Screen reader users navigate by heading.</li>
    <li><strong>Form labels</strong> &mdash; is every input associated with a real <code>&lt;label&gt;</code>? A placeholder is not a label; it disappears the moment you type.</li>
    <li><strong>Error identification</strong> &mdash; is the error announced, tied to the field, and does it say how to fix the problem?</li>
    <li><strong>Link text</strong> &mdash; does it make sense out of context? A page of "click here" links is unusable when read as a list.</li>
    <li><strong>Target size</strong> &mdash; are interactive targets big enough to hit with a finger or an unsteady hand?</li>
  </ul>
</section>""",

"""<section>
  <span class="lbl">Topic 4</span>
  <h3>Screen Readers</h3>
  <div class="g3">
    <div class="card"><strong>VoiceOver</strong>Built into macOS (Cmd + F5) and iOS. Nothing to install.</div>
    <div class="card g"><strong>NVDA</strong>Free and open source, Windows. The most common one in testing.</div>
    <div class="card o"><strong>TalkBack</strong>Built into Android. Pairs well with Lesson 13.</div>
  </div>
  <p style="font-size:.63em;margin-top:.5em">You do not need to be an expert user. Turn one on, close your eyes for one flow &mdash; log in, or add something to a basket &mdash; and see whether it is possible at all. That single exercise finds more real defects than any scan.</p>
  <blockquote>Listen for what the screen reader announces when focus lands on a control. If it just says "button", nobody knows what it does.</blockquote>
</section>""",

"""<section>
  <span class="lbl">Topic 5</span>
  <h3>Automated Tools &mdash; and Their Limits</h3>
  <div class="g2">
    <div class="card g"><strong>Tools worth having</strong>
      &middot; <strong style="display:inline">axe DevTools</strong> &mdash; browser extension, the industry standard engine<br>
      &middot; <strong style="display:inline">WAVE</strong> &mdash; visual overlay of issues on the page<br>
      &middot; <strong style="display:inline">Lighthouse</strong> &mdash; built into Chrome DevTools<br>
      &middot; Contrast checkers, built into DevTools and available online<br>
      &middot; <strong style="display:inline">axe-core</strong> in your CI pipeline, so regressions get caught automatically</div>
    <div class="card r"><strong>What they cannot tell you</strong>
      Automated checks find roughly a third of accessibility problems.<br>
      A tool can see that an image has <code>alt</code> text. It cannot see that the alt text says "image123.png".<br>
      It can see a heading. It cannot see that the heading is wrong.<br>
      It never knows whether a flow is actually usable.</div>
  </div>
</section>""",

"""<section>
  <span class="lbl">In-Class Exercise</span>
  <div class="teams">
    <h3>Ten Minutes, No Mouse</h3>
    <ul style="font-size:.68em">
      <li>Pick a well-known site &mdash; a shop, a bank, a public service, a news site.</li>
      <li>Put the mouse away. Complete one real task using only the keyboard: search for something, or start a checkout.</li>
      <li>Note every point where you got stuck, lost the focus indicator, or could not tell what was selected.</li>
      <li>Then run axe DevTools or Lighthouse on the same page. Compare: what did the tool catch that you missed, and what did you catch that the tool did not?</li>
    </ul>
  </div>
</section>""",

"""<section>
  <span class="lbl">Self-Check</span>
  <h3>Can You Answer These?</h3>
  <ul style="font-size:.68em">
    <li>What do the letters in POUR stand for, and give one check for each?</li>
    <li>What contrast ratio does normal body text need at level AA?</li>
    <li>Why is a placeholder not a label?</li>
    <li>Name an accessibility defect that no automated tool can detect.</li>
    <li>Write an accessibility requirement for your project that a tester could pass or fail.</li>
  </ul>
</section>""",

"""<section>
  <div class="hw">
    <h3>Homework 11 &mdash; Accessibility Audit</h3>
    <p style="font-size:.68em">Audit one public site and your own project: keyboard-only walkthrough, contrast check, structural checks and an automated scan. Report the findings mapped to WCAG criteria, with severity.</p>
    <p style="font-size:.62em">Full brief: <a href="homework/hw-11.html">Homework 11</a></p>
  </div>
</section>""",
])

# ---------------- LESSON 13 ----------------
write_lesson(13,
 "Mobile Testing",
 "Native, hybrid, web &middot; Device coverage &middot; Interruptions &middot; Networks &middot; Permissions &middot; Stores",
 "Everything that is different once the product is in someone's hand",
 ["Native, hybrid, web and PWA &mdash; and why it changes testing",
  "Device coverage: real devices, emulators, device clouds",
  "The test conditions that only exist on mobile",
  "Responsive web testing",
  "Install, upgrade and the app stores"],
 "Build a device matrix and run a mobile test charter against your project or a chosen app on a real phone.",
[
"""<section>
  <span class="lbl">Topic 1</span>
  <h3>Four Kinds of Mobile Application</h3>
  <div class="g2">
    <div>
      <div class="card" style="margin-bottom:6px"><strong>Native</strong>Built for one platform (Swift/Kotlin). Fastest, full access to device features. Two code bases, two release cycles, two sets of defects.</div>
      <div class="card g"><strong>Hybrid / cross-platform</strong>React Native, Flutter. One code base, near-native feel &mdash; but platform-specific defects still appear, usually in exactly the places the framework papers over.</div>
    </div>
    <div>
      <div class="card o" style="margin-bottom:6px"><strong>Mobile web</strong>A website in the phone's browser. No install, no store review &mdash; and no access to most device capabilities.</div>
      <div class="card p"><strong>PWA</strong>A web app that can be installed and work offline. Test it as a website <em>and</em> as an installed app, because the offline behaviour is a whole extra state.</div>
    </div>
  </div>
  <p style="font-size:.58em;margin-top:.4em">Ask which one you are testing before you write a single test &mdash; it decides your tooling, your device list and half your test conditions.</p>
</section>""",

"""<section>
  <span class="lbl">Topic 2</span>
  <h3>You Cannot Test Every Device</h3>
  <div class="g3">
    <div class="card"><strong>Real devices</strong>The only place you see real performance, real battery, real touch and real camera behaviour. Slow to scale, expensive to own.</div>
    <div class="card g"><strong>Emulators / simulators</strong>Free and fast for layout, flows and OS versions. They lie about performance, sensors, network and anything hardware.</div>
    <div class="card o"><strong>Device clouds</strong>BrowserStack, Sauce Labs, HeadSpin &mdash; hundreds of real devices, rented by the minute. What most teams actually use.</div>
  </div>
  <div class="card" style="margin-top:.6em"><strong>Build a device matrix from data, not opinion</strong>
    Take your analytics: top OS versions, top screen sizes, top device models, and the oldest version you still support. Cover the top ~80% of your real users, plus one deliberately old, small and slow device &mdash; that is where the defects are.</div>
</section>""",

"""<section>
  <span class="lbl">Topic 3</span>
  <h3>Test Conditions That Only Exist on Mobile</h3>
  <div class="g3">
    <div class="card"><strong>Interruptions</strong>Incoming call, alarm, notification, another app taking focus. Does state survive? Does the payment complete?</div>
    <div class="card g"><strong>Background and foreground</strong>Send the app to the background for 30 seconds, an hour, overnight. Is the session still valid? Is the form still filled in?</div>
    <div class="card o"><strong>Orientation</strong>Rotate mid-flow, mid-form, mid-upload. Rotation recreates the screen on Android &mdash; a classic state-loss defect.</div>
  </div>
  <div class="g3" style="margin-top:8px">
    <div class="card r"><strong>Network</strong>Offline, airplane mode, 3G, flaky connection, switching WiFi to mobile data mid-request. Retry logic and duplicate submissions live here.</div>
    <div class="card p"><strong>Permissions</strong>Deny camera, location, notifications, photos. Then grant them later. Then revoke them from settings while the app runs.</div>
    <div class="card"><strong>Device state</strong>Low battery and battery saver mode, low storage, dark mode, large system font, reduced motion, another language and region.</div>
  </div>
</section>""",

"""<section>
  <span class="lbl">Topic 3</span>
  <h3>Gestures and Touch</h3>
  <ul style="font-size:.66em">
    <li><strong>Touch targets</strong> &mdash; big enough to hit with a thumb, and far enough apart. This is an accessibility criterion too (Lesson 12).</li>
    <li><strong>Gestures</strong> &mdash; tap, double tap, long press, swipe, pinch, drag. Does a swipe conflict with the system back gesture?</li>
    <li><strong>Keyboard</strong> &mdash; does the on-screen keyboard cover the field you are typing into? Does the right keyboard type appear for email and numbers?</li>
    <li><strong>Scrolling</strong> &mdash; is anything unreachable behind a fixed header, a notch or the home indicator?</li>
    <li><strong>Double submission</strong> &mdash; tap the pay button twice, quickly. On a slow connection users always do.</li>
  </ul>
</section>""",

"""<section>
  <span class="lbl">Topic 4</span>
  <h3>Responsive Web Testing</h3>
  <div class="g2">
    <div class="card"><strong>Test at the breakpoints</strong>Not at random widths &mdash; ask the developers where the CSS breakpoints are, then test just below and just above each one. That is boundary value analysis applied to layout.</div>
    <div class="card g"><strong>Chrome device mode</strong>DevTools &rarr; toggle device toolbar. Good for layout, breakpoints and throttled network. Not a substitute for a real phone.</div>
  </div>
  <p style="font-size:.62em;margin-top:.4em">Then check on a real device: fonts render differently, tap targets feel different, and the on-screen keyboard changes the viewport in ways no emulator reproduces faithfully.</p>
</section>""",

"""<section>
  <span class="lbl">Topic 5</span>
  <h3>Install, Upgrade and the Stores</h3>
  <div class="g2">
    <div class="card o"><strong>Lifecycle testing</strong>
      &middot; Fresh install &mdash; the first-run experience and permission prompts<br>
      &middot; Upgrade from the previous version, with existing data and an active session<br>
      &middot; Upgrade from a very old version &mdash; do the data migrations still run?<br>
      &middot; Uninstall and reinstall &mdash; what is left behind, and should it be?<br>
      &middot; Deep links and push notifications &mdash; do they open the right screen when the app is closed?</div>
    <div class="card p"><strong>Store realities</strong>
      &middot; You cannot hotfix in minutes &mdash; review takes time, so a bad release lives longer<br>
      &middot; Users do not all update. Old versions must keep working against your API<br>
      &middot; Store listing content, screenshots and privacy declarations are also things that can be wrong<br>
      &middot; Crash reports and store reviews are your production monitoring</div>
  </div>
</section>""",

"""<section>
  <span class="lbl">Topic 5</span>
  <h3>Tools</h3>
  <div class="g3">
    <div class="card"><strong>Chrome DevTools device mode</strong>Responsive layout and network throttling. Free, instant.</div>
    <div class="card g"><strong>Android Studio / Xcode</strong>Emulator and simulator, plus device logs (logcat, Console).</div>
    <div class="card o"><strong>Appium / Maestro</strong>Mobile test automation &mdash; Maestro is by far the easier place to start.</div>
  </div>
  <div class="g3" style="margin-top:8px">
    <div class="card r"><strong>Charles / Proxyman</strong>See and manipulate the app's network traffic &mdash; the mobile equivalent of the Network tab.</div>
    <div class="card p"><strong>BrowserStack / Sauce Labs</strong>Real devices on demand for the models you do not own.</div>
    <div class="card"><strong>TalkBack / VoiceOver</strong>Accessibility on mobile &mdash; the same checks as Lesson 12, on a smaller screen.</div>
  </div>
</section>""",

"""<section>
  <span class="lbl">In-Class Exercise</span>
  <div class="teams">
    <h3>Break an App With Your Own Phone</h3>
    <ul style="font-size:.68em">
      <li>Take out your phone and pick an app you use often.</li>
      <li>Charter: <em>Explore &lt;app&gt; under interruption and poor network to discover state-loss defects.</em></li>
      <li>Start a flow &mdash; a search, a booking, a form. Mid-flow: rotate the device, switch to another app, turn on airplane mode, come back.</li>
      <li>Note everything that is lost, duplicated, frozen or silently wrong.</li>
      <li>Compare with the group: which conditions found the most defects?</li>
    </ul>
  </div>
</section>""",

"""<section>
  <span class="lbl">Self-Check</span>
  <h3>Can You Answer These?</h3>
  <ul style="font-size:.68em">
    <li>Name three things an emulator will not tell you.</li>
    <li>How would you choose five devices to test on?</li>
    <li>Give two defects that only appear when the network is flaky.</li>
    <li>Why does rotation cause state-loss defects?</li>
    <li>Why is a bad mobile release more expensive than a bad web release?</li>
  </ul>
</section>""",

"""<section>
  <div class="hw">
    <h3>Homework 12 &mdash; Mobile Test Charter</h3>
    <p style="font-size:.68em">Build a device matrix for your project, then run a time-boxed mobile exploratory session on a real device covering interruptions, network and orientation. Report the defects you found.</p>
    <p style="font-size:.62em">Full brief: <a href="homework/hw-12.html">Homework 12</a></p>
  </div>
</section>""",
])
