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
n = int(input())
l = list(map(int, input().split(" ")))
c1 = 0
c2 = 0
c3 = 0
for i in l:
    if i == 1:
        c1 += 1
    elif i == 2:
        c2 += 1
    else:
        c3 += 1
ans = 0
for c in [c1, c2, c3]:
    if c <= 1:
        continue
    s = c * (c-1) // 2
    ans += s
print(ans)
