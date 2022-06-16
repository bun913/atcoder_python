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
# H, Wは10**9なので、そもそも1ループも無理
# まぁでも、単純に市松模様で塗った時に同じ色のマスに行ける
# ということであるので、ますの数を求めれば良いだけO(n)でとけそう
H, W = list(map(int, input().split()))
# なぜこの結果になるのか？
# x + y が偶数になるところにだけ到達できる
# HWが奇数になるときには、数が一つ増える
ans = (H * W) // 2
if (H * W) % 2 == 1:
    ans += 1
if H == 1 or W == 1:
    ans = 1
print(ans)
