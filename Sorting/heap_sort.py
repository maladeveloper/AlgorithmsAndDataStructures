from heap import MinHeap

def heap_sort(arr):

    sorted_arr = []

    min_heap = MinHeap(array=arr)

    for i in range(len(arr)):

        sorted_arr.append(min_heap.extract_min())
        
    for i in range(len(sorted_arr)):

        arr.append(sorted_arr[i])

if __name__ == "__main__":

    arr = [3, 21, 123, 2, 1, 2, 3, 48, 12, 10, 13]

    print(f'''Using heap sort to sort the following array {arr}...''')
    
    heap_sort(arr)

    print(f'''Sorted array is: {arr}''')