# -*- coding: utf-8 -*-
"""
Tが最大で10**5である
穴が5しかないのが非常に怪しい
動的計画法でいけるんじゃないかな
n個目の出現ポイントまで使ってよい最大値を求めればよいのでは。

"""
from functools import reduce, lru_cache
from itertools import combinations
import math
