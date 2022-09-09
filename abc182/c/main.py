# -*- coding: utf-8 -*-
"""
Nは各桁に0が
Nの桁数をkとする。Nの桁数を0以上k個未満消して、残った桁をそのままの順序で結合
その数で3の倍数にしたい

解答前のメモ
3の倍数になるということは各桁が足して３になるということ
各桁を3で割ったあまりを足し合わせれば良いのでは
算数の知識で求めることもできそうだが、今回は最大でも18桁のNなのでギリギリ全探索でも間に合いそう
"""
from itertools import product

N = int(input())
L = list(map(int, list(str(N))))

limit = 10**18 + 5
ans = limit
for flags in product([True, False], repeat=len(L)):
    delete_cnt = 0
    # 全部の桁を消せないのでスキップ
    if flags.count(True) == len(flags):
        continue
    # 残った数の各桁の和が3の倍数か調べる
    rest_sum = 0
    for i in range(len(L)):
        is_delete = flags[i]
        if is_delete is True:
            delete_cnt += 1
            continue
        rest_sum += L[i] % 3
    if rest_sum % 3 == 0:
        ans = min(ans, delete_cnt)
if ans == limit:
    print(-1)
    exit()
print(ans)
