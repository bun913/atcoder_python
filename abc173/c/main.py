from itertools import product
from copy import deepcopy

H, W, K = map(int, input().split())
C = [list(input()) for _ in range(H)]

# H,Wが少ないのでbit全探索で求める
ans = 0
for row_choices in product([False, True], repeat=H):
    for col_choices in product([False, True], repeat=W):
        c = deepcopy(C)
        rows = [i for i, v in enumerate(row_choices) if v]
        cols = [i for i, v in enumerate(col_choices) if v]
        for row in rows:
            c[row] = ['r'] * W
        for col in cols:
            for i in range(H):
                c[i][col] = 'r'
        cnt = 0
        for c_row in c:
            cnt += c_row.count('#')
        if cnt == K:
            ans += 1
print(ans)
