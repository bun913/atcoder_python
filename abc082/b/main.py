# -*- coding: utf-8 -*-
"""
解く前のメモ

s,tの長さが100文字なので全て並び替えるのは無理100の階乗になる
ここで言っているのはs_dash < t_dash とできるか判定しろと言っているだけ
ということはs_dashを可能な限り辞書順で早く,t_dashを可能な限り辞書順で遅くすれば良いだけでは
"""
s = input()
t = input()

sd = sorted(s)
td = sorted(t, reverse=True)

ans = 'Yes' if ''.join(sd) < ''.join(td) else 'No'
print(ans)
