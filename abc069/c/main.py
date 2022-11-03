# -*- coding: utf-8 -*-
"""
Aの要素を自由に並び替える
a[i]とa[i+1]の積が4の倍数になる
- 4の倍数には何をかけてもOK
- 2の倍数と2の倍数のペアはOK
"""
from functools import reduce

N = int(input())
A = list(map(int, input().split()))
cnt_four, cnt_even, others = 0, 0, 0
for a in A:
    if a % 2 == 0 and a % 4 != 0:
        cnt_even += 1
    elif a % 4 == 0:
        cnt_four += 1
    else:
        others += 1
# 4の倍数の数が奇数以上の場合Ok
if others <= cnt_four:
    print("Yes")
    exit()
# 4の倍数ではない2の倍数がない場合
if others + cnt_four == N:
    if cnt_four + 1 == others:
        print("Yes")
        exit()
print("No")
