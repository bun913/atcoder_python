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
ans = 0


def is_acgt(s: str) -> bool:
    if s in set(['A', 'C', 'G', 'T']):
        return True
    return False


c_cnt = 0
for s in S:
    if is_acgt(s) is False:
        c_cnt = 0
        continue
    c_cnt += 1
    ans = max(c_cnt, ans)
print(ans)
