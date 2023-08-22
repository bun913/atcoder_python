# -*- coding: utf-8 -*-
"""
各頂点について20番目までの大きい数を記録しておけば良い(Kが20だから)
つまり子の頂点から上に登っていくように結果を更新していけば良い
そのために深さ優先探索で2回訪れるようにすればよい
"""
from collections import deque

# 入力の受け取り
N, Q = map(int, input().split())
X = [0] + list(map(int, input().split()))
G = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
querys = [list(map(int, input().split())) for _ in range(Q)]

# 20番目までの大きい数を記録する配列
leaves_memo = [[0]]
for i in range(1, N+1):
    leaves_memo.append([X[i]])
# (今の頂点,親の頂点,何回目の訪問か)
q = deque([(1, 0, 1)])

while q:
    # 右端から取り出す
    now, parent, count = q.pop()
    # 1回目の訪問
    if count == 1:
        q.append((now, parent, 2))
        for nex in G[now]:
            # 親の頂点はスキップしてとにかく降る
            if nex == parent:
                continue
            q.append((nex, now, 1))
    else:  # 2回目の訪問（上に上がる準備）
        for nex in G[now]:
            # 親の頂点は
            if nex == parent:
                continue
            leaves_memo[now] += leaves_memo[nex]
            leaves_memo[now].sort(reverse=True)
            leaves_memo[now] = leaves_memo[now][:20]
# クエリの処理
for q, x in querys:
    print(leaves_memo[q][x-1])
