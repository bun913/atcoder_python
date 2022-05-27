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
ans = "Alloy"
a, b = list(map(int, input().split()))

if 0 < a and b == 0:
    ans = "Gold"
elif a == 0 and 0 < b:
    ans = "Silver"
print(ans)
