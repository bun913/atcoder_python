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
# 辺はx, y軸と並行
# 最小の正方形の可能性を考えてみる
# 最小となり得る正方形の条件は、各辺上に点が1個存在する状態のはず
# ↑だって、どこかの辺に点が接していないと、まだ縮められるじゃんってなるから
# 左上端、右下端...と点を列挙していって、考えていけば良い

# 入力
N, K = list(map(int, input().split()))
xl = []
yl = []

for i in range(N):
    x, y = list(map(int, input().split()))
    xl.append(x)
    yl.append(y)


def count_in_box(lx, ly, rx, ry):
    # 点が何個長方形に含まれるか数え上げ
    cnt = 0
    for i in range(N):
        if lx <= xl[i] and ly <= yl[i] and xl[i] <= rx and yl[i] <= ry:
            cnt += 1
    return cnt


ans = float('inf')
for a in range(N):
    for b in range(N):
        for c in range(N):
            for d in range(N):
                # 左端のx座標
                lx = xl[a]
                # 左端のy座標
                ly = yl[b]
                # 右端辺のx座標
                rx = xl[c]
                # 右端のy座標
                ry = yl[d]
                count_dot = count_in_box(lx, ly, rx, ry)
                if count_dot >= K:
                    area = (rx-lx) * (ry-ly)
                    ans = min(ans, area)
print(ans)
