import random
import string


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

            if self.data [p] < self.data [parent]:
                self.data[p], self.data [parent]= self.data [parent] , self.data [p]
                p=parent
            else:
                break
        
    def is_empty(self):
        return len(self.data)==0
    
    def get_next(self):
        if self.is_empty():
            return None
        if len(self.data) == 1:
            return self.data.pop()

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



counter = 0  

class Flight:
    def __init__(self, flight_id, request):
        global counter
        self.flight_id = flight_id
        self.request = request

        if request == "Emergency":
            self.priority = 0
        else:
            self.priority = 1

        self.order = counter
        counter += 1

    def __lt__(self, other):
        if self.priority == other.priority:
            return self.order < other.order
        return self.priority < other.priority



used_flights=[]

def generate_flight_num(taken):
    while True:
        letter= random.choice(string.ascii_uppercase)
        num= random.randint(1000,9999)
        flight = letter + str(num)
        if flight not in taken:
            taken.append(flight)
            return flight

def create_flight_req():
    probability=random.randint(1,100)
    if probability <=5:
        return "Emergency"
    elif probability <= 60:
        return "Landing"
    else:
        return "Takeoff"



landing_queue = Heap()   
takeoff_queue = []       

for i in range(20):
    probability = random.randint(1,100)

   
    if probability < 40:
        if not landing_queue.is_empty():
            f = landing_queue.get_next()
            print(f"Control system: Flight no: {f.flight_id} landed")

        elif len(takeoff_queue) > 0:
            f = takeoff_queue.pop(0)
            print(f"Control system: Flight no: {f.flight_id} Take-Off")

        else:
            print("Control system: There are no waiting flights ")

    
    else:
        request = create_flight_req()
        flight_id = generate_flight_num(used_flights)

        if request == "Flight Takeoff":
            takeoff_queue.append(Flight(flight_id, request))
            print(f"Flight No: {flight_id} requests for Take-Off")

        elif request == "Flight Landing":
            landing_queue.add(Flight(flight_id, request))
            print(f"Flight No: {flight_id} requests for landing")

        else:
            landing_queue.add(Flight(flight_id, request))
            print(f"Flight No: {flight_id} requests emergency landing")