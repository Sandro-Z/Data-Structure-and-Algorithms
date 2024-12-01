from search_algorithms import *
import random
from timeit import Timer
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

ls=[]
for i in range(10000):
	ls.append(random.randint(0,10000))
ls.sort()

#循环二分搜索
bintimelst=[]
bin_src=Timer('binary_search(ls[:i],target)','from __main__ import binary_search,ls,target,i')
for i in range(1000):
	target=random.choice(ls[:i+1])
	bintimelst.append(bin_src.timeit(number=1000))
x_values=range(1000)
plt.scatter(x_values,bintimelst,color='blue',marker='o')
plt.xlabel('Problem size')
plt.ylabel('Total time')
plt.title('Binary searching Benchmark')
plt.show()

#递归二分搜索
binrectimelst=[]
binrec_src=Timer('binary_search_rec(ls[:i],target)','from __main__ import binary_search_rec,ls,target,i')
for i in range(1000):
	target=random.choice(ls[:i+1])
	binrectimelst.append(binrec_src.timeit(number=1000))
x_values=range(1000)
plt.scatter(x_values,binrectimelst,color='blue',marker='o')
plt.xlabel('Problem size')
plt.ylabel('Total time')
plt.title('Binary searching recursion Benchmark')
plt.show()

#带下标的递归二分搜索
binrec_timelst=[]
binrecnew_src=Timer('binary_search_rec_(ls,0,i,target)','from __main__ import binary_search_rec_,ls,target,i')
for i in range(10000):
	target=random.choice(ls[:i+1])
	binrec_timelst.append(binrecnew_src.timeit(number=1000))
x_values=range(10000)
plt.scatter(x_values,binrec_timelst,color='blue',marker='o')
plt.xlabel('Problem size')
plt.ylabel('Total time')
plt.title('Binary searching recursion with index Benchmark')
plt.show()

#顺序搜索
seqtimelst=[]
seq_src=Timer('ordered_sequential_search(ls[:i],target)','from __main__ import ordered_sequential_search,ls,target,i')
for i in range(1000):
	target=random.choice(ls[:i+1])
	seqtimelst.append(seq_src.timeit(number=i))
x_values=range(1000)
plt.scatter(x_values,seqtimelst,color='blue',marker='o')
plt.xlabel('Problem size')
plt.ylabel('Total time')
plt.title('Sequence searching Benchmark')
plt.show()
