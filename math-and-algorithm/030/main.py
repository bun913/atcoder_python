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
# このYoutubeが一番わかりやす方t
# https://www.youtube.com/watch?v=gVJ16ThsJYs
# i番目までの品物を使って、wグラムまでの荷物を入れた時の最大価値
n, W = list(map(int, input().split()))
# 二次元配列の表を0で初期化
dp = [[0 for _ in range(W+1)] for _ in range(n+1)]
# 品物1から順に選ぶ時、選ばない時の値段を計算していく
for i in range(1, n+1):
    wi, vi = list(map(int, input().split()))
    for w in range(W+1):
        # i番目の品物を入れるか入れないかを考える
        # そもそも入れることができるか考える
        # w-wi < 0 ならそもそも入れることができない
        if w - wi < 0:
            dp[i][w] = dp[i-1][w]
            continue
        # i番目の品物を入れれる場合
        # i番目の品物を使った方がよいか、使わない方が良いか考える
        # i-1番目の行から、w1を引いたものの最大価値を持ってくる
        # ↑なぜか、i-1は1個前の品物までを使っている最大価値を記録している
        # そこでwからw1の重さを引くことで、これまでの価値の最大値(wiを使ってない時点での最大価値)がわかるようになるということか
        unuse_i = dp[i-1][w]
        use_i = dp[i-1][w-wi] + vi
        dp[i][w] = max(unuse_i, use_i)
print(dp[n][W])
