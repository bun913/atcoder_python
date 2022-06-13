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
H, W, X, Y = list(map(int, input().split()))
S = [list(input()) for _ in range(H)]
dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
ans = 1
# 二次元配列のインデックスに合わせてx,yを調整
X -= 1
Y -= 1
for dx, dy in dxy:
    plux = X + dx
    pluy = Y + dy
    while True:
        if plux < 0 or pluy < 0 or plux >= H or pluy >= W:
            break
        if S[plux][pluy] == '.':
            ans += 1
        else:
            break
        plux += dx
        pluy += dy
print(ans)
