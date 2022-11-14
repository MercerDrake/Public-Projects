import time
import numpy

size = input("What is the size of your list? ") #Ask the user for the size of the list

def random_lists(size):
    array1 = []
    array2 = []
    tic = time.perf_counter()
    for num in range(size): #Append a random number to each list while the list size is < size
        array1.append(numpy.random.randint(1, 100))
        array2.append(numpy.random.randint(1, 100))
    toc = time.perf_counter()
    print(f"Downloaded the tutorial in {toc - tic:0.8f} seconds")
    return array1, array2 #Return the values of list 1 and 2

print(random_lists(int(size))) #Print both lists out side by side
print(time.time())