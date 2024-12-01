def fact(int):
	if int==1:return 1
	else:return int*fact(int-1)

print(fact(10))