# IEEE 2030.5-2023 ESI Trust & PKI Compliance Review

This document provides a technical compliance review of the extracted requirements from the IEEE 2030.5-2023 standard, focusing on client-server bidirectional trust, PKI architectures, and ESI trust boundaries.

---

### 1. SYSTEM CONTEXT (Extracted Standard Blueprint)
Below is the isolated PKI and trust-related compliance data extracted by the `ieee_parser` pipeline:

```json
[
  {
    "id": "REQ-159",
    "section_number": "6.5",
    "constraint_type": "Mandatory",
    "text": "The use of TLS (IETF RFC 5246) requires that all hosts implementing server functionality SHALL use a device certificate whereby the...",
    "page_number": 37
  },
  {
    "id": "REQ-161",
    "section_number": "6.5",
    "constraint_type": "Mandatory",
    "text": "Authentication of the server SHALL be done as part of the TLS handshake by validating its device certificate as described in (IETF...",
    "page_number": 37
  },
  {
    "id": "REQ-163",
    "section_number": "6.5",
    "constraint_type": "Mandatory",
    "text": "If the client has a device certificate, authentication of the client SHALL be done as part of the TLS handshake by validating the...",
    "page_number": 38
  },
  {
    "id": "REQ-165",
    "section_number": "6.5",
    "constraint_type": "Mandatory",
    "text": "If the client has a self-signed certificate, the self-signed certificate SHALL be validated for correctness.",
    "page_number": 38
  },
  {
    "id": "REQ-208",
    "section_number": "6.11.3.1",
    "constraint_type": "Recommendation",
    "text": "At the top level, Manufacturing PKI hierarchy SHOULD have one smart energy root certificate authority (SERCA).",
    "page_number": 48
  },
  {
    "id": "REQ-220",
    "section_number": "6.11.3.2",
    "constraint_type": "Mandatory",
    "text": "In such cases, the retired certificate and its associated private key SHALL no longer be used for issuing certificates.",
    "page_number": 49
  },
  {
    "id": "REQ-227",
    "section_number": "6.11.3.2",
    "constraint_type": "Mandatory",
    "text": "Retired certificates SHALL remain available to verify subsidiary certificates.",
    "page_number": 49
  },
  {
    "id": "REQ-229",
    "section_number": "6.11.3.2",
    "constraint_type": "Prohibition",
    "text": "A side effect of the indefinite lifetime requirement coupled with the permanent embedding of the device certificate and its certi... [is that certificates cannot be revoked using standard CRL/OCSP].",
    "page_number": 50
  },
  {
    "id": "REQ-230",
    "section_number": "6.11.3.2",
    "constraint_type": "Mandatory",
    "text": "Specifically, no MCA, MICA, or SERCA shall issue or be required to issue CRLs, and no MCA or MICA shall operate or have operated on...",
    "page_number": 50
  },
  {
    "id": "REQ-285",
    "section_number": "6.11.9.4",
    "constraint_type": "Permission",
    "text": "Vendors MAY provide a mechanism for a consumer/customer to set the trust status of any Root CA certificate and to add and delete...",
    "page_number": 63
  }
]
```

---

### 2. CORE COMPLIANCE DEFINITIONS
- **"SHALL" / "MUST"**: Absolute, non-negotiable mandatory design constraints.
- **"SHOULD"**: Strong recommendations where deviations require documented justification.
- **"MAY"**: Optional permissions that must not compromise any accompanying "shall" statements.

---

### 3. USER EXPLORATION QUERY
**Query**: *"How does the IEEE 2030.5-2023 certificate authority (PKI) architecture establish bidirectional trust between clients and servers at the Energy Service Interface (ESI) boundary, and what vulnerabilities are introduced by the lack of dynamic revocation (CRLs/OCSP)?"*

---

### 4. YOUR ANALYSIS STEPS

#### Step 1: Scope Isolation
- **Target Requirements**:
  - `REQ-159`/`161` (Section 6.5): Server authentication requirements.
  - `REQ-163`/`165` (Section 6.5): Client validation mandates.
  - `REQ-208` (Section 6.11.3.1): Root CA (SERCA) architecture.
  - `REQ-229`/`230` (Section 6.11.3.2): Revocation prohibition and indefinite device certificate lifetimes.
  - `REQ-285` (Section 6.11.9.4): User-managed trust store permissions.

#### Step 2: Constraint Mapping
- **Mandated (Shalls)**:
  - All hosts serving resources **SHALL** use a device certificate (`REQ-159`).
  - Server identity **SHALL** be authenticated during the TLS handshake by validating its certificate (`REQ-161`).
  - Client identity **SHALL** be authenticated during the TLS handshake if the client has a device certificate (`REQ-163`).
  - Self-signed client certificates **SHALL** be validated for correctness (`REQ-165`).
  - Retired CAs **SHALL NOT** issue new certificates (`REQ-220`), but retired CA certificates **SHALL** remain available for validating subordinate device certificates (`REQ-227`).
  - No Manufacturing CA (SERCA, MCA, MICA) **SHALL** issue Certificate Revocation Lists (CRLs) or operate OCSP responders (`REQ-230`).
- **Recommended (Shoulds)**:
  - The PKI hierarchy **SHOULD** terminate in a single Smart Energy Root CA (SERCA) (`REQ-208`).
- **Permitted (Mays)**:
  - Vendors **MAY** provide a mechanism for customers/consumers to add, delete, or modify Root CA trust status (`REQ-285`).

#### Step 3: Contradiction & Ambiguity Check
1. **The Revocation-Free Trust Hole (`REQ-230` vs `REQ-163`)**:
   - `REQ-163` mandates client certificate validation during the TLS handshake to establish client trust.
   - `REQ-230` prohibits Manufacturing CAs from issuing CRLs or operating OCSP responders due to embedded certificates having indefinite lifetimes (`REQ-229`).
   - *Contradiction/Ambiguity*: Under standard PKI, if a client device is compromised (e.g. private key extracted), its trust is revoked via CRLs or OCSP. Because IEEE 2030.5 forbids revocation for the Manufacturing PKI, a compromised client certificate remains cryptographically valid forever. This breaks standard trust assumptions: the ESI cannot rely on the TLS handshake results to verify that a device is still trusted. Trust revocation must be handled entirely at the application layer, forcing the ESI server to maintain external blocklists of compromised LFDIs, blending network-level and application-level security domains.
2. **The Custom Trust Anchor Hazard (`REQ-285` vs `REQ-208`)**:
   - `REQ-208` recommends a single SERCA to ensure a unified trust chain.
   - `REQ-285` permits vendors to allow consumers to modify the trust status of Root CAs.
   - *Conflict*: If a customer alters the root trust store on their local ESI gateway, they may inadvertently trust a rogue Root CA (enabling MitM attacks) or delete the utility's Root CA (breaking grid services synchronization).

#### Step 4: Implementation Blueprint (For EGoT Engineering Team)
- [ ] **Enforce Application-Layer LFDI Blacklisting (Mitigate REQ-230 revocation gap)**:
  - Since standard TLS certificate validation (`REQ-163`) cannot check for revocation, the EGoT server must maintain a real-time LFDI Blacklist in its database.
  - On every connection, extract the client's LFDI from its TLS certificate and check it against the blacklist. Reject the request immediately if it is blacklisted, regardless of TLS handshake success.
- [ ] **Strict OID and Constraint Checks during TLS Handshake**:
  - Configure the Go TLS listener (`tlsutil.NewServerConfig`) to validate that the client certificate chain matches the Smart Energy Root CA (SERCA) (`REQ-208`).
  - Verify that the certificate contains the mandatory IEEE 2030.5 Policy OIDs (e.g., `id-IEEE 2030.5-po-device`) to block generic or non-grid certificates from authenticating.
- [ ] **Isolate Consumer-Managed Roots (`REQ-285`)**:
  - If a user-facing dashboard is provided to modify trust status, partition the trust store:
    - Custom user roots must only authorize local consumer applications (e.g., local home automation).
    - Grid-critical services (DERControls, FlowReservation) must strictly validate certificates against the utility's official Root CA chain.
- [ ] **Hardware-Backed Key Protection**:
  - Secure EGoT server identities (`REQ-159`) using a Hardware Security Module (HSM) to prevent private key extraction, ensuring the server's identity remains completely tamper-proof.
