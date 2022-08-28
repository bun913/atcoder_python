# -*- coding: utf-8 -*-
"""
Nが最大100
最初全ての花の高さは0
l以上r以下の全てのxに対して花xの高さを1高くする

見た感じ lとrの間隔をどんどん狭めていけばよい感じがする
"""
from itertools import groupby

N = int(input())
H = list(map(int, input().split()))

ideal = [k for k, _ in groupby(H)]
cur_list = [0 for _ in range(len(ideal))]

left = 0
ans = 0
while left <= len(ideal)-1:
    # すでに一番左が水をやる必要がない場合
    if cur_list[left] == ideal[left]:
        left += 1
        continue
    right = left
    # どこまで右をみるべきか調査
    for i in range(left, len(cur_list)):
        if cur_list[i] >= ideal[i]:
            break
        right = i
    # 現在の値を更新(水やり)
    for i in range(left, right+1):
        cur_list[i] += 1
    ans += 1
print(ans)
