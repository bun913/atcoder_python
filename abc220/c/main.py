# -*- coding: utf-8 -*-
"""
Aを10 ** 100回連結した数列を数列Bとする
Bを前から順に足した時和が初めてXを超えるのはなんこうまで足した時か

これも長さがNって決まっているから
和とあまりを使えば簡単に求められそう
"""

N = int(input())
A = list(map(int, input().split()))
X = int(input())

one_sum = sum(A)
q = X // one_sum
m = X % one_sum

ans = q * N
cur = 0

for i in range(N):
    a = A[i]
    cur += a
    ans += 1
    if cur > m:
        print(ans)
        exit()
