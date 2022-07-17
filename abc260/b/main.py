# -*- coding: utf-8 -*-
"""
解く前のメモ

色々考えていたら時間内に解けなかった
よく考えればNが1000だから二重ループでもいけた

終わった後のメモ

このように2つのキーでソートしたい場合、まず第2キーでソートして、その後に第1キーを指定すれば良いみたい
https://ytyaru.hatenablog.com/entry/2021/10/13/000000

"""
from operator import itemgetter

N, X, Y, Z = list(map(int, input().split()))

memo = [{'i': i, 's': -1, 'e': -1, 'sum': -1} for i in range(N)]

A = list(map(int, input().split()))
B = list(map(int, input().split()))

# メモに追記
for i in range(N):
    a = A[i]
    b = B[i]
    _sum = a + b
    memo[i]['i'] = i + 1
    memo[i]['s'] = a
    memo[i]['e'] = b
    memo[i]['sum'] = _sum

ans_list = []

s_sort = sorted(memo, key=itemgetter('i'))
s_sort = sorted(memo, key=itemgetter('s'), reverse=True)


for _ in range(X):
    dic = s_sort.pop(0)
    i = dic['i']
    ans_list.append(i)

# まず第2キーでソートする
e_sort = sorted(s_sort, key=itemgetter('i'))
# 次に第1キーでソートする
e_sort = sorted(e_sort, key=itemgetter('e'), reverse=True)


for _ in range(Y):
    dic = e_sort.pop(0)
    i = dic['i']
    ans_list.append(i)

# まず第2キーでソートする
sum_sort = sorted(e_sort, key=itemgetter('i'))
# 次に第1キーでソートする
sum_sort = sorted(sum_sort, key=itemgetter('sum'), reverse=True)


for _ in range(Z):
    dic = sum_sort.pop(0)
    i = dic['i']
    ans_list.append(i)


ans_list = sorted(ans_list)

print(*ans_list, sep='\n')
