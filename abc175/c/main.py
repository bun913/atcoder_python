# -*- coding: utf-8 -*-
"""
数直線の左か右にDだけK回移動する
K回移動した座標の絶対値が最小になるようにしたい

0に向かって近づける
それでK回に回数が足りないなら、あとは+,-というのを繰り返しするだけでは
"""
X, K, D = list(map(int, input().split()))
# できるだけ0に近づけるように移動する
dis_to_zero = abs(X)
move_cnt = dis_to_zero // D
dis = D * min(move_cnt, K)
ans = X + dis
if X > 0:
    ans = X - dis
# この時点で移動を使い切ってしまった場合
if move_cnt >= K:
    print(abs(ans))
    exit()
# 残りが2の倍数なら現時点の位置が答え
rest = K - move_cnt
if rest % 2 == 0:
    print(abs(ans))
    exit()
if ans > 0:
    ans -= D
else:
    ans += D
print(abs(ans))
