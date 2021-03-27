'''
Given an array of integers, find the subset of non-adjacent elements with the maximum sum. 
Calculate the sum of that subset. It is possible that the maximum sum is , 
the case when all elements are negative.
'''
#Problem taken from Hackerrank - Solutions are my own.
def max_subset_sum(arr):
    
    ##Exit base case
    if len(arr) < 1:
        
        return None

    memo_arr = [None]*len(arr) #Initiate memoization which stores the max for each  index
    
    def find_max_subset(start_index):
        
        ##Initiate base case
        if start_index == len(arr) - 1:
            
            memo_arr[start_index] = arr[start_index]
            
            return arr[start_index]
        
        ##Make function stack calss
        if memo_arr[start_index + 1] is None: #Solution not stored.
            
            find_max_subset(start_index + 1)
        
        if start_index == len(arr) -2: #If second last then max itself
            
            memo_arr[start_index] = arr[start_index]
            
            return arr[start_index]
        
        ##The max of current index is either max of subset with or without this element or element itself
        subset_max = max(memo_arr[start_index + 2:])
       
        include_element = arr[start_index] + subset_max
        
        exclude_element = subset_max

        only_element = arr[start_index]
        
        memo_arr[start_index] = max(include_element, exclude_element, only_element)
        
        return memo_arr[start_index]
    
    find_max_subset(0)

    return max(memo_arr)

if __name__ == "__main__":

    test_arrays ={

        "Test-1":{
            "array": [3, 7, 4, 6, 5],
            "solution": 13
        },

        "Test-2":{
            "array": [2, 1, 5, 8, 4],
            "solution": 11
        },

        "Test-3":{
            "array": [3, 5, -7, 8, 10],
            "solution": 15
        },

        "Test-4":{
            "array": [-1],
            "solution": -1
        },

        "Test-5":{
            "array": [-3, -7, -1, -2, -3, -4],
            "solution": -1
        },

        "Test-6":{
            "array": [],
            "solution": None
        },
    }

    for test, test_info in test_arrays.items():

        if test_info["solution"] == max_subset_sum(test_info["array"]):

            print(f'''{test}...PASS''')
        
        else:

            print(f'''{test}...FAIL''')