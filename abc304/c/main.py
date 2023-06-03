# -*- coding: utf-8 -*-
"""
1,2,...,N人の人が二次元平面上に存在
人iは座標(Xi,Yi)で表される点にいる
最初は人1がウイルスに感染している
そこから距離がD以内にいる人はウイルスに感染する
だたし距離Dはユークリッド距離で算定する
十分な時間が経った後に誰がウイルスに感染しているか出力する問題

まずはそれぞれの人の座標を取得
そのあとそれぞれの人について、グラフで表現する
グラフで表現するときに、距離がD以内の人に辺を張る
グラフで表現したあとに、dfsで感染している人を探索する
"""
from collections import deque

N, D = list(map(int, input().split()))
XY = [list(map(int, input().split())) for _ in range(N)]
# グラフで表現する
G = [[] for _ in range(N)]
for i in range(N):
    for j in range(i+1, N):
        x1, y1 = XY[i]
        x2, y2 = XY[j]
        if (x1-x2)**2 + (y1-y2)**2 <= D**2:
            G[i].append(j)
            G[j].append(i)
# 答えをBFSで求める
ans = [False] * N
ans[0] = True
q = deque([0])
while q:
    v = q.popleft()
    for nv in G[v]:
        if ans[nv]:
            continue
        ans[nv] = True
        q.append(nv)
# 答えを出力する
for b in ans:
    if b is True:
        print("Yes")
    else:
        print("No")
