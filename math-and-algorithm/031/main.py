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
dp_study = [0 for _ in range(N+1)]
dp_no_study = [0 for _ in range(N+1)]
# i日目に勉強した場合と勉強しない場合を分けて考える
# これでi日目までの最大値を求める
for i in range(1, N+1):
    # i日目に勉強する場合の最大値
    # 2日続けて勉強はできないので、昨日勉強しなかった場合の実力のアップ値を使う
    dp_study[i] = dp_no_study[i-1] + A[i-1]  # iは1始まりなので-1
    # i日目に勉強しない場合の最大値
    # 単純に昨日までの勉強しない場合と、勉強する場合の最大値を比べれば良い
    no_study = dp_no_study[i-1]
    study = dp_study[i-1]
    dp_no_study[i] = max(no_study, study)
print(max(dp_study[-1], dp_no_study[-1]))
