# -*- coding: utf-8 -*-
"""
解く前のメモ

全てのiに対して3倍はできず、どれか一つは2で割らないと操作ができないということ
つまり2で割れる回数がボトルネックになる
例えば何回3で掛け算をしたとしても2で割れる数が増えることはない
"""

N = int(input())
A = list(map(int, input().split()))

ans = 0

for i in range(N):
    while A[i] % 2 == 0:
        ans += 1
        A[i] = A[i] // 2
print(ans)
