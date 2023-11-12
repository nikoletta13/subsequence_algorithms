# the_game

import numpy as np
from itertools import permutations

# what is that product package

# produce all possible arrangements of numbers 2-99

# for each arrangement, try to find the 4 subsequences
numbers = np.arange(2,10)

combs = permutations(numbers,len(numbers))

arrangements = []
for item in combs:  
    arrangements.append(item)

for seq in arrangements:
    used = []
    s1 = ()
    n0 = seq[0]
    s1.append(n0)
    for j in range(1,10): # ascending
        if seq[j]>n0:
            s1.append(seq[j])
            n0 = seq[j]
            used.append(j)
    s2 = ()
            
        