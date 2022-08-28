# -*- coding: utf-8 -*-
"""
xが素数でない場合: 叩かれたボールを消滅 aとbが書かれたボールを追加する
a,bは a>=2かつb>=2から自由に選ぶ
全てのボールに書かれている数を素数にしたい
素因数分解だよね
"""
from math import log2, ceil


def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


N = int(input())
f = prime_factorize(N)
L = len(f)
ans = ceil(log2(L))
print(ans)
