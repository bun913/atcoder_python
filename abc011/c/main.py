# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
N = int(input())
NG = set([int(input()) for _ in range(3)])

dp = [[False for _ in range(N+1)] for _ in range(100+1)]
dp[0][0] = True

for i in range(1, 101):
    for j in range(N+1):
        # NGワードはFalseのまま飛ばす
        if j in NG:
            continue
        # 1行前の1つ前、2つ前、3つ前のいずれかがTrueならTrue
        if j - 1 >= 0 and dp[i-1][j-1]:
            dp[i][j] = True
            continue
        if j - 2 >= 0 and dp[i-1][j-2]:
            dp[i][j] = True
            continue
        if j - 3 >= 0 and dp[i-1][j-3]:
            dp[i][j] = True
            continue

for row in dp:
    if row[N]:
        print('YES')
        exit()
print("NO")
