
def insertion_sort(arr):

    for comp_pos in range(1, len(arr)):

        swap_pos = comp_pos - 1 

        ##Swap current item down to place in ordered k elements from 0->comp_pos
        while swap_pos >= 0:

            if arr[swap_pos] > arr[comp_pos]:

                arr[swap_pos], arr[comp_pos], comp_pos = arr[comp_pos], arr[swap_pos], swap_pos

                swap_pos -= 1 
            
            else: #Break since element in correct position as it hasnt swapped.

                break 

if __name__ == "__main__":

    arr = [3, 21, 123, 2, 1, 2, 3, 48, 12, 10, 13]

    print(f'''Using insertion sort to sort the following array {arr}...''')
    
    insertion_sort(arr)

    print(f'''Sorted array is: {arr}''')