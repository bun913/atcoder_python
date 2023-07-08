# -*- coding: utf-8 -*-
"""
N種類の薬をもらう
i番目の薬はAi日間飲み続ける必要がありbi錠飲む必要がある
とはいえ最大で飲む薬の量はAを全てたしたものってわかっている
そこからbの小さい順に並べて弾いていけば良いのでは
"""
N, K = map(int, input().split())
drugs = []
days = []
day_drugs = []
for _ in range(N):
    day, drug = map(int, input().split())
    days.append(day)
    drugs.append(drug)
    day_drugs.append((day, drug))

sum_drugs = sum(drugs)
# すでにK錠以下の場合
if sum_drugs <= K:
    print(1)
    exit()

day_drugs.sort()
ans = 0
for day, drug in day_drugs:
    sum_drugs -= drug
    ans = day + 1
    if sum_drugs <= K:
        break
print(ans)
