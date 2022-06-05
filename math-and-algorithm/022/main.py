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
l = list(map(int, input().split(" ")))
# 組み合わせ列挙のため、1~99999までの数を数えておく
values = [0 for _ in range(1, 100000)]
keys = [i for i in range(1, 100000)]
dic = dict(zip(keys, values))
# 数え上げ
for i in l:
    dic[i] += 1
# (1,99999), (2,99998) と数え上げていく
ans = 0
for i in range(1, 50001):
    conbi = (dic[i], dic[100000-i])
    if i == 50000:
        # 50,000だけ同じ数なのでnC2で計算
        n = (conbi[0] * (conbi[0] - 1)) // 2
        ans += n
        break
    ans += (conbi[0] * conbi[1])
print(ans)
