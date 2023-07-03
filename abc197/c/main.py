"""
Nが最大で20しかないのでBit全探索で解けそう
1つ以上のからではなく連続した区間に分ける
つまり、Bit全探索で区間の境目を決められる
ただし全部Falseは除く
"""
from itertools import product
from functools import reduce

N = int(input())
A = list(map(int, input().split()))

ans = float("inf")
# 仕切りをAiとAi+1の間に入れると考える
for bools in product([True, False], repeat=N-1):
    or_list = []
    cur_or = 0
    for i in range(N):
        # orを取る
        cur_or |= A[i]
        # 仕切りがあったらorをリストに追加
        # bools[i]がTrueの時に仕切りがあるので計算結果の格納と初期化
        if i == N-1 or bools[i]:
            or_list.append(cur_or)
            cur_or = 0
    ans = min(ans, reduce(lambda x, y: x ^ y, or_list))
print(ans)
