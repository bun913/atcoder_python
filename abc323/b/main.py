# -*- coding: utf-8 -*-
"""
解く前のメモ用
N人の総当たり。必ずどっちかが勝つか負ける。
oのときプレイヤーiがjに勝ち
買った試合が同じならプレイヤー番号が若い方が強い
結果を順番に出力する

WIP
あとでバケットソートの解き方で解く
勝ち数の配列を作って、そこにプレイヤー番号を入れていく
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    N = int(input())
    S = [input() for _ in range(N)]
    memo = [[i, 0] for i in range(N)]
    calc(S, memo)
    s_memo = sorted(memo, key=lambda x: x[1], reverse=True)
    ans = [s[0]+1 for s in s_memo]
    print(*ans)


def calc(S, memo) -> None:
    for i in range(len(S)):
        si = S[i]
        for s in si:
            if s == 'o':
                memo[i][1] += 1


solve()
