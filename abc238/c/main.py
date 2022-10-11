# -*- coding: utf-8 -*-
"""
f(x) = x以下の正の整数でxと桁数が同じものの数
f(1) + f(2) + .. + f(N)を998244353で割ったあまりを求める
"""
N = int(input())


def s(A: int, B: int) -> int:
    """
    AからBまでの和を求める(和の公式)
    """
    return (B - A + 1) * (A + B) // 2


ans = 0
for x in range(1, 19):
    if 10**x <= N:
        ans += s(1, 9 * 10 ** (x - 1))
        ans %= 998244353
    else:
        ans += s(1, N - 10 ** (x - 1) + 1)
        ans %= 998244353
        break
print(ans)
