"""
0が含まれないNが与えられる
Nの桁を任意の数を消して（消さないでもよい）3の倍数を作ることができるか
たしか、各桁の数字を足して3の倍数になればよかったはず
Nがたかだか10の18**なので全探索でも良さそう
"""
from itertools import product

N = input()
ans = 50
for use_flags in product([True, False], repeat=len(N)):
    num_list = []
    for i, is_use in enumerate(use_flags):
        if is_use is True:
            num_list.append(int(N[i]))
    if len(num_list) == 0:
        continue
    if sum(num_list) % 3 == 0:
        ans = min(ans, len(N) - len(num_list))
if ans == 50:
    print(-1)
    exit()
print(ans)
