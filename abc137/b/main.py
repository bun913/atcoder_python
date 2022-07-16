# -*- coding: utf-8 -*-
"""
連続するK個の石が黒
Xにある石は黒で塗られている
"""

K, X = list(map(int, input().split()))
left = X - (K-1)
right = X + (K-1)
print(*list(range(left, right+1)))
