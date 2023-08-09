"""
"""
from collections import deque

N = int(input())
T = list(map(int, input().split()))
L = sorted(T, reverse=True)
q = deque(L)

o1 = []
o2 = []

cur1 = 0
cur2 = 0
while q:
    t = q.popleft()
    if cur1 <= cur2:
        o1.append(t)
        cur1 += t
    else:
        o2.append(t)
        cur2 += t
ans = max(cur1, cur2)
print(ans)
