from LinkedList import DoubleLinkedList

class Stack:

    def __init__(self):

        self.stack_list = DoubleLinkedList()
    
    def push(self,value):

        self.stack_list.add_to_front(value)

    def pop(self):

        return self.stack_list.extract_first_val()
    
    def print_stack(self):

        self.stack_list.print_list()


