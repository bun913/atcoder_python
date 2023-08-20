# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
S = list(input())
no_use = set(['a', 'i', 'u', 'e', 'o'])
f = filter(lambda x: x not in no_use, S)
print(*f, sep="")
