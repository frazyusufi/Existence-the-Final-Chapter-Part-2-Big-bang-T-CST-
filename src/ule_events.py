import random, numpy as np

def generate_events(N=10000, m_past=1, m_present=1, m_future=1, seed=42):
    random.seed(seed)
    np.random.seed(seed)
    A_p, A_pr, A_f = {}, {}, {}
    A_p[0], A_pr[0], A_f[0] = [], [], []
    for e in range(1, N):
        candidates = list(range(e))
        A_p[e] = random.sample(candidates, min(m_past, len(candidates))) if m_past > 0 else []
        A_pr[e] = random.sample(candidates, min(m_present, len(candidates))) if m_present > 0 else []
        A_f[e] = random.sample(candidates, min(m_future, len(candidates))) if m_future > 0 else []
    return A_p, A_pr, A_f
