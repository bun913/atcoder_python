# -*- coding: utf-8 -*-
"""
グラフの問題
N1+N2頂点M辺のグラフが与えられる
1 <= u,v <= N1を満たす整数u,vに対して、uとvは隣接している
N1+1 <= u,v <= N1+N2を満たす整数u,vに対して、uとvは隣接している
頂点1と頂点N1+N2は非連結

次の操作を1回のみ行う
1 <= u <= N1 を満たす整数u
N1+1 <= v <= N1+N2 を満たす整数v
uとvの間に変を追加して、uとvを連結する
頂点1と頂点N1+N2までを結ぶ経路の長さの最小値をdとする
dの最大値を求めよ

考察
頂点1から最も遠い頂点と、頂点N1+N2から最も遠い頂点を繋げれば良いのでは
"""
from collections import deque

# まずは条件通りグラフを作る
N1, N2, M = map(int, input().split())
G = [[] for _ in range(N1 + N2 + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

# 頂点1と隣接していて、頂点1から最も遠い頂点を求める
q = deque([1])
dis1 = [-1] * (N1 + N2 + 1)
dis1[1] = 0
while q:
    cur = q.popleft()
    for nex in G[cur]:
        # 訪問済みならスキップ
        if dis1[nex] != -1:
            continue
        dis1[nex] = dis1[cur] + 1
        q.append(nex)
most_far_index1 = dis1.index(max(dis1))

# 頂点N1+N2と隣接していて、頂点N1+N2から最も遠い頂点を求める
q = deque([N1 + N2])
dis2 = [-1] * (N1 + N2 + 1)
dis2[N1 + N2] = 0
while q:
    cur = q.popleft()
    for nex in G[cur]:
        # 訪問済みならスキップ
        if dis2[nex] != -1:
            continue
        dis2[nex] = dis2[cur] + 1
        q.append(nex)
most_far_index2 = dis2.index(max(dis2))

# 求めた頂点同士を繋げる
G[most_far_index1].append(most_far_index2)
G[most_far_index2].append(most_far_index1)

# であとは頂点1から頂点N1+N2までの最短経路を求める
q = deque([1])
dis3 = [-1] * (N1 + N2 + 1)
dis3[1] = 0
while q:
    cur = q.popleft()
    for nex in G[cur]:
        # 訪問済みならスキップ
        if dis3[nex] != -1:
            continue
        dis3[nex] = dis3[cur] + 1
        q.append(nex)
print(dis3[-1])
