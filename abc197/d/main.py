"""
正N角系という情報が与えられる
Nは偶数であることが保証されている
多角形の頂点の一つを割り出す問題
スタート地点との対角の頂点は与えられている
つまり三角形の2点は最初からわかっている
- 多角形の中心を求めて
- 中心から点を回転させた後の座標を求めればよい
"""
from math import radians, cos, sin


def rotation_matrix(x, y, angle):
    # 回転行列
    rad = radians(angle)
    ans = (x * cos(rad) - y * sin(rad), x * sin(rad) + y * cos(rad))
    return ans


N = int(input())
x0, y0 = map(int, input().split())
xx, yy = map(int, input().split())  # 対角の頂点
# 中心を求める
xo = (x0 + xx) / 2
yo = (y0 + yy) / 2
# 中心が原点に来る様に座標を移動させる
x0 -= xo
y0 -= yo
# 点を回転させる方法は持っているのであとは角度を求める
angle = 360 / N
ans = rotation_matrix(x0, y0, angle)
print(ans[0] + xo, ans[1] + yo)
