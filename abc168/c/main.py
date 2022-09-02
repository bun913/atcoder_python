# -*- coding: utf-8 -*-
"""
H時で何度動いているか
2辺の長さと成す角で求める余弦定理かな
"""
from math import radians, cos, sqrt

A, B, H, M = list(map(int, input().split()))
short_deg = H * 30
long_deg = M * 5.5
rad = radians(max(long_deg, short_deg) - min(long_deg, short_deg))
ans = sqrt(A**2 + B**2 - (2 * A * B * cos(rad)))
print(ans)
