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
import copy

H, W = list(map(int, input().split()))

inputs = []
# 2次元配列で入力を受け取る
for h in range(H):
    l = list(input())
    inputs.append(l)
ans = copy.deepcopy(inputs)
# xを横、yを縦の変数と考える
# 近接八方向を表すための数字の組み
dxy = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]
for h in range(H):
    for w in range(W):
        cur_col = ans[h][w]
        # #の場合はそのまま出力
        if cur_col == "#":
            continue
        count = 0
        # 近隣8マスを確認
        for dx, dy in dxy:
            # インデックス0を下回る、インデックス最大値を上回る場合はスキップ
            if w + dx < 0 or w + dx > W-1 or h + dy < 0 or h + dy > H - 1:
                continue
            target_col = inputs[h+dy][w+dx]
            if target_col == "#":
                count += 1
        ans[h][w] = str(count)
for l in ans:
    print("".join(l))
