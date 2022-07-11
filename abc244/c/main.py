# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用

全ての組み合わせを列挙する方法
list(0...8)から2つを抜き出す
list(combinations(l, 2))

bit全探索でフラグが立っているかチェックする
if ((i >> j) & 1)
"""
from sys import stdout

N = int(input())
cand = set([i for i in range(1, 2*N + 2)])

# 最初の出力
print(cand.pop())
stdout.flush()

# あとは繰り返し
while True:
    a = int(input())
    if a == 0:
        break
    cand.remove(a)
    t = cand.pop()
    print(t)
    stdout.flush()
