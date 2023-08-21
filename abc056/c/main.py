# -*- coding: utf-8 -*-
"""
解く前のメモ用
等差数列の最終項をnとすると
等差数列の和の公式を考えると以下のようになる
X <= n(n+1)/2
で、この時n**2となっている
Xはたかだか10**9という制限があるので、調べるのは10**5程度で十分
"""
X = int(input())

for n in range(1, 10**5):
    if n*(n+1)//2 >= X:
        print(n)
        break
