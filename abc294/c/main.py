# -*- coding: utf-8 -*-
"""
解く前のメモ用
普通に指示通り連結しても問題なし
ただし配列でinとか使うと死ぬからそこは考える必要がある
"""
from collections import deque

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = A + B
C = sorted(C)

aq = deque(A)
bq = deque(B)

a_list = []
b_list = []
i = 0
while aq or bq:
    c = C[i]
    if not aq:
        bq.popleft()
        b_list.append(i+1)
        i += 1
        continue
    if not bq:
        aq.popleft()
        a_list.append(i+1)
        i += 1
        continue
    a = aq.popleft()
    b = bq.popleft()
    if a == c:
        a_list.append(i+1)
        # bを元に戻す
        bq.appendleft(b)
        i += 1
        continue
    if b == c:
        b_list.append(i+1)
        # aを元に戻す
        aq.appendleft(a)
        i += 1
        continue
print(*a_list, sep=" ")
print(*b_list, sep=" ")
