# -*- coding: utf-8 -*-
"""
NこのブロックをK種類の色で塗る
1 <= abs(i-j) <=2ならブロックiとブロックjの色は異なる
使わない色があっても良い

ブロックの塗り方が何通りあるか
10**9 + 7 で割ったあまり
"""
N, K = list(map(int, input().split()))
# 最初の3ブロックの塗り分け
r = min(N, 3)
ans = 1
n = K
for _ in range(r):
    # N種類のボールを塗りきれない場合
    if n < 0:
        print(0)
        exit()
    mod = n % (10 ** 9 + 7)
    ans *= mod
    n -= 1
# 最初の3ブロックだけで終わる場合
if r == N:
    print(ans)
    exit()
# 残りの数を算出
rest = N - r
rest_block = (K-2) % (10 ** 9 + 7)
ans = ans * (pow(rest_block, rest))
ans = ans % (10 ** 9 + 7)
print(ans)
