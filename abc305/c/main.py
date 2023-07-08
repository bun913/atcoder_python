# -*- coding: utf-8 -*-
"""
自分の周りのクッキーが最大となる場所を探す
"""
H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]

max_cookie = 0
ans = (-1, -1)
for i in range(H):
    for j in range(W):
        # 自分がクッキーなら違う
        if S[i][j] == '#':
            continue
        cookie_cnt = 0
        for dx, dy in dxy:
            if 0 <= i + dx < H and 0 <= j + dy < W:
                if S[i + dx][j + dy] == '#':
                    cookie_cnt += 1
        if max(max_cookie, cookie_cnt) == cookie_cnt:
            max_cookie = cookie_cnt
            ans = (i+1, j+1)
print(ans[0], ans[1])
