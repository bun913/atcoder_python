# -*- coding: utf-8 -*-
"""
"""
from itertools import product
from collections import Counter

N, K = map(int, input().split())
S = [list(input()) for _ in range(N)]

ans = 0
for kumi in product([True, False], repeat=N):
    c = Counter()
    for i, is_use in enumerate(kumi):
        if is_use is False:
            continue
        s = S[i]
        to_set = set(s)
        c.update(to_set)
    k_cnts = [item for item, count in c.items() if count == K]
    ans = max(ans, len(k_cnts))

print(ans)
