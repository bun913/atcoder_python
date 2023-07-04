# -*- coding: utf-8 -*-
"""
解く前のメモ用
各テストケースについて、N個おん正の整数から奇数を数える
"""
from sys import setrecursionlimit

setrecursionlimit(10**7)
T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for a in A:
        if a % 2 == 1:
            ans += 1
    print(ans)
