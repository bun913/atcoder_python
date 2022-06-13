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

dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for i in range(H):
    for j in range(W):
        count = 0
        for dx, dy in dxy:
            plusi = i + dx
            plusj = j + dy
            if plusi < 0 or plusi >= H or plusj < 0 or plusj >= W:
                continue
            if S[plusi][plusj] == '#':
                count += 1
        if S[i][j] == '#' and count == 0:
            print("No")
            exit()
print("Yes")
