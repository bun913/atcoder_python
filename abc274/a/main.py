# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from decimal import Decimal, ROUND_HALF_UP

A, B = list(map(int, input().split()))
f = B / A
ans = Decimal(str(f)).quantize(Decimal("0.001"), rounding=ROUND_HALF_UP)
print(ans)
