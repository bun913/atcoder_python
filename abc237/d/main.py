# -*- coding: utf-8 -*-
from collections import deque

N = int(input())
S = input()
ans = deque([N])

for i in range(N - 1, -1, -1):
    s = S[i]
    if s == "R":
        ans.appendleft(i)
    else:
        ans.append(i)
print(*ans)
