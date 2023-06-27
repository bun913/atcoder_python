# -*- coding: utf-8 -*-
"""
これも今が反対の状態か管理しながら、文字列を追加する方向を考えれば良い
"""
from collections import deque

S = input()
Q = int(input())
q = deque(list(S))

is_reverse = False
for _ in range(Q):
    query = input().split()
    # 反転させる場合
    if query[0] == '1':
        is_reverse = not is_reverse
        continue
    f = query[1]
    c = query[2]
    if f == '1':
        if is_reverse is True:
            q.append(c)
            continue
        q.appendleft(c)
    else:
        if is_reverse is True:
            q.appendleft(c)
            continue
        q.append(c)
if is_reverse is True:
    print(*list(q)[::-1], sep='')
    exit()
print(*list(q), sep='')
