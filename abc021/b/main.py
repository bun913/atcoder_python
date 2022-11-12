# -*- coding: utf-8 -*-
"""
解く前のメモ用
aから出発してK回寄り道してbに到着
道路を通る回数が最小となる経路
"""
from collections import Counter

N = int(input())
a, b = list(map(int, input().split()))
K = int(input())
P = list(map(int, input().split()))
P.insert(0, a)
P.append(b)
c = Counter(P)
if c.most_common()[0][1] >= 2:
    print("NO")
    exit()
print("YES")
