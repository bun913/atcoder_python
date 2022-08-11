"""
解く前のメモ

N,Mが最大で10**5なので全探索はできない
正の整数というのがポイントな気がする
Aの方は固定にして、片方は二部探索で探せば間に合うのでは
"""
from bisect import bisect_left

N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
bd = sorted(B)

ans = float('inf')

for i in range(N):
    a = A[i]
    ind1 = bisect_left(bd, a)
    # 手前の要素があれば比べる
    if ind1-1 >= 0:
        cand = abs(a-bd[ind1-1])
        ans = min(ans, cand)
    # 挿入位置の要素があれば比べる
    if ind1 < M:
        cand = abs(a-bd[ind1])
        ans = min(ans, cand)
print(ans)
