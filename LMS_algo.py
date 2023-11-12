"""
Calculate longest monotone subsequence (LMS).
"""
from itertools import permutations
from sympy import factorial
from random import shuffle, randint, sample



def LIS(l):
    """
    Find the longest increasing subsequence of l using the algorithm 
    by Fredman (1975) (credited to Donald Knuth).
    This algorithm uses at most n log_2 n - n log_2 log_2 n + O(n) comparisons. 
    """
    n = len(l)
    if n==1:
        return l
    if n==2:
        if l[0]<l[1]:
            return l
        else:
            return [l[0]]
    newL = 1
    L=0
    best_seqs_dict = {}
    best_seqs_dict[1] = [l[0]] 
    for i in range(2,n):
        # check if c_i can be appended to the longest existing subseq
        if l[i]>best_seqs_dict[newL][-1]:
            newL+=1 # new longest subseq
            best_seqs_dict[newL] = best_seqs_dict[newL-1] + [l[i]] # create it
            print('appended to longest')
            input(best_seqs_dict)
        else:
            for j in range(newL,0,-1):
                if j>1:
                    if l[i]<best_seqs_dict[j][-1] and l[i]>best_seqs_dict[j-1][-1]:
                        best_seqs_dict[j] = best_seqs_dict[j-1] + [l[i]]
                        input('replaced a not best')
                        print(best_seqs_dict)
                        break
                else:
                    if l[i]<best_seqs_dict[1][0]: # if it does get to this then this is trivially satisfied
                        best_seqs_dict[1] = [l[i]]    
                        print('replaced 1')
                        input(best_seqs_dict)
    return best_seqs_dict                    



def LDS(l):
    """
    Find the longest decreasing subsequence of l using the algorithm 
    by Fredman (1975) (credited to Donald Knuth).
    This algorithm uses at most n log_2 n - n log_2 log_2 n + O(n) comparisons. 
    """
    n = len(l)
    if n==1:
        return l
    if n==2:
        if l[0]>l[1]:
            return l
        else:
            return [l[0]]
    newL = 1
    L=0
    best_seqs_dict = {}
    best_seqs_dict[1] = [l[0]] 
    for i in range(2,n):
        # check if c_i can be appended to the longest existing subseq
        if l[i]<best_seqs_dict[newL][-1]:
            newL+=1 # new longest subseq
            best_seqs_dict[newL] = best_seqs_dict[newL-1] + [l[i]] # create it
            print('appended to longest')
            input(best_seqs_dict)
        else:
            for j in range(newL,0,-1):
                if j>1:
                    if l[i]>best_seqs_dict[j][-1] and l[i]<best_seqs_dict[j-1][-1]:
                        best_seqs_dict[j] = best_seqs_dict[j-1] + [l[i]]
                        input('replaced a not best')
                        print(best_seqs_dict)
                        break
                else:
                    if l[i]>best_seqs_dict[1][0]: # if it does get to this then this is trivially satisfied
                        best_seqs_dict[1] = [l[i]]    
                        print('replaced 1')
                        input(best_seqs_dict)
    return best_seqs_dict     





l = [0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15]

print(LIS(l))
print(LIS_new(l))

input('asdgf')

def LMS(l):
    """
    Find the longest monotone subsequence of l by comparing LIS and LDS.
    """
    # D = LDS(l)
    # I = LIS(l)
    D_seq = LDS(l)
    I_seq = LIS(l)    
    d_max = len(D_seq)
    i_max = len(I_seq)
    if d_max>i_max:
        return D_seq,'D'
    else:# d_max<i_max:
        return I_seq, 'I'
    # else: # here they are equal 
    #     decision = input('decide I or D')
    #     if str(decision) == 'D':
    #         return D[d_max],'D'
    #     else:
    #         return I[i_max], 'I'



def monotone_subseq(l):
    """
    Given a list l, return subsequences. eventually make this smarter
    """
    n = len(l)
    subseqs = []
    removed_from_l = []
    f_l = l
    # D_count = 0
    # I_count = 0
    while len(f_l)>0:
        new_subseq,sign = LMS(f_l)
    #     if sign == 'D':
    #         D_count += 1
    #     else:
    #         I_count += 1
        subseqs.append(new_subseq)
        # input(new_subseq)
        f_l = [x for x in f_l if x not in new_subseq] 
    return len(subseqs)

# print(monotone_subseq(ll))

def M_N(n):
    current_max = 0
    seqs = permutations(range(1,n+1))
    i = 0
    for seq in seqs:
        # print(f'{i}/{factorial(n+1)}')
        n_seq = monotone_subseq(seq)
        if n_seq>current_max:
            current_max = n_seq
            # max_seq = seq
        i+=1
        if i>factorial(n)/2:
            break    

    # all_perms = list(permutations(range(1,n+1)))
    # # l_dict = {}
    # current_max = 0
    # for seq in all_perms:
    #     n_seq = monotone_subseq(seq)
    #     # l_dict[seq] = n_seq
    #     if n_seq>current_max:
    #         current_max = n_seq
    #         max_seq = seq

    return current_max#,max_seq#,l_dict
    

# for i in range(11,16):
#     print(M_N(i))



print(M_N(12))

# deck = [x for x in range(2,100)]


# shuffle(deck)

# print(monotone_subseq(deck))


def M_N_shuffle_approx(n):
    current_max = 0
    deck = [x for x in range(2,100)]
    for i in range(n):
        # print(f'{i}/{factorial(n+1)}')
        shuffle(deck)
        n_seq = monotone_subseq(deck)

        if n_seq>current_max:
            current_max = n_seq
            # max_seq = seq

    # all_perms = list(permutations(range(1,n+1)))
    # # l_dict = {}
    # current_max = 0
    # for seq in all_perms:
    #     n_seq = monotone_subseq(seq)
    #     # l_dict[seq] = n_seq
    #     if n_seq>current_max:
    #         current_max = n_seq
    #         max_seq = seq

    return current_max#,max_seq#,l_dict
    

# print(M_N_shuffle_approx(10))