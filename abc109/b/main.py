# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用

全ての組み合わせを列挙する方法
list(0...8)から2つを抜き出す
list(combinations(l, 2))

bit全探索でフラグが立っているかチェックする
if ((i >> j) & 1)
"""
N = int(input())
memo = set()

prev = ''

for i in range(N):
    s = input()
    if i == 0:
        memo.add(s)
        prev = s[-1]
        continue
    is_ok_rule1 = prev == s[0]
    is_ok_rule2 = s not in memo
    if is_ok_rule1 is True and is_ok_rule2 is True:
        memo.add(s)
        prev = s[-1]
        continue
    print('No')
    exit()
print('Yes')
