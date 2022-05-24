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
a, b, c, d = list(map(int, input().split()))
blue = a
red = 0
i = 0
ans = -1
for _ in range(10**5+1):
    if blue <= d * red:
        ans = i
        break
    blue += b
    red += c
    i += 1
print(ans)
