
def bubble_sort(arr):

    while True:

        swapped = False

        for cur_pos in range(len(arr)-1):

            next_pos = cur_pos + 1

            if arr[next_pos] <  arr[cur_pos]:#Compare with neighbour

                arr[cur_pos], arr[next_pos] = arr[next_pos], arr[cur_pos]

                swapped = True
        
        if not swapped: #If no swaps occurs then array is in order

            break

if __name__ == "__main__":

    arr = [3, 21, 123, 2, 1, 2, 3, 48, 12, 10, 13]

    print(f'''Using bubble sort to sort the following array {arr}...''')
    
    bubble_sort(arr)

    print(f'''Sorted array is: {arr}''')



