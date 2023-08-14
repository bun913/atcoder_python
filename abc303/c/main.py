# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
N, M, H, K = map(int, input().split())
S = list(input())
XY = [tuple(map(int, input().split())) for _ in range(M)]
item_set = set(XY)

cur = (0, 0)
hp = H
for s in S:
    if s == "U":
        cur = (cur[0], cur[1] + 1)
    elif s == "D":
        cur = (cur[0], cur[1] - 1)
    elif s == "L":
        cur = (cur[0] - 1, cur[1])
    elif s == "R":
        cur = (cur[0] + 1, cur[1])
    # 体力を減らす
    hp -= 1
    # 体力が負になったらその時点で終了
    if hp < 0:
        print("No")
        exit()
    # アイテム使う必要があれば消費
    if cur in item_set:
        if max(K, hp) == K:
            hp = K
            item_set.remove(cur)
if hp >= 0:
    print("Yes")
    exit()
print("No")
