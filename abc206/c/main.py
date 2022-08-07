"""
"""
from collections import Counter

N = int(input())
A = list(map(int, input().split()))

memo = Counter(A)

# 全部の組み合わせから条件を満たさないものを引いていく
ans = N * (N-1) // 2
for i in memo.values():
    ans -= (i * (i-1) // 2)
print(ans)
