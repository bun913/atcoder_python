"""
ボールの入った袋の個数をN
ボールの総数をAとする
今回の組み合わせの個数は ACNとなる
で、今回ボールの個数の総積は10**5を超えないとある
そのため全探索しても十分に間に合うはずである
N個の袋からボールを一つ選ぶことを全探索する
"""
N, X = map(int, input().split())

boals = []
for _ in range(N):
    L, *A = map(int, input().split())
    boals.append(A)

products = [1]
for boal in boals:
    tmp = []
    for prodcut in products:
        for boal_num in boal:
            tmp.append(prodcut * boal_num)
    products = tmp
print(products.count(X))
