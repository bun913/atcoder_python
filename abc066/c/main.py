# -*- coding: utf-8 -*-
"""
操作をn回行う
数列のi番目の要素aiをbの末尾に追加する

dequeで交互に入れ替え
"""
from collections import deque

N = int(input())
A = list(map(int, input().split()))
B = deque()

for i, a in enumerate(A):
    if i % 2 == 0:
        B.appendleft(a)
        continue
    B.append(a)
if N % 2 != 0:
    print(*B, sep=" ")
    exit()
print(*reversed(B), sep=" ")
