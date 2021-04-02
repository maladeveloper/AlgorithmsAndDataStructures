import random
import time
from insertion_sort import insertion_sort
from selection_sort import selection_sort
from merge_sort import merge_sort
from bubble_sort import bubble_sort
from quick_sort import quick_sort
from heap_sort import heap_sort

tester_arr = random.sample(range(1, 10000000), 15000)

sorted_arr = tester_arr[:]

sorted_arr.sort()

def built_in_sort(arr):

    arr.sort()

    return

battle_sorting_contestents = {

    "Insertion Sort": insertion_sort, 

    "Selection Sort": selection_sort, 

    "Merge Sort": merge_sort, 

    "Bubble Sort": bubble_sort, 

    "Quick Sort": quick_sort,

    "Heap Sort": heap_sort, 

    "Built-In Sort": built_in_sort
}

for name, sort_func in battle_sorting_contestents.items():

    copy_arr = tester_arr[:]

    print(f'''-----------------------------------------------\nSort: {name}''')

    t0 = time.time()

    sort_func(copy_arr)

    t1 = time.time()

    t_delta = t1 - t0

    status = "FAIL"
    
    if copy_arr == sorted_arr:

        status = "PASS"
    
    print(f'''Test Status: {status}\nSort Runtime: {t_delta}\n-----------------------------------------------\n''')


    