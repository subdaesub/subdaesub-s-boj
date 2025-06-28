import bisect
import sys
input = sys.stdin.readline

def find(u, parent):
    if parent[u] != u:
        parent[u] = find(parent[u], parent)
    return parent[u]

def union(u, v, parent):
    u = find(u, parent)
    v = find(v, parent)
    parent[u] = v

N, M, K = map(int, input().split())
minsu = list(map(int, input().split()))
chulsoo = list(map(int, input().split()))

minsu.sort()
idx_map = {v: i for i, v in enumerate(minsu)}
parent = list(range(M + 1))

for ch_card in chulsoo:

    idx = bisect.bisect_right(minsu, ch_card)
    rep = find(idx, parent)
    print(minsu[rep])
    union(rep, rep + 1, parent)