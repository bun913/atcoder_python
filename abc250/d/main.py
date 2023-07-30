# -*- coding: utf-8 -*-
"""
N以下の250に似た数の合計個数を求める
- kが素数p<qを使って、k=p*q**3と表せるとき250に似ているとする
q**3をbとすると
k=p*bとなるので、素数の数え上げはせいぜいNの平方根までで良い
"""
from math import pow

N = int(input())
if N <= 1:
    print(0)
    exit()
# エラストテネスの篩で素数を列挙する
limit = N // 2
# 3乗根を求める
limit = int(pow(limit, 1/3))+1
primes = [True] * (limit+1)
primes[0] = False
primes[1] = False
for i in range(2, limit+1):
    mul = 2
    while i * mul <= limit:
        primes[i*mul] = False
        mul += 1
# 面倒なので素数のリストに
prime_nums = [i for i, is_prime in enumerate(primes) if is_prime is True]
if len(prime_nums) <= 1:
    print(0)
    exit()
ans = 0
K = len(prime_nums)
for l in range(K):
    for r in range(l+1, K):
        if prime_nums[l] * pow(prime_nums[r], 3) <= N:
            ans += 1
        else:
            break
print(ans)
