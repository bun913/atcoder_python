# -*- coding: utf-8 -*-
"""
AもBもたかだか10**2なので、3重ループになっても大丈夫
"""

T = int(input())
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

octs = sorted(A)
customers = sorted(B)

# そもそもたこ焼きが足らない
if len(octs) < len(customers):
    print("no")
    exit()

ok_custmor_list = [False for _ in range(len(customers))]
for c_ind, c in enumerate(customers):
    for o_ind in range(len(octs)):
        oct = octs[o_ind]
        if c >= oct and c - oct <= T:
            ok_custmor_list[c_ind] = True
            octs.pop(o_ind)
            break
if all(ok_custmor_list) is True:
    print("yes")
    exit()
print("no")
