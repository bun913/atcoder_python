# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit
from collections import deque

setrecursionlimit(10**8)


def solve():
    N, G = arrange()
    act(G)


def arrange():
    N = int(input())
    g = {}
    for _ in range(N):
        a, b = map(int, input().split())
        a, b = a-1, b-1
        if a not in g:
            g[a] = [b]
        else:
            g[a].append(b)
        if b not in g:
            g[b] = [a]
        else:
            g[b].append(a)
    return N, g


def act(G):
    q = deque([0])
    ans = 0
    visited = {}
    while q:
        cur = q.popleft()
        if cur in visited:
            continue
        visited[cur] = True
        if cur not in G:
            continue
        for nex in G[cur]:
            if nex in visited:
                continue
            ans = max(ans, nex)
            q.append(nex)
    print(ans+1)


solve()
