# -*- coding: utf-8 -*-
"""
縦・横・ななめのいずれかの方向に連続してsunukeの文字が並んでいる場所が1個だけある
それらの場所を5行分出力する
"""
H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

# snukeの出現場所をメモる
memo = {}

for i in range(H):
    for j in range(W):
        if S[i][j] == 's':
            if "s" not in memo:
                memo["s"] = set([(i, j)])
            else:
                memo["s"].add((i, j))
        if S[i][j] == 'u':
            if "u" not in memo:
                memo["u"] = set([(i, j)])
            else:
                memo["u"].add((i, j))
        if S[i][j] == 'n':
            if "n" not in memo:
                memo["n"] = set([(i, j)])
            else:
                memo["n"].add((i, j))
        if S[i][j] == 'k':
            if "k" not in memo:
                memo["k"] = set([(i, j)])
            else:
                memo["k"].add((i, j))
        if S[i][j] == 'e':
            if "e" not in memo:
                memo["e"] = set([(i, j)])
            else:
                memo["e"].add((i, j))

for i, j in memo["s"]:
    # 横方向にnukeが並んでいるか
    if (i, j+1) in memo["n"] and (i, j+2) in memo["u"] and (i, j+3) in memo["k"] and (i, j+4) in memo["e"]:
        for k in range(5):
            print(i+1, j+k+1)
        exit()
    # マイナスの横方向にnukeが並んでいるか
    if (i, j-1) in memo["n"] and (i, j-2) in memo["u"] and (i, j-3) in memo["k"] and (i, j-4) in memo["e"]:
        for k in range(5):
            print(i+1, j-k+1)
        exit()
    # 縦方向にnukeが並んでいるか
    if (i+1, j) in memo["n"] and (i+2, j) in memo["u"] and (i+3, j) in memo["k"] and (i+4, j) in memo["e"]:
        for k in range(5):
            print(i+k+1, j+1)
        exit()
    # マイナスの縦方向にnukeが並んでいるか
    if (i-1, j) in memo["n"] and (i-2, j) in memo["u"] and (i-3, j) in memo["k"] and (i-4, j) in memo["e"]:
        for k in range(5):
            print(i-k+1, j+1)
        exit()
    # 右下斜め方向にnukeが並んでいるか
    if (i+1, j+1) in memo["n"] and (i+2, j+2) in memo["u"] and (i+3, j+3) in memo["k"] and (i+4, j+4) in memo["e"]:
        for k in range(5):
            print(i+k+1, j+k+1)
        exit()
    # 左下斜め方向にnukeが並んでいるか
    if (i+1, j-1) in memo["n"] and (i+2, j-2) in memo["u"] and (i+3, j-3) in memo["k"] and (i+4, j-4) in memo["e"]:
        for k in range(5):
            print(i+k+1, j-k+1)
        exit()
    # 右上斜め方向にnukeが並んでいるか
    if (i-1, j+1) in memo["n"] and (i-2, j+2) in memo["u"] and (i-3, j+3) in memo["k"] and (i-4, j+4) in memo["e"]:
        for k in range(5):
            print(i-k+1, j+k+1)
        exit()
    # 左上斜め方向にnukeが並んでいるか
    if (i-1, j-1) in memo["n"] and (i-2, j-2) in memo["u"] and (i-3, j-3) in memo["k"] and (i-4, j-4) in memo["e"]:
        for k in range(5):
            print(i-k+1, j-k+1)
        exit()
