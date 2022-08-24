# -*- coding: utf-8 -*-
"""
NこのブロックをK種類の色で塗る
1 <= abs(i-j) <=2ならブロックiとブロックjの色は異なる
使わない色があっても良い

ブロックの塗り方が何通りあるか
10**9 + 7 で割ったあまり

以下解説AC
繰り返し2乗法というテクニックで乗数の計算を早くできるらしい
pow関数ではすでにそれで実装されていて、さらに第3引数で剰余を計算してくれることも知った
"""
N, K = list(map(int, input().split()))
mod = 10 ** 9 + 7
if N == 1:
    print(K % mod)
    exit()
if N == 2:
    print(K * (K-1) % mod)
    exit()
ans = K * (K-1) * pow(K-2, N-2, mod)
print(ans % mod)
