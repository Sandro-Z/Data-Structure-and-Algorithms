'''def bubble_sort(list):#冒泡
	for i in range(len(list)-1,0,-1):
		for j in range(i):
			if list[j]>list[j+1]:
				list[j],list[j+1]=list[j+1],list[j]

def bubble_sort_short(list):#短冒泡
	for i in range(len(list)-1,0,-1):
		exchanged=False
		for j in range(i):
			if list[j]>list[j+1]:
				exchanged=True
				list[j],list[j+1]=list[j+1],list[j]
		if not exchanged:break

#此选择排序交换的是最小值，而不是最大值
def selection_sort(lst):
	for i,item in enumerate(lst):#按照lst的索引及值来迭代
		min_idx=len(lst)-1
		for j in range(i,len(lst)):
			if lst[j]<lst[min_idx]:
				min_idx=j
		if min_idx!=i:
			lst[min_idx],lst[i]=lst[i],lst[min_idx]

def insertion_sort(ls):#插入排序
	for i in range(1,len(ls)):
		current_value=ls[i]
		current_position=i
		while current_position>0 and ls[current_position-1]>current_value:
			ls[current_position]=ls[current_position-1]#往后移动让位置
			current_position=current_position-1
		ls[current_position]=current_value#最终插入

def shell_sort(ls):#希尔排序
	sublst_count=len(ls)//1000
	while sublst_count>0:
		for pos_start in range(sublst_count):
			gap_insertion_sort(ls,pos_start,sublst_count)
		#print('After increments of size {0} the list is {1}'.format(sublst_count,ls))
		sublst_count//=1000

def gap_insertion_sort(ls,start,gap):#带间隔的插入排序
	for i in range(start+gap,len(ls),gap):
		current_val=ls[i]
		current_pos=i
		while current_pos>=gap and ls[current_pos-gap]>current_val:
			ls[current_pos]=ls[current_pos-gap]
			current_pos-=gap
		ls[current_pos]=current_val

def merge_sort(ls):#归并
	#print('Splitting',ls)
	if len(ls)>1:
		mid=len(ls)//2
		left_half=ls[:mid]
		right_half=ls[mid:]
		merge_sort(left_half)
		merge_sort(right_half)
		i,j,k=0,0,0
		while i<len(left_half)and j<len(right_half):
			if left_half[i]<right_half[j]:
				ls[k]=left_half[i]
				i+=1
			else:
				ls[k]=right_half[j]
				j+=1
			k+=1
		while i<len(left_half):
			ls[k]=left_half[i]
			i+=1
			k+=1
		while j<len(right_half):
			ls[k]=right_half[j]
			j+=1
			k+=1
	#print("Merging",ls)

#快速排序
def quick_sort(ls): quick_sort_helper(ls,0,len(ls)-1)
def quick_sort_helper(ls,first,last):
	if first<last:
		split=partition(ls,first,last)
		quick_sort_helper(ls,first,split-1)
		quick_sort_helper(ls,split+1,last)
def partition(ls,first,last):
	mid_val=ls[first]
	left_mark=first+1
	right_mark=last
	done=False
	while not done:
		while left_mark<=right_mark and ls[left_mark]<=mid_val: left_mark+=1  #右移左标直到遇到大于基准值的元素
		while left_mark<=right_mark and ls[right_mark]>=mid_val: right_mark-=1
		if right_mark<left_mark:
			done=True
		else:
			ls[right_mark],ls[left_mark]=ls[left_mark],ls[right_mark]
	return right_mark'''

'''def mergeSort(ls,left,right):#归并（不切片）
	#print('Splitting',ls)
	if (right-left)>1:
		mid=(left+right)//2
		mergeSort(ls,left,mid)
		mergeSort(ls,mid+1,right)
		i,j,k=left,mid+1,right
		while i<mid and j<right:
			if ls[i]<ls[j]:
				ls[k]=left_half[i]
				i+=1
			else:
				ls[k]=right_half[j]
				j+=1
			k+=1
		while i<len(left_half):
			ls[k]=left_half[i]
			i+=1
			k+=1
		while j<len(right_half):
			ls[k]=right_half[j]
			j+=1
			k+=1'''

def bubble_sort (OO0000O0OO0OO0OO0 ):#line:1
	for O0OO0O00O00OO00O0 in range (len (OO0000O0OO0OO0OO0 )-1 ,0 ,-1 ):#line:2
		for OO0OOO00OO000OOO0 in range (O0OO0O00O00OO00O0 ):#line:3
			if OO0000O0OO0OO0OO0 [OO0OOO00OO000OOO0 ]>OO0000O0OO0OO0OO0 [OO0OOO00OO000OOO0 +1 ]:#line:4
				OO0000O0OO0OO0OO0 [OO0OOO00OO000OOO0 ],OO0000O0OO0OO0OO0 [OO0OOO00OO000OOO0 +1 ]=OO0000O0OO0OO0OO0 [OO0OOO00OO000OOO0 +1 ],OO0000O0OO0OO0OO0 [OO0OOO00OO000OOO0 ]#line:5
def bubble_sort_short (OO0OOO000O00OOOO0 ):#line:7
	for OOO00O0O00OOO00OO in range (len (OO0OOO000O00OOOO0 )-1 ,0 ,-1 ):#line:8
		O000OO00O00OOOO00 =False #line:9
		for OO000O0000O0OOO0O in range (OOO00O0O00OOO00OO ):#line:10
			if OO0OOO000O00OOOO0 [OO000O0000O0OOO0O ]>OO0OOO000O00OOOO0 [OO000O0000O0OOO0O +1 ]:#line:11
				O000OO00O00OOOO00 =True #line:12
				OO0OOO000O00OOOO0 [OO000O0000O0OOO0O ],OO0OOO000O00OOOO0 [OO000O0000O0OOO0O +1 ]=OO0OOO000O00OOOO0 [OO000O0000O0OOO0O +1 ],OO0OOO000O00OOOO0 [OO000O0000O0OOO0O ]#line:13
		if not O000OO00O00OOOO00 :break #line:14
def selection_sort (OOO0OO0000OOOOOO0 ):#line:17
	for O0OOOOOOOOO00O0OO ,OOO000O00OOO0OOO0 in enumerate (OOO0OO0000OOOOOO0 ):#line:18
		O0O0OOOO000O000OO =len (OOO0OO0000OOOOOO0 )-1 #line:19
		for OOOO0OO0O0OO000OO in range (O0OOOOOOOOO00O0OO ,len (OOO0OO0000OOOOOO0 )):#line:20
			if OOO0OO0000OOOOOO0 [OOOO0OO0O0OO000OO ]<OOO0OO0000OOOOOO0 [O0O0OOOO000O000OO ]:#line:21
				O0O0OOOO000O000OO =OOOO0OO0O0OO000OO #line:22
		if O0O0OOOO000O000OO !=O0OOOOOOOOO00O0OO :#line:23
			OOO0OO0000OOOOOO0 [O0O0OOOO000O000OO ],OOO0OO0000OOOOOO0 [O0OOOOOOOOO00O0OO ]=OOO0OO0000OOOOOO0 [O0OOOOOOOOO00O0OO ],OOO0OO0000OOOOOO0 [O0O0OOOO000O000OO ]#line:24
def insertion_sort (OOO0O00O0O000O000 ):#line:26
	for OOOOOO0OOOOO0OOO0 in range (1 ,len (OOO0O00O0O000O000 )):#line:27
		O00OOO00OO0OOO0OO =OOO0O00O0O000O000 [OOOOOO0OOOOO0OOO0 ]#line:28
		O0000000OO0O0000O =OOOOOO0OOOOO0OOO0 #line:29
		while O0000000OO0O0000O >0 and OOO0O00O0O000O000 [O0000000OO0O0000O -1 ]>O00OOO00OO0OOO0OO :#line:30
			OOO0O00O0O000O000 [O0000000OO0O0000O ]=OOO0O00O0O000O000 [O0000000OO0O0000O -1 ]#line:31
			O0000000OO0O0000O =O0000000OO0O0000O -1 #line:32
		OOO0O00O0O000O000 [O0000000OO0O0000O ]=O00OOO00OO0OOO0OO #line:33
def shell_sort (OOOO0O0000OOOO0OO ):#line:35
	OOOOOO00000O0O0OO =len (OOOO0O0000OOOO0OO )//1000 #line:36
	while OOOOOO00000O0O0OO >0 :#line:37
		for O0O0O0OO0O0O0OO0O in range (OOOOOO00000O0O0OO ):#line:38
			gap_insertion_sort (OOOO0O0000OOOO0OO ,O0O0O0OO0O0O0OO0O ,OOOOOO00000O0O0OO )#line:39
		OOOOOO00000O0O0OO //=1000 #line:41
def gap_insertion_sort (O0O0OOO00OOO0OOO0 ,OOO00O0OO0O000000 ,O000OOO00OO0OOOO0 ):#line:43
	for OO0000OO0OO00OOOO in range (OOO00O0OO0O000000 +O000OOO00OO0OOOO0 ,len (O0O0OOO00OOO0OOO0 ),O000OOO00OO0OOOO0 ):#line:44
		OOO0O00O0OOOO000O =O0O0OOO00OOO0OOO0 [OO0000OO0OO00OOOO ]#line:45
		OOO00000000O0O0O0 =OO0000OO0OO00OOOO #line:46
		while OOO00000000O0O0O0 >=O000OOO00OO0OOOO0 and O0O0OOO00OOO0OOO0 [OOO00000000O0O0O0 -O000OOO00OO0OOOO0 ]>OOO0O00O0OOOO000O :#line:47
			O0O0OOO00OOO0OOO0 [OOO00000000O0O0O0 ]=O0O0OOO00OOO0OOO0 [OOO00000000O0O0O0 -O000OOO00OO0OOOO0 ]#line:48
			OOO00000000O0O0O0 -=O000OOO00OO0OOOO0 #line:49
		O0O0OOO00OOO0OOO0 [OOO00000000O0O0O0 ]=OOO0O00O0OOOO000O #line:50
def merge_sort (O0O00OO000OO00O00 ):#line:52
	if len (O0O00OO000OO00O00 )>1 :#line:54
		O0OOOO0O00O0O000O =len (O0O00OO000OO00O00 )//2 #line:55
		OO00000O0000OOOOO =O0O00OO000OO00O00 [:O0OOOO0O00O0O000O ]#line:56
		O0000O00O000O0OO0 =O0O00OO000OO00O00 [O0OOOO0O00O0O000O :]#line:57
		merge_sort (OO00000O0000OOOOO )#line:58
		merge_sort (O0000O00O000O0OO0 )#line:59
		OOO0O0O0O0O0O0OO0 ,OO000OOO0000O000O ,OOOOOO000000OOOO0 =0 ,0 ,0 #line:60
		while OOO0O0O0O0O0O0OO0 <len (OO00000O0000OOOOO )and OO000OOO0000O000O <len (O0000O00O000O0OO0 ):#line:61
			if OO00000O0000OOOOO [OOO0O0O0O0O0O0OO0 ]<O0000O00O000O0OO0 [OO000OOO0000O000O ]:#line:62
				O0O00OO000OO00O00 [OOOOOO000000OOOO0 ]=OO00000O0000OOOOO [OOO0O0O0O0O0O0OO0 ]#line:63
				OOO0O0O0O0O0O0OO0 +=1 #line:64
			else :#line:65
				O0O00OO000OO00O00 [OOOOOO000000OOOO0 ]=O0000O00O000O0OO0 [OO000OOO0000O000O ]#line:66
				OO000OOO0000O000O +=1 #line:67
			OOOOOO000000OOOO0 +=1 #line:68
		while OOO0O0O0O0O0O0OO0 <len (OO00000O0000OOOOO ):#line:69
			O0O00OO000OO00O00 [OOOOOO000000OOOO0 ]=OO00000O0000OOOOO [OOO0O0O0O0O0O0OO0 ]#line:70
			OOO0O0O0O0O0O0OO0 +=1 #line:71
			OOOOOO000000OOOO0 +=1 #line:72
		while OO000OOO0000O000O <len (O0000O00O000O0OO0 ):#line:73
			O0O00OO000OO00O00 [OOOOOO000000OOOO0 ]=O0000O00O000O0OO0 [OO000OOO0000O000O ]#line:74
			OO000OOO0000O000O +=1 #line:75
			OOOOOO000000OOOO0 +=1 #line:76
def quick_sort (O00OO0OOOOOO00OOO ):quick_sort_helper (O00OO0OOOOOO00OOO ,0 ,len (O00OO0OOOOOO00OOO )-1 )#line:80
def quick_sort_helper (O000OO000000000O0 ,OOOOO000000O0OO00 ,O0000OOO0OO0OO00O ):#line:81
	if OOOOO000000O0OO00 <O0000OOO0OO0OO00O :#line:82
		O0OO0O00OO00OO0OO =partition (O000OO000000000O0 ,OOOOO000000O0OO00 ,O0000OOO0OO0OO00O )#line:83
		quick_sort_helper (O000OO000000000O0 ,OOOOO000000O0OO00 ,O0OO0O00OO00OO0OO -1 )#line:84
		quick_sort_helper (O000OO000000000O0 ,O0OO0O00OO00OO0OO +1 ,O0000OOO0OO0OO00O )#line:85
def partition (OOO0OOO00OO0OO0OO ,O00O0O0OOO0OOO000 ,O0OO00OO0OOOO0OO0 ):#line:86
	OOOO0OOOOO0OOO0OO =OOO0OOO00OO0OO0OO [O00O0O0OOO0OOO000 ]#line:87
	OOO000O0O00OOO0OO =O00O0O0OOO0OOO000 +1 #line:88
	O000OOO0O00OO0000 =O0OO00OO0OOOO0OO0 #line:89
	OOOO0OO000OOOO00O =False #line:90
	while not OOOO0OO000OOOO00O :#line:91
		while OOO000O0O00OOO0OO <=O000OOO0O00OO0000 and OOO0OOO00OO0OO0OO [OOO000O0O00OOO0OO ]<=OOOO0OOOOO0OOO0OO :OOO000O0O00OOO0OO +=1 #line:92
		while OOO000O0O00OOO0OO <=O000OOO0O00OO0000 and OOO0OOO00OO0OO0OO [O000OOO0O00OO0000 ]>=OOOO0OOOOO0OOO0OO :O000OOO0O00OO0000 -=1 #line:93
		if O000OOO0O00OO0000 <OOO000O0O00OOO0OO :#line:94
			OOOO0OO000OOOO00O =True #line:95
		else :#line:96
			OOO0OOO00OO0OO0OO [O000OOO0O00OO0000 ],OOO0OOO00OO0OO0OO [OOO000O0O00OOO0OO ]=OOO0OOO00OO0OO0OO [OOO000O0O00OOO0OO ],OOO0OOO00OO0OO0OO [O000OOO0O00OO0000 ]#line:97
	return O000OOO0O00OO0000