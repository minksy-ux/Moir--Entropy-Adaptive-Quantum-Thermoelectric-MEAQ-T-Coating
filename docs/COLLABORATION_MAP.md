# MEAQ-T Coating: Collaboration Expertise Map

**Status**: Skill requirements, facility access plan, and team composition  
**Last Updated**: 2026-07-15  
**Scope**: Prototype Phase (Year 1) through Production (Year 2+)

---

## Executive Summary: Critical Expertise Gaps

| Expertise Area | Internal Capacity | Gap | Priority | Partner Type |
|---|---|---|---|---|
| **High-entropy ceramics** | Partial (materials background) | Need HEA sintering expert | HIGH | Academic (materials dept) |
| **2D materials & transfer** | Minimal | Mechanical transfer highly specialized | CRITICAL | External fab or 2D expertise group |
| **DFT & simulation** | Basic (scripts exist) | Full pipeline optimization needed | HIGH | Theory collaborator or HPC center |
| **Magnetic characterization** (SQUID, Kerr) | No equipment | Requires facility access | HIGH | National lab or university facility |
| **Thermoelectric measurement** | Possible (outsource likely) | ZEM apparatus cost-prohibitive | MEDIUM | Commercial lab or facility access |
| **Thermal cycling & durability** | Moderate | Environmental chamber, ultrasonic | MEDIUM | Coating/materials testing center |
| **Product design & scale-up** | Minimal | Manufacturing optimization needed | MEDIUM | Industry partner or process engineer |

---

## Skill Matrix & Staffing Plan

### Core Team (In-House, Year 1)

| Role | Title | FTE | Key Skills | Hiring Timeline |
|---|---|---|---|---|
| **Project Lead** | Senior Researcher / PI | 0.5 | Materials science, project mgmt, writing | Month 0 (existing) |
| **HEA & Synthesis** | PhD Student / Postdoc | 1.0 | Ceramics, sintering, powder processing, materials characterization | Month 0 |
| **Computational** | PhD / Postdoc | 1.0 | DFT, Boltzmann transport, Python, VASP/QE | Month 1 |
| **2D Materials & Integration** | PhD Student | 1.0 | Micromechanics, 2D material transfer, microscopy | Month 1 |
| **Magnetic & Device Testing** | Graduate Research Assistant | 0.5 | Electronics, PPMS operation, data analysis | Month 2 |
| **Lab Technician** | Technician / Undergrad | 1.0 | Coating deposition, sample prep, safety | Month 0 |
| **Total Core Team** | | **4.5 FTE** | | **Months 0–2** |

### External Collaborators (Year 1)

| Partner | Role / Contribution | Time Commitment | Facility / Resource | Timeline |
|---|---|---|---|---|
| **Academic – Materials Dept** | HEA sintering optimization, phase analysis | 0.3 FTE (Prof) + 1 PhD student access | High-temp furnace, XRD, SEM | Months 1–8 |
| **Academic – Physics Dept** | SQUID magnetometry, Kerr microscopy | 0.2 FTE (Prof) + access | SQUID facility, Kerr optical setup | Months 3–10 |
| **National Lab (NIST / ORNL)** | Neutron diffraction, DFT computing (HPC) | 0.1 FTE (scientist) + computing time | Spallation source or HPC clusters (SUMMIT, Frontier) | Months 2–12 |
| **2D Materials Company** (Graphene Council, Grolltex) | MoTe₂/WSe₂ flake supply, CVD sourcing | Sales/support FTE (0.1) | Commercial 2D materials | Months 1–12 |
| **Thermal Characterization Lab** | Laser flash (thermal conductivity), ZEM (Seebeck) | 0.1 FTE access | Commercial instruments | Months 4–8 |
| **Industrial Partner** (Optional) | Design consultation, scale-up pathway | 0.2 FTE (engineer) | Meetings, process optimization | Months 6–12 |

---

## Facility Requirements & Access Plan

### On-Site Laboratory (Primary, Months 1–12)

**Estimated Space & Equipment Needs:**

| Equipment / Facility | Cost (Purchase or Annual Access) | Lead Time | Shared? |
|---|---|---|---|
| **Sample preparation area** | - | Existing | Yes (shared dept lab) |
| **High-temp furnace** (1600°C capable) | $30k–80k or $3k–5k/yr access | 2–4 weeks | **Partner furnace (negotiate access)** |
| **Spin coater / dip coater** | $5k–15k or borrow | 1 week | Can DIY or borrow |
| **Ball mill** (zirconia media) | $2k–8k | 2 weeks | Shared with department |
| **SEM cross-section station** | $1–3M (expect institutional) | Existing | Shared (pay per hour: $50–100/h) |
| **XRD diffractometer** | $500k–2M (expect institutional) | Existing | Shared ($80–150/sample) |
| **Raman spectrometer** | $200k–500k (expect institutional) | Existing | Shared ($100–200/sample) |
| **Optical microscope** (with heating stage) | $10k–30k (can acquire) | 1–2 weeks | Dedicated (research group) |
| **Adhesion testing rig** (pull-off apparatus) | $10k–20k or $200/sample outsource | 2 weeks or outsource | Outsource likely |

### Off-Site / Partner Facilities (Specialized)

| Facility / Measurement | Partner / Location | Timeline | Cost | FTE Required |
|---|---|---|---|---|
| **SQUID magnetometry** | University physics dept MPMS facility | Month 3+ | $100–200/sample | 0.1 FTE (student access) |
| **Kerr microscopy** (magnetic domains) | Research institute or university | Month 3+ | $2000–5000/run (facility fee) | 0.2 FTE (training) |
| **Laser flash (thermal conductivity)** | University materials lab or commercial | Month 4–5 | $300–500/sample | 0.1 FTE (sample prep) |
| **ZEM-3 (Seebeck/conductivity)** | Commercial lab (e.g., RMI, Linseis partner) | Month 4–5 | $1000–1500/sample | 0.1 FTE (sample delivery) |
| **TEM (cross-section / domains)** | University microscopy center | Month 5–8 | $500–1000/sample | 0.2 FTE (sample prep) |
| **Ion beam irradiation** (optional, Phase 2) | National lab (LANL, ORNL) | Month 10+ | $5000–15,000/day (facility time) | 0.3 FTE (planning/execution) |
| **Neutron diffraction** (optional) | Spallation source (SNS @ ORNL) | Month 8–12 | $5000–20,000/beamtime | 0.2 FTE (experiment planning) |

### Computing Infrastructure

| Resource | Requirement | Annual Cost | Availability |
|---|---|---|---|
| **Local workstations** | 2–3 Linux/GPU nodes for VASP, OOMMF | $5k–10k/ea (setup) | Buy or lease |
| **HPC cluster access** | XSEDE/NERSC allocation (free for academic) | $0 (merit review) | Allocate 100k CPU-hours/year |
| **COMSOL license** | University site license | $0–5k/yr (institutional negotiation) | Institutional or commercial |
| **Quantum ESPRESSO** | Free (open-source) | $0 | Installation on local clusters |
| **Software environment** | Python, MATLAB | ~$1k/yr (institutional) | Campus license or free alternatives |

---

## Collaboration & Partnership Strategy

### Phase 1 (Months 1–4): Foundation Building

**Objective**: Establish supplier relationships, negotiate facility access, define collaboration MOUs

**Actions**:
1. **Contact HEA expert** (Academic materials lab)
   - Propose co-authored paper on oxide HEA synthesis
   - Negotiate access to high-temp sintering equipment (~2–4 h/month)
   - MOU: Data sharing, co-authorship rights

2. **Engage 2D materials supplier** (Graphene Council or Grolltex)
   - Request sample pricing for bulk order (100 flakes MoTe₂, 100 flakes WSe₂)
   - Negotiate pilot pricing (likely 20–30% discount vs. list)
   - MOU: Feedback on quality, beta testing for new products

3. **Reserve SQUID facility time** (University physics)
   - Contact facility manager, schedule 2–4 measurement days in Month 3
   - Budget: ~$200/sample × 20 samples = $4,000
   - MOU: Student training, publication acknowledgment

4. **Submit HPC allocation request** (XSEDE/NERSC or PACS)
   - Request 50,000 CPU-hours for Year 1 DFT work
   - Justify with preliminary results and publications plan
   - Typical approval: 8-week turnaround

### Phase 2 (Months 5–10): Active Collaboration & Scale-Up

**Objective**: Execute joint research projects, optimize processes, build industry relationships

**Actions**:
1. **Joint paper** (HEA oxide synthesis)
   - Co-author with academic partner, target: *J. Mater. Res.* or *Acta Materialia*
   - Timeline: Submission Month 6, publication Month 9

2. **2D transfer workshop** (Industry or academic partner)
   - Invite external expert to 2–3 day hands-on training
   - Budget: ~$5,000–10,000 (expert travel, honorarium)
   - Outcome: Improved transfer yield, documented protocols

3. **Characterization campaign** (Multi-facility)
   - Systematically characterize 10–15 prototypes across SQUID, Kerr, ZEM
   - Coordinate samples (prioritize, batch shipping)
   - Monthly data compilation & analysis meetings

4. **Industry engagement** (Optional)
   - Approach aerospace/thermal management companies with preliminary data
   - Explore licensing/partnership interest
   - Budget for 2–3 industry meetings (travel): ~$5,000–10,000

### Phase 3 (Months 11–18): Production Pathway

**Objective**: Transition from research to development, establish manufacturing partners

**Actions**:
1. **Manufacturing partner negotiation**
   - Evaluate 2–3 coating/materials companies for scale-up capability
   - Technical meetings with engineering teams
   - Explore joint development agreements (JDA) or licensing

2. **Supply chain stabilization**
   - Lock in long-term pricing for HEA oxides, 2D materials, precursors
   - Volume contracts (~100 kg/yr HEA powders by Month 12)
   - Backup suppliers identified for critical materials

3. **IP strategy**
   - File provisional patents on key processes (Month 10–12)
   - Budget: ~$3,000–5,000 per patent application
   - Coordinate with university tech transfer office

---

## Budget Summary: Collaboration & Facility Costs

### Year 1 Collaboration Budget

| Category | Item | Cost |
|---|---|---|
| **Facility Access** | SQUID magnetic measurement | $4,000 |
| | Kerr microscopy | $5,000 |
| | Laser flash (thermal conductivity) | $2,000 |
| | ZEM (Seebeck/conductivity) | $5,000 |
| | SEM/XRD/Raman (shared hourly) | $3,000 |
| **External Materials & Services** | 2D materials supply (MoTe₂, WSe₂ flakes) | $8,000 |
| | HEA oxide powder orders | $2,000 |
| | Thermal cycling testing | $3,000 |
| **Partnerships & Agreements** | Travel (facility visits, meetings) | $3,000 |
| | Expert consultation (2–3 days) | $5,000 |
| **Computing & Software** | HPC allocation (included in research grant) | $0 |
| | COMSOL license negotiation | $0–2,000 |
| **Intellectual Property** | Patent application (provisional) | $3,000–5,000 |
| **TOTAL Year 1 Collaboration** | | **$42,000–49,000** |

### Estimated Budget Allocation (Total Project Budget)

| Category | Year 1 | Year 2 | Year 3+ |
|---|---|---|---|
| **Personnel (salaries & benefits)** | $300k | $350k | $400k+ |
| **Materials & Supplies** | $50k | $80k | $150k+ |
| **Facilities & Equipment** | $60k | $40k | $30k |
| **Collaboration & Partnerships** | $45k | $60k | $100k |
| **Travel & Conferences** | $10k | $15k | $20k |
| **Publication & IP** | $5k | $10k | $15k |
| **Contingency (10%)** | $47k | $55k | $71k |
| **TOTAL** | **$517k** | **$610k** | **$786k+** |

**Funding sources** (multi-source strategy):
- Federal research grants (NSF CAREER, DOE, ARPA-E): $200–300k/yr
- Industry partnerships: $50–100k/yr (if applicable)
- University matching / startup funds: $100–200k/yr (Year 1)
- Equipment grants (NSF MRI): One-time $100k+ for major instrument

---

## Expertise Map: Detailed Role Descriptions

### 1. HEA & Ceramic Processing Expert

**Institution**: Materials Science Department (Academic or National Lab)

**Expertise Required**:
- High-temperature sintering (>1400°C)
- High-entropy ceramics phase prediction (CALPHAD)
- XRD phase identification
- Microstructure characterization (SEM, TEM)

**Collaboration Model**:
- Monthly meetings (1 hour)
- Access to furnace (~100 h/year, shared time)
- Co-author on oxide HEA synthesis paper

**Deliverables**:
- Optimized sintering protocol by Month 4
- Phase stability assessment of (Hf,Zr,Ta,Nb,Ti)O
- Publication (1 joint paper, Month 9)

**Partner Examples**:
- University of Colorado (materials engineering)
- Penn State (ceramics & phase diagrams)
- National Institute of Standards (NIST, ceramic research)

---

### 2. 2D Materials & Transfer Specialist

**Institution**: Materials Science Group or 2D Technology Company

**Expertise Required**:
- Mechanical transfer of 2D materials (thermal release tape)
- Raman spectroscopy for quality assessment
- AFM for surface characterization
- CVD growth or flake sourcing

**Collaboration Model**:
- 2–3 day workshop (Month 4)
- Supply of MoTe₂ & WSe₂ flakes (100+ samples/year)
- Optimization feedback on transfer protocols

**Deliverables**:
- Transfer yield improvement (50% → 70%+) by Month 6
- Documented transfer SOP (Standard Operating Procedure)
- Publication (joint characterization paper, Month 10)

**Partner Examples**:
- Graphene Council (flakes supply)
- University of Washington (2D materials, Kibsgaard lab)
- MIT (Moire & transport, MIT.nano facility)

---

### 3. Computational & DFT Specialist

**Institution**: Theory Group (Physics or Chemistry Dept) or HPC Center

**Expertise Required**:
- DFT (VASP, Quantum ESPRESSO)
- Boltzmann transport (BoltzTraP2)
- Wannier90 interpolation
- Band structure analysis

**Collaboration Model**:
- Monthly video meetings (1.5 hours)
- Shared HPC allocation (provided by academic)
- Co-development of transport coefficient pipeline
- Review draft papers (1–2 papers/year)

**Deliverables**:
- Optimized HEA composition from DFT by Month 3
- Moire band structure prediction by Month 5
- Transport coefficient predictions vs. experiment (correlation analysis)

**Partner Examples**:
- University of Pennsylvania (materials theory)
- Lawrence Berkeley National Lab (materials simulation)
- University of California Santa Barbara (UCSB, condensed matter theory)

---

### 4. Magnetic Characterization Specialist

**Institution**: Physics Department (Experimental Magnetism Group)

**Expertise Required**:
- SQUID magnetometry (Quantum Design MPMS)
- Kerr microscopy (magnetization imaging)
- Domain structure analysis
- Magnetic phase transitions

**Collaboration Model**:
- 4–6 measurement sessions/year
- Student training in sample mounting & measurement
- Data interpretation meetings (monthly)
- Acknowledgment in publications

**Deliverables**:
- Saturation magnetization & anisotropy for baseline HEA
- Domain structure images confirming bistability
- Coercivity & switching field measurements

**Partner Examples**:
- NIST (magnetic measurements group)
- University of Minnesota (magnetic materials)
- University of California Santa Cruz (UCSC, magnetism)

---

### 5. Thermal Transport Measurement Facility

**Institution**: Commercial Lab or University Materials Lab

**Expertise Required**:
- Laser flash analysis (LFA)
- Thermal diffusivity measurement
- ZEM Seebeck/conductivity
- Temperature-dependent measurements

**Collaboration Model**:
- Commercial outsourcing (sample-by-sample fee)
- Or university facility access agreement
- Monthly progress meetings

**Cost**: $300–500/sample (commercial) or negotiate institutional rate

**Deliverables**:
- Thermal conductivity vs. temperature (2–3 samples minimum)
- Seebeck coefficient vs. temperature & doping
- Power factor mapping

**Partner Examples**:
- RMI (commercial, https://www.rmi-llc.com)
- Linseis (instrument manufacturer, USA distributor)
- University of Michigan (thermal characterization facility)

---

## Timeline Visualization

```
Month:   1   2   3   4   5   6   7   8   9  10  11  12
Synth:   |---HEA--|---2D---|---Int---|
         Furnace access          Transfer workshop
         
DFT:     |-----Comp-Model---|---Optimization---|
         HPC allocation           Band structure
         
Mag:     |--------Prep-----|-SQUID-|-Kerr-|
         Sample design        Meas.  Domains
         
Char:    |--Setup--|---Thermal-K---|---ZEM---|
         Lab access   LFA           Seebeck
         
Collab:  |Partner meetings-----|------Industry---------|
         Industry scoping     Scale-up exploration
         
Results: |---Phase-1--|---Phase-2---|---Phase-3--|
         Prototype   Optimization  Production-ready
```

---

## Risk Mitigation: Single-Point Failures

| Single Point of Failure | Impact | Mitigation |
|---|---|---|
| **2D material supply disruption** | Can't complete moire layer | Identify 2–3 suppliers; place pilot orders with each |
| **Furnace downtime** | HEA sintering blocked | Negotiate access to 2 institutions; prioritize sample queue |
| **Facility expert leaves** | Knowledge loss, collaboration interrupted | Document SOPs, train backup student |
| **Delayed HPC allocation** | DFT work stalls | Start with local computing; use commercial cloud (AWS, Google Cloud) as bridge |
| **Magnetic facility closure** | Can't characterize magnetism | Bring in temporary equipment or pivot to simulation-only for Prototype 1 |

**Mitigation Strategy**: Maintain 2–3 collaborative backup relationships in each critical area; never depend on single external partner.

---

## References & Related Documents

- [Risk Assessment](RISK_ASSESSMENT.md): Feasibility gates & resource requirements
- [Characterization Plan](CHARACTERIZATION_PLAN.md): Specific facility needs by test
- [Computational Roadmap](COMPUTATIONAL_ROADMAP.md): DFT collaboration details
- [Economics](ECONOMICS.md): Facility costs embedded in production budget
