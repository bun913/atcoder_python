# -*- coding: utf-8 -*-
"""
解く前のメモ用
Xを[Y-X]の絶対値が最小となる10**i+1の倍数のうち最大のものであるYに置き換える
"""
from decimal import Decimal, ROUND_HALF_UP

X, K = list(map(int, input().split()))
n = Decimal(str(X))

for i in range(1, K + 1):
    s = "1E" + str(i)
    n = n.quantize(Decimal(s), rounding=ROUND_HALF_UP)
print(int(n))
