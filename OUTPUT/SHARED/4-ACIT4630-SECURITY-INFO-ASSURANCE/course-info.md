# ACIT4630 — Information Assurance and Security

## Course Details
| Field | Info |
|-------|------|
| **Course Code** | ACIT4630 |
| **Course Title** | Information Assurance and Security |
| **Instructor** | (Set A — see D2L for contact) |
| **Term** | Term 4, Set A, 2025–2026 |

---

## Grade Rubric

> ⚠️ Exact weights not confirmed — verify on D2L → Grades.

| # | Component | Est. Weight | Details |
|---|-----------|:-----------:|---------|
| 1 | **Labs / Assignments** | ~30% | Hands-on security labs |
| 2 | **Quizzes** (11) | ~20% | Weekly D2L quizzes |
| 3 | **Presentation** | ~20% | Group/individual security topic presentation |
| 4 | **Final Exam** | ~30% | Written exam |
| | **Total** | **~100%** | |

> **Minimum passing:** 50%. Aim for **70%+**
> **Check D2L** → ACIT4630 → Grades for exact weights.

---

## Logical Course Structure

| Week | Topic |
|------|-------|
| 1 | Course intro; CIA triad; threat actors; hacker types |
| 2 | CIA triad deep dive; encryption vs hashing; RAID/availability |
| 3 | Vulnerability types; STRIDE threat model; CVE/CVSS/NVD; vulnerability management lifecycle; DFDs |
| 4 | Malware types (virus, worm, trojan, spyware, botnet, ransomware); malware prevention |
| 5 | Backup types (full/differential/incremental); incident response; SIEM; events vs incidents |
| 6 | Cryptography — symmetric vs asymmetric; RSA; digital signatures; hashing properties |
| 7 | PKI; digital certificates (X.509); CA hierarchy; OCSP; certificate pinning |
| 8 | (midterm/break week) |
| 9 | (content continues) |
| 10 | Secure protocols — TLS (handshake, ephemeral key); SSH; SFTP/SCP/FTPS; HTTPS |
| 11 | (continued) |
| 12 | Network security — firewalls, DMZ, IDS/IPS, NAC, VLANs; network attacks (DDoS, Smurf, ARP, replay) |
| 13 | VPN; DNS attacks (poisoning, sinkhole, URL redirection); ARP poisoning; split-tunnel VPN |
| 14 | Presentations; Final Exam Review (Apr 14 online for Set A) |

---

## Final Exam Context

| Field | Info |
|-------|------|
| **Date** | Tuesday–Wednesday, April 21–22, 2026 |
| **Time** | ~10:30 AM – 12:30 PM |
| **Duration** | ~120 minutes |
| **Location** | DTC 825, Level 4 |
| **Format** | Written exam (based on quiz format: MC + multi-select + T/F) |
| **Open/Closed Book** | Assumed closed book — verify on D2L |

> **Bring:** Student ID + pen or pencil · Presentations were Apr 14 online

---

## Course Overview

**CIA Triad:** Confidentiality (access controls, encryption), Integrity (hashing, checksums), Availability (RAID, redundancy, backups). Encryption → confidentiality; Hashing → integrity.

**Threat Actors:** APT (most sophisticated) · Insider · Hacktivist · Script kiddie. White hat = improves security by finding vulnerabilities.

**STRIDE:** Spoofing · Tampering · Repudiation · Information Disclosure · Denial of Service · Elevation of Privilege. DoS → Availability threat. Tampering → Integrity threat.

**Vulnerabilities:** Server · Endpoint (end-user devices) · Supply Chain (3rd party) · Configuration · Architectural. CVE = Common Vulnerabilities and Exposures. CVSS = scoring system. NVD = additional details (patches, severity scores) for CVEs.

**Vulnerability Management:** Discover → Prioritize → Remediate → Validate → Monitor.

**Malware:** Worm (spreads without user interaction) · Virus · Trojan · Spyware (keylogger) · Ransomware · Botnet. Botmaster controls zombies. Zero-day = code exploiting vendor-unknown flaw. Armored = prevents disassembly. Polymorphic = changes signature each execution.

**Backups:** Full · Differential (changes since last full; faster restore, more storage) · Incremental (changes since last full OR incremental; slower restore, less storage).

**SIEM:** Central log collection + correlates to detect attack patterns.

**Cryptography:** Asymmetric (RSA) — encrypt with recipient's public key, decrypt with private key. Hashing — one-way, fixed-length output, collision resistant, no key needed. Digital signature = hash value encrypted with sender's PRIVATE key.

**PKI:** X.509 certificate standard. CA provides digital signature. Root CAs are offline. DV < OV < EV (trust levels). OCSP = most effective revocation method. SAN = Subject Alternative Name (lists additional domains).

**Secure Protocols:** TLS (evolved from SSL; client initiates with cipher list; uses ephemeral session key). SSH (public key crypto; port forwarding). Secure file transfer: SFTP, SCP, FTPS. NOT secure: FTP, Telnet, HTTP.

**Network Security:** DMZ = public-facing servers isolated from internal network. Ingress = inbound threats; Egress = outbound monitoring. Orphaned rule = leftover after service decommission. Shadowed rule = overridden by previous rule. NAC = authentication + posture check + role-based access. IPS In-band = blocks traffic.

**Network Attacks:** Smurf = ICMP Echo Request flood. DDoS via botnet = bandwidth + blends in. TCP = 3-way handshake (SYN → SYN/ACK → ACK). UDP = no handshake.

**DNS/VPN:** DNS poisoning = false DNS records. DNS sinkhole = same technique used defensively (blocks botnet C2). Split-tunnel VPN = VPN for org traffic only; direct internet for general browsing.
