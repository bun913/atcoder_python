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
# 各列でピンが1つでも立っているか、立っていないかを判定するためのリスト
# 1が列に立っているピンがある・0が立っているピンが無い状態を表す
cols = [1 for _ in range(7)]

# 1番目のピンが立っているか判定
if S[0] == 1:
    print("No")
    exit()

# 同じ列に立っているピンの組と何列目かをタプルで表現# (前のピン番号, 後ろのピン番号, 列番号)
combi_list = [(2, 8, 3), (1, 5, 4), (3, 9, 5)]
for combi in combi_list:
    front, back, col_num = combi
    if S[front - 1] == 0 and S[back - 1] == 0:
        cols[col_num - 1] = 0
        continue
    cols[col_num] = 1

# ピン番号: 列番号のマップ(リストで扱いやすいように全て-1)
pin_col_map = {7: 1, 4: 2, 6: 6, 10: 7}
for i, v in enumerate(S):
    # 2ピンある列は上で確認済みなので飛ばす
    if i + 1 in set([2, 8, 1, 5, 3, 9]):
        continue
    col_num = pin_col_map[i + 1]
    cols[col_num - 1] = v

stand_cols, down_cols = ([], [])
for i, v in enumerate(cols):
    if v == 1:
        stand_cols.append(i)
        continue
    down_cols.append(i)

if len(stand_cols) < 2 or len(down_cols) <= 0:
    print("No")
    exit()

# 立っているピンがある列の最小値・最大値を算出
_min_stand = min(stand_cols)
_max_stand = max(stand_cols)
# 立っているピンとピンの間に全て倒れている列があればスプリット状態
for down_col in down_cols:
    if down_col > _min_stand and down_col < _max_stand:
        print("Yes")
        exit()
print("No")
