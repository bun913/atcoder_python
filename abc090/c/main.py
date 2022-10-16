# -*- coding: utf-8 -*-
"""
無限に広がる空間
一旦手で作成してみてヒントを探す
"""

N, M = list(map(int, input().split()))
n = N - 2
m = M - 2
ans = abs(n * m)
print(ans)
