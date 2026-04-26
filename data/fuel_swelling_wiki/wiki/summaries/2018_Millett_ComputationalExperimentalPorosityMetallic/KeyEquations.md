# Key Equations – 2018 Millett: Computational & Experimental Studies of Bimodal Porosity in Metallic Fuels

## Cahn-Hilliard Phase-Field Model

The densification process is governed by:

$$\frac{\partial \phi}{\partial t} = \nabla \cdot M \nabla \frac{\delta F}{\delta \phi}$$

where:
- $\phi$: order parameter representing local fuel density ($\phi = c_U - c_V$, with $c_U + c_V = 1$)
- $\phi = +1$: solid fuel; $\phi = -1$: pore
- $M$: mobility parameter (= 16 in reduced units)

## Free Energy Functional

$$F(\phi) = \int_V \left[ \frac{\phi^4}{4} - \frac{\phi^2}{2} + \frac{\kappa}{2} |\nabla \phi|^2 \right] dV$$

- Double-well terms $(\phi^4/4 - \phi^2/2)$: maintain two-phase structure
- Gradient term $(\kappa/2|\nabla\phi|^2)$: penalizes interfaces (controls interface width)
- $\kappa = 16$ (reduced units)

## Bimodal Porosity Parameter

$$\xi = \frac{A_S}{A_S + A_L} \times 100$$

where $A_S$ = total area of small pores, $A_L$ = total area of large pores.

- $\xi = 100$: monomodal small pores only
- $\xi = 0$: monomodal large pores only
- $\xi = 20, 40, 60, 80$: bimodal distributions

**Pore sizes**: small = 5h (h = 0.27 reduced units), large = 50h (diameter ratio 10:1).

## Simulation Parameters

| Parameter | Value |
|-----------|-------|
| Grid | 4096 × 4096 nodes |
| Grid spacing h | 0.27 reduced length units |
| Fuel body diameter | 1024 (base) reduced units |
| Time step Δt | 1.0 reduced time units |
| Simulation duration | 50,000 time steps |
| Statistical sampling | 5 independent runs per configuration |

## Initial Porosity (Theoretical Density)

| TD (%) | Overall Porosity (%) |
|--------|---------------------|
| 92 | 8 |
| 94 | 6 |
| 96 | 4 |

## See Also

- [[wiki/summaries/2018_Millett_ComputationalExperimentalPorosityMetallic|Index: Millett 2018]]
- [[wiki/summaries/2018_Millett_ComputationalExperimentalPorosityMetallic/FindingsDesign|Findings & Design Implications]]
- [[wiki/entities/PhaseFieldModeling|PhaseFieldModeling]] — Cahn-Hilliard model methodology
- [[wiki/entities/CavitationalVoid|CavitationalVoid]] — vacancy-driven void/pore evolution context
