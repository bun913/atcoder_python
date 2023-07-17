"""
H行、W列のますが最初にあるとする
マスは最初全て*だが
そのあとますのどの座標にカードがあるか情報が与えられる
そのあとカードが一枚もない行と列を消す
最終的に残るますを表示する
座標の圧縮を行う
行と列をそれぞれ圧縮する
"""
H, W, N = map(int, input().split())
A, B = [], []
AB = []

for _ in range(N):
    a, b = map(int, input().split())
    A.append(a-1)
    B.append(b-1)
    AB.append((a-1, b-1))

# 重複の排除
A = sorted(list(set(A)))
a_dic = {}
# 座標圧縮
for i, a in enumerate(A):
    a_dic[a] = i+1

# 列の座標圧縮
B = sorted(list(set(B)))
b_dic = {}
for i, b in enumerate(B):
    b_dic[b] = i+1

# 座標圧縮したものを元の座標に戻す
for row, col in AB:
    ans_row = a_dic[row]
    ans_col = b_dic[col]
    print(ans_row, ans_col)
