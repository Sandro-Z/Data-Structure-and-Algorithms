from timeit import Timer
def fibonacci_recursion(n):
	degree=n
	if degree>0:
		degree-=1
		if n>2:
			return fibonacci_recursion(n-1)+fibonacci_recursion(n-2)
		else:return 1
	else: return 0

def fibonacci_repeat(n):
	if n<3:
		return 1
	res,pre,cur=0,1,1
	for _ in range(n-2):
		res=pre+cur
		pre=cur
		cur=res
	return res

if __name__=='__main__':
	time_rec=Timer('fibonacci_recursion(20)','from __main__ import fibonacci_recursion')
	time_repeat=Timer('fibonacci_repeat(20)','from __main__ import fibonacci_repeat')
	#安装语句里面需要导入主程序中，此处需要使用的函数
	x=list(range(20000000))
	print("REC:{:.5f}ms".format(time_rec.timeit(number=1000)))
	print("REP:{:.5f}ms".format(time_repeat.timeit(number=1000)))