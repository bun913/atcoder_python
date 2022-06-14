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
"""
from operator import mul
from functools import reduce


def cmb(n, r):
    r = min(n-r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


N = int(input())
A = list(map(int, input().split()))

c1 = 0
c2 = 0
c3 = 0

for a in A:
    if a == 1:
        c1 += 1
    elif a == 2:
        c2 += 1
    else:
        c3 += 1

cmb1 = cmb(c1, 2) if c1 >= 2 else 0
cmb2 = cmb(c2, 2) if c2 >= 2 else 0
cmb3 = cmb(c3, 2) if c3 >= 2 else 0
print(cmb1 + cmb2 + cmb3)
