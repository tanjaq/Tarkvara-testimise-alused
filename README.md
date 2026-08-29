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

## 🎓 Course outline

| # | Lesson | Topics |
|---|---|---|
| 1 | Testing Fundamentals & the Quality Mindset | Course intro · AI ground rules · software quality · what can be tested · verification vs validation |
| 2 | The Purpose of Testing | Real-world failures · consequences · where defects come from · cost of a defect · goals of testing |
| 3 | The Testing Process & Test Plan | SDLC · waterfall, V-model, agile · the ISTQB five-step process · the test plan · seven principles |
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

| Lesson | # | Assignment | Format |
|---|---|---|---|
| 1 | 1 | The Quality Mindset — bring one good and one bad example | Individual |
| 2 | 2 | Failure case analysis | Group of 3–4 |
| 3 | 3 | Test process worksheet + one-page test plan | Group of 3–4 |
| 4 | 4 | Requirements for your project (FR + NFR) | Group project |
| 5 | 5 | Project architecture diagram | Group project |
| 6 | 6 | Peer review — [Rental-Car](https://github.com/tanjaq/Rental-Car/tree/peer-review) | Individual / pair |
| 7 | 7 | Decision table + EP/BVA on the trip planner form | Individual / pair |
| 8 | 8 | Boarding pass — coverage analysis | Individual / pair |
| 9 | 9 | Exploratory session + bug report → [Bug-Reporting](https://github.com/tanjaq/Bug-Reporting/issues) | Individual |
| 10 | 10 | Test cases for your project | Group project |
| 11 | 11 | SQL verification — shop database | Individual / pair |
| 12 | 12 | Accessibility audit | Individual / pair |
| 13 | 13 | Mobile test charter | Individual / pair |

The group project runs through the whole course: requirements (L4) → architecture (L5) → test cases (L10) all land in the same SRS document. One homework per lesson.

---

## 📎 Materials

- [SRS document template](materials/Software%20Requirements%20Specification%20(SRS)%20Document%20Template.docx) · [SRS example 1](materials/srs_example_1.pdf) · [SRS example 2](materials/srs_example_2.pdf)
- [Testing process worksheet](homework/testing-process-worksheet.html) — Homework 3
- [Trip planner form](materials/input-form-example.html) — a deliberately broken form, used in Lessons 3 and 7
- [shop-database.sql](materials/shop-database.sql) — a sample database with planted data defects, used in Lesson 11

## 🔗 Related repositories

- [Rental-Car](https://github.com/tanjaq/Rental-Car) — peer review exercise (Lesson 6)
- [Bug-Reporting](https://github.com/tanjaq/Bug-Reporting) — bug reporting exercise (Lesson 9)
- [Tarkvara-Testimine](https://github.com/tanjaq/Tarkvara-Testimine) — the automation-focused companion course

---

**Happy testing!**
