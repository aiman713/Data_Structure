
class Heap:
    def __init__(self):
        self.data=[]

    def add(self, value):
        self.data.append(value)
        self.heapify_up()

    def parent_of(self,p):
        return(p-1)//2

    def left_child(self,p):
        child= p*2 +1
        if child < len(self.data):
            return child
        else:
            return None
        
    def right_child(self,p):
        child=p*2 +2
        if child< len(self.data):
            return child
        else:
            return None
        
    def heapify_up(self):
        p=len(self.data)-1
        while p >0 :
            parent=self.parent_of(p)
            if self.data[p] < self.data[parent]:
                self.data[p], self.data[parent]= self.data[parent], self.data[p]
                p=parent
            else:
                break
        
    def is_empty(self):
        return len(self.data)==0
    
    def get_next(self):
        if self.is_empty():
            return None
        next=self.data[0]
        self.data[0]=self.data[-1]
        self.data.pop(-1)
        self.heapify_down()
        return next
    
    def heapify_down(self):
        p=0
        while True:
            left=self.left_child(p)
            right=self.right_child(p)
            if left is None:
                break
            elif right is None:
                child_pos = left
            else:
                child_pos = left if self.data[left]< self.data[right] else right
            if self.data[child_pos] < self.data[p]:
                self.data[child_pos], self.data[p]=self.data[p] , self.data[child_pos]
                p=child_pos
            else:
                break

heap=Heap()
heap.add(50)
print(heap.data)
heap.add(30)
print(heap.data)
heap.add(100)
print(heap.data)
heap.add(20)
print(heap.data)
heap.add(60)
print(heap.data)
heap.add(45)
print(heap.data)
heap.add(10)
print(heap.data)
heap.get_next()
print(heap.data)