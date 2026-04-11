# ACIT3495 — Advanced Topics in IT Infrastructure

## Course Details
| Field | Info |
|-------|------|
| **Course Code** | ACIT3495 |
| **Course Title** | Advanced Topics in IT Infrastructure |
| **Instructor** | Dr. Motasem Aldiab (maldiab@bcit.ca) |
| **Term** | Term 4, 2025–2026 |

---

## Grade Rubric

> ⚠️ Exact weights not confirmed — verify on D2L → Grades.

| # | Component | Est. Weight | Details |
|---|-----------|:-----------:|---------|
| 1 | **Labs** | ~40% | Docker + Kubernetes labs (Lab1–Lab9) |
| 2 | **Quizzes** (4) | ~20% | D2L quizzes |
| 3 | **Projects** (2) | ~20% | Project1 (presentations Feb 2026) + Project2 (presentations Apr 9–10, 2026) |
| 4 | **Final Exam** | ~20% | Written exam |
|   | **Total** | **~100%** | |

> **Check D2L** → ACIT3495 → Grades for exact weights.

---

## Logical Course Structure

| Week | Topic |
|------|-------|
| 1–2 | Course intro; Docker install (Ubuntu/Debian VM + Docker Desktop) |
| 3–4 | Docker fundamentals — images, containers, volumes, networks, port mapping |
| 5 | Docker Compose — multi-container apps |
| 6–9 | Kubernetes (K8s) basics — Pods, Deployments, Services (ClusterIP, NodePort, LoadBalancer) |
| 10 | Kubernetes Deployments — scaling, labels, namespaces, rolling updates |
| 11 | Kubernetes State Persistence — Volumes, PersistentVolumes (PV), PersistentVolumeClaims (PVC), initContainers, SideCar containers |
| 12 | ConfigMaps and Secrets |
| 13–14 | Project 2 presentations (Apr 9–10) + Final lab session (Apr 16–17) |

---

## Final Exam Context

| Field | Info |
|-------|------|
| **Date** | Thursday, April 24, 2026 |
| **Time** | 15:30 – 17:00 |
| **Duration** | ~90 minutes |
| **Location** | TBC — check D2L |
| **Format** | Written exam (based on quiz format: MC + T/F) |
| **Open/Closed Book** | Assumed closed book — verify on D2L |

> **Bring:** Student ID + pen or pencil

---

## Quiz Performance Summary

| Quiz | Score | Topics |
|------|-------|--------|
| Quiz 1 | **4/10 (40%)** ⚠️ | Docker basics — commands, images, containers, volumes |
| Quiz 2 | **6/6 (100%)** ✓ | Kubernetes basics — Pods, Deployments, Services, EKS |
| Quiz 3 | 7/10 (70%) | Kubernetes intermediate — ReplicaSet, kube-apiserver, service types |
| Quiz 4 | ~6/10 | Kubernetes advanced — PV/PVC, initContainers, RollingUpdate |

> Quiz 1 was rough — review Docker commands carefully (especially `docker run` vs `docker pull`, `docker rmi` vs `docker rm`).

---

## Course Overview

**Docker:** Container platform (NOT an orchestration tool — Kubernetes is). `docker run` = create + start container. `docker pull` = download image only. `docker exec` = connect to running container. `docker rmi` = remove image; `docker rm` = remove container. Volume = persist data after container deletion. Restart policy = restart when exits. Dockerfile = build instructions.

**Kubernetes (K8s):** Orchestration tool — automates deployment, scaling, management of containers. Pod = smallest unit (one or more containers sharing network + storage). Deployment = manages desired state + rolling updates. ReplicaSet = ensures specified replica count.

**K8s Services:** ClusterIP (default, internal only) · NodePort (static port 30000–32767 on each node) · LoadBalancer (provisions external cloud LB). kube-apiserver = exposes K8s API. Docker Desktop K8s = lightweight single-node cluster.

**State Persistence:** PersistentVolume (PV) = cluster storage resource. PersistentVolumeClaim (PVC) = request for storage from available PVs. Data on PV persists independently of Pod lifecycle. `capacity` field = how much storage is available. RollingUpdate = gradual update strategy.

**ConfigMaps + Secrets:** ConfigMap = stores non-sensitive key-value config data. Secret = stores sensitive data (passwords, tokens), stored base64-encoded in K8s.
