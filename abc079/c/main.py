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
from itertools import product

# product使ったバージョン
A, B, C, D = list(map(int, list(input())))
flags = product([True, False], repeat=3)
for flag in flags:
    O = []
    for i in range(3):
        if flag[i] is True:
            O.append('+')
            continue
        O.append('-')
    formula = "{}{}{}{}{}{}{}".format(A, O[0], B, O[1], C, O[2], D)
    if eval(formula) == 7:
        ans = formula + '=7'
        print(ans)
        exit()


# for i in range(2 ** 3):
#     O = []
#     # bitのフラグが立っているのを+とする
#     for j in range(3):
#         ope = '-'
#         if ((i >> j) & 1):
#             ope = '+'
#         O.append(ope)
#     formula = "{}{}{}{}{}{}{}".format(A, O[0], B, O[1], C, O[2], D)
#     if eval(formula) == 7:
#         ans = formula + '=7'
#         print(ans)
#         exit()
