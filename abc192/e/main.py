# -*- coding: utf-8 -*-
"""
解く前のメモ用
幅優先探索に近いけど、ダイクストラ法でとけるよ
幅優先探索はコストが一定の場合に使える、ダイクストラはコストが変わる場合にも使える
幅優先探索は常に自分から近いところを探索していた
ダイクストラの場合経路のコストが一定ではないから、次に探索する予定
のノードのコストを見積もっておいて、その中から一番コストが低いものを探索する
そこで優先度付きのキューを使う
"""
from heapq import heappush, heappop, heapify
from math import ceil

N, M, X, Y = map(int, input().split())
G = [[] for _ in range(N+1)]
for i in range(M):
    a, b, t, k = map(int, input().split())
    G[a].append((b, t, k))
    G[b].append((a, t, k))

q = list()
# 最もコストが低い都市を取り出したいのでヒープキューを使う
heapify(q)
# (コスト, 都市)のタプルを入れる。すると勝手にソートされてコストが低いものが取り出せる
heappush(q, (0, X))
# 到達時刻を格納する配列
times = [float('inf')] * (N+1)
times[X] = 0
# 確定マークをつけるための配列
done = [False] * (N+1)

while q:
    now_time, cur = heappop(q)
    if done[cur] is True:
        continue
    # ここに来ている時点で最小のコストで来ていることが確定しているので確定する
    done[cur] = True
    for nex, time, k in G[cur]:
        # もう訪問しているなら行かない
        if done[nex] is True:
            continue
        cost = ceil(now_time/k)*k + time
        if cost < times[nex]:
            times[nex] = cost
            heappush(q, (cost, nex))
if times[Y] == float('inf'):
    print(-1)
    exit()
print(times[Y])
