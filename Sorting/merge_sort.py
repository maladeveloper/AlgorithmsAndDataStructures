

def merge_arr(arr_1, arr_2):

    merged_arr, ind_1, ind_2 = [], 0, 0

    while len(merged_arr) < (len(arr_1) + len(arr_2)):

        if ind_1 == len(arr_1): #At the end of first array add the rest of second

            merged_arr.extend(arr_2[ind_2:])
        
        elif ind_2 == len(arr_2) : #End of second array add the rest of first.

            merged_arr.extend(arr_1[ind_1:])
        
        ##Add the smallest item to merged list from both arrays
        elif arr_1[ind_1] < arr_2[ind_2]:

            merged_arr.append(arr_1[ind_1])

            ind_1 += 1
        
        else:

            merged_arr.append(arr_2[ind_2])

            ind_2 += 1 
    
    return merged_arr


def merge_sort(arr):

    temp_arr = arr[:]

    def mergesort(arr):

        if len(arr) == 1: #Already sorted if only element

            return arr
        
        mid_pos = len(arr) // 2 

        arr = merge_arr(mergesort(arr[:mid_pos]), mergesort(arr[mid_pos:]))

        return arr
    
    sorted_arr =mergesort(temp_arr)
    
    for i in range(len(sorted_arr)):

        arr[i] = sorted_arr[i]


if __name__ == "__main__":

    arr = [3, 21, 123, 2, 1, 2, 3, 48, 12, 10, 13]

    print(f'''Using merge sort to sort the following array {arr}...''')
    
    merge_sort(arr)

    print(f'''Sorted array is: {arr}''')