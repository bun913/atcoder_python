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

N = int(input())
n = N
sqr = int(math.sqrt(N))

# 全探索ではなく平方根までの検索を行う
# なぜなら N = a * b と考えた時、aとbの両方が平方根より大きくなることはないため
# 25とかで考えるとわかりやすい
ans = []
for i in range(2, sqr+1):
    # iで割続けられるうちは続ける
    while True:
        if n % i == 0:
            ans.append(str(i))
            n = n // i
        else:
            break
if n != 1:
    ans.append(str(n))
print(' '.join(ans))
