

class Stack:
   def __init__(self):
      self.data=[] 

    
   def is_empty(self):
      return len(self.data) == 0
   
   def push(self,value):
      self.data.append(value)

   def pop(self):
      value= self.data.pop(-1)
      return value
   
stack= Stack()
stack.push(35)
stack.push(40)
stack.push(56)

value = stack.pop()
print(value)