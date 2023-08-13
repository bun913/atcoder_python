# -*- coding: utf-8 -*-
"""
Sの各文字について位置が変わるのは1回ずつ
書く数字の出現位置を覚えておけばずらしていくだけで良さそう
"""
N, M = map(int, input().split())
S = list(input())
C = list(map(int, input().split()))
# Sのi番目の位置を記録する配列
indexes = [i for i in range(N)]
# 1..Nまでの出現位置を記録する
number_map = dict()
for i, c in enumerate(C):
    if c in number_map:
        number_map[c].append(i)
        continue
    number_map[c] = [i]
# indexをずらしていく
for num, cur_index_list in number_map.items():
    cnt = len(cur_index_list)
    for i, ind in enumerate(cur_index_list):
        indexes[ind] = cur_index_list[(i+1) % cnt]
ans_list = S[:]
for i, ind in enumerate(indexes):
    ans_list[ind] = S[i]
print(*ans_list, sep="")
