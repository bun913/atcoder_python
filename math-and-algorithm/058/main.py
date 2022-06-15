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
# 実際に1回でいける数、2回で行ける数と考えてみる
# 市松模様に色を塗ってみると偶数奇数で行けるところが限られてくるとはっきりわかる
N, X, Y = list(map(int, input().split()))

ans = 'No'
if abs(X) + abs(Y) <= N and (abs(X) + abs(Y)) % 2 == N % 2:
    ans = 'Yes'

print(ans)
