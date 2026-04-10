# CLAUDE CONTEXT FILE — BCIT CIT Term 4 Set A Finals Prep
**Last Updated:** 2026-04-10
**Student:** Nick Sevostiyanov (confirmed from D2L username `NS`)
**Session Intent:** Say `read CONTEXT\claude-context-file for context` to load this at start of each session.

---

## PROJECT OVERVIEW

Nick has downloaded ALL Term 4 Set A BCIT CIT course content, organized by week, for 6 courses. The goal is to prepare for **final exams** in exam order (1→6). Content lives at:

- `Z:\BCIT-FINALS\CONTEXT\[N-COURSE-NAME]\` — full course context (slides, labs, quizzes, newsletters)
- `Z:\BCIT-FINALS\OUTPUT\SHARED\[N-COURSE-NAME]\` — generated study materials (SHARED = not personal)
- `Z:\BCIT-FINALS\OUTPUT\PERSONAL\` — Nick's personal labs, submissions, grades (DO NOT put in SHARED)
- `Z:\BCIT-FINALS\PERSONAL-CONTEXT\[N-COURSE-NAME]\` — Nick's personal context (grades, labs, submissions)

**Critical rule:** SHARED output is sharable with others. PERSONAL is private. Never mix them.

---

## EXAM SCHEDULE (Location: DTC 825 — Level 4)

| # | Course | Exam Date | Time | Duration | Notes |
|---|--------|-----------|------|----------|-------|
| 1 | ACIT4880 Data Analytics | Mon Apr 20 | 9:30–10:30 | 60 min | Standard |
| 2 | ACIT3855 Service Architectures | Mon Apr 20 | 14:30–17:30 | 180 min | GREEN (longer) |
| 3 | ACIT4850 Enterprise Integration | Mon Apr 20 | 14:30–17:00 | 150 min | GREEN (longer) |
| 4 | ACIT4630 Security Info Assurance | Tue/Wed Apr 21-22 | ~10:30–12:30 | ~120 min | — |
| 5 | ACIT3495 IT Infrastructure | Thu Apr 24 | 15:30–17:00 | 90 min | — |
| 6 | ACIT4640 IT System/Network Prov. | Fri Apr 24 | 9:30–11:00 | 90 min | — |

> Source: `Z:\BCIT-FINALS\CONTEXT\final-exam-schedule.png`

---

## OUTPUT\SHARED DELIVERABLES — PER COURSE

Each `OUTPUT\SHARED\[N-COURSE]\` folder contains:

### 1. `practice-quizzes/`
Three HTML quiz files, all built from REAL quiz content, real question formats, real answer styles:

- **`d2l-format.html`** — Full quiz page. All questions shown at once. User selects answers. Submit button at bottom. Final grade shown after submit. Style: matches D2L quiz interface. Multi-select where appropriate.
- **`per-question-format.html`** — One question at a time. User selects answer. Immediately shows CORRECT/INCORRECT + detailed explanation. Next question button.
- **`all-answers.html`** — No interaction. All questions listed with correct answer pre-selected + thorough explanation for each. Great for reading/reviewing. No timer.

> Quiz style MUST match actual course style (some courses use "select all that apply", some use "select the best answer"). Mirror real quizzes as closely as possible.

### 2. `course-info.md`
Nicely formatted markdown with:
- Course title, code, instructor, term
- **Grade rubric** (what % each component is worth, minimum passing grade)
- **Logical course structure** (brief, e.g. Week 1 = Intro, Week 4 = Docker Lab, etc.)
- **Final exam context** (open/closed book, AI allowed?, cheat sheet allowed?, date, time, duration, location)
- Course overview (topics covered across the weeks)

### 3. `finalexam-studyguide.md`
The ONE study guide. Must be:
- Genuine, concise, extremely useful
- Based on FULL course context (newsletters, slides, quizzes, labs)
- Cumulative or scoped to final only — determined by actual course evidence (e.g. newsletter saying "cumulative")
- No filler. Every line earns its place.
- Include important "basics" relevant to the domain even if not explicitly on exam (e.g. SSH commands for infra courses)

### 4. `cheatsheet/` *(ACIT3855 ONLY)*
- ACIT3855 (Mike Mulder) explicitly allows **unlimited printed cheat sheets** in the final exam
- Format: PDF preferred
- Content: 20+ pages. Dense. Everything. All architectures explained with WHY and HOW. Every lab pattern. Every concept from every week. Leave NOTHING out.

---

## COURSE DETAILS

### 1. ACIT4880 — Introduction to Data Analytics
- **Instructor:** Rafi Mohammad (`rafi_mohammad@bcit.ca`)
- **Exam:** Mon Apr 20, 9:30–10:30, DTC 825, **60 minutes**
- **Exam format:** Unknown (likely multiple choice based on in-class quizzes)
- **Open/closed book:** Unknown — check slides/newsletters. No explicit mention found.
- **Quizzes taken:** quiz1, quiz2, quiz3 (in `ALL-QUIZ-QUESTIONS/`)
- **Quiz 3 scope:** "everything covered since mid-term up to last week, i.e., machine learning"
- **Grade structure:** Unknown exact — check slides for syllabus
- **Week structure:**
  - Week 1: Jupyter Notebook intro, Chapter 1 (data intro)
  - Week 2: NumPy & Pandas
  - Week 3–4: Data Cleaning, Missing Values (continuous + discrete)
  - Week 5–6: Feature Selection (constant features, correlation, chi-square, mutual info)
  - Week 7–8: Regression Analysis, Classification Math
  - Week 9: kNN
  - Week 10: Advanced Classification — SVM, Decision Trees, Random Forest
  - Week 11: Model Tuning, Hyperparameter Tuning, Imbalanced Data
  - Week 12: Unsupervised Learning — K-Means, Hierarchical Clustering
  - (Also: Tableau / data visualization covered mid-semester)
- **Key materials:** Reference textbook chapters (ch01–ch10), PDF slides, Jupyter notebooks
- **Context path:** `CONTEXT\1-ACIT4880-DATA-ANALYSIS\`

---

### 2. ACIT3855 — Service Based Architectures
- **Instructors:** Mike Mulder (`mmulder10@bcit.ca`) + Rafi Mohammad
- **Exam:** Mon Apr 20, 14:30–17:30, DTC 825, **180 minutes** (GREEN = longer than default)
- **EXAM IS OPEN BOOK** — paper printouts, cheatsheets, paper notes ALLOWED. NO electronic devices.
- **Exam format (from midterm description, likely same for final):**
  - Multiple choice questions
  - Short written answers
  - Implement a simple API
  - Fill blanks in OpenAPI YAML file
  - Write basic Python code for API endpoints (app.py)
- **Midterm covered:** Weeks 1–7
- **Final likely covers:** Weeks 8–12 (possibly cumulative — verify in slides)
- **Quizzes taken:** quiz0-checkin, quiz1–quiz5, quiz7, quiz9, quiz10 (in `ALL-QUIZZES/`)
- **Assignment 1:** posted ~Mar 25 — "due before end of last class, good practice for final exam"
- **⭐ CHEAT SHEET ALLOWED:** Unlimited printed cheat sheets for final. Generate a comprehensive one.
- **Week structure:**
  - Week 1: Microservices intro (Martin Fowler), REST APIs, HTTP methods
  - Week 2: JMeter, load testing, microservices patterns
  - Week 3: Logging, tracing, event logging, Python logging module, config file types
  - Week 4: OpenAPI 3.0 spec (metadata, paths, requests/responses, parameters, reuse), apscheduler
  - Week 5: OpenAPI continued, periodic processing
  - Week 6: Messaging with microservices, Kafka (topics, publishers, consumers, brokers)
  - Week 7: Kafka continued, Event Sourcing, Lab 6 demo + midterm review
  - Week 8: Docker + Virtual Environments
  - Week 9: Docker + Microservices (continued)
  - Week 10: Same Origin Policy, CORS
  - Week 11: (pre-reading available)
  - Week 12: (pre-reading available) + Lab 12
- **Key materials:** Lesson PDFs (Lesson1–Lesson12), Lab PDFs (lab-01 to lab-12), pre-reading PDFs, weather_api.yml (OpenAPI example)
- **Context path:** `CONTEXT\2-ACIT3855-SERVICE-ARCHITECTURE\`

---

### 3. ACIT4850 — Enterprise Systems Integration
- **Instructors:** Mike Mulder (`mmulder10@bcit.ca`) + Johnny Zhang (`johnny_zhang@bcit.ca`)
- **Exam:** ~Mon Apr 20 or Tue Apr 21, ~14:30–17:00, DTC 825, **150 minutes** (GREEN)
- **Midterm format (likely indicative of final):**
  - Part 1 (70%): CLOSED BOOK on paper — pen/pencil required
  - Part 2 (30%): Laptop allowed — Apache/Jenkins/GitLab VMs, Python repos on GitLab, Jenkins pipeline with Jenkinsfile
  - No electronic devices except laptop in Part 2; phone face down
- **Quizzes taken:** quiz1–quiz11 (in `ALL-QUIZZES/`)
- **Assignments:** Assignment 1, 2, 3 (PDFs in respective folders)
- **Week structure:**
  - Week 1: Enterprise, System, Integration definitions; On-prem vs Cloud; Tool evaluation criteria
  - Week 2: JIRA, Confluence — Work Management, Knowledge Base; installation methods
  - Week 3: Functional vs Non-Functional Requirements
  - Week 4: DevOps definition and practices; Continuous Integration practices; Stakeholders
  - Week 5: CI Pipeline stages; Jenkins Pipeline purpose; Declarative vs Scripted; Controller/Nodes/Agents/Executors
  - Week 6: Jenkins Shared Libraries; Debugging Tools; Global Shared Libraries
  - Week 7: Static Code Analysis (definition, benefits); SonarQube (Quality Gate, Issues, Snapshots, Scanner, Platform); **Midterm Review**
  - Week 8: (Pre-reading available — covered in quiz)
  - Week 9: (Pre-reading available)
  - Week 10: (Pre-reading covers quiz 9 concepts)
  - Week 11–12: (Lesson PDFs available)
  - (Also: GitLab, Docker Compose, Maven, Jenkinsfiles covered in labs)
- **Lab tools:** Apache, Jenkins, GitLab VMs on Azure cloud; Python repos; docker-compose.yml; Jenkinsfile
- **Context path:** `CONTEXT\3-ACIT4850-ENTERPRISE-INTEGRATION\`

---

### 4. ACIT4630 — Information Assurance and Security
- **Instructor:** Unknown (from newsletter context)
- **Exam:** Tue/Wed Apr 21-22, ~10:30–12:30, DTC 825
- **Exam format:** Unknown — check Week-13 slides for final exam review info
- **Open/closed book:** Unknown — check slides
- **Final exam review:** Apr 14 online class (Teams) for presentations + final exam review
- **Quizzes taken:** quiz0-checkin, quiz1–quiz6, quiz8–quiz11 (in `ALL-QUIZZES/`)
- **Week structure:**
  - Week 1: (slides available)
  - Week 2: (slides + reading material)
  - Week 3: (slides)
  - Week 4: (slides + reading material)
  - Week 5: (slides)
  - Week 6: (slides) — MD5 collision demo mentioned
  - Week 7: (reading material)
  - Week 9: (slides)
  - Week 10: (slides)
  - Week 12: (slides + reading material)
  - Week 13: (slides) — likely final review
  - Week 14: (Week 13 slides repeated — confirm)
  - (Note: Week 8 and 11 slides not in context)
- **Notable:** BCIT CTF discord mentioned — course includes hands-on security
- **Context path:** `CONTEXT\4-ACIT4630-SECURITY-INFO-ASSURANCE\`

---

### 5. ACIT3495 — Advanced Topics in IT Infrastructure
- **Instructor:** Dr. Motasem Aldiab (`maldiab@bcit.ca`)
- **Exam:** Thu Apr 24, 15:30–17:00, DTC 825, **90 minutes**
- **Exam format:** Bring ID and pen/pencil (from previous term newsletter — likely similar)
- **Open/closed book:** Unknown — assumed closed book
- **Quizzes taken:** QUIZ1–QUIZ4 (in `ALL-QUIZZES/`)
- **Projects:** Project 1 (presentation Feb), Project 2 (presentation Apr 9-10, submission before class)
- **Week structure:**
  - Week 0 (intro): Install Docker on Ubuntu/Debian VM; set up DigitalOcean or AWS account
  - Week 1–2: Docker fundamentals (Docker.pdf), Lab 1
  - Week 3: Docker multi-container, Lab 2 (MySQL setup)
  - Week 4: Dockerfile, Docker Compose, Lab 3 (app.js Node app)
  - Week 5: Lab 4 (data cleaning context — docker-compose-mariadb)
  - Week 6–9: Kubernetes intro (Kubernetes.ppsx, Kubernetes_2.pps), Lab 5, Lab 6
  - Week 10: K8s Deployments (k8s_week7.zip), Lab 7
  - Week 11: StatePersistence, Init Containers (InitContainer.zip), SideCar pattern (SideCar.zip), Volumes (Volumes.zip), Lab 7b
  - Week 12: ConfigMaps & Secrets, Lab 9A + 9B (fortune app, yaml configs)
  - (k8s_commands.txt — key reference for exam)
- **Context path:** `CONTEXT\5-ACIT3495-IT-INFRASTRUCTURE\`

---

### 6. ACIT4640 — IT System and Network Provisioning
- **Instructor:** Dr. Motasem Aldiab (`maldiab@bcit.ca`)
- **Exam:** Fri Apr 24, 9:30–11:00, DTC 825, **90 minutes**
- **Exam format:** Bring ID and pen/pencil (likely closed book)
- **No quizzes folder** found in context
- **Week structure:**
  - Intro Week: Install Ubuntu/Debian VM; set up DigitalOcean or AWS account
  - Week 1: (week-1.md, lab-week1.md, reading-review) — basics
  - Week 2: (flipped-review, lab2) — cloud CLI basics
  - Week 3: AWS CLI (aws-cli.md), flipped-review, lab3
  - Week 4: Infrastructure as Code pptx, Terraform intro (terraform-intro.md), lab4 (diagram: VPC/subnet/EC2)
  - Week 6: Ansible + Packer (ansible_packer.pptx), lab6
  - Week 9: Ansible on Ubuntu EC2 guide (2 versions: standard + PEM key), lab, flipped-review
  - Week 10: flipped-review, lab
  - Week 11: flipped-review, lab
  - Week 13: (folder exists — no files listed)
  - Week 14: (folder exists — no files listed)
- **Key topics:** AWS CLI, Terraform (IaC), Ansible, Packer, VPC, EC2, SSH, cloud provisioning
- **Context path:** `CONTEXT\6-ACIT4640-IT-SYSTEM-NETWORK-PROVISIONING\`

---

## WORKFLOW INSTRUCTIONS

### How to work on a course:
1. Read relevant quiz files from `CONTEXT\[N-COURSE]\ALL-QUIZZES\` or `ALL-QUIZ-QUESTIONS\`
2. Read newsletters from `CONTEXT\[N-COURSE]\ALL-NEWSLETTERS` for exam-specific context
3. Read key lecture slides (PDFs) from the weekly folders
4. Generate the 3 deliverables: `course-info.md`, `finalexam-studyguide.md`, and the 3 practice-quiz HTML files
5. For ACIT3855 also generate `cheatsheet\` content

### File naming convention:
```
OUTPUT\SHARED\[N-COURSE-NAME]\
  practice-quizzes\
    d2l-format.html
    per-question-format.html
    all-answers.html
  course-info.md
  finalexam-studyguide.md
  cheatsheet\              ← ACIT3855 ONLY
    cheatsheet.pdf (or .html)
```

### Special notes:
- ACIT3855 is the ONLY course confirmed to allow unlimited printed cheat sheets for the final
- ACIT4850 midterm had laptop portion (Jenkins/GitLab VMs) — final may too
- ACIT3495 and ACIT4640 share same instructor (Dr. Aldiab) — same exam rules/style
- ACIT4880 has 60-minute exam — shortest, keep study guide focused
- All exams are in **DTC 825**
- Finals week: April 20–24, 2026

---

## PERSONAL CONTEXT (DO NOT PUT IN SHARED OUTPUT)

Nick's personal materials (grades, labs, submissions) are in:
- `Z:\BCIT-FINALS\PERSONAL-CONTEXT\[N-COURSE-NAME]\`
- `Z:\BCIT-FINALS\OUTPUT\PERSONAL\`

These are for Nick's own cheatsheets and personal learning outcomes. Not shared.
