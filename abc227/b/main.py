# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用

1行1列データ

#str型で受け取るとき
s = input()
#int型で受け取るとき
s = int(input())
#float型　(小数)で受け取るとき
s = float(input())

(1,N)行列データ
s = input().split()
# listで整数で受け取る
l = list(map(int, input().split()))

その他
https://qiita.com/jamjamjam/items/e066b8c7bc85487c0785

全ての組み合わせを列挙する方法
list(0...8)から2つを抜き出す
list(combinations(l, 2))
"""
from functools import reduce
from itertools import combinations
import math

# 素数判定


def is_prime(n: int) -> bool:
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def permutation(n, r):
    return math.factorial(n) // math.factorial(n-r)


def combination(n, r):
    return permutation(n, r) // math.factorial(r)


n = int(input())
l = list(map(int, input().split()))
ok = 0
break_flag = False

# ここのa,bをどこまで探索するかには課題がある
# sが1000までなので式を考慮すると333でも多いくらいの探索
for i in range(n):
    s = l[i]
    for a in range(1, 333):
        if break_flag:
            # 初期化
            break_flag = False
            break
        for b in range(1, 333):
            if (4*a*b) + (3*a) + (3*b) == s:
                break_flag = True
                ok += 1
                break
print(n-ok)
