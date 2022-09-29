"""
N個のキャンディ
色が最大10**9個
連続して並んだキャンディをK個もらえる
"""
from collections import defaultdict

N, K = list(map(int, input().split()))
C = list(map(int, input().split()))
memo = defaultdict(int)
for i in range(K):
    memo[C[i]] += 1
ans = len(set(memo))

for i in range(K, N):
    memo[C[i]] += 1
    memo[C[i - K]] -= 1
    if memo[C[i - K]] <= 0:
        del memo[C[i - K]]
    ans = max(ans, len(memo))
print(ans)
