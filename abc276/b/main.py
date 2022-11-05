# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
N, M = list(map(int, input().split()))
C = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = list(map(int, input().split()))
    C[a].append(b)
    C[b].append(a)
for i in range(1, N + 1):
    if len(C[i]) == 0:
        print(0)
        continue
    # sortedをstrでしたらだめ
    t = sorted(C[i])
    ans = " ".join(map(str, t))
    print("{} {}".format(len(C[i]), ans))
