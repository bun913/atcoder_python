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
    elif r < 0:
        return 0
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


N = int(input())
A = list(map(int, input().split()))

memo = dict([(k, 0) for k in range(1, 100001)])

for a in A:
    memo[a] += 1

ans = 0

for i in range(1, 50001):
    left = memo[i]
    right = memo[100000-i]
    # print(i, left, right)
    conb = 0
    if i == 50000:
        if left >= 2:
            conb = cmb(left, 2)
    else:
        conb = left * right
    ans += conb
print(ans)
