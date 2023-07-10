"""
普通にやると Ai / (Ai+Bi)と少数を扱うことになる
そのままだと誤差がでるので、とてつもなく大きい数をかけてやってみよう
（Pythonだと大きい数も扱える）
"""
from decimal import Decimal
from operator import itemgetter

N = int(input())
score_list = []
for i in range(N):
    a, b = map(int, input().split())
    score = Decimal(a) / Decimal(a+b)
    score_list.append((score, i+1))

score_list.sort(key=itemgetter(1))
score_list.sort(key=itemgetter(0), reverse=True)

ans_list = []
for _, ind in score_list:
    ans_list.append(ind)
print(*ans_list, sep=' ')
