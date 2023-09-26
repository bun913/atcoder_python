# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from itertools import accumulate

N, K = map(int, input().split())
A = list(map(int, input().split()))

# 累積和の準備
sums = list(accumulate(A))
sums.insert(0, 0)

ans = 0
for i in range(N - K + 1):
    ans += sums[i + K] - sums[i]
print(ans)
