"""
Algorithm for L(N).
"""
from math import sqrt, log1p

import matplotlib.pyplot as plt


def L(N):
    M=N
    n = int(sqrt(M-1))
    i = 0
    # print(f'Determine L({N}):')
    # print(f'The greatest integer whose square is less than M-1={M-1} is {n}.')
    while M>0:
        # print(f'{M} - ({n}+1) = {M-n-1}, so set M to {M-n-1}.')
        i+=1
        # print(f'At this stage, we have removed the longest subsequence {i} times.')
        M -= n+1 
        if M <= n**2:
            n-=1
        # if M>0:    
            # print(f'The greatest integer whose square is less than M-1={M-1} is {n}.')

    return i

L_N_arr = [L(N) for N in range(2,1000)]
# nln = [sqrt(n)/log1p(n) for n in range(2,1000)]

plt.figure()
plt.scatter([x for x in range(2,1000)], L_N_arr, marker='.')
# plt.plot(nln)
plt.xlabel('N')
plt.ylabel('L(N)')
plt.tight_layout()
plt.show()