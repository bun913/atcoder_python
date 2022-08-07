# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用

全ての組み合わせを列挙する方法
list(0...8)から2つを抜き出す
list(combinations(l, 2))

bit全探索でフラグが立っているかチェックする
if ((i >> j) & 1)
"""
A, B = list(map(int, input().split()))
S = input()


def is_int(s: str) -> bool:
    cand = set([str(i) for i in range(0, 10)])
    if s in cand:
        return True
    return False


if len(S) != A + B + 1:
    print('No')
    exit()

for i in range(len(S)):
    s = S[i]
    # A+1文字目がハイフンか
    if i == A:
        if s != '-':
            print('No')
            exit()
        else:
            continue
    # それ以外は全て数値になる
    if is_int(s) is False:
        print('No')
        exit()
print('Yes')
