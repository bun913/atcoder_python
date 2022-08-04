# -*- coding: utf-8 -*-
"""
解く前のメモ

実はX,pが全て100以下の数字であるので全部数えても間に合う
"""
X, N = list(map(int, input().split()))
P = list(map(int, input().split()))
p_set = set(P)

ans = 105
diff = 800
for y in range(0, 102):
    d = abs(y-X)
    if d < diff and y not in p_set:
        ans = y
        diff = d
print(ans)
