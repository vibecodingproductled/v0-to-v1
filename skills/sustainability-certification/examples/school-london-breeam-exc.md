# Worked Example: Secondary School in London, BREEAM Excellent

## Project brief

A 6,500 sqm secondary school in London, UK. The local authority requires BREEAM Excellent (New Construction 2023). The building has 3 stories.

### Room schedule

| Room type | Count | Area each (sqm) | Occupancy | Regularly occupied |
|-----------|-------|------------------|-----------|--------------------|
| Classroom | 24 | 55 | 30 | Yes |
| Science lab | 6 | 75 | 30 | Yes |
| Art studio | 2 | 70 | 25 | Yes |
| Staff office | 4 | 20 | 4 | Yes |
| Head's office | 1 | 15 | 2 | Yes |
| Staff room | 1 | 40 | 15 | Yes |
| Assembly hall | 1 | 300 | 250 | Yes |
| Library | 1 | 120 | 40 | Yes |
| Dining hall | 1 | 200 | 150 | Yes |
| Kitchen | 1 | 60 | 5 | Yes |
| Toilet blocks | 8 | 25 | - | No |
| Corridor | - | - | - | No |
| Plant room | 1 | 40 | 0 | No |
| Storage | 10 | 10 | 0 | No |

### Constraints

- Budget sensitivity: High (public sector)
- Local authority mandates BREEAM Excellent
- Owner priorities: Daylight, acoustics, low running costs
- Site: Suburban, existing playing fields retained

---

## Expected agent output

### Minimum standards for Excellent

BREEAM Excellent requires a minimum overall weighted score of 70% AND meeting all minimum standards. Failing any minimum standard blocks Excellent even if the overall score is sufficient.

| Issue | Minimum for Excellent | Requirement |
|---|---|---|
| Hea 01: Visual comfort | 2 credits | Daylight factor, glare control, view out, lighting quality |
| Ene 01: Energy use | 4 credits | Energy Performance Ratio <= 0.6 |
| Wat 01: Water consumption | 1 credit | Reduce below baseline |
| Mat 01: Life cycle impacts | Exemplary LCA and embodied carbon reporting | LCA at design stage |

These are non-negotiable. Design must address them from the start.

### Room-level requirements

**CLASSROOMS (24 rooms, ~55 sqm each)**

Visual Comfort (Hea 01, 4 credits available, min 2 for Excellent):
- Average daylight factor >= 3.0% on working plane at 850mm [BS EN 17037]
- Daylight uniformity ratio >= 0.3 [BS EN 17037]
- View of sky from seated position (desk height) through vision glazing
- Artificial lighting: maintained illuminance >= 300 lux on desks [BS EN 12464-1]
- Unified Glare Rating (UGR) <= 19 for artificial lighting [BS EN 12464-1]
- Glare control: occupant-operated blinds or external shading on glazing receiving direct sun
- Confidence: High (thresholds are clear; daylight factor requires simulation to verify compliance)

Indoor Air Quality (Hea 02, 3 credits available):
- Fresh air rate >= 8 L/s per person [BS EN 16798-1, Category II]
- CO2 monitoring with set point < 1000 ppm above outdoor level
- Provision for purge ventilation: >= 4 air changes per hour
- No smoking within 10m of building entrances
- Confidence: High

Thermal Comfort (Hea 04, 2 credits available):
- PMV between -0.5 and +0.5 [BS EN ISO 7730]
- OR adaptive comfort model for naturally ventilated spaces [BS EN 15251]
- Requires thermal modeling at detailed design
- For schools: avoid overheating per BB101 (Teaching spaces: operative temperature should not exceed 28C for more than 120 occupied hours/year)
- Confidence: Medium (requires thermal simulation)

Acoustic Performance (Hea 05, 3 credits available):
- Background noise level: 30-35 dB LAeq,30min [BB93: Acoustic Design of Schools]
- Reverberation time: per BB93 Table 1 (classrooms: Tmf <= 0.6-0.8s depending on volume)
- Sound insulation between teaching spaces: DnT,w >= 45 dB [BB93]
- Sound insulation from corridors: DnT,w >= 40 dB [BB93]
- Confidence: High (thresholds clear, compliance requires acoustic design)

**SCIENCE LABS (6 rooms, ~75 sqm each)**

All classroom requirements apply, plus:
- Ventilation: may require higher air change rates for fume extraction (6-10 ACH typical for science labs) [BB101, CIBSE Guide A]
- Background noise: additional consideration for fume cupboard noise
- Confidence: Medium (depends on fume cupboard specification)

**ASSEMBLY HALL (1 room, 300 sqm)**

Acoustic Performance (Hea 05):
- Reverberation time: Tmf 0.8-1.2s for multi-purpose hall [BB93]
- Background noise: <= 35 dB LAeq,30min [BB93/BS 8233]
- Sound insulation from adjacent spaces: DnT,w >= 50 dB [BB93]
- Confidence: High

Daylight (Hea 01):
- Average daylight factor >= 2.0% [BS EN 17037, for non-teaching occupied spaces]
- View out requirements apply
- Confidence: Medium (large floor plate may make daylight factor challenging)

**STAFF OFFICES (4 rooms + head's office)**

Visual Comfort (Hea 01):
- Average daylight factor >= 2.0% on working plane [BS EN 17037]
- Uniformity ratio >= 0.3
- Maintained illuminance >= 500 lux for office tasks [BS EN 12464-1]
- UGR <= 19 [BS EN 12464-1]
- Confidence: High

Ventilation (Hea 02):
- Fresh air: 8 L/s per person [BS EN 16798-1, Category II]
- Confidence: High

**TOILETS (8 blocks)**

Water Consumption (Wat 01, 5 credits available, min 1 for Excellent):
- Baseline: WC 6/4 L dual flush, WHB taps 6 L/min
- For 1 credit: 12.5% reduction from baseline (e.g., WC 4/2.6 L, WHB taps 4 L/min)
- For further credits: progressive reductions toward 55% below baseline
- Showers (if provided): baseline 8 L/min, reduce for credits
- Confidence: High (fixture specification)

**KITCHEN / DINING (commercial kitchen + dining hall)**

Water: process water efficiency for commercial kitchen equipment
Energy: sub-metering of kitchen energy use (Ene 02)
Ventilation: kitchen extract per DW/172 (HVCA guide)
Note: commercial kitchens have specialist requirements. Consult kitchen equipment supplier for BREEAM compliance.

### Building-level requirements

Energy Performance (Ene 01, 15 credits, min 4 for Excellent):
- Energy Performance Ratio (EPR) <= 0.6 for 4 credits (minimum for Excellent)
- EPR <= 0.4 for 8 credits (recommended to hit 70% overall)
- Calculated using NCM (National Calculation Methodology) or SBEM
- Requires energy model
- Confidence: Low (requires energy model; significant design dependency)

Energy Monitoring (Ene 02, 2 credits):
- Sub-metering by end use: heating, cooling, lighting, small power, renewable generation
- Display of energy consumption in publicly accessible area
- Confidence: High (design specification)

Low Carbon Design (Ene 04, 3 credits):
- Passive design analysis at concept stage
- Free cooling feasibility assessment
- Low/zero carbon energy feasibility study
- Confidence: High (process requirement)

Surface Water Run-off (Pol 03, 5 credits):
- Attenuate surface water discharge to greenfield run-off rates (Qbar)
- Sustainable drainage systems (SuDS)
- For 1 in 100 year storm + climate change allowance
- Confidence: Medium (depends on site conditions)

Cyclist Facilities (Tra 03, 2 credits):
- Cycle storage: 1 space per 10 staff as minimum
- For students: per local authority requirements (London Plan: 1 per 8 students)
- Shower/changing facilities for staff: 1 shower per 10 cycle spaces
- Confidence: High

Responsible Construction (Man 03, 2 credits):
- Register with Considerate Constructors Scheme
- Achieve score >= 35/50
- Confidence: High (process/contract requirement)

### Credit strategy for Excellent (>= 70% weighted score)

| Category | Weight | Estimated % achieved | Weighted contribution |
|---|---|---|---|
| Management (12%) | 12 | 70% | 8.4 |
| Health & Wellbeing (15%) | 15 | 80% | 12.0 |
| Energy (19%) | 19 | 50% | 9.5 |
| Transport (8%) | 8 | 60% | 4.8 |
| Water (6%) | 6 | 70% | 4.2 |
| Materials (12.5%) | 12.5 | 50% | 6.3 |
| Waste (7.5%) | 7.5 | 60% | 4.5 |
| Land Use & Ecology (10%) | 10 | 50% | 5.0 |
| Pollution (10%) | 10 | 60% | 6.0 |
| Innovation | +up to 10% | | +3.0 |
| **Estimated total** | | | **63.7 + 3.0 = 66.7** |

This is tight for 70%. The school needs strong performance in Health & Wellbeing (daylight, acoustics are natural strengths for a well-designed school) and must secure at least 50% in Energy (requires good envelope and efficient systems). Budget sensitivity means Materials credits may be hard to maximize.

### Design trade-offs

1. **Daylight vs. acoustics**: Large windows for daylight (Hea 01) can compromise acoustic insulation (Hea 05) if not carefully detailed. Use high-performance acoustic glazing.

2. **Daylight vs. overheating**: Schools are particularly vulnerable to overheating (BB101 compliance). External shading is critical for south-facing classrooms.

3. **Energy vs. budget**: EPR 0.4 (8 credits) would significantly help the overall score but requires higher capital cost for efficient HVAC and better envelope. EPR 0.6 (4 credits) is the minimum for Excellent.

4. **Natural ventilation vs. IAQ**: Natural ventilation can earn Hea 02 credits and reduce energy, but must demonstrate adequate fresh air rates and overheating compliance.

### What to simulate

| Simulation | Issue | Threshold | Tool |
|---|---|---|---|
| Daylight factor | Hea 01 | >= 3.0% classrooms, >= 2.0% offices | Radiance, DIVA, Velux Daylight Visualizer |
| Energy model (SBEM/DSM) | Ene 01 | EPR <= 0.6 (min), ideally <= 0.4 | IES VE, DesignBuilder, SBEM |
| Overheating (BB101) | Hea 04 | < 120 hours above 28C | IES VE, TAS |
| Acoustic performance | Hea 05 | Background noise, Tmf, DnT,w per BB93 | Acoustic modeling |
