from Queue import Queue

my_queue = Queue()

test_list = ["M", "A", "L", "A", "V"]



for value in test_list:

    my_queue.queue(value)
    
    my_queue.print_queue()
    
    print("-------------------------------------")

for _ in range(len(test_list) - 1):

    my_queue.dequeue()

    my_queue.print_queue()

    print("-------------------------------------")