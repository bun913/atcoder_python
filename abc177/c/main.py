# -*- coding: utf-8 -*-
"""
Nが2*10**5と大きい
1 <=j <= Nを満たす全ての組のAi*Ajの和をmodする

以下解説AC
求めるものを式変形したら累積和だった
"""
from itertools import accumulate

N = int(input())
A = list(map(int, input().split()))
AD = list(accumulate(A))
AD.insert(0, 0)
mod = 10 ** 9 + 7

ans = 0
for i in range(1, N):
    rest_sum = AD[-1]
    rest_sum -= AD[i]
    ans += A[i-1] * rest_sum % mod
print(ans % mod)
