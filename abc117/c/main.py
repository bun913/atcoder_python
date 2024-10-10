# -*- coding: utf-8 -*-
"""
解く前のメモ用
N+1個のグループに分けると考える
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    N, M, X = arrange()
    act(N, M, X)


def arrange():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    return N, M, X


def act(N, M, X):
    # マイナスがちょっと面倒なので、マイナスを0にしておく
    X.sort()
    m = min(X)
    A = []
    for x in X:
        A.append(x+abs(m))
    # グループ分けを考える時に差が最大になる部分を考える
    diffs = [None] * (M-1)
    for i in range(1, len(A)):
        diffs[i-1] = (A[i] - A[i-1], i)
    diffs.sort(reverse=True, key=lambda x: x[0])
    # 大きい方からN個のグループに分ける
    kugiri = []
    cur = 0
    for val, index in diffs[:N-1]:
        if cur == N:
            break
        kugiri.append(index-1)
        cur += 1
    kugiri.sort()
    groups = []
    start = 0
    for k in kugiri:
        groups.append(A[start:k+1])
        start = k+1
    groups.append(A[start:])
    # グループごとの手数を出す
    ans = 0
    for group in groups:
        if len(group) == 1:
            continue
        ans += group[-1] - group[0]
    print(ans)


solve()
