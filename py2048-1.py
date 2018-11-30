# 输入开始表格
# a=[None]*4
# for i in range(4):
# 	a[i]=int(input("%s: " %i))


# a[]
# for i in range(5):
# 	a.remove(0)

# n=4-len(a)

# for i in range(n):
# 	a.insert(0,0)

# for i in range(:4:-1):
# 	if a[i]=a[i-1]:
# 		a[i]=a[i]+a[i-1]
# 		a[i-1]=a[i-2]
# 		for j in range()

# def plus2(a,b):
# 	b=a+b
# 	a=0
def plusrow(a,command):

	C = {'a':False,'d':True,'w':False,'s':True}
	if command =='w' or command == 's':
		a = trans(a)
		print(a)

	if not C[command]:
		a.reverse()
		print(a.reverse())

	for i in range(4):
		for j in range(3)[::-1]:
			if (a[j] == a[j+1]) or (a[j]==0) or (a[j+1]==0) :
				# plus2(a[j],a[j+1])
				a[j+1] = a[j+1] + a[j]
				a[j] = 0
				# print(a)
	if not C[command]:
		a.reverse()
		print(a.reverse())

	if command =='w' or command == 's':
		a = trans(a)
		print(a)
	return a

# 按格式打印
def tableprint(a):
	for i in range(len(a)):
		for j in range(len(a[i])):
			print(str(a[i][j])+'\t',end="")
		print("\n",end="")

# 上下（w，s）转置，变为左右操作（a，d）
def trans(a):
	# b = [[None]*4 for i in range(4)]
	# b = [a[j][i] for i in range(len(a)) for j in range(len(a[i]))]
	# for i in range(len(a)):
	# 	for j in range(len(a[i])):
	# 		b[j][i] = a[i][j]
	c = list(map(list, zip(*a)))
	return c

if __name__ == '__main__':
	# a = [[0,2,0,4]]*4
	result = [[0,2,2,2], [0,4,0,4], [0,2,0,2], [0,4,2,4]]
	print(plusrow(result,'a'))
	print("============")
	print(plusrow(result,'s'))
	print("============")
	print(plusrow(result,'w'))
	print("============")
	print(plusrow(result,'d'))
	print("the initial table is :\n")
	tableprint(result)
	command = input("input the move: ")
	# result = a
	while(command != 'q'):
		result = plusrow(result,command)
		tableprint(result)
		command = input("input the move: ")
	# for i in a:
	# 	a[a.index(i)] = plusrow(i,command)
	
	print("the result table is :\n")
	tableprint(result)
	# print(a)
	# print(c)

