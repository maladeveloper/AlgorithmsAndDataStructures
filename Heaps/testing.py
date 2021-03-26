from Heap import MinHeap

test_arr = [7,12,3,1,2]

my_heap = MinHeap(array=test_arr)

print(my_heap.heap_arr)
print(my_heap.extract_min())
print(my_heap.extract_min())
print(my_heap.extract_min())
print(my_heap.extract_min())
print(my_heap.heap_arr)

for item in test_arr:

    my_heap.add_element(item)
    print(my_heap.heap_arr)


