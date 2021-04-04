from pprint import pprint
from math import factorial


'''
Uses backtracking to achieve combinations without replacement
TODO:NEED TO FIX
'''
def backtrack_combinations_wo_replacement(arr , r):

    all_combs = []

    def backtrack_comb(arr, k_group):

        if len(arr) < k_group:

            return 
        
        next_pos, k_wo_first = 1, k_group-1

        next_vals = next_pos + k_wo_first

        while  next_vals <= len(arr):

            first_val_arr = [arr[0]]

            first_val_arr.extend(arr[next_pos : next_vals])

            if first_val_arr not in all_combs:
                
                all_combs.append(first_val_arr)

            next_pos += 1

            next_vals = next_pos + k_wo_first

        backtrack_comb(arr[1:], k_group)

    backtrack_comb(arr, r)

    return set([tuple(comb) for comb in all_combs])



def permutations(arr, r_original, replace=True):

    all_perms = []

    def permutate(arr,r):

        if r == 1:
            
            return_arr = [j for j in arr]
            
            return return_arr
        
        perms = []

        for i in range(len(arr)):
            
            new_arr = arr if replace else (arr[:i]+arr[i+1:])
            
            new_perms = permutate(new_arr, r-1)

            for n_perm in new_perms:
                
                i_perm = [arr[i]]
                
                i_perm.extend(n_perm)
                
                perms.append(i_perm)
            
        return perms
    
    all_perms =set( [tuple(perm) for perm in permutate(arr, r_original)])
    
    return all_perms


def permutations_wo_replacement(arr, r):

    return permutations(arr, r, replace=False)

def permutations_w_replacement(arr, r):

    return permutations(arr, r, replace=True)

def combinations_w_replacement(arr, r):

    ##Find all permutations with replacement
    all_perms_tuple = permutations_w_replacement(arr, r)

    all_perms_arr = [list(perm) for perm in all_perms_tuple]

    [perm.sort() for perm in all_perms_arr]

    return set([tuple(perm) for perm in all_perms_arr])

def combinations_wo_replacement(arr, r):

    ##Find all permutations without replacement
    all_perms_tuple = permutations_wo_replacement(arr, r)

    all_perms_arr = [list(perm) for perm in all_perms_tuple]

    [perm.sort() for perm in all_perms_arr]

    return set([tuple(perm) for perm in all_perms_arr])

def calculate_perms(n, r, replace=True):

    if replace:

        return n**r
    
    return factorial(n)/factorial(n-r)

def calculate_combs(n, r, replace=True):

    if replace:

        return factorial(r + n -1)/(factorial(r) * factorial(n-r))
    
    return factorial(n)/(factorial(r) * factorial(n-r))








