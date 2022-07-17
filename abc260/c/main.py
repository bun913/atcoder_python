# -*- coding: utf-8 -*-
"""
解く前のメモ
木の構造でひたすら増えていく

解説見てから
なるほど木構造をそのまま再起関数で表すという手があるのか
分かれる木構造をそのまま再起関数2つで表すというテクニックがすごい

bit全探索でフラグが立っているかチェックする
if ((i >> j) & 1)
"""

N, X, Y = list(map(int, input().split()))


def calc(level, is_red):
    # 再起終了の条件
    if level == 1:
        return 0 if is_red is True else 1
    # 赤の木構造の場合、青のレベルが同じやつをX個分返すのを忘れないように
    if is_red:
        return calc(level-1, True) + (calc(level, False)) * X
    # 青の木構造の場合、青のレベル1こさげたのをY個分返すのを忘れないように
    return calc(level-1., True) + (calc(level-1, False)) * Y


print(calc(N, True))
