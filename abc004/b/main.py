# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
C = [input().split() for _ in range(4)]
for r in reversed(C):
    print(*reversed(r))
