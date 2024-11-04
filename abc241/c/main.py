# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    N, grid = arrange()
    act(N, grid)


def arrange():
    N = int(input())
    grid = [list(input()) for _ in range(N)]
    return N, grid


def act(N, grid):
    # 行の判定から
    # 6つの連続した区間に黒が4つ以上あればOK
    for i in range(N):
        for j in range(N-5):
            black_cnt = 0
            for x in range(6):
                if grid[i][j+x] == "#":
                    black_cnt += 1
            if black_cnt >= 4:
                print("Yes")
                exit()
    # 同様に列の判定を行う
    for j in range(N):
        for i in range(N-5):
            black_cnt = 0
            for x in range(6):
                if grid[i+x][j] == "#":
                    black_cnt += 1
            if black_cnt >= 4:
                print("Yes")
                exit()
    # 右斜方向の判定
    for i in range(N-5):
        for j in range(N-5):
            black_cnt = 0
            for x in range(6):
                if grid[i+x][j+x] == "#":
                    black_cnt += 1
            if black_cnt >= 4:
                print("Yes")
                exit()
    # 左斜方向の判定
    for i in range(N-5):
        for j in range(5, N):
            black_cnt = 0
            for x in range(6):
                if grid[i+x][j-x] == "#":
                    black_cnt += 1
            if black_cnt >= 4:
                print("Yes")
                exit()
    print("No")


solve()
