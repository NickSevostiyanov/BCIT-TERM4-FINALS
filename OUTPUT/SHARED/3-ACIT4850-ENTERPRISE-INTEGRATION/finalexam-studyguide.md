# ACIT4850 — Final Exam Study Guide
> 150 min | Two-Part | Part 1: Closed Book Paper (~70%) | Part 2: Laptop/VMs (~30%) | Mon Apr 20, 2026 @ 14:30 | DTC 825
> **Topics: Enterprise Systems, Requirements, DevOps/CI, Jenkins, SonarQube, GitLab CI, Artifact Repos, CD, Branching**

---

## 1. Enterprise Fundamentals

| Term | Definition |
|------|-----------|
| **Enterprise** | Large organization — business, govt, non-profit |
| **System** | Set of interacting/interdependent components |
| **Integration** | Connecting disparate enterprise systems to improve efficiency |
| **On-Premise** | You own/control hardware; Capital Expense; Pay Upfront; Controlled by your org |
| **Cloud** | 3rd party hosts infra; Operational Expense; Pay As You Go; Controlled by 3rd party |

**On-Premise best when:**
- Storing sensitive/trade-secret data
- Already have on-prem infrastructure
- IT dept has specific security/configuration requirements

**Cloud best when:**
- Small team with limited IT resources
- Prototyping / auto-scaling needed
- Pay As You Go model preferred

**Tool Evaluation Criteria:** Pricing/cost model · Security & compliance · Integration ecosystem/features · Support · Scalability

---

## 2. JIRA & Confluence

| Tool | Purpose |
|------|---------|
| **JIRA** | Work Management (tasks, sprints, bugs, backlogs) |
| **Confluence** | Knowledge Base (wikis, documentation, meeting notes) |

**Production Install Methods (JIRA/Confluence):**
- Installer — Linux ✓
- Installer — Windows ✓
- Cluster (High-Availability) ✓
- Zip or Archive File ✓
- ❌ Docker Container — NOT for production
- ❌ Installer — Mac — NOT available

**Supported Production Databases:**
- Oracle, PostgreSQL, MySQL, Microsoft SQL Server ✓
- ❌ Embedded H2 — development/evaluation ONLY

---

## 3. Functional vs Non-Functional Requirements

**Functional Requirement (FR):**
- Defines a **function** of a system or its component
- Specification of behavior between **outputs and inputs**
- Involves: calculations, data manipulation, technical details
- Example: "System shall bill the user's credit card immediately after order confirmation"

**Non-Functional Requirement (NFR):**
- Defines **constraints** on the design or implementation
- Also called: **"ilities"** · **System Quality Attributes** · **Architecturally Significant Requirements**
- Categories: **Security, Scalability, Availability, Usability, Testability, Maintainability** (all are valid)

**Distinguishing examples:**
| Statement | FR or NFR? |
|-----------|-----------|
| Bill credit card on order confirm | FR |
| System must handle 2M concurrent users without degradation | NFR |
| Support Chrome, Firefox, Safari browsers | NFR |
| Allow users to enter and track orders | FR |
| System should be restored from backup within 8 hours | NFR |

---

## 4. DevOps & Continuous Integration

**DevOps definition:**
> The practice of operations and development engineers participating together in the entire service lifecycle, from design through development to production support.

**3 Primary Practice Areas of DevOps:**
1. **Infrastructure Automation** — creating systems, OS configs, deployments as code; stored in SCM
2. **Continuous Delivery** — automating build, test, deploy (NOT manually daily)
3. **Site Reliability Engineering (SRE)** — operating systems; monitoring; orchestration; designing for operability

**Continuous Integration (CI):**
- Build triggered **every time code changes** (not on a schedule, not manually)
- When build breaks: **1–2 developers fix it** (NOT all developers)

**What goes in the single source code repo:**
- ✓ Code · Test Scripts · Database Schema · Install Scripts
- ✗ Compiled Binaries · Operating System

**Good CI Pipeline Characteristics (all apply):**
- Automated Build
- Automated Tests
- Runs on every checkin to SCM
- Fast Build and Test
- Visibility (status is visible to team)

**Stakeholders for Enterprise Dev Environment (all apply):**
- Project Manager, IT Operations, Test Team, Development Team, HR Manager
- ❌ Office Receptionist — not a stakeholder

---

## 5. Jenkins Pipelines

**Jenkinsfile:** Text file in source control containing the pipeline definition.

**Why Jenkinsfile in source control:**
- Single source of truth for the pipeline
- Audit trail
- Code review/iteration on pipeline
- Auto-creates pipeline for all branches/PRs

**Declarative Pipeline Structure:**
```groovy
pipeline {           // top-level block
  agent any          // where to run; required; can specify docker image
  stages {
    stage('Build') {
      steps {
        sh 'make'    // a Step = single task
      }
    }
    stage('Test') { steps { ... } }
    stage('Deploy') { steps { ... } }
  }
}
```

**Jenkins Components:**
| Term | Role |
|------|------|
| **Controller** | Web server + brains of Jenkins; manages the system |
| **Agent** | Manages task execution on a node; ≈ equivalent to a Node |
| **Executor** | Runs the stages in a pipeline |
| **Node** | Machine (physical or VM) where builds run; ≈ Agent |

**Separate Agent Nodes (key reasons):** Scalability · Security

**Pipeline triggered by:** Change to source code (NOT fixed schedule, NOT buildmaster, NOT manually)

**Best practice:** Define pipeline in Jenkinsfile in SCM, NOT directly in a Jenkins build job.

---

## 6. Jenkins Shared Libraries

**Purpose:** Share pipeline code across projects; keep code DRY (Don't Repeat Yourself)

**Written in:** Groovy

**Shared Library = 3 items (Version is optional):**
1. **Name**
2. **Source Code Retrieval Method**
3. **Version** *(optional)*

**Repository Structure:**
```
/src        → Groovy source files (classes)
/vars       → Script files exposed as variables in pipelines
/resources  → Non-Groovy files
```

**Import syntax:**
```groovy
@Library('my-shared-library') _       // imports the library; _ is required

evenOrOdd(currentBuild.getNumber())   // call function defined in vars/evenOrOdd.groovy
```

**Global Pipeline Libraries:** Available to ALL pipeline jobs on the Jenkins server (not just specific ones).

**Pipeline Debugging Tools:**
- Blue Ocean Editor
- Replay Pipeline Runs with Modifications
- IDE Plugin (Eclipse, VS Code, etc.)
- Command-Line Pipeline Linter

---

## 7. Static Code Analysis & SonarQube

**Static Code Analysis = inspection of code WITHOUT execution**

| Testing Type | Definition |
|--------------|-----------|
| **Static analysis** | Code inspection without running it |
| **Dynamic analysis** | Code inspection during execution |
| **Glass box testing** | Static + Dynamic combined |
| **White box testing** | Testing with knowledge of internal program flow/logic |
| **Black box testing** | Testing without knowledge of internals (testing interfaces) |

**SonarQube Issue Types (exactly 3):**
- **Bugs** — code defects likely to cause runtime errors
- **Vulnerabilities** — security risks
- **Code Smells** — maintainability issues

**Key SonarQube Concepts:**
| Term | Definition |
|------|-----------|
| **Quality Gate** | Set of conditions for release readiness. Apply to **new code first**. |
| **Technical Debt** | Estimated time to fix ALL maintainability issues + code smells |
| **Snapshot** | Set of measures and issues at a given time; generated per analysis |
| **Scanner** | Client app that analyzes source code to compute snapshots |

**SonarQube Platform Components (4):**
1. Scanners (for code analysis)
2. Server (Web Server + Search Server + Compute Engine)
3. Database
4. ❌ NOT: Cluster, REST API, or Plugins (wrong answers on quiz)

**Where to first analyze code:** SonarLint **in the IDE** (earliest feedback, before pushing to server)

---

## 8. GitLab CI

**Key Components:**
| Term | Definition |
|------|-----------|
| **Runners** | Agents that run jobs in GitLab CI |
| **Pipelines** | Made up of jobs and stages |
| **CI/CD Variables** | Way to store re-usable values in a pipeline |
| **CI/CD Components** | Reusable single pipeline configuration units |

**`.gitlab-ci.yml` ≡ `Jenkinsfile`** — pipeline definition file in source control

**Critical relationship:** Each **job** belongs to a **stage**. A stage can have multiple jobs (running in parallel). NOT: "each stage belongs to a job".

**Runner Executors:**
- **Shell executor** — has access to all dependencies installed on the machine
- **Docker executor** — runs pipeline jobs on containers based on Docker images

**Self-managed runners** — hosted on your own infrastructure

**CI/CD Variables:**
- Do NOT store sensitive info in .yml file (not encrypted there)
- Handle sensitive vars: **Mask** the variable (hidden in logs) · Use **external password manager**
- Reasons: Store values for re-use · Avoid hard-coding · Control job behavior
- Global vars = visible to entire pipeline; Job vars = only visible inside that job
- **Pre-Defined variables** = provided BY GitLab (not defined by the developer)

**GitLab CI Rules ≡ Jenkins `when`**

**CI/CD Component types:** job component · step component · trigger component
(NOT: pipeline component, variable component, stage component)

---

## 9. Artifact Repositories

**Artifact Repository:** Centralized storage for binary artifacts (build outputs)

**Two key characteristics:**
- Artifacts are **shared**
- Artifacts are **version-controlled**

**Advantage over plain filesystem:** Artifacts are **versioned**

**Use Nexus/Artifactory instead of Git:** Avoid **bloating SCM** with large binary files

**Tools:** Sonatype Nexus · Artifactory · Maven Artifact Repository · Archiva

**Public Repositories:** Maven Central Repository · Docker Hub

**Proxying public repos provides:**
- Insulation from internet/public repo outages
- Reduced network bandwidth
- Faster build times

**Artifact formats:** Docker Images · JAR/WAR/EAR · Zip/tar.gz · RubyGem

---

## 10. Continuous Delivery

**Core insight:** High performance teams deliver **faster AND more reliably** — speed does not trade off with stability.

**Benefits of CD:**
- Higher quality
- Higher revenues
- Low risk releases (small, frequent releases; blue/green deployments enable rollback)
- ❌ NOT: Lower costs or fewer developers

**5 Principles of Continuous Delivery:**
| # | Principle | Description |
|---|-----------|-------------|
| 1 | **Build quality in** | Create feedback loops early; never-ending quality work |
| 2 | **Work in small batches** | Reduces feedback time; easier triage; prevents sunk cost fallacy |
| 3 | **Computers perform repetitive tasks** | Humans solve problems; computers do regression testing |
| 4 | **Relentlessly pursue continuous improvement** | Every team member treats improvement as daily work |
| 5 | **Everyone is responsible** | Developers own quality AND stability; ops helps developers build quality in |

**Configuration Management — 2 goals:**
- **Reproducibility** — any environment can be reproduced identically from config
- **Traceability** — determine versions of every dependency, compare environments

**Deployment Pipeline:** Every change runs a build that:
1. Runs unit tests (developer feedback)
2. Creates deployable packages
3. Runs additional tests on packages that pass unit tests
4. Allows self-service deployment of packages that pass all tests

**Every change is a release candidate** (if it passes all stages).

**Docker 3 use cases:**
- Fast, consistent delivery
- Responsive deployment and scaling
- Running more workloads on same hardware

**Docker Compose:** Defines and runs multi-container apps; `docker-compose start` / `docker-compose stop`

---

## 11. Branching Strategies

| Strategy | Description |
|----------|-------------|
| **Trunk-Based Dev** | Branch only when absolutely necessary; all changes back to mainline quickly |
| **Feature Branching** | Separate branch per feature; associated with Gitflow |

**Trunk-Based Benefits:** Eliminates divergence · Minimizes merge conflicts · Developers move fast

**Trunk-Based Best For:** Experienced team · Pushing out new product fast

**Feature Branching Benefits:** Manage large-scale projects · Tight control over merges

**Feature Branching Best For:** Big team with varied skill levels · Mission-critical software requiring quality control

**Merge/Pull Requests:**
- **Pull Request** = GitHub terminology
- **Merge Request (MR)** = GitLab terminology
- How to use MR/PR to improve quality: Get feedback from team · Require approval before merge · Run CI pipeline on proposed changes

---

## 12. Jenkins vs GitLab CI

| Tool | Best For |
|------|---------|
| **Jenkins** | Larger orgs; diverse build requirements; complex enterprise environments |
| **GitLab CI** | Smaller teams; already using GitLab; prefers SaaS; easier adoption |

---

## 13. Part 2 Practical — Know These

**Jenkinsfile for Python project (Lab 5 stages):** Build → Unit Test → Integration Test

**GitLab CI `.gitlab-ci.yml` structure:**
```yaml
stages:
  - build
  - test
  - deploy

build-job:
  stage: build
  script:
    - echo "Building..."

test-job:
  stage: test
  script:
    - python -m pytest
```

**Jenkins Declarative Pipeline:**
```groovy
pipeline {
  agent any
  stages {
    stage('Build') { steps { sh 'pip install -r requirements.txt' } }
    stage('Unit Test') { steps { sh 'python -m pytest tests/unit' } }
    stage('Integration Test') { steps { sh 'python -m pytest tests/integration' } }
  }
}
```

---

## 14. Quick-Fire True/False Traps

| Statement | Answer |
|-----------|--------|
| Docker Container is a production install method for JIRA | **FALSE** — not for production |
| Embedded H2 is a supported production DB for JIRA | **FALSE** — dev/evaluation only |
| CI server should run build on a fixed daily schedule | **FALSE** — run on every code change |
| When build breaks, ALL developers must fix it | **FALSE** — 1-2 developers |
| Continuous Delivery means manually building/testing daily | **FALSE** — it's automated |
| Pipeline best practice: define it in Jenkinsfile in SCM | **TRUE** |
| Global Shared Libraries are only available to specific pipeline jobs | **FALSE** — available to ALL |
| Static + Dynamic code analysis = white box testing | **FALSE** — it's glass box testing |
| SonarQube Quality Gate should initially apply to ALL old code | **FALSE** — new code first |
| In gitlab-ci.yml, each stage belongs to a job | **FALSE** — each JOB belongs to a stage |
| Pre-Defined CI/CD variables are defined by the developer | **FALSE** — defined by GitLab |
| It is safe to store sensitive info in CI/CD variables in .yml file | **FALSE** — not encrypted |
| High performance teams trade stability for delivery speed | **FALSE** — they achieve both |
| Pull Request is GitLab terminology | **FALSE** — that's GitHub; GitLab uses Merge Request |
