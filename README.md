# Bridging the Gap: How Transferable is Reinforcement Learning for Traffic Signal Control?

> **Antoine Karila-Cohen, Rim Slama, Pierre-Antoine Laharotte**  
> EMob-Lab, ENTPE, Univ. Gustave Eiffel, Lyon, France  
> *hEART 2026*

---

## Overview

This repository contains the full list of articles reviewed in the systematic literature review (SLR) on **transferability of Deep Reinforcement Learning (DRL) for Traffic Signal Control (TSC)**.

Despite impressive results in simulation, DRL-based TSC systems consistently fail when deployed in new environments. This paper investigates **why** and **how** to fix it, through a unified taxonomy covering three transfer dimensions:

| Dimension | Acronym | Challenge |
|---|---|---|
| Location-to-Location | **L2L** | New road topologies, junction geometries |
| Scenario-to-Scenario | **S2S** | Demand shifts, sensor noise, non-stationarity |
| Simulation-to-Reality | **S2R** | The "reality gap" — noise, latency, hardware |

---

## Repository Contents

```
├── articles/
│   └── full_article_list.csv       # All 117 reviewed articles with metadata
├── figures/
│   ├── annual_progression.png      # Publication growth 2021–2026
│   ├── literature_distribution.png # L2L / S2S / S2R breakdown
│   ├── l2l_strategies.png
│   ├── s2s_strategies.png
│   └── s2r_strategies.png
└── README.md
```

---

## Methodology

- **117 peer-reviewed articles** (2021–2026)
- Sources: Scopus, Web of Science, Google Scholar
- Selection: abstract screening + snowballing
- Keywords: reinforcement learning · traffic signal control · transferability · sim2real · cross-city · meta-learning

---

## Key Findings

### L2L — Topological Transfer
- MLP/CNN agents are **hard-coded to a fixed input size** → cannot handle new junction geometries
- **Graph Neural Networks (GNNs)** enable permutation-invariant policies that generalize across topologies
- IG-RL demonstrated zero-shot city-scale transfer across thousands of signals in Manhattan
- **Transformers** (X-Light) identify universal traffic patterns via attention, regardless of topology

### S2S — Scenario Transfer
- Real traffic is non-stationary: peak-hour ≠ off-peak ≠ incident conditions
- **Distributional RL** (Implicit Quantile Networks) models the full return distribution, providing robustness to sensor dropout
- **Adaptive exploration** prevents catastrophic gridlocks during saturated conditions
- Agents trained in high-CAV environments can transfer logic to human-dominated traffic

### S2R — Simulation-to-Reality
- Simulators assume perfect sensing, zero latency, and deterministic dynamics — none of which hold in the field
- **Action Masking** enforces safety constraints (min. green times, yellow clearance) irrevocably
- **Domain Randomization** (Gaussian noise injection, artificial latency) hardens policies against sensor failure
- **Offline RL** enables pre-training on historical loop detector data, eliminating live on-road exploration risk
- **Digital Twins** allow verification in a mirror simulator before any physical command is issued

---

## Open Research Directions

1. **Cumulative Transferability** — most studies isolate a single shift; real deployment combines spatial + temporal + physical shifts simultaneously
2. **Knowledge Distillation for Edge Computing** — large Transformers are too expensive for roadside controllers; distillation into lightweight student models is needed
3. **Mathematical Similarity Metrics** — Graph Edit Distance, Mahalanobis metrics to quantify the structural gap between source and target networks
4. **Partial Observability & State Recovery** — agents must maintain internal world models to recover missing states from failing sensors

---

## Citation

```bibtex
@inproceedings{karilacohon2026transferability,
  title     = {Bridging the Gap: How Transferable is Reinforcement Learning for Traffic Signal Control?},
  author    = {Karila-Cohen, Antoine and Slama, Rim and Laharotte, Pierre-Antoine},
  booktitle = {hEART 2026 -- European Association for Research in Transportation},
  year      = {2026},
  address   = {Lyon, France}
}
```

---

## Contact

Antoine Karila-Cohen — EMob-Lab, ENTPE, Univ. Gustave Eiffel, Lyon, France
