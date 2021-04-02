import random

def quick_sort(arr):

    start, end =  0, len(arr)-1

    def sort(arr, start, end):

        if start - end == 1 : #Already sorted if only elem or no elem

            return arr

        pivot = random.randint(start, end )

        arr[pivot], arr[end], pivot = arr[end], arr[pivot], end #Move pivot elem to end

        swap_pos = end - 1 #First free position to swap to

        ##Partition the array to one side larger than pivot and other smaller
        for com_pos in range(end-1, start-1, -1):

            if arr[com_pos] > arr[pivot]:

                arr[com_pos], arr[swap_pos] = arr[swap_pos], arr[com_pos]

                swap_pos -= 1 #Update the next position to swap to
        
        arr[pivot], arr[swap_pos+1], pivot = arr[swap_pos+1], arr[pivot], swap_pos+1 #Swap pivot to last item that was swapped. 

        ##Call quick sort on both the partitions either side of pivot
        sort(arr, start, pivot-1)

        sort(arr, pivot+1, end)
    
    sort(arr, start, end)

if __name__ == "__main__":

    arr = [3, 21, 123, 2, 1, 2, 3, 48, 12, 10, 13]

    print(f'''Using merge sort to sort the following array {arr}...''')
    
    quick_sort(arr)

    print(f'''Sorted array is: {arr}''')