# -*- coding: utf-8 -*-

"""
解く前のメモ

先頭につけることしかできない
また、回文にできるかどうか判定するだけでよい
つまり逆から見ていって、aが連続してある数を数える。
足りないaを先頭につける。
その分が回文かどうか判定するだけでよいんじゃね
"""

S = input()

ba_cnt = 0
# 後ろに何文字aがついているかカウント
for s in S[::-1]:
    if s != 'a':
        break
    ba_cnt += 1

fa_cnt = 0
for s in S:
    if s != 'a':
        break
    fa_cnt += 1

add_cnt = max(ba_cnt-fa_cnt, 0)

added = 'a' * add_cnt + S
reverse = added[::-1]

ans = 'No'
if added == reverse:
    ans = 'Yes'

print(ans)
