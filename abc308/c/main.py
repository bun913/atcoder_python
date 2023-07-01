# -*- coding: utf-8 -*-
"""
方向を変えてめっちゃでかい数を利用して整数演算をしてみる
"""
N = int(input())
success_rates = []
for _ in range(N):
    a, b = map(int, input().split())
    # めっちゃでかい数で整数演算を盛り込んでみる
    success_rate = a * (10**20) // (a + b)
    success_rates.append(success_rate)

people = list(range(1, N + 1))
people.sort(key=lambda i: (-success_rates[i-1], i))

print(*people, sep=' ')
