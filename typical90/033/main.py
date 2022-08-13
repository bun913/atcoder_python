# -*- coding: utf-8 -*-
"""
解く前のメモ

不適切: 縦2,横2の4つのLEDを含む領域で点灯しているLEDが領域内に2つい上あるものが存在する
適切なイルミのパターンのうち点灯しているLEDの個数としてありえる最大値

i,jが両方とも奇数のところに点灯できる
"""
from math import ceil

H, W = list(map(int, input().split()))
if H == 1 or W == 1:
    print(H*W)
    exit()
ans = ceil(H/2) * ceil(W/2)
print(ans)
