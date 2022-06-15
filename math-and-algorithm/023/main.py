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

N = int(input())
B = list(map(int, input().split()))
R = list(map(int, input().split()))

s = 0

# 二重ループはできない
# 期待値の線形性を使う
# 2つを同時に降った時の期待値が知りたければ
# ここのサイコロでの期待値を出して、それを足し合わせればなぜか2つのサイコロを同時に投げた期待値が出てくる

for i in range(N):
    s += B[i] / N
    s += R[i] / N

print(s)
