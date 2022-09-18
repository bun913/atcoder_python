"""
1以上N以下の人は時刻tに宝石をもらうとSi時間後にi+1の人に渡す
高橋はTiにi番目のすぬけくんに宝石を渡す

つまり前の人から宝石をもらう時間か、高橋くんからもらう時間か早い方を答えるということ
回した場合と高橋からもらう場合の最小値を求める
"""
N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

# 高橋くんから宝石がもらえる時間を初期値としてメモ
results = [T[i] for i in range(N)]
# 2周回して各人の最小値の結果を反映してあげる
for i in range(2 * N):
    cur = i % N
    bef = (i + N - 1) % N
    # 前の人から渡ってくる時間をcandとして、高橋くんからもらえる時間との最小値を取る
    cand = results[bef] + S[bef]
    results[cur] = min(cand, results[cur])
print(*results, sep="\n")
