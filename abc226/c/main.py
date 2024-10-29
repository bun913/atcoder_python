# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit
from collections import deque

setrecursionlimit(10**8)


def solve():
    N, T, G = arrange()
    act(N, T, G)


def arrange():
    N = int(input())
    T = []
    G = [[] for _ in range(N)]
    for i in range(N):
        L = list(map(int, input().split()))
        t = L[0]
        T.append(t)
        k = L[1]
        if k == 0:
            continue
        for a in L[2:]:
            G[i].append(a-1)
    return N, T, G


def act(N, T, G):
    q = deque([N-1])
    ans = T[N-1]
    visited = [False] * N
    visited[N-1] = True
    while q:
        cur = q.popleft()
        for nex in G[cur]:
            if visited[nex] is True:
                continue
            visited[nex] = True
            ans += T[nex]
            q.append(nex)
    print(ans)


solve()
