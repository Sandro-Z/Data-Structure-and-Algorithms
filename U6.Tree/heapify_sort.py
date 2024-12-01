from pythonds3.trees import BinaryHeap
import matplotlib.pyplot as plt
from timeit import Timer
import random

def heapSort(ls):
	heap=BinaryHeap()
	heap.heapify(not_a_heap=ls)
	while heap:
		heap.delete()

list=[]
for i in range(1000):
	list.append(random.randint(1,10000))

heap_timelst=[]
haepSort_time=Timer('heapSort(list)','from __main__ import heapSort,list')
for i in range(1000):heap_timelst.append(haepSort_time.timeit(number=1))
x_values=range(1000)
plt.scatter(x_values,heap_timelst,color='blue',marker='o')
plt.xlabel('Problem size')
plt.ylabel('Total time')
plt.title('BinaryHeap sort Benchmark')
plt.show()