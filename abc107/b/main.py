# -*- coding: utf-8 -*-
"""
解く前のメモ

まず各行をみて、消すべき行を数える
次に各列を見て、消すべき列を数える

というふうに繰り返していって、消せるものがなくなれば終了とする
"""
import numpy as np

H, W = list(map(int, input().split()))
A = [list(input()) for _ in range(H)]


def extra_delete_row_numbers(rows):
    remove_rows = []
    for i in range(len(rows)):
        row = rows[i]
        should_remove = True if row.count('.') == len(row) else False
        if should_remove is True:
            remove_rows.append(i)
    return remove_rows


def extra_delete_col_numbers(rows):
    remove_cols = []
    for i in range(len(rows[0])):
        cols = [row[i] for row in rows]
        cols = list(cols)
        shold_remoe = True if cols.count('.') == len(cols) else False
        if shold_remoe is True:
            remove_cols.append(i)
    return remove_cols


# 少々オーバーキルではあるが確実にこれ以上消せない数だけ繰り返す
for i in range(H+W):
    # 行の削除
    del_rows = extra_delete_row_numbers(A)
    for i in del_rows[::-1]:
        A.pop(i)
    # 列の削除
    del_cols = extra_delete_col_numbers(A)
    for i in del_cols[::-1]:
        for j in range(len(A)):
            A[j].pop(i)

for i in range(len(A)):
    print(*A[i], sep='')
