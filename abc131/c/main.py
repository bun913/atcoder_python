# -*- coding: utf-8 -*-
"""
解く前のメモ

A以上B以下の整数のうちCでもDでも割り切れないものの個数を求める
普通ならA以上B以下のの数を1こづつ列挙して、割り切れるか試していくが
今回はA,Bが最大で10**18なのでlog2にしても間に合わないという（約数列挙かと思った)

ベン図を書けば一発だった。
A以上B以下の数を集合の全体として
(c or bで割れるもの -  c and d で割れるもの)
↑を全体から引いてやれば残りの数が答え
"""
from math import gcd


def lcm(a, b):
    return (a * b) // gcd(a, b)


A, B, C, D = list(map(int, input().split()))


# 集合を求める
set_all = (B-A) + 1
# CとDでたまたま同じ数が出ることがある
set_c = (B // C) - ((A-1) // C)
set_d = (B // D) - ((A-1) // D)
lc = lcm(C, D)
set_c_and_d = (B // lc) - ((A-1) // lc)

ans = set_all - (set_c + set_d - set_c_and_d)
print(ans)
