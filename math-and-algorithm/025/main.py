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
al = list(map(int, input().split()))
bl = list(map(int, input().split()))

ans = 0.0
for i in range(n):
    # 和の期待値を合計すると答えになる
    a = al[i]
    b = bl[i]
    ans += (a * 1/3) + (b * 2/3)
print(ans)
