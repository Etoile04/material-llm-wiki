# Key Findings & Design Implications – 2018 Millett: Bimodal Porosity in Metallic Fuels

## Physical Mechanism: Why Bimodal Porosity Resists Densification

1. **Small pores dissolve quickly**: High surface curvature drives rapid vacancy release into the solid matrix
2. **Large pores act as vacancy sinks**: Lower curvature → absorb vacancies from dissolving small pores; some large pores temporarily **grow** at early times
3. **Interrupted diffusion pathways**: Large pores break long-range vacancy transport routes to the outer surface, reducing the driving concentration gradient
4. **Intermediate pore nucleation** (ξ = 40, 60): Vacancy-dense regions nucleate new intermediate pores, further consuming vacancies that would otherwise cause shrinkage

## Densification Results

| Configuration | Densification Rate | Long-term Behavior |
|---------------|--------------------|--------------------|
| ξ = 100 (monomodal small) | **Very rapid** | Complete porosity elimination |
| ξ = 0 (monomodal large) | Slow, continued | Slow steady shrinkage |
| ξ = 40, 60 (bimodal) | Intermediate early → **similar to ξ = 0** | Resembles large-pore-only behavior |
| **ξ = 60 at TD = 96%** | **Slowest of all** | Even slower than ξ = 0 |

- Early vacancy concentration spike: ξ = 100 reaches $c_v \approx 0.040$; bimodal configurations show reduced spikes
- System size independence confirmed across D = 512, 1024, 2048 reduced units

## Key Findings

1. **Bimodal porosity resists densification** significantly more than monomodal small-pore distributions at the same overall porosity — computationally confirms Maier et al. (1988) UO₂ experiments
2. **Large pores act as vacancy sinks**: vacancies from small pores flow into large pores rather than out to the surface
3. **Intermediate pore nucleation** in bimodal configurations provides additional densification resistance mechanism
4. **System size independence**: bimodal advantage not a computational artifact
5. **Optimal: ξ = 60 at TD = 96%** — best densification resistance, even outperforms monomodal large-pore case
6. After small pores dissolve, long-term behavior determined entirely by large pore evolution
7. **Design implication**: Deliberate large pore introduction via "burnable" pore formers before pressing provides densification-resistant fuel architecture

## Experimental Work (Texas A&M)

- Hydride-dehydride method: U powder (1–10 µm flakes)
- Rotating electrode atomization: U, U-10Zr microspheres (75–150 µm)
- Sintering conditions: U-10%Zr at 900°C for 10–12 h
- Copper surrogates used for cold-process validation

## MEAM/MD Results (Georgia Tech)

- Computed self-diffusion coefficients in pure U and U-Zr for single crystals, grain boundaries, free surfaces
- Calculated grain boundary and free surface interfacial energies for U-Zr alloys

## Relevance to Fuel Swelling

| Connection | Detail |
|------------|--------|
| Gas collection volume | Pre-existing large pores can absorb fission gas, reducing irradiation swelling |
| Densification resistance | Bimodal pores survive early in-pile service, maintaining gas collection capacity |
| Swelling accommodation | Porosity provides volumetric buffer to accommodate swelling without cladding stress |
| Fabrication route | Pore former + powder metallurgy route enables controlled bimodal porosity |

## Open Questions (from authors)

1. Grain boundaries and crystalline defects interacting with vacancy fields
2. Fuel-cladding interface effects
3. In-situ pore creation from in-pile irradiation
4. Extension to 3D simulations
5. Experimental validation with actual U and U-10Zr bimodal compacts
6. Optimization of pore size ratios for specific fuel designs

## See Also

- [[wiki/summaries/2018_Millett_ComputationalExperimentalPorosityMetallic|Index: Millett 2018]]
- [[wiki/summaries/2018_Millett_ComputationalExperimentalPorosityMetallic/KeyEquations|Key Equations]]
- [[wiki/entities/CavitationalVoid|CavitationalVoid]] — vacancy-driven cavitation; related porosity evolution mechanism
- [[wiki/entities/PhaseFieldModeling|PhaseFieldModeling]] — Cahn-Hilliard methodology
- [[wiki/summaries/2009_Rokkam_PhaseFieldVoidNucleationGrowth|Rokkam 2009 PF Void]] — void nucleation/growth phase-field model
- [[wiki/summaries/2008_Surh_VoidNucleationGrowthCoalescence|Surh 2008 Void]] — void nucleation, growth and coalescence
- [[wiki/summaries/1990_Hofman_SwellingBehaviorUPuZr|Hofman 1990]] — metallic fuel swelling behavior context (U-Pu-Zr)
