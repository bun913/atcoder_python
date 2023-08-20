# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
M = int(input())
days = list(map(int, input().split()))
sum = sum(days)
# 中央の値
central = (sum+1) // 2
cur = 0
for i in range(M):
    day_cnt = days[i]
    month_day = 0
    for cnt in range(1, day_cnt+1):
        cur += 1
        month_day += 1
        if cur == central:
            print(i+1, month_day)
