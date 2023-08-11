# -*- coding: utf-8 -*-
"""
区間スケジューリング問題というものになるらしい
https://algo-method.com/tasks/363/editorial
↑の問題では終了時刻が早い順に選ぶのが最適になっている
終了時間が早い者を選ぶことで、その後の選択肢が増えるから
最後にパンチした壁の位置を覚えておく
"""
N, D = map(int, input().split())
walls = [list(map(int, input().split())) for _ in range(N)]
# 右の位置を基準にソートする
walls = sorted(walls, key=lambda x: x[1])

ans = 0
last = -1 #初期状態
for l,r in walls:
    if last == -1:
        last = r
        ans += 1
        continue
    # 最後のパンチからD以上離れていたらパンチをする
    if last + D <= l:
        last = r
        ans += 1

print(ans)
