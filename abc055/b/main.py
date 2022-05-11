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
# 非常に大きな数同士の計算についての問題
# 今回で言えばあまりを求めるわけだが階乗を続けていくと非常に大きな値になる
# それを 10^9 + 7 という非常に大きな数と計算しようとするとオーバーフローする
# https://math.nakaken88.com/textbook/cp-remainder/
n = int(input())
c = 10**9 + 7
ans = 1
for i in range(1, n+1):
    ans = (ans * i) % c
print(ans)