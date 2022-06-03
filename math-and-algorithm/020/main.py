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
# 一見すると n= 100 ** 5で10の10条にになって無理じゃんと思うけど
# 重複ないようにカードを選ぶようにするので 100C5 となって
# 最大で7千万くらいの組み合わせになる
# ループで始点が右にずれていっているので、実際は100*98*97*96も探索しない
# 順番も考慮しないでどんどん右に行くので、つまり重複度5!で割った数がせいぜいとなる
n = int(input())
l = list(map(int, input().split(" ")))

ans = 0
for a in range(0, n):
    for b in range(a+1, n):
        for c in range(b+1, n):
            for d in range(c+1, n):
                for e in range(d+1, n):
                    if l[a] + l[b] + l[c] + l[d] + l[e] == 1000:
                        ans += 1
print(ans)
