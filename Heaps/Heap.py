class MinHeap:
    
    def __init__(self, array=[]):

        self.heap_arr = array
        
        self.heapify(self.array)
    
    def heapify(self, heap_arr):
        
        for i in range(len(heap_arr)): #Sink each element in array to its position
            
            self.sink_root(heap_arr)
    
    
    def sink_root(heap_arr):
        
        i = 0 
        
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
        
        i = len(heap_arr) - 1
             
                
                
            
            
            
            
            
            
            
