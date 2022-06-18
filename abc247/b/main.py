# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用

全ての組み合わせを列挙する方法
list(0...8)から2つを抜き出す
list(combinations(l, 2))

bit全探索でフラグが立っているかチェックする
if ((i >> j) & 1)
"""
N = int(input())
s, t = [], []
for i in range(N):
    u, v = input().split()
    s.append(u)
    t.append(v)
for i in range(N):
    can_give_a_nickname = False
    for S in [s[i], t[i]]:
        s_ok = True
        for j in range(N):
            if i != j:
                if S == s[j] or S == t[j]:
                    s_ok = False
        if s_ok == True:
            can_give_a_nickname = True
    if can_give_a_nickname == False:
        print("No")
        exit()
print("Yes")
