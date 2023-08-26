# -*- coding: utf-8 -*-
"""
バケツソートの考え方を使う
今回だとaがたかだか10**5であるのに注目
aの値をインデックスとする配列を用意してあげて、それぞれの配列の要素数をカウントすれば良い
"""
N, K = map(int, input().split())
counts = [0 for _ in range(10**5+1)]

for _ in range(N):
    a, b = map(int, input().split())
    counts[a] += b

cur_cnt = 0
for num, cnt in enumerate(counts):
    cur_cnt += cnt
    if cur_cnt >= K:
        print(num)
        break
