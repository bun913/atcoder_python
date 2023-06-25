# -*- coding: utf-8 -*-
"""
整数Nがくる。
1以上Nの整数のうち、2以上の整数a,bを用いてa**bと表せないものの数
これもa**bってことは少なくともbは2以上の整数であることがわかる。
ということはどんなにあれでも N = a * aとなるはず（a=1は除く）
であれば、これもNまで調べなくても、Nの平方根まで調べればいい。
a,bは2以上の整数という制約がある
"""
N = int(input())
limit = int(N**0.5) + 1
can_pow = 0
visited = set()
for a in range(2, limit):
    b = 2
    while a**b <= N:
        if a ** b not in visited:
            can_pow += 1
        visited.add(a**b)
        b += 1
print(N-can_pow)
