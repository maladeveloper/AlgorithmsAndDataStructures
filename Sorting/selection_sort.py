def selection_sort(arr):

    for sorted_pos in range(len(arr)):

        ##Find the minimum between the sorted position and the rest of array
        min_pos = sorted_pos

        for compare_pos in range(sorted_pos, len(arr)):

            if arr[compare_pos] < arr[min_pos]:

                min_pos = compare_pos
        
        arr[sorted_pos], arr[min_pos] = arr[min_pos], arr[sorted_pos] #Swap to sorted position


if __name__ == "__main__":

    arr = [3, 21, 123, 2, 1, 2, 3, 48, 12, 10, 13]

    print(f'''Using selection sort to sort the following array {arr}...''')
    
    selection_sort(arr)

    print(f'''Sorted array is: {arr}''')