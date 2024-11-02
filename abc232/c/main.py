# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit
from itertools import permutations

setrecursionlimit(10**8)


def solve():
    N, M, ga, gb = arrange()
    act(N, M, ga, gb)


def arrange():
    N, M = map(int, input().split())
    # 隣接行列の形式でグラフを作る
    ga = [[False]*N for _ in range(N)]
    gb = [[False]*N for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        a, b = a-1, b-1
        ga[a][b] = True
        ga[b][a] = True

    for _ in range(M):
        a, b = map(int, input().split())
        a, b = a-1, b-1
        gb[a][b] = True
        gb[b][a] = True

    return N, M, ga, gb


def act(N, M, ga, gb):
    for map_table in permutations(range(N)):
        # 青木くんのボールと高橋くんのボールの対応するリストを全パターン作る
        is_ok = True
        for i in range(N):
            for j in range(N):
                aoki_i = map_table[i]
                aoki_j = map_table[j]
                if ga[i][j] != gb[aoki_i][aoki_j]:
                    is_ok = False
                    break
        if is_ok is True:
            print("Yes")
            exit()
    print("No")


solve()
