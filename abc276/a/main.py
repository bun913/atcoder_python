# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
S = input()
if S.count("a") == 0:
    print(-1)
    exit()
print(S.rindex("a") + 1)
