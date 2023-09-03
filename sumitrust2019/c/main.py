# -*- coding: utf-8 -*-
"""
Xは10**6以下の整数
1個100円のおにぎり
1個101円のおにぎり
1個102円のおにぎり
1個103円のおにぎり
1個104円のおにぎり
1個105円のおにぎり
これらの商品を任意の数を買って合計金額をちょうどX円にすることができるかを判定する
動的計画法でi個目までの商品を使って良い時にj円を作ることができるかを求める
"""
X = int(input())
items = [100, 101, 102, 103, 104, 105]
dp = [[False for _ in range(X+1)] for _ in range(6+1)]
dp[0][0] = True

for i in range(1, 6+1):
    item = items[i-1]
    for j in range(X+1):
        if dp[i-1][j] is True:
            dp[i][j] = True
        if j + item <= X:
            # 先を見るタイプのDPにすれば倍数とか気にしないでよい
            if dp[i][j] is True:
                dp[i][j+item] = True
                continue
for i in range(6+1):
    if dp[i][X] is True:
        print(1)
        exit()
print(0)
