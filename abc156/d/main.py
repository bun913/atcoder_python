# -*- coding: utf-8 -*-
"""
全体の数 2**n -1 
引く数 C(n, a) + C(n, b)
"""


def nCr_mod(n: int, r: int, mod: int) -> int:
    # 分子
    numerator = 1
    for i in range(n-r+1, n+1):
        numerator = numerator * i % mod
    # 分母
    demoninator = 1
    for i in range(1, r+1):
        demoninator = demoninator * i % mod
    # 分子*分母の逆元
    return numerator * pow(demoninator, mod-2, mod) % mod


N, a, b = map(int, input().split())
ans = pow(2, N, 10 ** 9 + 7) - 1
mod = 10 ** 9 + 7
ans -= nCr_mod(N, a, mod)
ans -= nCr_mod(N, b, mod)
ans %= mod
print(ans)
