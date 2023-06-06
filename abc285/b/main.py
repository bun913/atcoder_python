# -*- coding: utf-8 -*-
"""
解く前のメモ用
i=1,2,...N-1それぞれについて以下の条件を満たす最大の負ではない整数lを求める
l +i <= N
全ての 1 <= k <=lを満たす整数kについて Sk != Si+k
"""
from sys import setrecursionlimit

setrecursionlimit(10**7)
N = int(input())
S = input()

# iはずらす数
for i in range(1, N):
    # lは1から
    ans = 0
    for l in range(0, N-i):
        if S[l] != S[l+i]:
            ans += 1
        else:
            break
    print(ans)
