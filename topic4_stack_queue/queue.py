class Queue:
   def __init__(self):
      self.data=[] 

    
   def is_empty(self):
      return len(self.data) == 0
   
   def enqueue(self,value):
      self.data.append(value)

   def dequeue(self):
      
      value= self.data.pop(-1)
      return value
   
queue= Queue()
queue.enqueue(35)
queue.enqueue(59)
queue.enqueue(67)

value = queue.dequeue()
print(value)