
class Listnode:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

    def __str__(self):
        return str(self.data)
    
class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail=None

    def insert(self,value):
        new_node=Listnode(value)


        #If the List is empty 
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
    
    def display_frwd(self):
        iterator=self.head
        while iterator is not None:
            print(iterator, end=" ")
            iterator=iterator.next
        print()
    
    def display_back(self):
        iterator=self.tail
        while iterator is not None:
            print(iterator, end=" ")
            iterator=iterator.prev
        print()

    def find(self,value):
        iterator=self.head
        while iterator is not None:
            if iterator.data==value:
                return iterator
            iterator=iterator.next
        return None
    
    def remove(self,value):
        iterator=self.head
        while iterator is not None:
            if iterator.data==value:

                #if remove from head
                if iterator==self.head:
                    self.head=iterator.next #The next iterator becomes head
                    if self.head is not None: 
                        self.head.prev=None
                    else:
                        self.tail=None #If self.head none means self.tail is also none and list is empty

                #If remove from tail
                elif iterator==self.tail:
                    self.tail=iterator.prev
                    self.tail.next=None

                #if want to remove from middle
                else:
                    iterator.prev.next=iterator.next
                    iterator.next.prev=iterator.prev
                return True
            iterator=iterator.next
        return False

data=Linkedlist()
data.insert(30)
data.insert(20)
data.insert(10)
data.display_frwd()

data.display_back()

it=data.find(20)
print(f'Looking for 20 and found {it}')
it =data.find(40)
print(f'Looking for 40 and found {it}')

data.remove(10)
data.display_frwd()