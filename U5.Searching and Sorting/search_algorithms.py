def ordered_sequential_search(a_list,item):
	pos=0
	while pos<len(a_list):
		if a_list[pos]==item:return True
		if a_list[pos]>item:return False
		pos+=1
	return False

def binary_search(a_list,item):
	first=0
	last=len(a_list)-1
	while first<=last:
		mid=(first+last)//2
		if a_list[mid]==item:return True
		elif a_list[mid]>item:last=mid-1
		else:first=mid+1
	return False

def binary_search_rec(a_list,item):
	if len(a_list)==0:return False
	mid=len(a_list)//2
	if a_list[mid]==item:return True
	elif a_list[mid]>item:return binary_search_rec(a_list[:mid],item)
	else:return binary_search_rec(a_list[mid+1:],item)

def sequential_searching(a_list,item):
	pos=0
	while pos<len(a_list):
		if a_list[pos]==item:return True
		pos+=1
	return False

def binary_search_rec_(a_list,left,right,item):
	if len(a_list)==0:return False
	mid=(left+right)//2
	if a_list[mid]==item:return True
	elif a_list[mid]>item:return binary_search_rec_(a_list,left,mid-1,item)
	else:return binary_search_rec_(a_list,mid+1,right,item)