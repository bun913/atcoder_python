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
l = [list(map(int, input().split())) for _ in range(n-1)]
dic = dict([[i, 0] for i in range(1, n+1)])
if len(l) != n-1:
    print("No")
    exit()
# dicのキーが全て1以上かつ、どれかの数字がn-1個出てきていればよい
for a, b in l:
    dic[a] += 1
    dic[b] += 1
# 判定
_max = max(dic, key=dic.get)
is_all_kind = True
for k, v in dic.items():
    if k != _max:
        if v != 1:
            print("No")
            exit()
    else:
        if v != n-1:
            print("No")
            exit()
print("Yes")
