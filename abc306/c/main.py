# -*- coding: utf-8 -*-
"""
解く前のメモ用
1,2,...Nがちょうど3回ずつ現れる長さ3Nの数列Aがある。
で、Aの中に出てくるiのうちちょうど2回目に出てくる添字番号をメモしておく
"""
N = int(input())
A = list(map(int, input().split()))
# 出現回数の管理用
cnt_list = [0 for _ in range(N+1)]
# 2回目に現れるインデックスの管理用
ind_list = [0 for _ in range(N+1)]

# Aの中に出てくるiのうちちょうど2回目に出てくる添字番号をメモしておく
for i, a in enumerate(A):
    cnt_list[a] += 1
    if cnt_list[a] == 2:
        ind_list[a] = i+1
# ind_listのうち要素を再度取得して大きい順に並び替え
inds = sorted(ind_list[1:])
ans = []
for ind in inds:
    ans.append(A[ind-1])
print(*ans, sep=" ")
