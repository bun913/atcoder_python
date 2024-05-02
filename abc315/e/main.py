# -*- coding: utf-8 -*-
"""
1からNまでの番号がついたN冊の本がある
本iにはCi冊の前提となる本があって、それぞれPijが書かれている
本1を読むために必要な最小の数の本を読みたい
本1以外によまなければならない本を順番に出力せよ

制約
2 <= N <= 2 *10^5

考察
DFSで子から親に向かって答えに詰めていけば良さそう
だけどそのままやるとTLEになるから、計算量を減らす工夫が必要
"""
from collections import deque

N = int(input())
parents = []
# まずグラフを作る
G = [[] for _ in range(N+1)]

for i in range(N):
    C, *P = map(int, input().split())
    if i == 0:
        parents = P[:]
    G[i+1] = P[:]

# DFSで子から親に向かってリストに詰める
# 2回目の訪問（子から親）と判別できるようにキューに必要な情報を詰めていく
# (今いるノード,親のノード,頂点の訪問回数)
q = deque([(1, 0, 1)])
ans_list = []
visited = [False] * (N+1)
while q:
    now, parent, cnt = q.pop()
    # ここですでに答えに詰めているノードはスキップ
    if visited[now]:
        continue
    # 1回目の訪問
    if cnt == 1:
        q.append((now, parent, 2))
        for to in G[now]:
            q.append((to, now, 1))
    else:
        for to in G[now]:
            if visited[to]:
                continue
            visited[to] = True
            ans_list.append(to)
print(*ans_list, sep=' ')
