# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用

全ての組み合わせを列挙する方法
list(0...8)から2つを抜き出す
list(combinations(l, 2))

bit全探索でフラグが立っているかチェックする
if ((i >> j) & 1)
"""
S = input()

cond1 = S[0] == 'A'
extract = S[2:-1]
cond2 = extract.count('C') == 1

if cond1 is False or cond2 is False:
    print('WA')
    exit()

# 条件3の判定
for i in range(len(S)):
    s = S[i]
    if i == 0:
        continue
    if 2 <= i <= len(S)-2:
        if s == 'C':
            continue
    if s.isupper() is True:
        print('WA')
        exit()
print('AC')
