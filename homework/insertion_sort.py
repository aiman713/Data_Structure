
def insertionsort(arr):
    for i in range(1, len(arr)): #Started from 1(index) because it considered 0(index) sorted
        value = arr[i] 
        j= i -1 #j means previous value from current value

        while j >=0 and value  < arr[j]:
            arr[j+1] = arr[j] #
            j= j-1
        arr[j + 1 ] = value 

def printArray(arr):
    for i in range(len(arr)):
        print(arr[i], end= " ")
    print()


arr = [12,23,45,65,34,76,40]
insertionsort(arr)
printArray(arr)