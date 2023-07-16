from itertools import permutations

S, K = input().split()
K = int(K)
cands = list(permutations(S))
cands = list(set(cands))
ans_list = sorted(cands)
print("".join(ans_list[K-1]))
