# -*- coding: utf-8 -*-
"""
解く前のメモ

YYMMしか考えらえれないとは
MMの条件 01 ~ 12のどれか
YYの条件: 特になし
"""


def is_mm_format(s: str):
    cand = set(['01', '02', '03', '04', '05', '06', '06',
                '07', '08', '09', '10', '11', '12', ])
    if s in cand:
        return True
    return False


def is_na(l: str, r: str):
    if is_mm_format(l) is False and is_mm_format(r) is False:
        return True
    return False


def is_yymm(l: str, r: str):
    if is_mm_format(l) is False and is_mm_format(r) is True:
        return True
    return False


def is_mmyy(l: str, r: str):
    if is_mm_format(l) is True and is_mm_format(r) is False:
        return True
    return False


def is_ambigous(l: str, r: str):
    if is_mm_format(l) is True and is_mm_format(r) is True:
        return True
    return False


S = input()
l = S[:2]
r = S[2:]


if is_na(l, r) is True:
    print('NA')
    exit()

if is_yymm(l, r) is True:
    print('YYMM')
    exit()

if is_mmyy(l, r) is True:
    print('MMYY')
    exit()

if is_ambigous(l, r) is True:
    print('AMBIGUOUS')
    exit()
