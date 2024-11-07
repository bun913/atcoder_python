# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit
from bisect import bisect_left, bisect_right

setrecursionlimit(10**8)


def solve():
    N, S, W = arrange()
    act(N, S, W)


def arrange():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    return N, S, W


def act(N, S, W):
    # ソートしたWの小さい方からforで確認するが最初はW[0]からジャッジを始める
    # そのため、W[0]未満の体重はいないため全員大人とみなした結果となるのが初期状態
    # 最終的な答えを格納する(maxをとる変数)
    ans = S.count("1")
    # 今の正解数を格納する変数
    same_cnt = ans
    # W[i]の各要素のインデックスを保有する変数
    sort_indexes = sorted(range(N), key=lambda x: W[x])
    for i in range(N):
        # W[i]の要素のインデックスを取得
        ind = sort_indexes[i]
        # S[ind]と比較して正解かどうか
        # W[i]を使うことで正解に変わる場合は正解数を増加させる
        if S[ind] == "0":
            same_cnt += 1
        else:
            # 不正解に変えてしまうなら減らす
            same_cnt -= 1
        # 同じ体重が続く間は結果を更新しない
        if i == N - 1 or W[sort_indexes[i]] < W[sort_indexes[i + 1]]:
            ans = max(ans, same_cnt)

    print(ans)


solve()
