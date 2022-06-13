"""
Atcoderの問題解く用

1行1列データ

#str型で受け取るとき
s = input() 
#int型で受け取るとき
s = int(input()) 
#float型　(小数)で受け取るとき
s = float(input())

(1,N)行列データ
s = input().split()
# listで整数で受け取る
l = list(map(int, input().split()))

その他
https://qiita.com/jamjamjam/items/e066b8c7bc85487c0785
"""
H, W = list(map(int, input().split()))
S = [list(input()) for _ in range(H)]
# 8方向
dxy = [
    (-1, 0), (1, 0),
    (0, -1), (0, 1),
    (-1, 1), (1, 1),
    (-1, -1), (1, -1)
]
for x in range(H):
    for y in range(W):
        now = S[x][y]
        if now == '#':
            continue
        # 8方向を確認する
        count = 0
        for dx, dy in dxy:
            plux = x + dx
            pluy = y + dy
            if plux < 0 or plux >= H or pluy < 0 or pluy >= W:
                continue
            if S[plux][pluy] == '#':
                count += 1
        S[x][y] = str(count)
for i in range(H):
    s = ''.join(S[i])
    print(s)
