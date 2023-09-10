# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
N = int(input())
A = list(map(int, input().split()))

# エッジケースは先に弾いておく
if N == 1:
    print(1)
    exit()

# 単調増加になっている区間を調べて、その区間の長さを調べれば良い
cur = 1
length_list = []
cur_length = 1

while cur < N:
    if A[cur] > A[cur - 1]:
        cur_length += 1
        cur += 1
        continue
    # 条件を満たさないならその区間の長さを記録して次の区間へ
    length_list.append(cur_length)
    cur_length = 1
    cur += 1
# 最後の区間の長さを記録
length_list.append(cur_length)

ans = 0
for l in length_list:
    ans += l * (l + 1) // 2
print(ans)
