# -*- coding: utf-8 -*-
"""
解く前のメモ

乱暴だけど全ての数の組み合わせを出してそれから単調増加の分だけ出力する?
"""
from itertools import combinations

N, M = list(map(int, input().split()))
cand_nums = [i for i in range(1, M+1)]
cands = list(combinations(cand_nums, N))

for cand in cands:
    print(*cand, end=' \n')
