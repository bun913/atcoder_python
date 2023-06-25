"""
"""
X, K, D = map(int, input().split())
# Xを0に近づけるには何回移動すれば良いか
c = abs(X) // D
# 0に限りなく近づけるまでKが足りない場合
if c > K:
    print(abs(X) - K * D)
    exit()
# それ以外の場合K-cのあまりを考える
rest = K - c
if rest % 2 == 0:
    ans = abs(X) - c * D
    print(ans)
    exit()
# 奇数回の場合は1回余分に移動する
ans = abs(X) - (c+1) * D
print(abs(ans))
