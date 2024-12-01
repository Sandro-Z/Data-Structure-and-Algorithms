'''这个重写是为了练习matplotlib的'''

from search_algorithms import *
import random
from timeit import Timer
import matplotlib.pyplot as plt
import numpy as np


#创建有序的列表以备搜索
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
x_values_1=range(1000)

#递归二分搜索
binrectimelst=[]
binrec_src=Timer('binary_search_rec(ls[:i],target)','from __main__ import binary_search_rec,ls,target,i')
for i in range(1000):
	target=random.choice(ls[:i+1])
	binrectimelst.append(binrec_src.timeit(number=1000))
x_values_2=range(1000)

#带下标的递归二分搜索
binrec_timelst=[]
binrecnew_src=Timer('binary_search_rec_(ls,0,i,target)','from __main__ import binary_search_rec_,ls,target,i')
for i in range(10000):
	target=random.choice(ls[:i+1])
	binrec_timelst.append(binrecnew_src.timeit(number=1000))
x_values_3=range(10000)

#顺序搜索
seqtimelst=[]
seq_src=Timer('ordered_sequential_search(ls[:i],target)','from __main__ import ordered_sequential_search,ls,target,i')
for i in range(1000):
	target=random.choice(ls[:i+1])
	seqtimelst.append(seq_src.timeit(number=i))
x_values_4=range(1000)

#绘图开始
map=plt.figure(figsize=(8,8),dpi=80)
#plt.rcParams['font.sans-serif']=['SimHei']

ax1=map.add_subplot(2,2,1)
plt.rcParams['lines.linewidth']=2
plt.scatter(x_values_1,bintimelst,color='c',marker='o')
plt.xlabel('Problem size')
plt.ylabel('Total time')
plt.title('二分搜索测试')

ax2=map.add_subplot(2,2,2)
plt.rcParams['lines.linewidth']=2
plt.scatter(x_values_2,binrectimelst,color='m',marker='o')
plt.xlabel('Problem size')
plt.ylabel('Total time')
plt.title('Binary searching recursion Benchmark')

ax3=map.add_subplot(2,2,3)
plt.rcParams['lines.linewidth']=2
plt.scatter(x_values_3,binrec_timelst,color='y',marker='o')
plt.xlabel('Problem size')
plt.ylabel('Total time')
plt.title('Binary searching recursion with index Benchmark')
z=np.polyfit(x_values_3,binrec_timelst,2)
p=np.poly1d(z)
plt.plot(x_values_3,p(x_values_3))

ax4=map.add_subplot(2,2,4)
plt.rcParams['lines.linewidth']=2
plt.scatter(x_values_4,seqtimelst,color='k',marker='o')
plt.xlabel('Problem size')
plt.ylabel('Total time')
plt.title('Sequence searching Benchmark')
z=np.polyfit(x_values_4,seqtimelst,3)
p=np.poly1d(z)
plt.plot(x_values_4,p(x_values_4))
print(p)
plt.show()