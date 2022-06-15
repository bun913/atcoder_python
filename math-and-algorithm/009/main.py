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
# Nが最大60なので全探索は無理(2**60)でタイムアウト
# 1こだけ使う場合,2こだけ使う場合・・と最適解を求め続けていく必要がある
# そこでDPですよ（表的計算法ですよ)
N, S = list(map(int, input().split()))
A = list(map(int, input().split()))
dp = [[False for _ in range(S+1)] for _ in range(N+1)]
dp[0][0] = True

for i in range(1, N+1):
    v = A[i-1]
    for j in range(0, S+1):
        # 横からj番目の数が現在のカードの値に満たない場合はそのカードを使えない
        # なので１個前の結果（１個前までの最適な結果)から持ってくるしかない
        no_use = dp[i-1][j]
        if j < v:
            dp[i][j] = no_use
            continue
        # 今回のカードを使う場合
        # 単純にj-vを引いた列がTrueならjの組み合わせがあり得るということ
        # 例: 今4にできるか考えている時に、v(カードの値)が3なら、4-3=1の組み合わせがあり得るなら当然1に3を足した4も出せるだろうということ
        use = dp[i-1][j-v]
        dp[i][j] = any([use, no_use])
if dp[N][S] is True:
    print('Yes')
    exit()
print('No')
