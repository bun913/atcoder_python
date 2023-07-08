# -*- coding: utf-8 -*-
"""
pairwise coprimeは全ての数について素因数分解した時に
同じ素因数を持つものが一つもないことを言う
素因数分解を高速に行えばわかる
"""
from math import gcd
from functools import reduce

N = int(input())
A = list(map(int, input().split()))
# D[i] = iの最小の素因数
D = [0] * (10 ** 6 + 10)
# 最大の数までその数の最小の素因数を持っていれば、簡単に素因数分解ができるのか
for i in range(2, 10**6 + 10):
    if D[i] != 0:
        continue
    for k in range(1, 10**6):
        if i * k < 10 ** 6 + 10:
            if D[i*k] == 0:
                D[i*k] = i
        else:
            break


# 高速で素因数分解
def fast_prime_fuct(x):
    prime = []
    while 1 < x:
        prime.append(D[x])
        # なるほどxの最小の素因数すらも持っているから高速で素因数分解できるのか
        x //= D[x]
    return prime


pairwise = True
prime_used = set()
for i in range(N):
    prime_list = fast_prime_fuct(A[i])
    prime_set = set(prime_list)
    for i in prime_set:
        if i in prime_used:
            pairwise = False
            break
        prime_used.add(i)
if pairwise is True:
    print("pairwise coprime")
    exit()

gc = reduce(gcd, A)
if gc == 1:
    print("setwise coprime")
    exit()
print("not coprime")
