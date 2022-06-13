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
A, B, C, D = list(map(int, input().split()))
# 重なりを求めるAが先,Bが先で条件分岐ではなく最大値を使う
ans = min(B, D) - max(A, C)
if ans < 0:
    ans = 0
print(ans)
