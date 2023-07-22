# -*- coding: utf-8 -*-
"""
N個の頂点、N個の辺からなる有向グラフが与えられます。
A[i]はi番目の辺の行き先を表します。
このグラフにはからなず閉路が存在することがわかっています。
どれか1つの閉路を出力してください。
ただしA[i]
"""
import sys
sys.setrecursionlimit(10**8)


def find_cycle(N, A):
    visited = [False] * N  # 頂点の訪問状態を管理するリスト
    path = []  # 閉路のパスを保存するリスト

    def dfs(node):
        visited[node] = True
        path.append(node)

        next_node = A[node]
        if visited[next_node]:
            start_index = path.index(next_node)
            cycle = path[start_index:]
            return cycle

        return dfs(next_node)

    for i in range(N):
        if not visited[i]:
            cycle = dfs(i)
            if cycle is not None:
                return cycle


N = int(input())
A = list(map(int, input().split()))
for i in range(N):
    A[i] -= 1

cycle = find_cycle(N, A)
for i in range(len(cycle)):
    cycle[i] += 1
print(len(cycle))
print(*cycle)
