Existence: The Final Chapter — Part 2
Universal Law of Existence (ULE): Time Primacy and the Big Bang

Author: Ahmad Fraz Yusufi
Tagline: Existence begins with when, not where.

📖 Overview

This repository contains the code, theory, and draft paper for the Universal Law of Existence (ULE) — a new paradigm where time is the fundamental substrate of reality.

The first something is time, not space.

From a time singularity (unstable 1D time), the universe unfolded into 3D time, which in turn generated space, energy, and matter.

The Big Bang is reinterpreted as the expansion of 3D time, not spacetime.

This repo provides:

Formal axioms and conjectures of ULE

Python simulations of event-graph universes

Spectral dimension analysis showing convergence to 3D

Motif detection (proto-matter via triangle density)

LaTeX draft paper (for arXiv/journal submission)

🔬 Scientific Vision

Primacy of Time: Temporal order exists independently of space.

Emergence: Space, fields, and matter arise from correlations in event structure.

Testable Predictions: Dimensional flow, motif stability, and possible signatures in decoherence and cosmology.

📂 Repository Structure
ULE-Event-Graphs/
│
├── README.md                  # Overview and usage
├── LICENSE                    # Open-source license
├── requirements.txt           # Python dependencies
│
├── src/                       # Core simulation code
│   ├── ule_events.py          # Event generation
│   ├── ule_analysis.py        # Correlation + motifs
│   ├── ule_viz.py             # Spectral dimension analysis
│   └── run_simulation.py      # Command-line runner
│
├── results/                   # Output data & plots
│   ├── flow_curve.png         # Example dimension flow
│   └── rho_graph.gexf         # Graph for Gephi visualization
│
├── paper/                     # Draft paper
│   ├── ULE_paper.tex          # LaTeX source
│   ├── ULE_paper.pdf          # Compiled PDF (to add after compile)
│   └── figures/               # Figures for the paper
│
└── notebooks/                 # Interactive exploration
    └── exploration.ipynb

🔧 Installation

Clone the repository:

git clone https://github.com/YOUR-USERNAME/ULE-Event-Graphs.git
cd ULE-Event-Graphs


Install dependencies:

pip install -r requirements.txt


Dependencies:

numpy

networkx

matplotlib

For large-scale runs (N ≥ 100k), install:

python-igraph or graph-tool

🚀 Quick Start

Run a 10k event simulation:

python src/run_simulation.py --N 10000 --past 1 --present 1 --future 1 --theta 0.5


Outputs:

results/flow_curve.png → spectral dimension flow plot

results/rho_graph.gexf → graph file (load in Gephi)

Console log with mean dimension, deviation, triangle density, fitness

📊 Example Results (N=10k)

Mean effective dimension: 3.45

Flow: 3.8 → 3.0 (convergent toward 3D)

Triangle density: 0.032

Fitness: 0.715

📄 Paper Draft

The draft paper (paper/ULE_paper.tex) includes:

Formal axioms of ULE

Central Conjecture (Manifold Emergence)

Theorem + Lemma proof sketch

Simulation evidence (figures + table)

Discussion and outlook

Compiled PDF: paper/ULE_paper.pdf (to be built with LaTeX).

🌌 Philosophical Perspective

Nothing = Something. Absolute nothingness cannot exist.

The First Something = Time.

The Big Bang = the unfolding of 3D time from a singular seed.

Space and matter are emergent consequences of temporal order.

Multiverse = the memory of all events recorded in 3D time.

🤝 Contributing

Contributions are welcome — ideas, simulations, visualizations, or rigorous proofs.

Fork the repo, create a branch, and submit a pull request.

📜 License

This project is released under the MIT License.
