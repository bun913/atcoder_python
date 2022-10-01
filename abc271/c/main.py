# -*- coding: utf-8 -*-
"""
解く前のメモ用

以下解説AC
本iを持っている場合は1冊、持っていない場合は2冊消費して本iを読める
なので1巻数から初めてあれば1冊を引く、なければ2冊を引くというように数え上げて行けば良い
"""
from sys import setrecursionlimit

setrecursionlimit(10**7)

N = int(input())
A = list(map(int, input().split()))
S = set(A)
read = 0
while N >= 0:
    read += 1
    N -= 1 if read in S else 2
print(read - 1)
