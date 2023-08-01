# -*- coding: utf-8 -*-
"""
解く前のメモ用
MEX・・・与えられた集合に含まれない最小の非負整数
要するにMEXを最大にするには0から数を連鎖させていくしかない
K個選ぶまでに選べない数字があればそれが答えになる
逆にK個まで選べてしまったらそれが答えになる
Mexの場合数字が多いほど大きくなる可能性がある
数列のどれかを消した結果Mexが大きくなるということはない
K個まで連続の数を数え続けると考えれば、答えは最大でもKとなる
"""
N, K = map(int, input().split())
A = list(map(int, input().split()))
s = set(A)
for i in range(K):
    if i not in s:
        print(i)
        exit()
print(K)
