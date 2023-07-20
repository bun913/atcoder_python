"""
ボールの入った袋の個数をN
ボールの総数をAとする
今回の組み合わせの個数は ACNとなる
で、今回ボールの個数の総積は10**5を超えないとある
そのため全探索しても十分に間に合うはずである
N個の袋からボールを一つ選ぶことを全探索する
"""
from itertools import product

N, X = map(int, input().split())
L = []
A = []
for _ in range(N):
    l, *a = map(int, input().split())
    L.append(l)
    A.append(a)
# 全ての数字を掛け合わせる全探索を行う
P = [1]
# productで書くとこうなる
for i in range(N):
    P = [p * ai for p, ai in product(P, A[i])]
ans = P.count(X)
print(ans)
# for i in range(N):
#     tmp_product = []
#     for ai in A[i]:
#         for p in P:
#             tmp_product.append(p * ai)
#     P = tmp_product

# ans = P.count(X)
# print(ans)
