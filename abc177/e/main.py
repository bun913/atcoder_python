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


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr


pairwise = True
prime_used = set()
for i in range(N):
    prime_list = factorization(A[i])
    prime_set = set([i[0] for i in prime_list])
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
