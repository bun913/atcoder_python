"""
2点を全探索する
その前に辞書で全ての点を何個あるか管理しておく
2点をx1,y1,x2,y2とすると、
その辞書にx2,y1 および x1,y2があればx軸y軸に並行な長方形が存在することになる
この探す2点は対角の点を探していて、その対角と同じ線上に点が存在するかを確かめる
"""
from collections import defaultdict

N = int(input())
points = []
point_dict = defaultdict(int)
for _ in range(N):
    x, y = map(int, input().split())
    points.append((x, y))
    point_dict[(x, y)] += 1

ans = 0
for i in range(N):
    for j in range(i+1, N):
        x1, y1 = points[i]
        x2, y2 = points[j]
        # 対角の点ではないのでスキップ
        if x1 == x2 or y1 == y2:
            continue
        if point_dict[(x1, y2)] > 0 and point_dict[(x2, y1)] > 0:
            ans += 1
# 同じ2点の組み合わせがあるので2で割る
print(ans//2)
