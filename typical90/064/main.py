# -*- coding: utf-8 -*-
"""
N個の区間。標高はAi
地殻変動で標高がQ回変わるLからRまでV変わる

Nが最大で10**5で、LR間も最大同程度ある
毎回リストの要素を全て変更していたら間に合わないのではないかと思われる

数列の階差を考える
変わっていくのは実はL-1とRだけ
"""
N, Q = list(map(int, input().split()))
A = list(map(int, input().split()))
s = 0

B = [A[i+1] - A[i] for i in range(N-1)]
B.append(0)
ans = sum(map(abs, B))

for i in range(Q):
    L, R, V = list(map(int, input().split()))
    L -= 1
    R -= 1
    before = abs(B[L-1]) + abs(B[R])
    if L > 0:
        B[L-1] += V
    if R < N-1:
        B[R] -= V
    after = abs(B[L-1]) + abs(B[R])
    ans += after-before
    print(ans)
