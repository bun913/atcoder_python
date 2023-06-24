# -*- coding: utf-8 -*-
"""
N個のシュークリームを平等に分けることができる人数
つまり約数を列挙すれば良いだけ。
普通にNを**0.5まで数え上げる方法で間に合う
"""
N = int(input())
ans_set = set()
for i in range(1, int(N ** 0.5)+1):
    if N % i == 0:
        ans_set.add(i)
        ans_set.add(N // i)
for s in sorted(list(ans_set)):
    print(s)
