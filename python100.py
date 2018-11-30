# iplaypy-python100wxamples
# author: liyy
# date: 20170809

import itertools

# 这里有四个数字，分别是：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
def python1():
    li = [1,2,3,4]
    result = []
    for i,hundred in enumerate(li):
        lia = li[:]
        lia.pop(i)
        for j,ten in enumerate(lia):
            lia.pop(j)
            for k,one in enumerate(lia):
                # if hundred != ten && ten != one && hundred != one:
                res = hundred*100+ten*10+one
                result.append(res)

    return result

def pythontest():
    a = itertools.combinations('1234',3)
    print('the following is results of combinations')
    for i in a:
        print (i)

    b = itertools.permutations('1234',3)
    print('the following is results of permutations')
    for i in b:
        print (i)
    return a



    

if __name__ == '__main__':
    # print (python1())
    # E:\py > python python100.py
    # [123, 124, 143, 213, 214, 243, 312, 314, 342, 412, 413, 432]

    pythontest()