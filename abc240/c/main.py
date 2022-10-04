# -*- coding: utf-8 -*-
"""
N回のジャンプの後に座標Xの位置にいるようにすることはできるか
Nが100なのでbit全探索は無理
座標Xを限界としたDPの表を作る
"""
N, X = list(map(int, input().split()))
dp = [[False for _ in range(X + 1)] for _ in range(N + 1)]
dp[0][0] = True
AB = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N + 1):
    a, b = AB[i - 1]
    for j in range(X + 1):
        if j >= a:
            if dp[i - 1][j - a] is True:
                dp[i][j] = True
        if j >= b:
            if dp[i - 1][j - b] is True:
                dp[i][j] = True
print("Yes" if dp[-1][-1] is True else "No")
