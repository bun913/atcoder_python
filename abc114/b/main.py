# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用

全ての組み合わせを列挙する方法
list(0...8)から2つを抜き出す
list(combinations(l, 2))

bit全探索でフラグが立っているかチェックする
if ((i >> j) & 1)
"""
S = input()
ans = float('inf')

for i in range(len(S)-2):
    s = S[i:i+3]
    num = int(s)
    ans = min(ans, abs(num-753))
print(ans)
