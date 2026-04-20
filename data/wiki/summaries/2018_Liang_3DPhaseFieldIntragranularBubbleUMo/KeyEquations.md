# Key Equations – 2018 Liang: 3D Phase-Field Simulations of Intragranular Gas Bubbles in U-Mo

## Total Free Energy (Eq. 1)

$$F(c_X, c_V, c_I, g, \varepsilon_{ij}) = \int \left[ f^\text{chem}(c_X, c_V, c_I, g, T) + \frac{\kappa_X}{2}|\nabla c_X|^2 + \frac{\kappa_V}{2}|\nabla c_V|^2 + \frac{\kappa_I}{2}|\nabla c_I|^2 + \frac{\kappa_g}{2}|\nabla g|^2 + f^\text{elas}(c_X, c_V, c_I, g, \varepsilon_{ij}) \right] dV$$

**Fields**: $c_X$ (Xe), $c_V$ (vacancy), $c_I$ (SIA), $g$ (bubble phase parameter, 0=matrix, 1=bubble)

## Chemical Free Energy (Eqs. 2–5)

Interpolation:
$$f^\text{chem} = h(g) f^b + [1 - h(g)] f^m + w\, g(g)$$

where $h(g) = g^3(6g^2 - 15g + 10)$, $\;g(g) = g^2(1-g)^2$

**Matrix free energy** (ideal solution):
$$f^m = E_X^f c_X + E_V^f c_V + E_I^f c_I + k_B T \left[ c_X \ln c_X + c_V \ln c_V + c_I \ln c_I + (1-c_X-c_V-c_I)\ln(1-c_X-c_V-c_I) \right]$$

**Bubble free energy** (van der Waals Xe EOS):
$$f^b(c_X, c_V, c_I, T) = A(c_V - 1)^2 + B c_I^2 + f_X^b(c_X)$$

## Governing Evolution Equations (Eqs. 6a–6d)

**Phase parameter** (Allen-Cahn):
$$\frac{\partial g}{\partial t} = -L \frac{\delta F}{\delta g} + \dot{n}_g$$

**Xe concentration** (Cahn-Hilliard + source/sink):
$$\frac{\partial c_X}{\partial t} = \nabla \cdot \left[ M_X \nabla \frac{\delta F}{\delta c_X} \right] + \dot{n}_X + \dot{P}_X - \dot{R}_\text{re} - \dot{S}_X$$

**Vacancy concentration**:
$$\frac{\partial c_V}{\partial t} = \nabla \cdot \left[ M_V \nabla \frac{\delta F}{\delta c_V} \right] + \dot{n}_V + \dot{P}_V - \dot{R}_{VI} - \dot{S}_V$$

**SIA concentration**:
$$\frac{\partial c_I}{\partial t} = \nabla \cdot \left[ M_I \nabla \frac{\delta F}{\delta c_I} \right] + \dot{n}_I + \dot{P}_I - \dot{R}_{VI} - \dot{S}_I$$

## Key Sink/Source Terms

- **V-I recombination**: $\dot{R}_{VI} = \mu_r c_V c_I$; enhanced at voids via $\mu_r = \mu_b + g^2 \mu_s$
- **Gas re-solution**: $\dot{R}_\text{re} = g^2 \beta c_X$ (homogeneous, $\beta = 2.0\times10^{-25}$ per fission rate)
- **Grain boundary sink**: $\dot{S}_X = (1-g)^2 r_g S_g V_X c_X$
- **Dislocation sink**: $\dot{S}_i = k_i^2 D_i c_i$, $\; k_V^2 = Z_V\rho,\; k_I^2 = Z_I\rho$
- **Frenkel pair production**: $\dot{P}_V = \dot{P}_I = f_r/d$

## Mobility and Elastic Energy

$$M_i = \frac{c_i D_i}{k_B T}$$

Stress-free strain (Vegard's law):
$$\varepsilon_{ij}^{0m} = \varepsilon_X^0(c_X - c_X^\text{eq0})\delta_{ij} + \varepsilon_V^0(c_V - c_V^\text{eq0})\delta_{ij} + \varepsilon_I^0(c_I - c_I^\text{eq0})\delta_{ij}$$

## Swelling

$$\frac{\Delta V}{V_0} = \frac{V_f - V_0}{V_0}$$

Computed from integrated phase field $g$ over simulation volume.

## See Also

- [[wiki/summaries/2018_Liang_3DPhaseFieldIntragranularBubbleUMo|Index: Liang 2018]]
- [[wiki/summaries/2018_Liang_3DPhaseFieldIntragranularBubbleUMo/ParametersFindings|Parameters & Findings]]
- [[wiki/entities/PhaseFieldModeling|PhaseFieldModeling]] — PF methodology context
- [[wiki/entities/RateTheory|RateTheory]] — rate-theory basis of sink/source terms
- [[wiki/summaries/2011_Millett_PhaseFieldGasBubbleKinetics|Millett 2011 Phase-Field]] — 2D PF model this work extends to 3D
