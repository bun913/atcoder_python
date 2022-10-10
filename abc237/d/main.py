# -*- coding: utf-8 -*-
from collections import deque

N = int(input())
S = input()
L = deque()
R = deque()
ans = deque([0])
for i, c in enumerate(S):
    if c == "L":
        R.appendleft(i)
    else:
        L.append(i)
print(*list(list(L) + [N] + list(R)))
