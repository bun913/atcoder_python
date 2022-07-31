# -*- coding: utf-8 -*-
"""
解く前のメモ

普通にやるならiとjをそれぞれ二重ループで全探索
だが、Nが10**5まであるのでi<jとなる組を数えるとTLE
"""

N = int(input())
A = list(map(int, input().split()))

# まず全てのくみをみてみる
for i in range(N):
    for j in range(i+1, N):
        a = A[i]
        b = A[j]
        if min(a, b) == i+1 and max(a, b) == j + 1:
            print(i+1, j+1)

# asc_set = set()
# desc_set = set()

# AR = A[::-1]

# for i in range(N):
#     if i+1 == A[i]:
#         asc_set.add(i+1)

# for i in range(N):
#     if i + 1 == AR[i]:
#         desc_set.add(i+1)
# print(asc_set)
# print(desc_set)
