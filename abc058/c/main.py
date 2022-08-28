# -*- coding: utf-8 -*-
"""
どの文字列が書かれていても作れる文字列のうち最長のもの
複数ある場合は辞書順で最小のもの

各文字列が共通して何回出現しているか数えればよし
"""
from itertools import groupby

n = int(input())

# まず全ての文字列に共通して出現している文字列を列挙する
s_list = [input() for _ in range(n)]
commons = set(list(s_list[0]))
for S in s_list:
    to_set = set(list(S))
    commons = commons.intersection(to_set)

# 各文字列の共通文字列の出現回数を数える
memo = dict()
for S in s_list:
    grouped = [(k, len(list(g))) for k, g in groupby(sorted(list(S)))]
    for k, length in grouped:
        if k not in commons:
            continue
        if k not in memo:
            memo[k] = length
            continue
        memo[k] = min(memo[k], length)
ans_list = []
for k, length in memo.items():
    ans_list.append(k * length)
ans = ''.join(ans_list)
print(ans)
