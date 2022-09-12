"""
各要素同士の2乗の和を求める

普通に全探索しようとするとNが10**5を超えるので間に合わない
解説AC
Aの全ての要素の差ではなく、Aがたかだか-200以上200以下なので全ての組み合わせを先に出しておけば良い
"""
from collections import Counter

N = int(input())
A = list(map(int, input().split()))
C = Counter(A)
C = [(a, b) for a, b in C.items()]

ans = 0
N = len(C)
for i in range(N):
    a1, b1 = C[i]
    for j in range(i + 1, N):
        a2, b2 = C[j]
        ans += (a1 - a2) ** 2 * (b1 * b2)
print(ans)
