# ACIT3855 — Service Based Architectures

## Course Details
| Field | Info |
|-------|------|
| **Course Code** | ACIT3855 |
| **Course Title** | Service Based Architectures |
| **Instructors** | Mike Mulder — mmulder10@bcit.ca &nbsp;|&nbsp; Rafi Mohammad — rafi_mohammad@bcit.ca |
| **Term** | Term 4, Set A, 2025–2026 |
| **Discord** | Available (see welcome post) |

---

## Grade Rubric

> ⚠️ **Exact weights not confirmed from readable materials — syllabus PDFs not accessible. Verify on D2L → Grades.**

| # | Component | Est. Weight | Details |
|---|-----------|:-----------:|---------|
| 1 | **Quizzes** (quiz0–quiz10, ~9 quizzes) | ~20% | 10–12 pts each, multiple select + T/F |
| 2 | **Labs** (Lab 1–12) | ~20% | Hands-on coding; REST APIs, Kafka, Docker, etc. |
| 3 | **Assignment 1** | ~20% | Posted Mar 25, due end of last class; "good practice for final exam" |
| 4 | **Midterm Exam** | ~15% | Feb 24, 2026; 2 hours; open book (paper only) |
| 5 | **Final Exam** | ~25% | 180 min; open book (paper only) |
| | **Total** | **~100%** | |

> **Minimum passing:** 50% overall. Aim for **70%+**
>
> **Check D2L** → ACIT3855 → Grades for exact weights.

---

## Logical Course Structure

| Week | Topic |
|------|-------|
| 1 | Microservices intro (Martin Fowler), REST API, HTTP methods, Connexion, operationId |
| 2 | JMeter load testing, Polyglot Persistence, Database-per-Service pattern, SQLAlchemy |
| 3 | Event Logging vs Tracing, Python logging module, config file formats (YAML/JSON/INI/XML) |
| 4 | OpenAPI 3.0 spec: metadata, paths, components, reuse, apscheduler/periodic processing |
| 5 | OpenAPI continued; messaging with microservices — why REST doesn't scale |
| 6 | Kafka: topics, producers, consumers, brokers, offsets, pub/sub, use cases |
| 7 | Kafka continued, Event Sourcing, Lab 6 demo, **Midterm review** |
| 8 | Docker + Virtual Environments, externalized config, log aggregation |
| 9 | Docker + Microservices, Docker volumes/mounts, distributed tracing, technical debt, testing types |
| 10 | Same Origin Policy (SOP), CORS, load balancing, NGINX, deployment strategies |
| 11 | Deployment strategies cont'd, canary/blue-green/recreate, scaling |
| 12 | Lab 12, Assignment 1 due |

---

## Final Exam Context

| Field | Info |
|-------|------|
| **Date** | Monday, April 20, 2026 |
| **Time** | 2:30 PM – 5:30 PM |
| **Duration** | **180 minutes** (3 hours) |
| **Location** | DTC 825, Level 4 |
| **Open/Closed Book** | ⭐ **FULLY OPEN BOOK** — paper printouts, cheatsheets, paper notes ALLOWED. **NO electronic devices.** |
| **Cheat Sheet Allowed** | ✅ **YES — unlimited printed cheat sheets** |
| **Exam Format** | • Multiple choice questions<br>• Short written answers<br>• Implement a simple API<br>• Fill in OpenAPI YAML blanks<br>• Write Python code for API endpoints (app.py) |
| **Midterm Scope** | Weeks 1–7 |
| **Final Exam Scope** | Likely weeks 8–12 (possibly cumulative — open book so bring everything) |

> **Key tip:** Because it's open book + unlimited printouts, your cheatsheet quality IS your advantage. Print the dense cheatsheet in this folder.

---

## Course Overview

**Architecture Concepts:** Microservices vs monolith, Conway's Law, polyglot persistence, database-per-service, eventual consistency, independent deployment, technology diversity.

**API Development:** REST/HTTP methods (GET/POST/PUT/DELETE), OpenAPI 3.0 specification (YAML), Connexion framework, operationId routing, strict_validation, apscheduler.

**Data & Persistence:** SQLAlchemy ORM (declarative model), SQLite vs MySQL, polyglot persistence, private-tables/schema/server-per-service.

**Observability:** Python logging (DEBUG/INFO/WARNING/ERROR/CRITICAL), event logging vs tracing, log_conf.yml, externalized config (app_conf.yml), log aggregation, distributed tracing.

**Messaging:** Apache Kafka (producers, consumers, brokers, topics, offsets), pub/sub pattern, event-driven microservices, async vs sync communication, Event Sourcing.

**Docker:** Containers, images, Dockerfile, docker-compose, volumes, bind mounts, tmpfs, log aggregation, externalized config pattern, `docker logs`, `docker-compose logs`.

**Web Security:** Same Origin Policy (SOP), CORS (Cross-Origin Resource Sharing), preflight requests.

**Deployment & Scaling:** NGINX (software load balancer, round robin default), load balancing strategies (round robin, IP hash, least connected), deployment strategies (recreate, blue/green, canary, ramped), `docker-compose up --scale`.

**Testing & Quality:** Unit testing, integration testing, UI functional testing, end-to-end testing, distributed tracing, technical debt.
