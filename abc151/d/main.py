# -*- coding: utf-8 -*-
"""
迷路の問題
"""
from collections import deque

H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
# 迷路のつながっている道同士をグラフで表現する
G = [list() for _ in range(H*W)]
# 縦方向
for i in range(H):
    for j in range(W-1):
        if S[i][j] == '.' and S[i][j+1] == '.':
            G[i*W+j].append(i*W+j+1)
            G[i*W+j+1].append(i*W+j)
# 横方向
for i in range(H-1):
    for j in range(W):
        if S[i][j] == '.' and S[i+1][j] == '.':
            G[i*W+j].append((i+1)*W+j)
            G[(i+1)*W+j].append(i*W+j)
ans = -1
# 幅優先探索
for start in range(H*W):
    q = deque([start])
    dist = [-1] * (H*W)
    dist[start] = 0
    while q:
        cur = q.popleft()
        for nex in G[cur]:
            # 訪問済みの場合
            if dist[nex] != -1:
                continue
            # 訪問していない場合
            dist[nex] = dist[cur] + 1
            q.append(nex)
    ans = max(ans, max(dist))
print(ans)
