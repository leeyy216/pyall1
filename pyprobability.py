import random

# wrong example
def random_pick(seq,probabilities):
    x = random.uniform(0, 1)#首先随机生成一个0，1之间的随机数
    cumulative_probability = 0.0
    for item, item_probability in zip(seq, probabilities):#seq代表待输入的字符串，prob代表各自字符串对应的概率
        cumulative_probability += item_probability#只有当累加的概率比刚才随机生成的随机数大时候，才跳出，并输出此时对应的字符串
        if x < cumulative_probability:
            break
        return item

# correct example
def select():
    num_ = ['a', 'b', 'c']
    #概率列表
    r_ = [0.1, 0.3, 0.6]
    sum_ = 0
    ran = random.random()
    for num, r in zip(num_, r_):
        sum_ += r
        if ran < sum_ :break
    return num

# changed correct example
def select1(num_, r_):
    sum_ = 0
    ran = random.random()
    for num, r in zip(num_, r_):
        sum_ += r
        if ran < sum_ :break
    return num

if __name__ == '__main__':
	# random_pick("sjb", [0.1,0.3,0.6])
	num_a, num_b ,num_c = 0, 0, 0
	num_ = ['a', 'b', 'c']
	#概率列表
	r_ = [0.1, 0.3, 0.6]
	for each in range(100000):
	    # result = random_pick("sjb", [0.1,0.3,0.6])
	    result = select1(num_, r_)

	    if result == 'a':
	        num_a += 1
	    elif result == 'b':
	        num_b += 1
	    else:
	        num_c += 1
        
	print("num-a = ",num_a,"num-b = ",num_b, "num-c = ", num_c)