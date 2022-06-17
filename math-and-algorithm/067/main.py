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
H, W = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(H)]
# 行ごとの和と列ごとの和を計算しておく
row_sum = [sum(row) for row in A]
col_sum = []
zipped = list(zip(*A))
for col in zipped:
    col_sum.append(sum(list(col)))
# 計算した結果を元に重複部分（自分）を除いた結果を出力する
ans = []
for i in range(H):
    l = []
    for j in range(W):
        s = row_sum[i] + col_sum[j] - A[i][j]
        l.append(str(s))
    ans.append(l)
# 答えの出力
for i in range(H):
    print(' '.join(ans[i]))
