class Node:

  def __init__(self, value, next, previous):

    self.value, self.next, self.previous = value, next, previous



class DoubleLinkedList:

  def __init__(self):

    self.head, self.tail, self.len = None, None, 0#Initialise empty LinkedList

  def append(self, value):

    new_node = Node(value, None, self.tail)

    ##Different logic for  the first element to be added
    if self.len == 0:#The first item will also be the head

      self.head = new_node

    else:

      self.tail.next = new_node #Point current tail forward to new node

    self.tail = new_node #Point tail of list to new node.

    self.len += 1

  def add_to_front(self, value):

    new_node = Node(value, self.head, None)

    ##Different logic for not the first element
    if self.len == 0:

      self.tail = new_node

    else:

      self.head.previous = new_node

    self.head = new_node

    self.len += 1

  def extract_first_val(self):

    val_return = self.head.value

    self.head = self.head.next #Point head to next in list.

    self.len -= 1 

    if self.len > 0:#Not if there is nothing there
      
      self.head.previous = None #Remove the referance to the old head.

    else:

      print("No More elements to extract !")

      self.len = 0

    

    return val_return

  def extract_last_val(self):

    val_return = self.tail.value

    self.tail = self.tail.previous #Point the global tail to second last element.
    
    self.len -= 1

    if self.len > 0:#No need to worry about

      self.tail.next = None #Point the new tail to nothing.
    
    else:

      print("No More elements to extract !")

      self.len = 0

    

    return val_return

  def print_list(self):

    temp_pointer = self.head

    while temp_pointer is not None:

      print(temp_pointer.value)

      temp_pointer = temp_pointer.next


