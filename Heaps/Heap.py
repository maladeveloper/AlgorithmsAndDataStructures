import math

class MinHeap:

    def __init__(self, array=[]):

        self.heap_arr = array
        
        self.heapify(self.heap_arr)


    
    def heapify(self, heap_arr):
        
        for i in range(len(heap_arr)-1 , -1, -1): #Sink each element in array to its position
            
            self.sink_node(heap_arr, i)
        
    
    def sink_node(self, heap_arr, start_ind):
        
        i = start_ind
        
        while True:
            
            child_one_pos = (i*2 + 1)
            
            if child_one_pos < len(heap_arr): #Check if node has atleast one child
                
                min_child_pos = child_one_pos
                
                child_two_pos = (i*2 + 2)
                
                if  child_two_pos < len(heap_arr): #Check if it has a second child
                    
                    min_child_pos = min( [(heap_arr[child_one_pos], child_one_pos), (heap_arr[child_two_pos], child_two_pos)], key=lambda child_info: child_info[0])[1] #Get the minimum value child's position
                    
            else: #If it doesnt have a child then it has moved to correct position
                
                break
            
            if heap_arr[min_child_pos] < heap_arr[i]: #Swap if current node is smaller than the smallest child
                
                heap_arr[i], heap_arr[min_child_pos] = heap_arr[min_child_pos], heap_arr[i] #Swap nodes
                
                i = min_child_pos #Update the new index of the current node
            
            else: #This means current node is smaller than its child and can be kept in the same place
                
                break
    
    def add_element(self, new_element):
        
        self.heap_arr.append(new_element)
        
        self.float_up(self.heap_arr)

    
    def float_up(self, heap_arr):
        
        i = len(heap_arr) - 1 #Start at the end

        while True:

            ##Find the parent position
            temp_parent = i/2

            if temp_parent % 1 == 0 : #If right child then need to minus 1 

                parent_pos = temp_parent - 1

                if parent_pos <= 0: #This mean current node is parent

                    break

            else: #This means left child 

                parent_pos = int(math.floor(temp_parent))
                        
            ##Compare and swap with parent
            if heap_arr[parent_pos] > heap_arr[i]:

                heap_arr[i], heap_arr[parent_pos] = heap_arr[parent_pos], heap_arr[i]

                i = parent_pos
            
            else:#Means node is in correct position

                break
    
    def extract_min(self):

        extracted_min = self.heap_arr[0]

        ##Reestablish heap property by moving last element to root and letting it sink
        self.heap_arr[0] = self.heap_arr[-1]

        self.heap_arr.pop()

        self.sink_node(self.heap_arr, 0)

        return extracted_min

    
    def insert_item(self, new_item):

        self.heap_arr.append(new_item)

        ##Reestablish heap property by floating new element up to where it belongs
        self.float_up(self.heap_arr)




        

        




            


            

        

                


             
                
#[0,1,2,3,4] floor(index/2)
# 
#               0
#           1       2
#       3      4 
# 
# 
#    
            
            
            
            
            
            
