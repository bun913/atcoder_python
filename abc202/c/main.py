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
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

a_dic = {}
c_dic = {}

# 辞書の初期化
for i in range(N+1):
    a_dic[i] = 0
    c_dic[i] = 0

# AとCを辞書にして数をメモ
for i in range(N):
    a = A[i]
    c = C[i]
    if a in a_dic:
        a_dic[a] += 1
    if c in c_dic:
        c_dic[c] += 1

ans = 0

# Bをループで回していき、AとBが同じになるもののうちCから選べるものを数え上げる
for j in range(N):
    jd = j+1
    b = B[j]
    if b in a_dic:
        # Cの中にjdがあるか
        if jd in c_dic:
            cnt = a_dic[b] * c_dic[jd]
            ans += cnt

print(ans)
