# Software Testing Fundamentals

Course materials for **Tarkvara testimise alused** — the manual software testing fundamentals course.

## 🌐 Live Course

**Access the course here:** https://tanjaq.github.io/Tarkvara-testimise-alused/

## 📚 What's in here

| File | What it is |
|---|---|
| `index.html` | Course homepage with all lesson cards |
| `lesson-01.html` … `lesson-12.html` | The twelve lesson presentations |
| `lesson-bonus-ai.html` | Bonus lesson — using AI responsibly in testing |
| `homework/` | One page per assignment: task, deliverable, assessment criteria |
| `materials/` | SRS template, real SRS examples, testing process worksheet |

Lessons are reveal.js presentations. Use **→** to move between slides and **ESC** for the slide overview.

---

## 🎓 Course outline

| # | Lesson | Topics |
|---|---|---|
| 1 | Testing Fundamentals & the Quality Mindset | Course intro · software quality · what can be tested · verification vs validation · AI mindset |
| 2 | The Purpose of Testing | Real-world failures · consequences · where defects come from · cost of a defect · goals of testing |
| 3 | The Testing Process | SDLC · waterfall, V-model, agile · the ISTQB five-step process · seven testing principles |
| 4 | Software Requirements | Business vs system requirements · FR and NFR · SMART · SRS |
| 5 | Software Architecture | Monolith · layered · microservices · event-driven · serverless · modular · monorepo |
| 6 | Test Techniques I — Static Testing | Reviews · walkthroughs · inspections · static code analysis · PR review etiquette |
| 7 | Test Techniques II — Black Box | Equivalence partitioning · boundary value analysis · decision tables · state transition · use cases |
| 8 | Test Techniques III — White Box | Function, statement and branch coverage · the limits of coverage |
| 9 | Defect Management | Error/defect/failure · bug report anatomy · severity vs priority · lifecycle · RCA |
| 10 | Test Cases & Documentation | User story → requirement → test case · re-testing · regression · test management tools |
| 11 | Performance Testing | Response time · throughput · resource utilization · load, stress and endurance testing |
| 12 | Application Security | CIA · OWASP Top 10, ASVS, WSTG · injection · XSS · authentication · business logic |
| ★ | Bonus — Using AI Responsibly | Where AI helps · where it fails silently · ground rules |

---

## 📝 Homework

Full briefs with assessment criteria: **[homework/](homework/index.html)**

| Lesson | Assignment | Format | Where to submit |
|---|---|---|---|
| 1 | The Quality Mindset — bring one good and one bad example | Individual | Discussed in class |
| 2 | Failure case analysis | Group of 3–4 | Teams |
| 3 | Test process worksheet — calculator | Group of 3–4 | Teams |
| 4 | Requirements for your project (FR + NFR) | Group project | Teams — SRS document |
| 5 | Project architecture diagram | Group project | Teams — SRS document |
| 6 | Peer review — [Rental-Car](https://github.com/tanjaq/Rental-Car/tree/peer-review) | Individual / pair | Teams |
| 7 | Decision table — photo ordering discounts | Individual / pair | Teams |
| 8 | Boarding pass — coverage analysis | Individual / pair | Teams |
| 9 | Write a real bug report | Individual | [GitHub Issue](https://github.com/tanjaq/OnlineShopping/issues) |
| 10 | Test cases for your project | Group project | Teams — SRS section 7.1 |
| 11 | Performance requirements | Group project | Teams — SRS document |
| 12 | Security review + Dependabot + SonarLint | Group project | Teams — SRS document |

The group project runs through the whole course: requirements (L4) → architecture (L5) → test cases (L10) → performance (L11) → security (L12) all land in the same SRS document.

---

## 📎 Materials

- [SRS document template](materials/Software%20Requirements%20Specification%20(SRS)%20Document%20Template.docx)
- [SRS example 1](materials/srs_example_1.pdf) · [SRS example 2](materials/srs_example_2.pdf)
- [Testing process worksheet](materials/testing-process-worksheet.html)

## 🔗 Related repositories

- [Rental-Car](https://github.com/tanjaq/Rental-Car) — peer review exercise (Lesson 6)
- [OnlineShopping](https://github.com/tanjaq/OnlineShopping) — bug reporting exercise (Lesson 9)
- [Tarkvara-Testimine](https://github.com/tanjaq/Tarkvara-Testimine) — the automation-focused companion course

---

**Happy testing!**
