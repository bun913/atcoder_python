"""
N人のうち身長がxj以上の生徒は何人か
Qが10**5なので、O(NQ)は間に合わない
2分探索で求める
"""
from bisect import bisect_left

N, Q = map(int, input().split())
A = list(map(int, input().split()))
AD = sorted(A)

for _ in range(Q):
    x = int(input())
    ind = bisect_left(AD, x)
    print(N-ind)
