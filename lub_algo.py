"""
Algorithm for L(N), defined as the lowest upper bound of mutually exclusive subsequences for
a sequence of N distinct numbers. For full description see https://nikoletta13.github.io/thisisalsoagame/Tangents/The-function-L(N)
"""
from math import sqrt, log1p

import matplotlib.pyplot as plt


def L(N, description=False):
    """
    Algorithm for determining L(N). Result based on Erdos-Szekeres Theorem. 
    To see description for why L(N) is calculated as such set description to True. 

    input
    -----
    N: int, number of items
    description: boolean, option to print descriptions
    """
    M=N
    n = int(sqrt(M-1))
    i = 0
        
    if description:
        print(f'Determine L({N}):')
        print(f'The greatest integer whose square is less than M-1={M-1} is {n}.')
    while M>0:
        if description:
            print(f'{M} - ({n}+1) = {M-n-1}, so set M to {M-n-1}.')
        i+=1
        if description:
            print(f'At this stage, we have removed the longest subsequence {i} times.')
        M -= n+1 
        if M <= n**2:
            n-=1
        if description:    
            if M>0:    
                print(f'The greatest integer whose square is less than M-1={M-1} is {n}.')

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