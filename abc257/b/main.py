# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用

全ての組み合わせを列挙する方法
list(0...8)から2つを抜き出す
list(combinations(l, 2))

bit全探索でフラグが立っているかチェックする
if ((i >> j) & 1)
"""
from functools import reduce
from itertools import combinations
import math

n, k, q = map(int, input().split())
a = list(map(int, input().split()))
l = list(map(int, input().split()))
for i in range(q):
    if(a[l[i]-1] == n):
        continue
    elif(l[i] == k):
        a[l[i]-1] += 1
    elif(a[l[i]-1]+1 < a[l[i]]):
        a[l[i]-1] += 1
print(*a)
