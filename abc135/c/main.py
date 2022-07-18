# -*- coding: utf-8 -*-
"""
解く前に考えたこと

どうもこうも今の街の数を減らし切って、余ったら次の街の数を減らすだけなのでは
"""

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0
for i in range(N):
    cur_town = A[i]
    nex_town = A[i+1]
    attack = B[i]
    if cur_town >= attack:
        ans += attack
        A[i] -= attack
        continue
    ans += cur_town
    rest = attack - cur_town
    A[i] = 0
    if nex_town >= rest:
        ans += rest
        A[i+1] -= rest
        continue
    ans += nex_town
    A[i+1] -= nex_town

# 数え上げ
print(ans)
