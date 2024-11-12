# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit
from collections import deque

setrecursionlimit(10**8)


def solve():
    N, A, B, S = arrange()
    act(N, A, B, S)


def arrange():
    N, A, B = map(int, input().split())
    S = list(input())
    return N, A, B, S


def act(N, A, B, S):
    # 今回操作1と操作2の性質をまず理解する
    # こういう時には操作同士の性質や関係性を整理してみると良さそう
    # 対立、依存、操作の逆を考えてみよう
    # すると今回は操作Bの結果の後に操作Bを行うことで、せっかくやった操作が無駄になることがわかる
    # であれば、操作Aを任意の数やり切った後に、操作Bを行うと良さそうであることが見えてくる
    ans = float("inf")
    for a in range(N-1):
        # まず操作1を必要な回数最初に行ってみる
        q = deque(S)
        for _ in range(a):
            first = q.popleft()
            q.append(first)
        # 残された結果から操作Bを行う必要のある回数を数える
        cnt = 0
        for i in range(N//2):
            left = q[i]
            right = q[N-1-i]
            if left != right:
                cnt += 1
        ans = min(ans, a*A + cnt*B)
    print(ans)


solve()
