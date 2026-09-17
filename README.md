# Software Testing Fundamentals

Course materials for the software testing fundamentals course — manual testing, from the quality mindset through to mobile.

## 🌐 Live course

**https://tanjaq.github.io/Tarkvara-testimise-alused/**

## 📚 What's in here

| Path | What it is |
|---|---|
| `index.html` | Course homepage with all lesson cards |
| `lesson-01.html` … `lesson-13.html` | The thirteen lesson presentations |
| `lesson-bonus-ai.html` | Bonus — using AI responsibly in testing |
| `lesson-bonus-performance.html` | Bonus — performance testing |
| `lesson-bonus-security.html` | Bonus — application security |
| `homework/` | One page per assignment: task, deliverable, assessment criteria |
| `materials/` | SRS template and examples, trip planner form, sample shop database |
| `images/` | Diagrams and screenshots used in the lessons |

Lessons are reveal.js presentations. Use **→** to move between slides and **ESC** to return to the course homepage.

---

## ⏱️ Compact track — 6 sessions

For groups that meet every other week: **[compact/](compact/index.html)** maps the thirteen lessons onto six sessions, naming which slides to cover in class, which to leave as reading, and a reduced set of five homework assignments. It links to the same lesson decks — there is no second copy of anything to maintain.

## 🎓 Course outline

| # | Lesson | Topics |
|---|---|---|
| 1 | Testing Fundamentals & the Quality Mindset | Course intro · AI ground rules · software quality · what can be tested · verification vs validation |
| 2 | The Purpose of Testing | Real-world failures · consequences · where defects come from · cost of a defect · goals of testing |
| 3 | The Testing Process | SDLC · waterfall, V-model, agile · the ISTQB five-step process · seven principles |
| 4 | Software Requirements | Business vs system requirements · FR and NFR · SMART · SRS |
| 5 | Software Architecture | Monolith · layered · microservices · event-driven · serverless · modular · monorepo |
| 6 | Test Techniques I — Static Testing | Reviews · walkthroughs · inspections · static code analysis · PR review etiquette |
| 7 | Test Techniques II — Black Box | Equivalence partitioning · boundary value analysis · decision tables · state transition · use cases |
| 8 | Test Techniques III — White Box | Function, statement and branch coverage · the limits of coverage |
| 9 | Defect Management & Exploratory Testing | Charters · tours · heuristics · bug report anatomy · severity vs priority · lifecycle · RCA |
| 10 | Test Cases & Documentation | User story → requirement → test case · re-testing · regression · test management tools |
| 11 | Database & SQL Testing | SQL for testers · data integrity · constraints · migrations · test data |
| 12 | Accessibility Testing | WCAG 2.2 · POUR · keyboard · contrast · screen readers · automated vs manual |
| 13 | Mobile Testing | Native/hybrid/web · device matrix · interruptions · network · permissions · stores |
| ★ | Bonus — Using AI Responsibly | Good and bad worked examples · prompting for testers · testing AI features |
| ★ | Bonus — Performance Testing | Response time · throughput · resource utilization · load, stress, endurance |
| ★ | Bonus — Application Security | CIA · OWASP Top 10, ASVS, WSTG · injection · XSS · business logic |

---

## 📝 Homework

Full briefs with assessment criteria: **[homework/](homework/index.html)**

| Lesson | # | Assignment | Format | Submit to |
|---|---|---|---|---|
| 1 | — | No homework — something to think about, discussed next lesson | — | — |
| 2 | 1 | Failure case analysis | Group of 3–4 | Teams |
| 3 | 2 | Test process worksheet — calculator | Group of 3–4 | Teams |
| 4 | 3 | Requirements for your project (FR + NFR) | Group project | Teams |
| 5 | 4 | Project architecture diagram | Group project | Teams |
| 6 | 5 | Peer review — [Rental-Car](https://github.com/tanjaq/Rental-Car/tree/peer-review) | Individual / pair | Teams |
| 7 | 6 | Decision table + EP/BVA on the trip planner form | Individual / pair | Teams |
| 8 | 7 | Boarding pass — coverage analysis | Individual / pair | Teams |
| 9 | 8 | Exploratory session + bug report | Individual | [Bug-Reporting](https://github.com/tanjaq/Bug-Reporting/issues) |
| 10 | 9 | Test plan + test cases for your project | Group project | Teams |
| 11 | 10 | SQL verification — shop database | Individual / pair | Teams |
| 12 | 11 | Accessibility audit | Individual / pair | Teams |
| 13 | 12 | Mobile test charter | Individual / pair | Teams |

The group project runs through the whole course: requirements (L4) → architecture (L5) → test plan and test cases (L10) all land in the same SRS document.

---

## 📎 Materials

- [SRS document template](materials/Software%20Requirements%20Specification%20(SRS)%20Document%20Template.docx) · [SRS example 1](materials/srs_example_1.pdf) · [SRS example 2](materials/srs_example_2.pdf)
- Testing process worksheet — Homework 2: [Word version](materials/testing-process-worksheet.docx) to type into, or [fill it in on the page](homework/testing-process-worksheet.html) and print to PDF
- [Trip planner form](materials/input-form-example.html) — a deliberately broken form, used in Lessons 3 and 7
- [shop-database.sql](materials/shop-database.sql) — a sample database with planted data defects, used in Lesson 11

## 🛠️ Rebuilding the pages

The lesson decks, homework pages and homepage are generated from the scripts in **[tools/](tools/README.md)** — `cd tools && python3 build.py`. If you edit a lesson's HTML by hand, make the same change in its generator, or the next rebuild will overwrite it.

## 🔗 Related repositories

- [Rental-Car](https://github.com/tanjaq/Rental-Car) — peer review exercise (Lesson 6)
- [Bug-Reporting](https://github.com/tanjaq/Bug-Reporting) — bug reporting exercise (Lesson 9)
- [Tarkvara-Testimine](https://github.com/tanjaq/Tarkvara-Testimine) — the automation-focused companion course

---

**Happy testing!**
