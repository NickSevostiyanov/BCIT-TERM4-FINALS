# ACIT4630 — Final Exam Study Guide
> ~120 min | Closed Book (assumed) | Written MC + T/F + Multi-Select | Tue/Wed Apr 21–22, 2026 @ ~10:30 | DTC 825
> **Topics: CIA, STRIDE, Malware, Cryptography, PKI, TLS, Network Security, DNS Attacks, VPN**

---

## 1. CIA Triad — Core Objectives of Information Security

| Goal | Controls / Examples |
|------|-------------------|
| **Confidentiality** | Encryption · Access controls · Steganography |
| **Integrity** | Hashing · Checksums · File integrity monitoring |
| **Availability** | RAID · Redundancy · Backups · Uptime SLAs |

**Key mappings (exam traps):**
- Encryption → **Confidentiality**
- Hashing → **Integrity** (NOT confidentiality)
- RAID (redundant drives) → **Availability** (NOT integrity)
- Access controls (can't read files outside your job) → **Confidentiality**
- Steganography (hides info inside images) → **Confidentiality**
- DoS attack → threatens **Availability**
- Tampering → threatens **Integrity**

---

## 2. Threat Actors

| Actor | Description |
|-------|-------------|
| **APT** (Advanced Persistent Threat) | Most sophisticated; nation-state level; long-term access |
| **Insider** | Employee/contractor with legitimate access |
| **Hacktivist** | Politically motivated |
| **Script Kiddie** | Uses existing tools, low skill |

- **White hat** = ethical hacker; uncovers vulnerabilities to improve security
- **Black hat** = malicious attacker
- Security pros must **balance** security against other business needs (TRUE)

---

## 3. STRIDE Threat Model

| Letter | Threat | CIA Impact |
|--------|--------|-----------|
| **S** | **Spoofing** | Confidentiality / Authentication |
| **T** | **Tampering** | Integrity |
| **R** | **Repudiation** | Non-repudiation |
| **I** | **Information Disclosure** | Confidentiality |
| **D** | **Denial of Service** | Availability |
| **E** | **Elevation of Privilege** | Authorization |

**STRIDE is used to:** identify different types of security threats (used with DFDs for threat modeling)

---

## 4. Vulnerabilities & Vulnerability Management

**Vulnerability Types:**
| Type | Example |
|------|---------|
| **Server** | Outdated web server allowing code execution |
| **Endpoint** | Weaknesses in end-user devices (computers, smartphones) |
| **Supply Chain** | Risks from 3rd-party components/services |
| **Configuration** | Default configs, weak ciphers, missing patches |
| **Architectural** | Design flaws in system structure |

**Vulnerability Management Lifecycle:**
1. **Discover** — identify all vulnerabilities
2. **Prioritize** — decide which need immediate attention based on risk
3. **Remediate** — patch/fix issues
4. **Validate** — confirm fixes worked
5. **Monitor** — ongoing tracking

**Key Terms:**
- **CVE** — Common Vulnerabilities and Exposures (identifier)
- **CVSS** — Common Vulnerability Scoring System (severity score)
- **NVD** — National Vulnerability Database; adds patch availability + severity scores to CVEs

**Data Flow Diagrams (DFD):**
- Graphical representation of data flow through an information system
- Used in security to: **identify points where data is at risk**
- **Privilege Boundary** = where web server communicates with database at different privilege levels

**Configuration Vulnerability Management (ordered steps):**
1. **Avoid** default configurations
2. **Verify** device security before network integration
3. **Follow** documented security standards and best practices
4. **Apply** secure cryptographic protocols and strong ciphers
5. **Choose** the principle of least privilege

---

## 5. Malware

| Type | Key Characteristic |
|------|--------------------|
| **Worm** | Spreads WITHOUT user interaction |
| **Virus** | Requires user interaction to spread |
| **Trojan** | Disguised as legitimate software |
| **Spyware** | Monitors activity (keylogger = spyware) |
| **Ransomware** | Encrypts files, demands payment |
| **Adware** | Displays unwanted advertisements |
| **Botnet** | Network of compromised (zombie) systems |

**Botnet concepts:**
- **Botmaster** = controls command-and-control (C2) systems over legitimate compromised machines
- **Zombie** = a compromised computer receiving and executing botmaster commands
- Botnets useful for: brute force attacks, DDoS (bandwidth + blends in with legit traffic)

**Phishing variants:**
| Type | Target |
|------|--------|
| **Phishing** | Mass email |
| **Spear phishing** | Specific individual |
| **Whaling** | Senior executives specifically |
| **Vishing** | Voice/phone-based |
| **Pharming** | Redirects web traffic via DNS manipulation |

**Zero-day exploit:** Code written to take advantage of a software flaw **unknown to its vendor**

**Virus types:**
- **Armored** = prevents disassembly and debugging
- **Polymorphic** = changes form/signature each execution to avoid detection

**Malware prevention methods:**
| Method | Best For |
|--------|---------|
| **Signature detection** | KNOWN malwares (most effective for known) |
| **Heuristic detection** | Unknown, based on suspicious patterns |
| **Behavior analysis** | Anomaly-based; monitors runtime behavior |
| **Sandboxing** | Execute suspicious code in contained environment before allowing it on protected system |

---

## 6. Backups & Incident Response

**Backup Types:**
| Type | What it includes | Storage | Recovery speed |
|------|-----------------|---------|----------------|
| **Full** | Everything | Most | Fastest (1 file) |
| **Differential** | Changes since last **full** | More than incremental | Fast (2 files: full + latest differential) |
| **Incremental** | Changes since last **full OR incremental** | Least | Slowest (merge entire chain) |

**Incident Response:**
- **Security event** = any observable occurrence (login attempt = event, whether successful or not)
- **Security incident** = adverse event that actually violates security policy — NOT all adverse events are incidents
- After compromise: **rebuild** the system (TRUE — do not trust it)
- Assign **severity ratings** based on nature and scope of potential impact
- Assess data availability impact: consider **recovery time** from downtime
- Sources for incident data: Firewalls · IDS/IPS · Integrity monitors · Vulnerability scanners · Authentication systems

**SIEM (Security Information and Event Management):**
- Central secure collection point for ALL log entries
- Correlates security info from multiple devices to detect patterns of malicious activity

---

## 7. Cryptography

### Symmetric vs Asymmetric

| Feature | Symmetric | Asymmetric (RSA) |
|---------|-----------|-----------------|
| Keys | Same key for encrypt/decrypt | Public key + private key pair |
| Speed | Fast | Slow |
| Use case | Bulk data encryption | Key exchange, digital signatures |

**Asymmetric (RSA):**
- Anything encrypted with one key → decrypted with the OTHER key from same pair
- **Encrypt message**: use recipient's **public** key
- **Decrypt message**: use recipient's **private** key
- RSA keys = made from **prime numbers**
- RSA is slow → used to exchange a **symmetric session key** (hybrid approach)

**Hashing:**
- Does NOT use a key (just the input data)
- Properties of secure hash function:
  - **Fixed-length output** (regardless of input size)
  - **One-way** (cannot reverse)
  - **Collision resistant** (hard to find two inputs with same output)
- Hashing → protects **integrity**

**Longer encryption key:** More secure, but **lower performance** (slower)

### Digital Signatures
> = Hash value of message encrypted with **sender's private key**

Process:
1. Sender hashes the message
2. Sender encrypts hash with their **private key** → this is the signature
3. Recipient decrypts signature with sender's **public key** → gets hash
4. Recipient hashes received message → compares to decrypted hash
5. Match = message is authentic and untampered

**Inputs/outputs of encryption:**
- Input: plaintext + encryption key
- Output: ciphertext

---

## 8. PKI & Digital Certificates

**X.509** = standard governing structure and content of digital certificates

**What a certificate does:** Vouches for the subject's **identity** and their **public key**

**Digital signature on certificate** = provided by the **Certificate Authority (CA)**

**CA hierarchy:**
- **Root CA** = usually **offline** to protect private key; only occasionally signs intermediate CA certs
- **Intermediate CA** = actually issues certificates to customers

**Trust levels (lowest to highest):**
1. **DV** (Domain Validation) — lowest trust
2. **OV** (Organization Validation) — medium
3. **EV** (Extended Validation) — highest trust

**Self-signed / internal CA certs:** NOT trusted by the outside world (only for internal use)

**SAN** (Subject Alternative Name) = lists all other domain names covered by the same certificate

**Certificate Pinning:** Protects against fraud; tells users that the certificate should NOT change over time; if it changes, flag as potential security issue. NOT used to create false certificates.

**Certificate Revocation:**
- **OCSP** (Online Certificate Status Protocol) = **most effective** revocation method
- CRL (Certificate Revocation List) = older, less efficient

**Eavesdropping during asymmetric key exchange:** NOT needed (public key is already public)

---

## 9. Secure Protocols

| Protocol | Port | Secure? | Notes |
|----------|------|---------|-------|
| **TLS** | 443 | ✓ | Evolved from SSL; use instead of all SSL versions |
| **SSH** | 22 | ✓ | Public key crypto; ephemeral session key; port forwarding |
| **SFTP** | 22 | ✓ | File transfer over SSH |
| **SCP** | 22 | ✓ | Secure copy over SSH |
| **FTPS** | 990 | ✓ | FTP over TLS |
| **HTTPS** | 443 | ✓ | HTTP over TLS |
| **HTTP** | 80 | ✗ | Unencrypted — anyone can see traffic |
| **FTP** | 21 | ✗ | Not secure — use SFTP/FTPS |
| **Telnet** | 23 | ✗ | Not secure — use SSH |
| **SSLv1/v2/v3** | — | ✗ | Deprecated; use TLS instead |

**TLS Handshake (in order):**
1. **Client sends** request with list of supported cipher suites
2. Server responds (selects cipher suite, sends certificate)
3. Key exchange → ephemeral session key negotiated
4. Encrypted communication begins

**TLS ephemeral key:**
- Used **only for one session** (also called session key)
- Encrypted with server's **public key**; decrypted with server's **private key**

**SSL Inspection:** Performs a "friendly" MITM attack on organization's own users to inspect traffic content (TRUE)

**Heartbleed:** A past OpenSSL vulnerability — **current** versions are patched; not still vulnerable

---

## 10. Network Security

### Firewalls & Segmentation

| Term | Definition |
|------|-----------|
| **DMZ** | Zone for servers accepting external connections (web, email); isolated from internal network |
| **Ingress filtering** | Watches for threats **entering** the network |
| **Egress filtering** | Monitors traffic **leaving** the network (detects compromised systems) |
| **Orphaned rule** | Firewall rule left after service is decommissioned |
| **Shadowed rule** | Rule overridden/made unreachable by a previous rule |
| **Promiscuous rule** | Overly permissive rule |
| **NAC** | Network Access Control — user authentication + security posture check + role-based access |

**VLAN pruning** = limits exposure of sensitive traffic on switches

### IDS / IPS

| Type | Behavior |
|------|---------|
| **IDS** (detection) | Monitors and alerts; does NOT block |
| **IPS In-band** | Sits directly on network path; **can block** suspicious traffic |
| **IPS Out-of-band/Passive** | Monitors copy of traffic; cannot block in real time |

---

## 11. Network Attacks

**TCP vs UDP:**
| Feature | TCP | UDP |
|---------|-----|-----|
| Connection | 3-way handshake (SYN→SYN/ACK→ACK) | No handshake |
| Reliability | Reliable (guaranteed delivery) | Unreliable |
| Use cases | Email, web, file transfer | Voice, video, streaming |
| Layer | Transport layer | Transport layer |

- First TCP handshake step = **SYN** (client → server), NOT SYN/ACK
- Only **TCP** does 3-way handshake — NOT UDP

**Attack types:**
| Attack | Description |
|--------|-------------|
| **Smurf attack** | Floods target with ICMP Echo Requests (amplification) |
| **DDoS via botnet** | Large bandwidth + traffic blends with legitimate requests |
| **Replay attack** | Attacker captures **encrypted** credentials and replays them (cannot see actual credentials) |
| **ARP poisoning** | Poisons ARP cache; only works on **local network** |
| **Network sniffing** | Capturing network traffic; has legitimate security/troubleshooting uses |

- Traffic on **non-standard ports** may indicate port-based filtering bypass attempt

---

## 12. DNS Attacks & VPN

**DNS Attack Types:**
| Attack | Description |
|--------|-------------|
| **DNS Poisoning** | Inserts false DNS records → redirects users to fake sites |
| **DNS Sinkhole** | Same technique used DEFENSIVELY (security pros redirect botnet C2 traffic) |
| **URL Redirection** | Content on legitimate site auto-forwards user to malicious site |
| **Typosquatting** | Registers similar-looking domain names |
| **Domain Hijacking** | Takes over legitimate domain registration |

DNS caching: name server caches IP + all nameserver locations along the query path

**VPN:**
- Provides access to private network services over **public** network infrastructure
- Performance issue: firewalls/routers/servers lack specialized encryption hardware → use dedicated VPN appliances
- **Split-tunnel VPN**: org-specific traffic → VPN tunnel; general web browsing → direct internet
- **Full tunnel VPN**: ALL traffic through the VPN
- SSH can forward ports securely (limited VPN-like functionality for remote users)

---

## 13. Quick-Fire True/False Traps

| Statement | Answer |
|-----------|--------|
| RAID = Integrity control | **FALSE** — RAID = Availability |
| Steganography enforces Confidentiality | **TRUE** |
| DoS attack threatens Integrity | **FALSE** — it threatens Availability |
| Hashing uses a cryptographic key | **FALSE** — no key needed |
| Worm spreads without user interaction | **TRUE** |
| Virus spreads without user interaction | **FALSE** — needs user action |
| Signature detection = best for UNKNOWN malware | **FALSE** — best for KNOWN; heuristic for unknown |
| Differential backup is faster to restore than incremental | **TRUE** (2 files vs chain) |
| Incremental backup uses LESS storage than differential | **TRUE** |
| All adverse security events are security incidents | **FALSE** — not all adverse events become incidents |
| A login attempt (whether successful or not) = security event | **TRUE** |
| Rebuild any system that may have been compromised | **TRUE** |
| RSA is used to encrypt long messages directly | **FALSE** — used to exchange session key |
| Encrypt with recipient's private key to send secure message | **FALSE** — use recipient's PUBLIC key |
| Digital signature uses sender's PRIVATE key | **TRUE** |
| Self-signed CA certs are trusted by the outside world | **FALSE** — only internal |
| Root CAs are usually offline | **TRUE** |
| DV provides highest trust level among cert types | **FALSE** — DV is LOWEST; EV is highest |
| OCSP is the most effective certificate revocation method | **TRUE** |
| Eavesdropping protection needed in asymmetric key exchange | **FALSE** — public key is already public |
| HTTP traffic is unencrypted | **TRUE** |
| Heartbleed still affects current OpenSSL | **FALSE** — patched |
| TLS first step = client sends cipher suite list | **TRUE** |
| UDP performs 3-way handshake | **FALSE** — only TCP |
| First TCP handshake step = SYN/ACK | **FALSE** — SYN is first |
| Replay attacker can see actual credentials | **FALSE** — they're encrypted |
| ARP poisoning works across the internet | **FALSE** — local network only |
| Network sniffing is only malicious | **FALSE** — also used for troubleshooting |
| DNS sinkhole = same technique as DNS poisoning | **TRUE** — but used defensively |
| Split-tunnel VPN routes all traffic through VPN | **FALSE** — only org traffic |
