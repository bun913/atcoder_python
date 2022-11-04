# -*- coding: utf-8 -*-
"""
N個の数。Nは偶数
i=1,2,...NからXiを除いたものの中央値をBiとする
中央値Biを求める
"""
from collections import deque

n = int(input())
x = list(map(int, input().split()))
q = deque(x)
pushq = deque([])
for i, x in enumerate(x):
    q = deque(q)
    rm = q.popleft()
    pushq.append(rm)
    if i != 0:
        q.append(pushq.popleft())
    t = sorted(q)
    print(t[len(t) // 2])
