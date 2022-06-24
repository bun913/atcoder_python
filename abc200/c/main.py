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
# N個の正の整数からなる数列Aが与えられる
# iとjの組の個数を求める
# Ai- Ajが200の倍数となる
# Nが2 * 10 **5なので全組み合わせ列挙は無理
# 今回はあまりの性質を利用して全ての数の200での余りを求めていけばO(N)ですみそう

N = int(input())
A = list(map(int, input().split()))
# 全てのAの要素の余りを求めてここから逆算していく
# 辞書の初期化
dic = dict([(i, 0) for i in range(200)])
for a in A:
    mod = a % 200
    dic[mod] += 1
# 数え上げ
ans = 0
for i in range(200):
    i_cnt = dic[i]
    # あまりが同じになるものから2つ選ぶ
    if i_cnt >= 2:
        ans += (i_cnt * (i_cnt-1)) // 2
print(ans)
