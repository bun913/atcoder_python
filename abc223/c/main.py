# -*- coding: utf-8 -*-
"""
N本の導火線を一直線に繋げている
左端と右端から火をつけて左から何センチのところで火がぶつかるか

二つの火がぶつかる時間は片側から火をつけて燃え尽きるまでの時間の半分になる
"""

N = int(input())
A = []
B = []
for _ in range(N):
    a, b = list(map(int, input().split()))
    A.append(a)
    B.append(b)
t = 0.0

for i in range(N):
    t += A[i] / B[i]
t /= 2

ans = 0
for i in range(N):
    if A[i] / B[i] <= t:
        ans += A[i]
        t -= A[i] / B[i]
    else:
        ans += B[i] * t
        break
print(ans)
