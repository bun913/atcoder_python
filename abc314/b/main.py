# -*- coding: utf-8 -*-
"""
人がかけた目がわかる
それに対して最終的に当たった目を持っている人を取得
かけたコマの数が少ない人から順に出力する
Cがたかだが37だからsetにしなくても良さそう
"""
from sys import setrecursionlimit

setrecursionlimit(10**7)

N = int(input())
memo = {}
for i in range(N):
    C = int(input())
    A = list(map(int, input().split()))
    memo[i+1] = set(A)
X = int(input())

# Xを持っている人を取得
cand_list = []
min_cnt = 10**20
for man, numbers in memo.items():
    if X in numbers:
        cand_list.append((man, len(numbers)))
        min_cnt = min(min_cnt, len(numbers))
# まずコマの数でソート
cand_list.sort(key=lambda x: x[1])
# 次に人の番号でソート
cand_list.sort(key=lambda x: x[0])
ans_list = [man for man, cnt in cand_list if cnt == min_cnt]
print(len(ans_list))
print(*ans_list)
