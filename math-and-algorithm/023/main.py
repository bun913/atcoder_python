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
# 普通に考えればBとRを全列挙して確率と期待値を計算
# でも今回は各サイコロで最高10**6面となるため2重ループは無理
# 期待値を計算ということに注目
# 期待値の線形性を利用すれば全ての期待値の合計はそれぞれ1ループで実装できそう

N = int(input())
B = list(map(int, input().split()))
R = list(map(int, input().split()))

be = 0
re = 0

for i in range(N):
    b = B[i]
    r = R[i]
    be += (1 / N) * b
    re += (1 / N) * r
print(be+re)
