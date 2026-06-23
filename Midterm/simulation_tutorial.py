import random
import time
import string

used_flights=[]

def generate_flight_number(taken):
    while True:
        letter= random.choice(string.ascii_uppercase)
        num= random.randint(1000,9999)
        flight = letter + str(num)
        if flight not in taken:
            taken.append(flight)
            return flight

def create_flight_request():
    probability=random.randint(1,100)
    if probability <=5:
        request_type="Emergency"
    elif probability <= 60:
        request_type = "Landing"
    else:
        request_type="take off"
    return request_type

for i in range(20):
    probability= random.randint(1,100)
    if probability <30:
        action_type=2
    else:
        action_type=1
    if action_type==1:
        print("Create flight request")
        request=create_flight_request()
        flight=generate_flight_number(used_flights)

        print(f"{request} by {flight}")
    else:
        print("Control decision")
    time.sleep(random.randint(2,5))