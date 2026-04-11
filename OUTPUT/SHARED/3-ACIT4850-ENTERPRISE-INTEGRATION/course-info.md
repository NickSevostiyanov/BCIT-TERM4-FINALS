# ACIT4850 — Enterprise Systems Integration

## Course Details
| Field | Info |
|-------|------|
| **Course Code** | ACIT4850 |
| **Course Title** | Enterprise Systems Integration |
| **Instructors** | Mike Mulder — mmulder10@bcit.ca (Sets B/C) · Johnny Zhang — johnny_zhang@bcit.ca (Set A) |
| **Term** | Term 4, Set A, 2025–2026 |

---

## Grade Rubric

> ⚠️ Exact weights not confirmed — syllabus PDFs not machine-readable. Verify on D2L → Grades.

| # | Component | Est. Weight | Details |
|---|-----------|:-----------:|---------|
| 1 | **Labs / Assignments** (3) | ~40% | Jenkins/GitLab/SonarQube/Nexus hands-on labs |
| 2 | **Quizzes** (11) | ~10% | Weekly reading-based quizzes on D2L |
| 3 | **Midterm Exam** | ~20% | Part 1 closed book paper, Part 2 practical laptop |
| 4 | **Final Exam** | ~30% | Two-part format (see below) |
| | **Total** | **~100%** | |

> **Minimum passing:** 50%. Aim for **70%+**
> **Check D2L** → ACIT4850 → Grades for exact weights.

---

## Logical Course Structure

| Week | Topic |
|------|-------|
| 1 | Enterprise, System, Integration definitions; On-prem vs Cloud; Tool evaluation criteria |
| 2 | JIRA (Work Management) & Confluence (Knowledge Base); installation methods & DB options |
| 3 | Functional vs Non-Functional Requirements; "ilities"; system quality attributes |
| 4 | DevOps definition + 3 practice areas; Continuous Integration; Stakeholders |
| 5 | CI Pipeline stages; Jenkins Pipeline; Declarative vs Scripted; Controller/Agents/Executors |
| 6 | Jenkins Shared Libraries; Global Shared Libraries; Debugging tools |
| 7 | Static Code Analysis; SonarQube (Quality Gate, Issues, Snapshots, Scanner, Platform); **Midterm** |
| 8 | GitLab CI — Runners, Pipelines, .gitlab-ci.yml, executors |
| 9 | Artifact Repositories (Nexus, Artifactory); components & formats |
| 10 | Continuous Delivery — 5 principles; deployment pipeline; Docker; Configuration Management |
| 11 | Trunk-Based Development vs Feature Branching; Merge/Pull Requests |
| 12 | GitLab CI variables; CI/CD components; pipeline use cases; Jenkins vs GitLab CI comparison |

---

## Final Exam Context

| Field | Info |
|-------|------|
| **Date** | Monday, April 20, 2026 |
| **Time** | 14:30 – 17:00 (150 minutes) |
| **Duration** | 150 minutes |
| **Location** | DTC 825, Level 4 |
| **Format** | **Two-part exam** (based on midterm format) |
| **Part 1 (~70%)** | Closed book, on paper — bring pen/pencil. Conceptual questions, definitions, MC, short answers. |
| **Part 2 (~30%)** | Laptop allowed. Jenkins/GitLab VMs on Azure; Python repos on GitLab; Jenkins pipeline with Jenkinsfile. |
| **Allowed Devices** | Laptop in Part 2 ONLY — no phone, no headphones |

> **Bring:** Student ID + pen or pencil for Part 1 · Laptop (charged) + VMs ready for Part 2

---

## Course Overview

**Enterprise Systems:** Define enterprise (large organization), system (set of interacting components), integration (connecting disparate systems to improve efficiency). On-premise vs Cloud trade-offs. Tool evaluation criteria: pricing, security/compliance, integration ecosystem.

**JIRA & Confluence:** JIRA = work management; Confluence = knowledge base. Production installs: Linux/Windows Installer, Cluster (HA), Zip/Archive. Supported DBs: Oracle, PostgreSQL, MySQL, MS SQL Server.

**Requirements:** Functional = behavior between inputs/outputs. Non-Functional (NFRs) = constraints on design; also called "ilities", quality attributes, architecturally significant requirements. Categories: Security, Scalability, Availability, Usability, Testability, Maintainability.

**DevOps:** Dev + Ops working together across the full service lifecycle. 3 practice areas: Infrastructure Automation, Site Reliability Engineering, Continuous Delivery.

**Continuous Integration:** Build triggered on every code change. Characteristics: automated build, automated tests, fast build, visibility, runs on every checkin. Repo should include: code, tests, DB schema, install scripts (NOT binaries, NOT OS).

**Jenkins:** Jenkinsfile in source control = pipeline definition. Declarative syntax: `pipeline { stages { stage { steps } } }`. Controller = brains/web server. Agent = manages task execution on a node. Executor = runs stages. Agent ≈ Node.

**Shared Libraries:** Written in Groovy. Structure: `/src` (classes), `/vars` (pipeline variables), `/resources`. Import: `@Library('name') _`. Global libraries visible to ALL jobs.

**SonarQube/Static Analysis:** Static = inspection without execution. Static + Dynamic = glass box testing. Issue types: Bugs, Vulnerabilities, Code Smells. Quality Gate = release conditions (apply to new code first). Snapshot = measures at a point in time. Scanner = client that computes snapshots. First analysis: SonarLint in IDE.

**GitLab CI:** `.gitlab-ci.yml` ≡ Jenkinsfile. Pipelines = jobs + stages. Jobs belong to stages (not vice versa). Runners = agents (Shell executor = machine dependencies; Docker executor = containers). Variables: mask sensitive ones or use external password manager.

**Artifact Repositories:** Nexus, Artifactory, Archiva, Maven. Advantage: versioning. Public repos: Maven Central, Docker Hub. Use artifact repo instead of Git: avoid bloating SCM with large files.

**Continuous Delivery:** 5 principles: Build quality in, Work in small batches, Computers do repetitive tasks, Relentlessly improve, Everyone is responsible. Config management goals: Reproducibility + Traceability. Docker: fast delivery, responsive scaling, more workloads on same hardware.

**Branching Strategies:** Trunk-based = branch only when necessary → fast, minimizes conflicts, good for experienced teams. Feature branching (Gitflow) = per-feature branches → more control, large teams. Pull Requests = GitHub; Merge Requests = GitLab.
