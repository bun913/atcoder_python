# -*- coding: utf-8 -*-
"""
Nが10の5乗と非常に大きい数

まずはグラフを作ってみよう
次に単純にXが繋がっている木を深さ優先探索で探してみようか
"""
from sys import setrecursionlimit

setrecursionlimit(10**7)
from collections import deque

N, X, Y = list(map(int, input().split()))
graphs = [[] for _ in range(N + 1)]

# 木構造を二次元の配列で保有
# 例1なら3の頂点で: [1,4,5] という形
for i in range(N - 1):
    U, V = list(map(int, input().split()))
    graphs[U].append(V)
    graphs[V].append(U)

# すでに訪れている頂点の管理
visited = [False for _ in range(N + 1)]
ans = deque()

# DFS(深さ優先探索)
def dfs(a):
    visited[a] = True
    ans.append(a)
    # 目的の頂点に到達した場合
    if a == Y:
        print(*list(ans))
        exit()
    for next_target in graphs[a]:
        # まだ訪れていないならその頂点を際に探索
        if visited[next_target] is False:
            dfs(next_target)
    # ここまで来たということはこの頂点は目的地に繋がっていなかった
    # よってルートから除外する
    ans.pop()


dfs(X)
