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
l = [2, 1]
for i in range(2,N+1):
    n = l[i-1] + l[i-2]
    l.append(n)
if N <= 1:
    if N == 1:
        print(1)
    else:
        print(2)
else:
    print(l[-1])