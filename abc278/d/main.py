# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    act()


def act():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    # 今1番目のクエリで指定されている値を持つ
    change_num = -1
    change_cnt = 0
    # 2番目のクエリで足された値を持つ
    # 2番目のクエリが呼ばれた時のchange_cntを合わせて持つ
    pluses = [[0, 0] for _ in range(N)]
    for _ in range(Q):
        q, *l = map(int, input().split())
        if q == 1:
            x = l[0]
            change_num = x
            change_cnt += 1
        elif q == 2:
            i, x = l
            i -= 1
            if pluses[i][1] < change_cnt:
                pluses[i][0] = 0
                pluses[i][1] = change_cnt
            pluses[i] = [pluses[i][0] + x, change_cnt]
        else:
            i = l[0]
            i -= 1
            a = A[i]
            if change_num == -1:
                print(a + pluses[i][0])
            # 2のクエリで足した後に全変更のクエリが呼ばれている場合
            elif pluses[i][1] < change_cnt:
                print(change_num)
            else:
                print(change_num + pluses[i][0])


solve()
