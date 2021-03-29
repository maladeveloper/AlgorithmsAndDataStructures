from Stack import Stack
from Queue import Queue

my_stack = Stack()

test_list = ["M", "A", "L", "A", "V"]

for value in test_list:

    my_stack.push(value)
    
    my_stack.print_stack()
    
    print("-------------------------------------")

for _ in range(len(test_list) - 1):

    my_stack.pop()

    my_stack.print_stack()

    print("-------------------------------------")


    