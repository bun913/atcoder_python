# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用

全ての組み合わせを列挙する方法
list(0...8)から2つを抜き出す
list(combinations(l, 2))

bit全探索でフラグが立っているかチェックする
if ((i >> j) & 1)
"""
# Aがたかだか1000以下と決まっているので全部調べれば良い
N = int(input())
A = list(map(int, input().split()))

max_cnt = 0
ans = 0
for k in range(2, 1001):
    cnt = 0
    for a in A:
        if a % k == 0:
            cnt += 1
    if cnt >= max_cnt:
        max_cnt = cnt
        ans = k
print(ans)
