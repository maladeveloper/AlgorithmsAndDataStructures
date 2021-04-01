from SingleLinkedList import Linked List

'''
Code for reversing a list via both functions was written by me.
'''

my_list = LinkedList()

my_list.append("M")

my_list.append("A")

my_list.append("L")

my_list.print_list()

##Implementation of reversing a linked list using recursion
def reverse_list(prev_node, curr_node):
    
    if curr_node.next is not None:
        
        reverse_list(curr_node, curr_node.next)
    
    else:
        
        my_list.tail = my_list.head
        
        my_list.head = curr_node
    
    curr_node.next = prev_node


reverse_list(None, my_list.head)

print(f'''-----------reversed list---------------''')

my_list.print_list()

##Implementation of reversing a list using for loops.
def reverse_list(my_list):
    
    temp_stack = []
    
    ##Put the referances and the nodes to the stack 
    curr_node = my_list.head
    
    while curr_node.next is not None:
        
        next_node = curr_node.next
        
        temp_stack.append([curr_node, next_node])
        
        curr_node = curr_node.next
    
    my_list.head.next = None #Current head to be tail point None
    
    ##Now reverse the stack and point the new referances
    for i in range(len(temp_stack)-1, -1, -1):            
        
        next_node, curr_node = temp_stack[i]
        
        curr_node.next = next_node
    
    my_list.head = temp_stack[-1][-1]
        
reverse_list(my_list)

print(f'''-----------reversed list---------------''')

my_list.print_list()
