# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
A, B, C = list(map(int, input().split()))
can_plus = A + B == C
can_minus = A - B == C
if can_plus is True and can_minus is True:
    print("?")
elif can_plus is True:
    print("+")
elif can_minus is True:
    print("-")
else:
    print("!")
