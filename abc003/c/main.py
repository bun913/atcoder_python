# -*- coding: utf-8 -*-
"""
解く前のメモ用
全部のビデオは見れないからi番目に大きいビデオを見続ければ良いのでは
"""
from decimal import Decimal

N, K = list(map(int, input().split()))
R = list(map(int, input().split()))
rd = sorted(R, reverse=True)
# 1の場合は最大のものを選ぶ
rates = rd[:K]
ans = Decimal("0")
for r in reversed(rates):
    ans = (ans + Decimal(str(r))) / Decimal("2")
print(ans)
