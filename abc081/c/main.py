# -*- coding: utf-8 -*-
"""
解く前のメモ

ボールに書かれた数を変更して、ボールに書かれた数がK種類以下になるようにしたい
単純にボールの数が少ない順にソートして、K種類以下になるまで引いていけば良くね
"""
from collections import defaultdict
from operator import itemgetter

N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

memo = defaultdict(int)
for a in A:
    memo[a] += 1
sorted_memo = sorted(memo.items(), key=itemgetter(1))
cur_kinds = len(sorted_memo)
ans = 0

for k, v in sorted_memo:
    if cur_kinds <= K:
        print(ans)
        exit()
    ans += v
    cur_kinds -= 1
