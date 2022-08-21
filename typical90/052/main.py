# -*- coding: utf-8 -*-
N = int(input())
ans = 1
for i in range(N):
    A = list(map(int, input().split()))
    s = sum(A)
    ans *= s
    ans %= 10 ** 9 + 7
print(ans)
