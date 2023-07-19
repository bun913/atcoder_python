# -*- coding: utf-8 -*-
"""
再帰関数で経路を列挙する
"""
import sys
sys.setrecursionlimit(10**8)

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]


def dfs(x, y, s):
    # 終端を決める。ゴールに着いたら終了
    if (x, y) == (H-1, W-1):
        # 1を返すのは、ゴールに着いたら1通りあるということ
        return 1
    cnt = 0
    # マスの外部にはいけない and すでに通ったマスにはいけない
    if x < H-1:
        next_num = A[x+1][y]
        if next_num not in s:
            s.add(next_num)
            cnt += dfs(x+1, y, s)
            s.remove(next_num)
    if y < W-1:
        next_num = A[x][y+1]
        if next_num not in s:
            s.add(next_num)
            cnt += dfs(x, y+1, s)
            s.remove(next_num)
    return cnt


ans = dfs(0, 0, set([A[0][0]]))
print(ans)
