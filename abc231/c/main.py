# -*- coding: utf-8 -*-
"""
N人のうち身長がxj以上の生徒は何人か

普通に考えるならばQ回のループの中で、それぞれN人をfilterにかけて何人いるか数える方法
ただ、これだとN,Qがそれぞれ最大で2*10**5であるため二重ループにしたら間に合わないと思われる

なのであらかじめAをソートしておく
あとは目的となる値を二部探索で求めれば良いだけ
pythonならbisectというライブラリがある
"""
from bisect import bisect_left

N, Q = list(map(int, input().split()))
A = list(map(int, input().split()))
AD = sorted(A)

for j in range(Q):
    x = int(input())
    i = bisect_left(AD, x)
    print(N-i)
