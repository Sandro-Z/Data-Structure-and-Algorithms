from sort_algorithms import *
import random
from timeit import Timer
import matplotlib.pyplot as plt
import sys
sys.setrecursionlimit(10000)

ls=[]
for i in range(10000):
	ls.append(random.randint(0,10000))

bubbletimelst=[]
bub_sort_time=Timer('bubble_sort(ls[:i])','from __main__ import bubble_sort,ls,i')
for i in range(1000):bubbletimelst.append(bub_sort_time.timeit(number=1))
x_values=range(1000)
plt.scatter(x_values,bubbletimelst,color='blue',marker='o')
plt.xlabel('Problem size')
plt.ylabel('Total time')
plt.title('Bubble sort Benchmark')
plt.show()

selecttimelst=[]
sel_sort_time=Timer('selection_sort(ls[:i])','from __main__ import selection_sort,ls,i')
for i in range(1000):selecttimelst.append(sel_sort_time.timeit(number=1))
x_values=range(1000)
plt.scatter(x_values,selecttimelst,color='blue',marker='o')
plt.xlabel('Problem size')
plt.ylabel('Total time')
plt.title('Selection sort Benchmark')
plt.show()

inserttimelst=[]
ins_sort_time=Timer('insertion_sort(ls[:i])','from __main__ import insertion_sort,ls,i')
for i in range(1000):inserttimelst.append(ins_sort_time.timeit(number=1))
x_values=range(1000)
plt.scatter(x_values,inserttimelst,color='blue',marker='o')
plt.xlabel('Problem size')
plt.ylabel('Total time')
plt.title('Insertion sort Benchmark')
plt.show()

shelltimelst=[]
shell_sort_time=Timer('shell_sort(ls[:i])','from __main__ import shell_sort,ls,i')
for i in range(1000):shelltimelst.append(shell_sort_time.timeit(number=1))
x_values=range(1000)
plt.scatter(x_values,shelltimelst,color='blue',marker='o')
plt.xlabel('Problem size')
plt.ylabel('Total time')
plt.title('Shell sort Benchmark')
plt.show()
mergetimelst=[]
merge_sort_time=Timer('merge_sort(ls[:i])','from __main__ import merge_sort,ls,i')
for i in range(1000):mergetimelst.append(merge_sort_time.timeit(number=1))
x_values=range(1000)
plt.rcParams['lines.markersize']='3'
plt.scatter(x_values,mergetimelst,color='blue',marker='o')
plt.xlabel('Problem size')
plt.ylabel('Total time')
plt.title('Merge sort Benchmark')
plt.show()

quicktimelst=[]
quick_sort_time=Timer('quick_sort(ls[:i])','from __main__ import quick_sort,ls,i')
for i in range(1000):quicktimelst.append(quick_sort_time.timeit(number=1))
x_values=range(1000)
plt.scatter(x_values,quicktimelst,color='blue',marker='o')
plt.xlabel('Problem size')
plt.ylabel('Total time')
plt.title('Quick sort Benchmark')
plt.show()
'''merge_timelst=[]
mergeSort_time=Timer('mergeSort(ls,0,i)','from __main__ import mergeSort,ls,i')
for i in range(1000):merge_timelst.append(mergeSort_time.timeit(number=1))
x_values=range(1000)
plt.scatter(x_values,merge_timelst,color='blue',marker='o')
plt.xlabel('Problem size')
plt.ylabel('Total time')
plt.title('Merge sort without slicing Benchmark')
plt.show()'''