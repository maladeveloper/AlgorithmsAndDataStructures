from SingleLinkedList import Linked List

'''
Code for reversing a list was written by me.
'''

my_list = LinkedList()

my_list.append("M")

my_list.append("A")

my_list.append("L")

my_list.print_list()
    
def reverse_list(prev_node, curr_node):
    
    if curr_node.next is not None:
        
        reverse_list(curr_node, curr_node.next)
    
    else:
        
        my_list.tail = my_list.head
        
        my_list.head = curr_node
    
    curr_node.next = prev_node


reverse_list(None, my_list.head)

print(f'''-----------reversedlist---------------''')

my_list.print_list()
