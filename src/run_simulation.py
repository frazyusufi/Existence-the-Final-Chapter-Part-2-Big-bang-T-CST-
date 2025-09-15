import argparse
import networkx as nx
from src.ule_events import generate_events
from src.ule_analysis import build_thresholded_graph, count_triangles_exact
from src.ule_viz import spectral_dimension_flow, plot_flow
import numpy as np

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--N", type=int, default=10000)
    parser.add_argument("--past", type=int, default=1)
    parser.add_argument("--present", type=int, default=1)
    parser.add_argument("--future", type=int, default=1)
    parser.add_argument("--theta", type=float, default=0.5)
    args = parser.parse_args()

    A_p, A_pr, A_f = generate_events(N=args.N, m_past=args.past, m_present=args.present, m_future=args.future)
    G = build_thresholded_graph(A_p, A_pr, A_f, theta=args.theta)
    tri = count_triangles_exact(G)
    tri_density = tri / args.N
    centers, D_vals = spectral_dimension_flow(G)
    dev = np.mean(np.abs(np.array(D_vals) - 3))
    fitness = -dev + 5 * tri_density
    meanD = np.mean(D_vals)

    print(f"Parameters: past={args.past}, present={args.present}, future={args.future}, N={args.N}, theta={args.theta}")
    print(f"MeanD≈{meanD:.2f}, Dev≈{dev:.2f}, Tri≈{tri_density:.3f}, Fit≈{fitness:.3f}")

    plot_flow(centers, D_vals, out_file="results/flow_curve.png")
    nx.write_gexf(G, "results/rho_graph.gexf")
    print("Saved results to results/ folder")
