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
a, b, c, d = input()
# + or -しかないので 2**3で計算できる
for i in range(2**3):
    # 3桁を一つずつフラグが立っているか確認する(ビットが1かどうか)
    # 000 のように 各a b の間、b c の間, c d の間に入る演算子を表現する
    opes = []
    for j in range(3):
        # ビットを一番右までずらして積を取ることで1かどうか判定できる
        is_flaged = (i >> j) & 1
        if is_flaged:
            opes.append("+")
        else:
            opes.append("-")
    # 3桁揃ったら計算
    s = "{}{}{}{}{}{}{}".format(a, opes[0], b, opes[1], c, opes[2], d)
    _sum = eval(s)
    if _sum == 7:
        print(s + "=7")
        exit()
