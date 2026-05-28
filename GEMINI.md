# Project Context: EGoT PhD Research Workspace

This workspace contains the PhD research and implementation of the **Energy Grid of Things (EGoT)**, focused on high-performance IEEE 2030.5 (Smart Energy Profile 2.0) infrastructure.

## 1. Project Structure

The repository is divided into two main components:

- **`egot/`**: A comprehensive Go implementation of the IEEE 2030.5 / SEP 2 server and device emulation platform.
- **`dissertation/`**: LaTeX source for the PhD dissertation, documenting the theoretical background, methods, and results.

---

## 2. EGoT Platform (`egot/`)

### Overview
`egot` is a microservices-based implementation of the IEEE 2030.5 standard. It hosts a fleet of services, each responsible for a distinct SEP 2 function set (e.g., Metering, Demand Response, DER Management).

### Architecture
- **Microservices:** Each service runs on a dedicated port. Key services:
  - `DCAP` (:8012): Root discovery service.
  - `EDevice` (:8015): End device management.
  - `DER` (:8026): DER status and settings (extracted from EDevice).
  - `FlowReservation` (:8027): Grid reservation requests (extracted from EDevice).
  - `MUP` (:8017): Mirror Usage Point for telemetry.
  - `DERP` (:8013): DER Programs and Controls.
- **Nginx API Gateway:** Centralized routing and load balancing via `./bin/nginx-config-gen`.
- **mTLS Security:** All communication is secured via mutual TLS.

### Key Commands (Run from `egot/`)
- **Building:**
  - `make build-all`: Build all microservices, tools, and emulators.
- **Tools:**
  - `./bin/emulator-der`: Advanced DER emulator (Load, ESS, PV profiles).
  - `./bin/data-export`: Export telemetry from `gob` store to CSV for OpenDSS.
  - `python3 scripts/grid_services_sim.py`: OpenDSS simulation of grid services.
- **WADL-Driven:**
  - `./bin/wadl-extract`: Pull specific resource subsets from WADL files.
  - `./bin/scaffold-gen`: Generate Go microservice boilerplate.

### Development Conventions
- **Routing:** Centralized in `internal/routes/routes.go`.
- **Naming:** Handlers use `<HTTP_METHOD><ResourceName>` (e.g., `GETUsagePointList`).
- **Path Parameters:** Consistently use `{id1}`, `{id2}`, etc.
- **TLS:** Use `tlsutil.NewServerConfig("./ssl")` for consistent mTLS setup.

---

## 3. Dissertation (`dissertation/`)

### Overview
The `dissertation` directory contains the LaTeX project for the PhD thesis. It covers:
- **Background:** Energy Service Interfaces (ESI), standards, and grid services.
- **Methods:** Implementation details of the EGoT server and emulators.
- **Results:** Performance analysis and grid impact studies.

### Key Files
- `main.tex`: The root LaTeX file.
- `FrontMatter/`: Abstract, acknowledgements, title.
- `MainMatter/`: Core chapters (introduction, background, methods, etc.).
- `BackMatter/`: Appendix and bibliography.
- `Figures/`: Architectural diagrams and data plots.

---

## 4. Shared Resources
- **`sep/`**: Go types auto-generated from the SEP 2 XSD.
- **`wadl/`**: WADL definitions for all IEEE 2030.5 resources.
- **`ssl/`**: Local directory for mTLS certificates (do not commit secrets).
