"""
個数の方を全探索すればいけそう
"""
A, B, W = map(int, input().split())
W *= 1000

max_cnt = -1
min_cnt = float('inf')
for x in range(1, 1000001):
    # 最小の重さA * xがW以下かつ、最大の重さB * xがW以上でないと条件を満たせない
    if A * x <= W <= B * x:
        max_cnt = max(max_cnt, x)
        min_cnt = min(min_cnt, x)
if max_cnt != -1 and min_cnt != float('inf'):
    print(min_cnt, max_cnt)
    exit()
print('UNSATISFIABLE')
