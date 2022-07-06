# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用

全ての組み合わせを列挙する方法
list(0...8)から2つを抜き出す
list(combinations(l, 2))

bit全探索でフラグが立っているかチェックする
if ((i >> j) & 1)
"""
from functools import reduce, lru_cache
from itertools import combinations
import math

# 正当数ACを1会以上出した問題の数(setで十分かな)
# ACを1回以上出した問題において、初めてACを出すまでに出したWAの総和
# ACを1回以上出した各問題において、初めてACを出すまでに出したWAの総和

N, M = list(map(int, input().split()))
ac_set = set()
wc_cnt_dic = dict([(str(i), 0) for i in range(1, N+1)])

for i in range(M):
    p, S = input().split(' ')
    # ACの場合はsetで管理
    if S == 'AC':
        ac_set.add(p)
        continue
    # wc_cntに加えるのはまだACを出していない問題のみ
    if p not in ac_set:
        wc_cnt_dic[p] += 1

wc_sum = 0
# wc数の数え上げ
for acp in ac_set:
    wc_sum += wc_cnt_dic[acp]
print(len(ac_set), wc_sum)
