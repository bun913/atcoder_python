# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from collections import deque

q = deque([])
S = input()

for s in S:
    if s == "B":
        if q:
            q.pop()
        continue
    q.append(s)
ans = "".join(list(q))
print(ans)
