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
# 最大公約数を返す関数


def GCD(A, B):
    while A >= 1 and B >= 1:
        if A < B:
            B = B % A  # A < B の場合、大きい方 B を書き換える
        else:
            A = A % B  # A >= B の場合、大きい方 A を書き換える
    if A >= 1:
        return A
    return B

# 最小公倍数を返す関数


def LCM(A, B):
    return int(A / GCD(A, B)) * B


# 入力
N, K = map(int, input().split())
V = list(map(int, input().split()))

# ビット全探索で答えを出す
# この問題で出すべきはいずれかの数という点に注意
# だから、極端な話Nを周回できるなら全部の倍数をとって、そこから和集合 - 積集合としてやるのが良い
# ただNが途方もないのでとても全ての倍数を列挙することはできない
ans = 0
for i in range(1, 1 << K):
    cnt = 0
    lcm = 1
    for j in range(K):
        if (i & (1 << j)) != 0:
            cnt += 1
            # このlcmは選ばれた数が1つの場合、単純にその数の倍数の数になる
            # だから例えば選んだ組み合わせが2の場合は、その数は1つだけ選んだ数に含まれていることになるので差し引いてやる
            lcm = LCM(lcm, V[j])
    mutliple = N // lcm
    print("lcm: {}, cnt:{}, multiple: {}".format(lcm, cnt, mutliple))
    if cnt % 2 == 1:
        ans += mutliple
    else:
        ans -= mutliple
# 出力
# print(ans)
