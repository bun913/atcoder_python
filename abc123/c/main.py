# -*- coding: utf-8 -*-
"""
解く前のメモ

なんかいかにも、グループが関係してそうだなと思った
それで各都市を回って、グループ数が最大になるところがボトルネックっぽいなと思った

それでテストケースに当てはめてみたら全部通った
"""

N = int(input())
cap_list = [int(input()) for _ in range(5)]

max_group_cnt = -1
for cap in cap_list:
    q = N // cap
    rest = N % cap
    group_cnt = q
    if rest > 0:
        group_cnt += 1
    max_group_cnt = max(max_group_cnt, group_cnt)

ans = 5 + (max_group_cnt - 1)
print(ans)
