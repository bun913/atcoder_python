"""
Atcoderの問題解く用

1行1列データ

# str型で受け取るとき
s = input()
# int型で受け取るとき
s = int(input())
# float型　(小数)で受け取るとき
s = float(input())

(1,N)行列データ
s = input().split()
# listで整数で受け取る
l = list(map(int, input().split()))

その他
https://qiita.com/jamjamjam/items/e066b8c7bc85487c0785
"""
import math
n = int(input())
sqr = int(math.sqrt(n))

# 約数
# 整数の性質上、a*b = N とするなら
# a or b もしくはその両方が Nの平方根以下となる
# 例えば36なら 6*6が最大 1*36,2*18のようにa,bの少なくとも片方はnの平方根以下
# そのため平方根まで約数をみていけば最後まで割り算をする必要がないので
# 最大でも 10**6の計算ですむ
ans = []
i = 2
while True:
    if i >= sqr:
        break
    if n % i == 0:
        n //= i
        ans.append(str(i))
    else:
        i += 1
if n != 1:
    ans.append(str(n))
print(" ".join(ans))
