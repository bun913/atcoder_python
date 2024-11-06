# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    h1, h2, h3, w1, w2, w3 = arrange()
    act(h1, h2, h3, w1, w2, w3)


def arrange():
    return map(int, input().split())


def act(h1, h2, h3, w1, w2, w3):
    ans = 0
    for a in range(1, 29):
        for b in range(1, 29):
            for c in range(1, 29):
                for d in range(1, 29):
                    # 4箇所だけ全探索
                    is_ok = True
                    rows = [[0 for _ in range(3)] for _ in range(3)]
                    rows[0][0] = a
                    rows[0][1] = b
                    rows[1][0] = c
                    rows[1][1] = d
                    # 1行目の3列目の数字を決める
                    rows[0][2] = w1 - rows[0][0] - rows[0][1]
                    # 2行目の3列目の数字を決める
                    rows[1][2] = w2 - rows[1][0] - rows[1][1]
                    # 3行目の1列目の数字を決める
                    rows[2][0] = h1 - rows[0][0] - rows[1][0]
                    # 3行目の2列目の数字を決める
                    rows[2][1] = h2 - rows[0][1] - rows[1][1]
                    # 3行目の3列目の数字を決める
                    rows[2][2] = h3 - rows[0][2] - rows[1][2]
                    # 矛盾をチェック
                    for i in range(3):
                        row_sum = 0
                        for j in range(3):
                            if rows[i][j] < 1:
                                is_ok = False
                                break
                            row_sum += rows[i][j]
                        if row_sum != [w1, w2, w3][i]:
                            is_ok = False
                            break
                    for j in range(3):
                        col_sum = 0
                        for i in range(3):
                            col_sum += rows[i][j]
                        if col_sum != [h1, h2, h3][j]:
                            is_ok = False
                            break
                    if is_ok:
                        ans += 1
    print(ans)


solve()
