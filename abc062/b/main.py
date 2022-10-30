# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
H, W = list(map(int, input().split()))
A = [list(input()) for _ in range(H)]
for i in range(H):
    A[i].insert(0, "#")
    A[i].append("#")
A.append(["#"] * (W + 2))
A.insert(0, ["#"] * (W + 2))
for i in range(len(A)):
    print(*A[i], sep="")
