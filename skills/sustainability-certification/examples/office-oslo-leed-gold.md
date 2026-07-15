# Worked Example: Office in Oslo, LEED Gold

## Project brief

A 22,000 sqm office building in Oslo, Norway. The owner wants LEED Gold certification (BD+C v4.1, New Construction). The building has 6 above-grade stories.

### Room schedule

| Room type | Count | Area each (sqm) | Occupancy | Regularly occupied |
|-----------|-------|------------------|-----------|--------------------|
| Open office | 8 | 200 | 30 | Yes |
| Private office | 24 | 12 | 1 | Yes |
| Meeting room (small) | 16 | 15 | 6 | Yes |
| Meeting room (large) | 4 | 40 | 16 | Yes |
| Reception/lobby | 1 | 150 | 5 | Yes |
| Break room/kitchen | 4 | 30 | 10 | Yes |
| Toilet | 24 | 8 | 1 | No |
| Corridor | - | - | - | No |
| Server room | 1 | 25 | 0 | No |
| Storage | 6 | 15 | 0 | No |

### Constraints

- Budget sensitivity: Medium
- Owner priorities: Energy performance, occupant wellbeing, daylight
- Site: Urban, close to public transit

---

## Expected agent output

### Prerequisites (mandatory)

| Prerequisite | Requirement | Standard | Status |
|---|---|---|---|
| EAp2: Minimum Energy Performance | >= 5% improvement over ASHRAE 90.1-2010 baseline | ASHRAE 90.1-2010 | Requires energy model |
| WEp2: Indoor Water Use Reduction | >= 20% reduction from baseline fixture rates | EPA WaterSense | Design to fixture schedule |
| IEQp1: Minimum IAQ Performance | Outdoor air rates per ASHRAE 62.1-2010 Sec 4-7 | ASHRAE 62.1-2010 | Requires HVAC design |
| EAp1: Fundamental Commissioning | Commissioning authority, OPR, BOD, Cx plan | - | Process requirement |

All prerequisites must be met regardless of target level. Failing any one means no certification at all.

### Room-level requirements

**OPEN OFFICES (8 rooms, ~200 sqm each)**

Daylight (IEQ Credit: Daylight, up to 3 points):
- sDA300/50% >= 55% of regularly occupied floor area for 2 points, >= 75% for 3 points [IES LM-83-12]
- ASE1000/250h must not exceed 10% of floor area [IES LM-83-12]
- Confidence: Medium (requires daylight simulation)

Thermal Comfort (IEQ Credit: Thermal Comfort, 1 point):
- Comply with ASHRAE 55-2010
- PMV between -0.5 and +0.5, PPD < 10% for all regularly occupied spaces
- Individual thermal comfort controls for >= 50% of individual occupant spaces
- Confidence: Medium (depends on HVAC design)

Ventilation (IEQ Prerequisite: Minimum IAQ Performance):
- Outdoor air rates per ASHRAE 62.1-2010, Ventilation Rate Procedure (Section 6.2)
- For offices: 5 cfm/person outdoor air rate + 0.06 cfm/sqft
- Monitor outdoor airflow for mechanically ventilated spaces
- MANDATORY PREREQUISITE

Interior Lighting (IEQ Credit: Interior Lighting, 2 points):
- Personal lighting controls for >= 90% of individual occupant spaces
- Multi-zone controls for all shared multi-occupant spaces
- Confidence: High

Quality Views (IEQ Credit: Quality Views, 1 point):
- 75% of regularly occupied floor area has direct line of sight to vision glazing
- Confidence: High (design geometry determines this)

Low-Emitting Materials (IEQ Credit: Low-Emitting Materials, up to 3 points):
- Adhesives/sealants: VOC limits per SCAQMD Rule 1168
- Paints/coatings: VOC limits per GS-11
- Flooring: FloorScore certified or equivalent
- Composite wood: no added urea-formaldehyde
- Confidence: High (material specification)

**PRIVATE OFFICES (24 rooms, ~12 sqm each)**

Same requirements as open offices for daylight, thermal comfort, ventilation, lighting, views, and materials. Additionally:
- Individual thermal comfort controls required for each private office

**MEETING ROOMS (20 rooms total)**

Daylight: same sDA/ASE thresholds apply (regularly occupied spaces)
Ventilation: ASHRAE 62.1-2010 rates (5 cfm/person + 0.06 cfm/sqft for conference rooms)
Acoustic: meet ASHRAE 2011 Handbook background noise criteria for conference/meeting rooms (RC 25-30 or NC 25-30)
Views: 75% of floor area with direct line of sight to glazing

**TOILETS (24 rooms)**

Water Efficiency (WE Prerequisite + Credit):
- Baseline: 1.28 gpf (4.8 Lpf) for toilets
- For 20% reduction (prerequisite): <= 1.02 gpf (3.9 Lpf) or use dual-flush 1.28/0.8 gpf
- For additional points: further reduction toward 50% (WEc2)
- Lavatory faucets baseline: 0.5 gpm (1.9 Lpm); reduce further for credits

### Credit strategy for Gold (60+ points)

| Category | Strategy | Estimated points |
|---|---|---|
| Energy (EA) | Target 20-24% improvement → 8-10 points | 8-10 |
| Water (WE) | 35-40% indoor reduction → 3-4 points | 3-4 |
| IEQ | Daylight + thermal + lighting + views + acoustics + materials | 8-10 |
| Location (LT) | Urban Oslo, good transit → 8-10 points | 8-10 |
| Sustainable Sites (SS) | Heat island, rainwater | 3-4 |
| Materials (MR) | EPDs, LCA | 3-5 |
| Innovation | 2-3 innovation credits | 2-3 |
| Regional Priority | Check USGBC for Norway | 1-2 |
| **Total estimate** | | **36-48** |

With prerequisites providing the foundation, this puts Gold (60 points) within reach but requires strong performance across EA, LT, and IEQ. The owner's priorities (energy, wellbeing, daylight) align well with the highest-value credits.

### Design trade-offs to consider now

1. **Daylight vs. thermal performance**: Maximizing glazing for IEQ daylight credits (sDA 55-75%) may increase cooling loads, affecting EA energy performance. Consider high-performance glazing (low SHGC) or external shading.

2. **Energy target**: 20-24% improvement is achievable for a well-designed Oslo office but requires early commitment to envelope quality, efficient HVAC, and LED lighting.

3. **Water**: Oslo has no water stress, but the points are relatively easy. Specify low-flow fixtures early.

### What to simulate

| Simulation | Credit | Threshold | Tool |
|---|---|---|---|
| Whole-building energy model | EAc2 | >= 20% improvement over ASHRAE 90.1-2010 | EnergyPlus, IES VE, eQUEST |
| Daylight simulation | IEQc7 | sDA300/50% >= 55%, ASE1000/250h <= 10% | Radiance, DIVA, ClimateStudio |
| Thermal comfort analysis | IEQc5 | PMV -0.5 to +0.5 | IES VE, DesignBuilder |
