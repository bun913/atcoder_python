"""
Atcoderの問題解く用

1行1列データ

# str型で受け取るとき
s = input()
# int型で受け取るとき
s = int(input())
# float型　(小数)で受け取るとき
s = float(input())

(1,N)行列データ
s = input().split()
# listで整数で受け取る
l = list(map(int, input().split()))

その他
https://qiita.com/jamjamjam/items/e066b8c7bc85487c0785
"""
n = int(input())
ans = 0
# p番目の問題の全ての組み合わせを選んでいたらタイムアウト
# 期待値の和 = 和の期待値を使って溶ける
# 単純にn番目の問題の和を求められ場良い
for _ in range(n):
    p, q = list(map(int, input().split()))
    ans += (q / p)
print(ans)
