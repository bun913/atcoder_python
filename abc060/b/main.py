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

A, B, C = list(map(int, input().split()))

s = A
judge = False

# aの倍数はaの集まりだからaを足しあげるだけで良い
# あまりは除数(今回はB)を超えることは絶対にない
# https://qiita.com/yaju/items/aad350c6662d9d3b77cd
# 〜ごとに処理をするのにぴったり
# 剰余はグループ分けであるとのこと

for i in range(1, B):
    s += A
    if s % B == C:
        print("YES")
        exit()
print("NO")
