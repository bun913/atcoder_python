# -*- coding: utf-8 -*-
"""
Nカップのアイスクリームを食べる
iカップ目の味はFi,おいしさはSi
N個から2つを選んで食べて、満足度を最大化する

満足度
- 2つのカップが同じ味なら s + t//2
- 違う味なら s + t

となれば、最大化さえるパターンは以下2つのどちらか
- 違う味の最大値 + 違う味の最大値
- 同じ味の最大値 + 同じ味の2番目の値
だからたかだか、同じ味の上位2種を持っておけば良い
"""
N = int(input())
F = []
S = []
memo = {}

for _ in range(N):
    f, s = map(int, input().split())
    F.append(f)
    S.append(s)
    if f in memo:
        memo[f].append(s)
        memo[f].sort(reverse=True)
        # 2種だけ持つ
        memo[f] = memo[f][:2]
        continue
    memo[f] = [s]

# 1: 同じ味から2つ選んだ場合の最大
cand1 = -1
for k, v in memo.items():
    if len(v) < 2:
        continue
    cand1 = max(cand1, v[0] + v[1] // 2)
# 1種類しかない場合はここで終了
if len(set(F)) == 1:
    print(cand1)
    exit()

# 2: 違う味から2つ選んだ場合の最大値
cand2 = -1
number1_list = [lis[0] for lis in memo.values()]
number1_list.sort(reverse=True)
cand2 = number1_list[0] + number1_list[1]
print(max(cand1, cand2))
