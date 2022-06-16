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
N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
# この問題を考える時には、テレポートの周期性とそのループに至るまでの初期回数を考える
# 例えば 1,2,[3,4,5],[3,4,5]...と繰り返す場合を考える
# でkが8だとする、
# この場合ループに入るまでに2つの町を通り、あとは3回のループを繰り返すことがわかる
# 今回は周期性と、1回目までに訪れるまでの回数を利用してたかだか2週目で回答を行う

first = [-1 for i in range(N+1)]
second = [-1 for i in range(N+1)]
# curが今いる街
# cntがテレポーターの使用が何回目かカウント
cur, cnt = 1, 0

while True:
    # 初めての場合はfirst, 2回目の場合はsecondに格納する
    if first[cur] == -1:
        first[cur] = cnt
    elif second[cur] == -1:
        second[cur] = cnt
    # ここからK回目の移動と同じ周期・もしくはK回目そのものと考えてみる
    # まず一番簡単なのがKが結構小さい値で1周で終わる時
    if cnt == K:
        print(cur)
        exit()
    # 次に2週目に突入している場合
    if second[cur] != -1 and \
            (K - first[cur]) % (second[cur] - first[cur]) == 0:
        print(cur)
        exit()
    # cntをインクリメントして、curを次の街にセット
    cur = A[cur-1]
    cnt += 1
