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

x, y = list(map(int, input().split()))
ans = x
if x != y:
    l = [x, y]
    if 0 not in l:
        ans = 0
    if 1 not in l:
        ans = 1
    if 2 not in l:
        ans = 2
print(ans)
