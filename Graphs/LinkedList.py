class Node:
  
  def __init__(self, value, next, previous):
    
    self.value, self.next, self.previous = value, next, previous
    
    
  
class DoubleLinkedList:
  
  def __init__(self):
    
    self.head, self.tail, self.len = None, None,None, 0#Initialise empty LinkedList
    
  def append_node(self, value):
      
    new_node = (value, None, self.tail)
    
    ##Different logic for not thefirst element to be added
    if self.len != 0:
  
      self.tail.next = new_node #Point current tail forward to new node
      
    self.tail = new_node #Point tail of list to new node.
    
    self.len += 1
  
  def extract_first_val(self):
    
    val_return = self.head.value
    
    self.head = self.head.next #Point head to next in list.
    
    self.head.previous = None #Remove the referance to the old head.
    
    self.len -= 1 
    
    return val_return
  
  def extract_last_val(self):
    
    val_return = self.tail.value
    
    self.tail = self.tail.previous #Point the global tail to second last element.
    
    self.tail.next = None #Point the new tail to nothing.
    
    self.len -= 1
    
    reuturn val_return
  
  def print_list(self):
    
    temp_pointer = self.head
    
    while temp_pointer is not None:
      
      print(temp_pointer.value)
      
      temp_pointer = temp_pointer.next
    
    
    
  
    
