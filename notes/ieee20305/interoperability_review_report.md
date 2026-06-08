# IEEE 2030.5-2023 Grid Services Client-Server Interoperability Compliance Review

This document provides a technical compliance review of the extracted requirements from the IEEE 2030.5-2023 standard, focusing on client-server interoperability, primacy configurations, and overlapping event scheduling for grid services.

---

### 1. SYSTEM CONTEXT (Extracted Standard Blueprint)
Below is the isolated grid service scheduling and primacy compliance data extracted by the `ieee_parser` pipeline:

```json
[
  {
    "id": "REQ-578",
    "section_number": "10.2.2.3",
    "constraint_type": "Mandatory",
    "text": "Clients that act on Events that do not subscribe to their Event lists SHALL poll the Event lists for new Events at the less frequent of every 15 minutes or pollRate.",
    "page_number": 134
  },
  {
    "id": "REQ-580",
    "section_number": "10.2.2.3",
    "constraint_type": "Mandatory",
    "text": "Clients SHALL monitor the active Event(s) for status changes at the less frequent of every 15 minutes or pollRate.",
    "page_number": 134
  },
  {
    "id": "REQ-582",
    "section_number": "10.2.2.3",
    "constraint_type": "Prohibition",
    "text": "Editing Events SHALL NOT be allowed except for updating status.",
    "page_number": 134
  },
  {
    "id": "REQ-583",
    "section_number": "10.2.2.3",
    "constraint_type": "Mandatory",
    "text": "Service providers SHALL cancel Events that they wish clients to not act upon and/or provide new superseding Events.",
    "page_number": 134
  },
  {
    "id": "REQ-585",
    "section_number": "10.2.2.3",
    "constraint_type": "Mandatory",
    "text": "When comparing two Overlapping Events from servers with the same primacy, the creationTime element SHALL be used to determine which event takes precedence.",
    "page_number": 134
  },
  {
    "id": "REQ-586",
    "section_number": "10.2.2.3",
    "constraint_type": "Recommendation",
    "text": "Servers SHOULD make minimum use of Overlapping Events.",
    "page_number": 134
  },
  {
    "id": "REQ-596",
    "section_number": "10.2.2.3",
    "constraint_type": "Mandatory",
    "text": "For function sets with direct control, regardless of the state of an Event (scheduled or active), when a client detects an Overlapping Event, the client SHALL adjust the duration of the overlapped Event.",
    "page_number": 135
  },
  {
    "id": "REQ-597",
    "section_number": "10.2.2.3",
    "constraint_type": "Mandatory",
    "text": "If the Effective Start Time of the overlapped Event is before the Effective Start Time of the Overlapping Event, the client SHALL change the duration of the overlapped Event to end at the Effective Start Time of the Overlapping Event.",
    "page_number": 135
  },
  {
    "id": "REQ-598",
    "section_number": "10.2.2.3",
    "constraint_type": "Mandatory",
    "text": "If the Effective End Time of the overlapped Event is after the Effective End Time of the Overlapping Event, the client SHALL change the start time of the overlapped Event to the Effective End Time of the Overlapping Event.",
    "page_number": 135
  },
  {
    "id": "REQ-613",
    "section_number": "10.2.2.3",
    "constraint_type": "Mandatory",
    "text": "Differing DERControl Modes from differing DERPrograms that cannot be executed simultaneously by a device SHALL execute the DERControl of the higher primacy. If primacy values are identical, the event with the latest creationTime SHALL be executed.",
    "page_number": 136
  },
  {
    "id": "REQ-655",
    "section_number": "10.2.4.6",
    "constraint_type": "Mandatory",
    "text": "Clients SHALL determine the primacy of DRLC and DER Control based on the following in order of precedence:...",
    "page_number": 142
  },
  {
    "id": "REQ-656",
    "section_number": "10.2.4.6",
    "constraint_type": "Mandatory",
    "text": "Servers SHALL indicate their primacy in the primacy element of the function set instance.",
    "page_number": 142
  },
  {
    "id": "REQ-657",
    "section_number": "10.2.4.6",
    "constraint_type": "Mandatory",
    "text": "Clients SHALL prioritize execution of DRLC and DER function set Events with different PrimacyType attributes using the following guidelines...",
    "page_number": 142
  },
  {
    "id": "REQ-660",
    "section_number": "10.2.4.6",
    "constraint_type": "Recommendation",
    "text": "Reputable service providers should appropriately self-select their PrimacyType attribute so as not to disadvantage the consumer’s operations.",
    "page_number": 142
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
**Query**: *"How do clients and servers achieve deterministic synchronization and conflict resolution when scheduling overlapping grid service events (DERControls) from different programs or servers, and what interoperability challenges arise in multi-primacy configurations?"*

---

### 4. YOUR ANALYSIS STEPS

#### Step 1: Scope Isolation
- **Target Requirements**:
  - `REQ-578`/`580` (Section 10.2.2.3): Event pulling and active status monitoring polling limits.
  - `REQ-585`/`596`/`597`/`598` (Section 10.2.2.3): Precedence and truncation math for overlapping events.
  - `REQ-613` (Section 10.2.2.3): Program mode clashes and resolution via `creationTime` and primacy.
  - `REQ-655`/`656`/`657`/`660` (Section 10.2.4.6): Primacy definitions and client prioritization rules.

#### Step 2: Constraint Mapping
- **Mandated (Shalls)**:
  - Clients **SHALL** poll for new events at the less frequent of 15 minutes or `pollRate` (`REQ-578`).
  - Clients **SHALL** monitor active events for status changes every 15 minutes or at `pollRate` (`REQ-580`).
  - Clients **SHALL** adjust durations when an overlapping event is detected (`REQ-596`).
  - If a new event overlaps:
    - If the old event starts before the new one, the client **SHALL** shorten the old event to end exactly when the new event begins (`REQ-597`).
    - If the old event ends after the new one, the client **SHALL** shift the old event's start time to align with the new event's end time (`REQ-598`).
  - Clashing DERControl modes from different DERPrograms **SHALL** run the control of the higher primacy, falling back to the latest `creationTime` if primacy values match (`REQ-613`, `REQ-585`).
  - Servers **SHALL** specify their primacy (`REQ-656`), and clients **SHALL** prioritize events according to standard primacy categories (`REQ-657`, `REQ-655`).
- **Recommended (Shoulds)**:
  - Servers **SHOULD** minimize overlapping events (`REQ-586`), using them only if conditions mandate supersession (`REQ-587`).
  - Service providers **SHOULD** self-select primacy values responsibly (`REQ-660`).
- **Prohibited (Shall Nots)**:
  - Clients **SHALL NOT** edit events except to update status (`REQ-582`).

#### Step 3: Contradiction & Ambiguity Check
1. **The Polling Latency Loophole (`REQ-578` vs `REQ-596`)**:
   - `REQ-578` allows client devices to poll for events up to every 15 minutes (if `pollRate` is 15 mins or higher).
   - However, `REQ-596` mandates that a client *shall* immediately adjust the duration of a scheduled or active event upon detecting an overlap.
   - *Contradiction*: If a server issues an emergency grid control event (e.g. load shedding) that overlaps with an active event and starts in 5 minutes, a client polling on a 15-minute interval will miss the start of the emergency event, continuing to run the lower-priority event. This latency violates the real-time reliability expectations of grid services.
2. **The Primacy Self-Selection Conflict (`REQ-660` vs `REQ-613`/`656`)**:
   - `REQ-656` mandates that servers define their own primacy, and `REQ-660` recommends they "self-select" it.
   - *Conflict*: If multiple independent aggregators or utilities communicate with the same client device (e.g., a smart solar inverter participating in a local VPP and utility program) and both self-select primacy as `0` (highest), the client is forced to resolve the overlap based on `creationTime` (`REQ-613`). This makes grid control order non-deterministic and dependent on which server posted their event last, rather than operational grid requirements.

#### Step 4: Implementation Blueprint (For EGoT Engineering Team)
- [ ] **Enforce SSE Subscriptions for Real-Time Events (Bypass REQ-578)**:
  - In the EGoT client emulator, do not rely on polling to fetch events. Establish a persistent Server-Sent Events (SSE) connection to the `DERControlList` to receive and process control adjustments instantly (<1s).
- [ ] **Stateful Event Scheduler & Duration Truncation (`REQ-597`/`598`)**:
  - Implement a stateful queue of active and scheduled events.
  - Upon receiving an overlapping event, calculate the start/end times and modify duration settings:
    - If `New_Event.primacy == Old_Event.primacy` and `New_Event.creationTime > Old_Event.creationTime`:
      - Cut short the duration of the old event (`REQ-597`).
      - Queue the remaining segment of the old event to resume execution once the new event expires, if the duration is still valid (`REQ-598`).
- [ ] **Sanitize Primacy Configuration at the EGoT ESI Gateway**:
  - Override declared server primacy values (`REQ-660` bypass) at the API gateway level based on local utility regulations (e.g., Local Utility (Primacy 0) > Aggregator (Primacy 1) > Customer (Primacy 2)).
- [ ] **Enforce Clock Synchronization (Clock Drift Mitigation)**:
  - Enforce clock sync via NTP or the IEEE 2030.5 Time resource. If a client device's clock drifts by more than $\pm 2$ seconds from the server time, reject event schedules to prevent overlapping sequence failures.
