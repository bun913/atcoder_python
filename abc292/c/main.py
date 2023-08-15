# -*- coding: utf-8 -*-
"""
Nが2*10**5以下であることは確定
N = X + Yという形にシンプルに考える
このときXは2*10**5未満であることがわかる
で、Xが決まればYも決まるのでXを全探索する
その時Xをバラして考える X = a * bとする
Xの約数を素早く求めれば良い
"""


def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


N = int(input())
ans = 0
for x in range(1, 200000):
    if N-x <= 0:
        break
    y = N-x
    # xを x = a * bと考え直す
    x_cands = len(make_divisors(x))
    y_cands = len(make_divisors(y))
    ans += x_cands * y_cands
print(ans)
