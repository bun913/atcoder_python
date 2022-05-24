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
import math

p = int(input())
n = 10
s = 0
i = 0
while True:
    a = math.factorial(n)
    if s == p:
        print(i)
        break
    # 大きい場合は数を小さくする
    if s + a > p:
        n -= 1
        continue
    s += a
    i += 1
