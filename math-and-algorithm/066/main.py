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
# 3枚のカードにN以下の数を書き込んで・・・
# 全探索すると10**3 を3回のため間に合わない

# 入力受け取り
N, K = list(map(int, input().split()))
# 余事象を考えるとのこと
# 条件がor orなのでとても数が多くなる
# 一方良事象を考えれば、 and and になるので条件が絞られる
# 例えばa,bを赤色、青色の数と考えると
# abs(a-b) <= K-1 を満たす必要がある
# つまり aが大きい方の条件とbが大きい時の条件を数式に表してやれば良い
yojisyo = 0
for a in range(1, N+1):
    _min = max(1, a-(K-1))
    _max = min(N, a+(K-1))
    for b in range(_min, _max+1):
        # if _min <= b and b <= _max:
        for c in range(_min, _max+1):
            if (abs(b-c)) <= K - 1:
                yojisyo += 1
print(N**3 - yojisyo)
