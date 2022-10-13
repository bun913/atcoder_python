# -*- coding: utf-8 -*-
"""
答えは2**63以下

A**3<=Nが絶対条件（Aが最小だから)
"""
N = int(input())

a = 1
ans = 0

while a**3 <= N:
    # 初期値
    b = a
    while a * (b**2) <= N:
        # cはb以上である必要があるので-bして+1
        ans += N // (a * b) - b + 1
        b += 1
    a += 1
print(ans)
