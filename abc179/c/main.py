# -*- coding: utf-8 -*-
"""
一見A*B+Cを全て探索しないようにいけないように感じる
A,B,Cは全て正の整数の組なのでA*B=Nとなるような約数以外を列挙すれば良いのでは
約数列挙の別バージョンで約数じゃ無い時に数え上げればよし
"""
from math import sqrt

N = int(input())

ans = 0
for A in range(1, N):
    # AxBは確実にAの倍数になる
    # つまりAの倍数個分だけ答えがある
    cnt = (N - 1) // A
    ans += cnt
print(ans)
