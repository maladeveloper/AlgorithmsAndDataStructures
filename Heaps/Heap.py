class MinHeap:
    
    def __init__(self, array=[]):

        self.heap_arr = array
        
        self.heapify(self.array)
    
    def heapify(self, heap_arr):
        
        for i in range(len(heap_arr)):
            
            self.sink_root(heap_arr)
    
    
    def sink_root(heap_arr):
        
        i = 0 
        
        while True:
            
            
            
            
            
            
