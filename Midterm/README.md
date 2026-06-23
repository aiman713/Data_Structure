# Airport runway simulation
1. This project manages the runway of the airport by using python

## Used concepts:
1. Heap
2. Queue
3. Priority queue

## Features:
1. One runway for both landing and take-off
2. Flight requests will be generated randomly
3. Emergency landings always have the highest priority
4. Landing queue used the Heap(priority queue), higher priority after emergnecy requests
5. Take-off queue using the First-in-First-out queue.

## Rules for decision:
1. Emergency flight requests will always proceed first because of higest priority.
2. Landing flight requests will proceed before the take-off flights.
3. Take-off flight requests will proceed as in order they arrived.

## Expected Output:
1. Flight no: F4566 requests landing

2. Flight no: G7890 requests emergency landing
3. Control: Flight no G7890 landed

## How to run:
1. Open the airportsimulation.py file in python
2. Run the file

## Report:
1. There is Airport simulation.docx file which explain the project more in detail.
