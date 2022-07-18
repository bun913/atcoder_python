# -*- coding: utf-8 -*-
"""
解く前のメモ

これまでの処理をした場合の最大値を持っていて、自分-1がそれより大きければアウト
"""

_max = -1
N = int(input())
A = list(map(int, input().split()))

R = A[::-1]
_min = R[0]

for i in range(N):
    cur = R[i]
    # これまでの最小値以下だったら気にせずによい
    if cur <= _min:
        _min = cur
        continue
    # 1引いてこれまでの最小値と同じだったら気にせずよいがminを更新
    if cur - 1 <= _min:
        _min = cur-1
        continue
    # 1引いてもこれまでの最小値より大きかったらアウト
    if cur - 1 > _min:
        print('No')
        exit()
print('Yes')
