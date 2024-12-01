def calc_row(n):
	list=[]
	list.append(1)
	if n>2:
		for i in range(n-2):
			list.append((calc_row(n-1)[i]+calc_row(n-1)[i+1]))
		list.append(1)
		return list
	elif n==2:return [1,1]
	else:return [1]

if __name__=='__main__':
	for i in [1,2,3,4,5,6]:
		print(calc_row(i))