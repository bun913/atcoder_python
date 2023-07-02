# -*- coding: utf-8 -*-
"""
まず素因数分解をする関数を作成
"""


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


N = int(input())
# エッジケースの排除
if N == 1:
    print(0)
    exit()
primes = factorization(N)
ans = 0
for prime, num in primes:
    i = 1
    while num >= i:
        num -= i
        ans += 1
        i += 1
print(ans)
