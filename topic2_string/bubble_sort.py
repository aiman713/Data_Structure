import random

data=[random.randint(1, 100) for i in range(10)]
print(data)

n= len(data)
stop= n-1

print("===SORTING===")
for i in range(n-1):
    for pos in range(stop):
        if data[pos] > data[pos+1]:
            data[pos], data[pos+1] = data[pos+1], data[pos]
    stop-=1

print(data)