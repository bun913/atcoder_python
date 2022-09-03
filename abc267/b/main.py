# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用

全ての組み合わせを列挙する方法
list(0...8)から2つを抜き出す
list(combinations(l, 2))

bit全探索でフラグが立っているかチェックする
if ((i >> j) & 1)
"""
S = list(map(int, list(input())))
pins = [[-1, -1, 2, 1, 3, -1, -1], [7, 4, 8, 5, 9, 6, 10]]

# ピン1が倒れていないのは早めにアウトにする
if S[0] == 1:
    print("No")
    exit()

# 倒しているピンのメモ
for i, s in enumerate(S):
    pin = i + 1
    is_layed = True if s == 0 else False
    for j in range(7):
        cand1 = pins[0][j]
        cand2 = pins[1][j]
        if is_layed is False:
            continue
        if cand1 == pin:
            pins[0][j] = 0
        if cand2 == pin:
            pins[1][j] = 0

standed = []
all_layed = []
for i in range(7):
    col1 = pins[0][i]
    col2 = pins[1][i]
    # 立っているピンがあるか調べる
    if col1 not in (0, -1) or col2 not in (0, -1):
        standed.append(i)
    # 全て倒れている列か調べる
    if col1 in (0, -1) and col2 in (0, -1):
        all_layed.append(i)

# print(pins, standed, all_layed)

if len(standed) < 2:
    print("No")
    exit()
if len(all_layed) <= 0:
    print("No")
    exit()
_min = min(standed)
_max = max(standed)

for i in all_layed:
    if i > _min and i < _max:
        print("Yes")
        exit()
print("No")
