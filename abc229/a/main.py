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


l = [list(input()) for _ in range(2)]
dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for i in range(2):
    for j in range(2):
        black_count = 0
        for dx, dy in dxy:
            if l[i][j] == '#':
                if i + dx < 0 or i + dx > 1 or j + dy < 0 or j + dy > 1:
                    continue
                if l[i+dx][j+dy] == '#':
                    black_count += 1
        if l[i][j] == '#' and black_count == 0:
            print('No')
            exit()
print('Yes')
