# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用

全ての組み合わせを列挙する方法
list(0...8)から2つを抜き出す
list(combinations(l, 2))

bit全探索でフラグが立っているかチェックする
if ((i >> j) & 1)
"""
# ボールが跳ねる回数
# Xが10,000が最大なので素直にループで数え上

N, X = list(map(int, input().split()))
L = list(map(int, input().split()))
# 跳ねるポイントを配列で持っておく
D = [0]
for i in range(1, len(L)+1):
    d = D[i-1] + L[i-1]
    D.append(d)

ans_list = [d for d in D if d <= X]
print(len(ans_list))
