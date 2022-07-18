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
memo = {}

for s in S:
    if s in memo:
        memo[s] += 1
        continue
    memo[s] = 1

kinds = len(memo)
is_two = True

for v in memo.values():
    if v != 2:
        is_two = False
        break

ans = 'No'

if kinds == 2 and is_two is True:
    ans = 'Yes'

print(ans)
