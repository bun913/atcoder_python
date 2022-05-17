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

A, B = list(map(int, input().split()))
s = A + B

ans = 4

if s >= 15 and B >= 8:
    ans = 1
elif s >= 10 and B >= 3:
    ans = 2
elif s >= 3:
    ans = 3
print(ans)
