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

N = int(input())
al = []
bl = []

for _ in range(N):
    a, b = list(map(int, input().split()))
    al.append(a)
    bl.append(b)

ans = 10**6
for ai in range(N):
    for bi in range(N):
        a = al[ai]
        b = bl[bi]
        if ai == bi:
            if a+b <= ans:
                ans = a+b
            continue
        if max(a, b) <= ans:
            ans = max(a, b)
print(ans)
