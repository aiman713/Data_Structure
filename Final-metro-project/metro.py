import pandas as pd
import random
from collections import deque
import heapq


df=pd.read_csv ('processed_stations.csv')

class Station:
    def __init__(self, code,name, line,number):
        self.code=code
        self.name=name
        self.line=line
        self.number=number
        self.connections=  {} # empty dictionary for connecting stations.

stations=  {} # Empty dictionary to store stations.
for i in range(len(df)): # loop through every row of the DF
    code= df.iloc[i]['code'] #  get code column like (C9) from row(i) , same for name,line,serial
    name =df.iloc[i] ['name']
    line=df.iloc[i] ['line']
    number= df.iloc[i] ['serial']
    stations [code] =Station(code,name,line,number)

#Connection
for code in stations:
    station= stations[code]
    
    #Next station
    next= station.line+ str(station.number+ 1) 
    if next in stations:
        travel_time=random.randint (4, 7) #If station exists then create random travel time between 4_7 mins
        station.connections[next]= travel_time #Connect current station to next and viceversa
        stations[next].connections[code]= travel_time
    
    #Previous station
    previous=station.line + str (station.number- 1)
    if previous in stations:
        travel_time= random.randint(4, 7)
        station.connections[previous]= travel_time
        stations[previous].connections[code] =travel_time

#Change stations 
for code1 in stations: #EW8 in Paya lebar
    for code2 in stations: # CC9 in paya lebar
        if code1 != code2 and stations[code1].name == stations[code2].name: #Codes are different (EW8,CC9) , however station name is same paya lebar
            stations[code1].connections[code2] = 4 #Add 4 min for changing the line or code.
            stations[code2].connections[code1] = 4


#BFS 
def shortest_way(start,end):
    if start not in stations or end not in stations:
        return None, 0
    
    queue = deque([(start, [start])])
    visited = {start}
    
    while queue:
        cur, path = queue.popleft()
        if cur == end:
            return path, len(path) - 1
        for neighbors in stations[cur].connections:
            if neighbors not in visited:
                visited.add(neighbors)
                queue.append((neighbors, path + [neighbors]))
    
    return None, 0

#DIJKSTRA
def fastest_way(start,end):
    if start not in stations or end not in stations:
        return None, float('inf')
    
    distances = {c: float('inf') for c in stations}
    distances[start] = 0
    prev = {c: None for c in stations}
    pqueue = [(0, start)]
    
    while pqueue:
        distance, cur_stat = heapq.heappop(pqueue)
        if cur_stat == end:
            path = []
            while cur_stat:
                path.insert(0, cur_stat)
                cur_stat = prev[cur_stat]
            return path, distances[end]
        if distance > distances[cur_stat]:
            continue
        for neighbor, weight in stations[cur_stat].connections.items():
            new_dis = distance + weight
            if new_dis < distances[neighbor]:
                distances[neighbor] = new_dis
                prev[neighbor] = cur_stat
                heapq.heappush(pqueue, (new_dis, neighbor))
    
    return None, float('inf')


def test(start, end):
    print(f"\n{stations [start].name} ({start}) , {stations[end].name}({end})")
    
    path,stops = shortest_way(start, end)
    if path:
         print(f" Shortest way: {stops} stops :{' , '.join(path)}")
    
    route,mins = fastest_way(start,end)
    if route:
        print(f"  Fastest way: {mins} min : {' , '.join(route)}")


test("EW7", "EW1")
test("NS1", "NE1")
test("EW8", "CC9")