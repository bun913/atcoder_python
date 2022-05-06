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

import statistics

l = list(map(int, input().split()))
# 最初の要素を取得
a = l[0]
if l.count(a) == 1:
    print(a)
elif l[1] == a:
    print(l[2])
else:
    print(l[1])