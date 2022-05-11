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
grids = []
for _a in range(H):
    l = input()
    grids.append(l)
# 上下左右4方向を確認するための配列
dxy = [
    (-1, 0), (1, 0), (0, -1), (0,1)
]
ans = "Yes"
for y in range(H):
    for x in range(W):
        now_col = grids[y][x]
        # 白に塗るべきマスは飛ばす
        if now_col == ".":
            continue
        count = 0
        for dx, dy in dxy:
            if x + dx < 0 or x + dx > W - 1 or y + dy < 0 or y + dy > H - 1:
                continue
            target_col = grids[y+dy][x+dx]
            if target_col == "#":
                count += 1
        # 上下左右に黒マスがなければ白に色を塗ってしまうことになるため失敗
        if count == 0:
            ans = "No"
            break
print(ans)
