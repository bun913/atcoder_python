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

h, w, x, y = list(map(int, input().split()))
cols = []
for _ in range(h):
    l = list(input())
    cols.append(l)
x -= 1
y -= 1
dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
ans = 1
# X, Yの左右上下のマスを見続けていく。左からみ初めて#が見つかったら次は右をずっと見ていく。その次は下、その次は上
for dx, dy in dxy:
    curx = x+dx
    cury = y+dy
    while True:
        # インデックスが上下左右に過ぎたら次の方向を見る
        if curx < 0 or curx > h-1 or cury < 0 or cury > w-1:
            break
        # #が見つかったら次の方向を見る
        if cols[curx][cury] == "#":
            break
        ans += 1
        curx += dx
        cury += dy
print(ans)
