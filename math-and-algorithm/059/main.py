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
N = int(input())
if N == 0:
    print(1)
    exit(1)

mod = N % 4
if mod == 1:
    print(2)
elif mod == 2:
    print(4)
elif mod == 3:
    print(8)
else:
    print(6)
