# -*- coding: utf-8 -*-
A, B, K = list(map(int, input().split()))
cand1 = set([i for i in range(A, A+K) if i <= B])
cand2 = set([i for i in range(B, B-K, -1) if A <= i])
ans = sorted(list(cand1.union(cand2)))

for a in ans:
    print(a)
