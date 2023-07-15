# -*- coding: utf-8 -*-
"""
SにはN個の文字列が入っている
Nは最大で2*10**5個ある
でSも最大の長さが10**5ある
S[i]の要素を左右反転させて同じ文字列がSの中にあれば1種類としてカウントする
このSの中にある種類数を求める
"""
N = int(input())
S = set()
for _ in range(N):
    s = input()
    l = list(s)
    rl = list(reversed(l))
    r = "".join(rl)
    if s not in S and r not in S:
        S.add(s)
print(len(S))
