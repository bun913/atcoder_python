# -*- coding: utf-8 -*-
"""
"""
X, Y, Z = list(map(int, input().split()))
trim_x = X - Z
y_plus_rest = Y + Z
ans = trim_x // y_plus_rest
print(ans)
