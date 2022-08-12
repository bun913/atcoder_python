"""
解く前のメモ

村が10**100という膨大すぎる数がある
"""
from collections import defaultdict

N, K = list(map(int, input().split()))
memo = defaultdict(int)

for i in range(N):
    A, B = list(map(int, input().split()))
    memo[A] += B

sorted_memo = sorted(memo.items())
cur = 0
rest = K

for villege, point in sorted_memo:
    if cur + rest < villege:
        # 次の村に辿りつけない場合
        print(cur+rest)
        exit()
    # restを減らす
    rest = rest - (villege - cur)
    rest += point
    cur = villege
    # 友達からポイントをもらう
# 友達からポイントをもらい切った場合
ans = cur + rest
print(min(ans, (10 ** 100) + 1))
