# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    H, W, C = arrange()
    act(H, W, C)


def arrange():
    H, W = map(int, input().split())
    C = [list(input()) for _ in range(H)]
    return H, W, C


def act(H, W, C):
    S = [0 for _ in range(min(H, W) + 1)]
    levels = {1: 3, 2: 5}
    bef = 2
    for i in range(3, 102):
        levels[bef+1] = levels[bef] + 2
        bef += 1
    streak_map = {}
    for k, v in levels.items():
        streak_map[v] = k
    visited = [[False for _ in range(W)] for _ in range(H)]
    for i in range(H):
        for j in range(W):
            cur = C[i][j]
            if cur == ".":
                continue
            if visited[i][j] is True:
                continue
            visited[i][j] = True
            streak = 1
            x, y = i, j
            while True:
                x, y = x + 1, y + 1
                if 0 <= x < H and 0 <= y < W and C[x][y] == "#":
                    streak += 1
                    visited[x][y] = True
                    continue
                break
            if streak >= 3:
                if streak in streak_map:
                    S[streak_map[streak]] += 1

    print(*S[1:])


solve()
