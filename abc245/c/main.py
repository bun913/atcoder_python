# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用
"""
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.insert(0, 0)
b.insert(0, 0)
ap = [False for _ in range(n + 1)]  # (X1, X2...Xi)まで考慮したとき、Xi = Aiとしてよいか
bp = [False for _ in range(n + 1)]  # (X1, X2...Xi)まで考慮したとき、Xi = Biとしてよいか

ap[1] = True
bp[1] = True

for i in range(2, n + 1):
    if ap[i - 1]:
        if abs(a[i - 1] - a[i]) <= k:
            ap[i] = True
        if abs(a[i - 1] - b[i]) <= k:
            bp[i] = True

    if bp[i - 1]:
        if abs(b[i - 1] - a[i]) <= k:
            ap[i] = True
        if abs(b[i - 1] - b[i]) <= k:
            bp[i] = True

if ap[n] or bp[n]:
    print("Yes")
else:
    print("No")
