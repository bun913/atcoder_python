# -*- coding: utf-8 -*-
"""
解く前のメモ

8新法の数字を9新法にして、8を5に描き直す
最後に出てくるKを8新法で出力する
Kが100,Nが20桁くらいなので操作はできそう
折角ライブラリがあるから使おうスタイル
"""
from numpy import base_repr

N, K = list(map(int, input().split()))

cur = int(str(N), 8)
for i in range(K):
    nine_base = base_repr(cur, 9)
    replaced = nine_base.replace('8', '5', len(nine_base))
    if i != K-1:
        cur = int(replaced, 8)
    else:
        cur = int(replaced)
print(cur)
