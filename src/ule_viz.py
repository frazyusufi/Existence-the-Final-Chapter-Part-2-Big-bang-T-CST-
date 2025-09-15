import matplotlib.pyplot as plt
import numpy as np

def spectral_dimension_flow(G, steps=20, trials=200, window=4):
    nodes = list(G.nodes())
    rng = np.random.default_rng()
    P_ret = []
    for t in range(1, steps+1):
        count = 0
        for _ in range(trials):
            start = rng.choice(nodes)
            current = start
            for _ in range(t):
                nbrs = list(G.successors(current)) + list(G.predecessors(current))
                if not nbrs: break
                current = rng.choice(nbrs)
            if current == start:
                count += 1
        P_val = count / trials
        if P_val == 0: P_val = 1e-10
        P_ret.append(P_val)

    steps_arr = np.arange(1, steps+1)
    x = np.log(steps_arr)
    y = np.log(P_ret)
    D_vals, centers = [], []
    for i in range(len(steps_arr)-window+1):
        xx, yy = x[i:i+window], y[i:i+window]
        slope, _ = np.polyfit(xx, yy, 1)
        D_vals.append(-2*slope)
        centers.append(np.mean(steps_arr[i:i+window]))
    return centers, D_vals

def plot_flow(centers, D_vals, out_file="results/flow_curve.png"):
    plt.figure(figsize=(6,4))
    plt.plot(centers, D_vals, "o-", label="Dimensional flow")
    plt.axhline(3, color="red", linestyle="--", label="Target ~3")
    plt.xlabel("Scale (step length)")
    plt.ylabel("Effective Dimension")
    plt.legend()
    plt.tight_layout()
    plt.savefig(out_file)
