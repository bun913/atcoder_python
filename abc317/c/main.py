# -*- coding: utf-8 -*-
"""
解く前のメモ用
Nが10しかないからbit全探索で良さそう
全部の街の経路を列挙して、長さCの合計が最小のものを探す
好きな街からスタートとして同じ街を2ど以上通らずに別の街へ移動する時の通る道路の長さの合計の最大値を求める
"""
import sys
sys.setrecursionlimit(10**8)

N, M = map(int, input().split())
G = [[] for _ in range(N+1)]
length = dict([(i, {}) for i in range(1, N+1)])

for _ in range(M):
    a, b, c = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
    length[a][b] = c
    length[b][a] = c


def dfs(cur, visited, cost):
    max_cost = cost
    for nex in G[cur]:
        load_cost = length[cur][nex]
        if visited[nex]:
            continue
        # 訪問済みにする
        visited[nex] = True
        max_cost = max(max_cost, dfs(nex, visited, cost+load_cost))
        # 再起で見終わったら次のルートのために訪問済みフラグを落とす
        visited[nex] = False
    return max_cost


ans = -1
for i in range(1, N+1):
    visited = [False] * (N+1)
    visited[i] = True
    ans = max(ans, dfs(i, visited, 0))
print(ans)
