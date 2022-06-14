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
from math import sqrt

N = int(input())
sqr = int(sqrt(N))

ans = set()

for i in range(1, sqr+1):
    if N % i == 0:
        ans.add(i)
        ans.add(N // i)
for i in ans:
    print(i)
