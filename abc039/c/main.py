# -*- coding: utf-8 -*-
"""
ピアノの鍵盤の上に載せられているので自分がいる鍵盤音階を知りたい
12の色を繰り返している

たかだか20文字の入力しか与えられないなら先頭文字から順に右にずらしていく
先頭の文字がSと一致すれば何文字目からスタートかわかるので音階がわかる
"""
one_set = "WBWBWWBWBWBW"
sounds = ["Do", "", "Re", "", "Mi", "Fa", "", "So", "", "La", "", "Si"]
keyboards = one_set + one_set + one_set

S = input()

n = -1
for i in range(len(keyboards)):
    cur = keyboards[i:]
    if cur.startswith(S):
        n = i % 12
ans = sounds[n]
print(ans)
