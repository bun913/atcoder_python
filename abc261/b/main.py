# -*- coding: utf-8 -*-
"""
解く前のメモ

対戦表に矛盾がないかを調べる
辞書で対戦の結果を持っておいて、jのときにそれを参照させる感じか
人の番号: {対戦相手: 'W'} みたいな感じ?
"""

N = int(input())
memo = {}

A = [list(input()) for _ in range(N)]


def is_incorect(i_result: str, j_result: str):
    # 勝ち
    if i_result == 'W':
        if j_result == 'L':
            return True
        else:
            return False
    # 負け
    if i_result == 'L':
        if j_result == 'W':
            return True
        else:
            return False
    # 引き分け
    if i_result == 'D':
        if j_result == 'D':
            return True
        else:
            return False


# 辞書にそれぞれの結果を格納
for i in range(N):
    for j in range(N):
        # 同じなら飛ばす
        if i == j:
            continue
        result = A[i][j]
        # 辞書に結果がまだ格納されてない場合
        if i not in memo:
            memo[i] = {}
        if j not in memo[i]:
            memo[i][j] = result
            continue
ans = 'correct'

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        # 結果を比較する
        i_result = memo[i][j]
        j_result = memo[j][i]
        r = is_incorect(i_result, j_result)
        if r is False:
            print('incorrect')
            exit()
print(ans)
