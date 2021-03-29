from LinkedList import DoubleLinkedList

class Queue: 

    def __init__(self):

        self.queue_list = DoubleLinkedList()
    
    def queue(self, value):

        self.queue_list.add_to_front(value)
    
    def dequeue(self):

        self.queue_list.extract_last_val()
    
    def print_queue(self):
        
        self.queue_list.print_list()