def list_reverse(list):
	if len(list)==0:return list
	else:return list_reverse(list[1:])+[list[0]]#list【0】是一个整数，要想连接列表必须将其两侧加上中括号形成列表

print(list_reverse([0,1,2,3,4]))