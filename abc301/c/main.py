# -*- coding: utf-8 -*-
"""
まずSとTで同じ文字があったらそれらを消滅させてよい
"""
from collections import defaultdict
from string import ascii_lowercase as lowercase

can_changes = set(['a', 't', 'c', 'o', 'd', 'e', 'r'])

S = list(input())
s_dict = defaultdict(int)
t_dict = defaultdict(int)
[s_dict.update({s: s_dict[s] + 1}) for s in S]
[t_dict.update({s: t_dict[s] + 1}) for s in input()]

s_at_cnt = s_dict['@']
t_at_cnt = t_dict['@']

ans = True
# 英小文字を全列挙してS,Tの文字を対消滅させていく
for s in lowercase:
    s_cnt = s_dict[s]
    t_cnt = t_dict[s]
    # 文字が余った時に、文字列が can_changes に含まれていなければダメ
    if s_cnt != t_cnt and s not in can_changes:
        ans = False
        break

    # S,Tの文字を対消滅させて残った個数分文字@を削る
    if s_cnt > t_cnt:
        t_at_cnt -= (s_cnt - t_cnt)
    else:
        s_at_cnt -= (t_cnt - s_cnt)

if s_at_cnt < 0 or t_at_cnt < 0:
    ans = False

print("Yes" if ans is True else "No")
