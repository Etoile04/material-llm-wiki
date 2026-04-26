# Missing PDFs - 2026-04-22

Network blocked: unable to reach external sites (DNS returns 198.18.x.x proxy addresses, all curl/web requests fail).

## Papers needing PDF download (retry when network available)

### 1. 2020_Beeler_RadiationDrivenDiffusionUMo
- **Title**: Radiation driven diffusion in γ U-Mo
- **Authors**: Beeler, Cooper, Mei, Schwen, Zhang
- **Journal**: Journal of Nuclear Materials, 2020
- **Likely DOI**: 10.1016/j.jnucmat.2019.151846 or similar (check JNM vol ~530)
- **Source**: ScienceDirect (likely paywalled), check OSTI.gov for preprint

### 2. 2022_Qian_U10Zr_CavitationalVoidSwelling
- **Title**: U-10Zr金属燃料低温区空化空洞肿胀行为研究
- **Authors**: Qian, Xie, Fu, Yun, Liu et al.
- **Journal**: Journal of Nuclear Materials, 564, 153665 (2022)
- **DOI**: 10.1016/j.jnucmat.2022.153665
- **Source**: ScienceDirect (likely paywalled)

### 3. 2025_Aagesen_VoidSuperlattice_Mo
- **Title**: 辐照诱导超晶格形成中的相变机制研究（钼）
- **Authors**: Aagesen, Zhang, Jiang, Gan
- **Year**: 2025
- **Source**: INL report, no DOI confirmed - check OSTI.gov or INL website

## Duplicate Resolved

### 2024_MURR_LEU_U10Mo_SwellingCreep = 2019_Mohamed_MURRLEU10MoSwellingCreep
- Same title: "Fuel Swelling and Creep Analysis for a MURR LEU U-10Mo Monolithic Plate"
- Same authors: Walid Mohamed, Hee Seok Roh, John Stillman, Erik Wilson
- Same report: ANL/RTR/TM-18/19, March 2019
- **Action**: Delete 2024_MURR_LEU_U10Mo_SwellingCreep.md as duplicate

## Status
- All external network access blocked (proxy/VPN returning 198.18.x.x)
- Cannot download any PDFs or search DOIs
- All 3 papers need manual retry when network is restored
- Recommended: use `web_search` to find DOIs and download URLs, then `curl` to fetch PDFs
