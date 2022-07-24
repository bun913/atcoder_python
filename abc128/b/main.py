# -*- coding: utf-8 -*-
"""
解く前のメモ

- 得点を大きい方からsort
- 市名を小さい方からsort
"""
from operator import itemgetter

N = int(input())
memo = []

for i in range(N):
    name, score = input().split(' ')
    score = int(score)
    memo.append({'name': name, 'score': score, 'i': i+1})

scored_sorted = sorted(memo, key=itemgetter('score'), reverse=True)
name_sorted = sorted(scored_sorted, key=itemgetter('name'))

ig = itemgetter('i')
[print(ig(dic)) for dic in name_sorted]
