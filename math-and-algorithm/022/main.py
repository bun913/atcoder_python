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
# 2枚選んで100,000になる組み合わせを数え上げるだけ
dic = {}
for a in A:
    if a in dic:
        dic[a] += 1
    else:
        dic[a] = 1
s = 0
for i in range(1, 50000+1):
    if i not in dic:
        continue
    left = dic[i]
    if 100000-i not in dic:
        continue
    right = dic[100000-i]
    c = 0
    if i == 50000:
        if left >= 2:
            c = ((left) * (left-1)) // 2
    # ただ50,000の場合はnC2とする
    else:
        c = left * right
    s += c
print(s)
