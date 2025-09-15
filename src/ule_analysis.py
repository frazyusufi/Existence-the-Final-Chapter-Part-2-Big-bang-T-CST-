import numpy as np
import networkx as nx

def compute_rho(e1, e2, A_p, A_pr, A_f, N):
    anc1 = set(A_p.get(e1, []) + A_pr.get(e1, []))
    anc2 = set(A_p.get(e2, []) + A_pr.get(e2, []))
    j_anc = len(anc1 & anc2) / len(anc1 | anc2) if anc1 or anc2 else 0
    fut1 = set(A_f.get(e1, []))
    fut2 = set(A_f.get(e2, []))
    j_fut = len(fut1 & fut2) / len(fut1 | fut2) if fut1 or fut2 else 0
    s_layer = 1 - abs(e1 - e2) / N
    rho = (1/3) * j_anc + (1/3) * j_fut + (1/3) * s_layer
    return rho

def build_thresholded_graph(A_p, A_pr, A_f, theta=0.5, range_limit=100):
    G = nx.DiGraph()
    events = list(A_p.keys())
    N = len(events)
    for i, e1 in enumerate(events):
        start = max(0, i - range_limit)
        end = min(N, i + range_limit + 1)
        for e2 in events[start:end]:
            if e1 != e2:
                rho = compute_rho(e1, e2, A_p, A_pr, A_f, N)
                if rho >= theta:
                    etype = []
                    if e1 in A_p.get(e2, []): etype.append("past")
                    if e1 in A_pr.get(e2, []): etype.append("present")
                    if e1 in A_f.get(e2, []): etype.append("future")
                    G.add_edge(min(e1,e2), max(e1,e2), weight=rho, etype=",".join(etype) or "correlated")
    return G

def count_triangles_exact(G):
    UG = G.to_undirected()
    return sum(nx.triangles(UG).values()) // 3
