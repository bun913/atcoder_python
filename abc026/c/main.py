# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from collections import deque
from sys import setrecursionlimit

setrecursionlimit(10**7)

# グラフの作成
N = int(input())
G = [[] for _ in range(N+1)]
for i in range(2, N+1):
    b = int(input())
    G[b].append(i)
    G[i].append(b)

# (次のノード, どのノードから来たか,訪問回数)
q = deque([(1, 0, 1)])
fees = [1] * (N+1)
visited = [False] * (N+1)

while q:
    cur, from_node, visited_cnt = q.pop()
    if visited_cnt == 1:
        # キューに追加
        q.append((cur, from_node, 2))
        for nex in G[cur]:
            if nex == from_node:
                continue
            q.append((nex, cur, 1))
    else:
        # 2回目の訪問（上に上がっていく）
        for nex in G[cur]:
            if nex == from_node:
                continue
            # 繋がり先が直属の上司のみの場合
            if G[cur] == [from_node]:
                fees[cur] = 1
                continue
            # 部下が1人しかいない場合
            if len(G[cur]) == 1:
                child = G[cur][0]
                fees[cur] = fees[child] * 2 + 1
                continue
            min_child_fee = float('inf')
            max_child_fee = 0
            for child in G[cur]:
                if child == from_node:
                    continue
                min_child_fee = min(min_child_fee, fees[child])
                max_child_fee = max(max_child_fee, fees[child])
            fees[cur] = min_child_fee + max_child_fee + 1
print(fees[1])
