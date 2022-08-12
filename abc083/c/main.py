# -*- coding: utf-8 -*-
"""
解く前のメモ

最大まで数列に数を詰めてあげたいのであれば、2をかけ続ければ良いのでは
2で何回かけらえるか考えれば良さそう

最初はlogの計算でやってたけどWA出した
よく考えれば2倍ずつ増えていくんだから普通に数え上げればよかった
"""
from math import log2, floor

X, Y = list(map(int, input().split()))
# div = Y // X
# ans = floor(log2(div)) + 1
# print(ans)
ans = 0
mul = 0
cur = X
while True:
    n = cur * (2 ** mul)
    if n <= Y:
        ans += 1
        mul += 1
        continue
    break
print(ans)
