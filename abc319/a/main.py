# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)

S = input()
tourist_dict = {
    'tourist': 3858,
    'ksun48': 3679,
    'Benq': 3658,
    'Um_nik': 3648,
    'apiad': 3638,
    'Stonefeang': 3630,
    'ecnerwala': 3613,
    'mnbvmar': 3555,
    'newbiedmy': 3516,
    'semiexp': 3481
}

print(tourist_dict[S])
