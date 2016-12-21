#!D:\Program Files\Python35
#/usr/bin/env python3
# -*- coding: utf-8 -*-
#filename: helloworld.py
#20161208
'''
print ('Hello World')

s='hello world!!'
print (s)

pi=3.14
print('pi=',pi)

flag=1
pi=3
while flag==1:
    guess= int(input('enter an integer:'))
    if guess==pi:
        print("that's right")
        flag=0
    elif guess<pi:
        print('too small')
    else:
        print('too big')
else:
    print ('done')

for i in range(6,10):
    print (i-5)
else:
    print('over')

for i in range(6,10,2):
    print (i-5)
else:
    print('over')
'''
#20161215 1358
'''
while True:
    s = input('the string:')
    if s == 'end':
        break
    print('length is:',len(s))

while True:
    s = input('the string:')
    if s == 'skip it':
        continue
    if s == 'end':
        break
    print (s,'is',len(s))
'''
#function
'''
def max(a,b):
def max():
    a=int(input('a = '))
    print('\n')
    b=int(input('b = '))
    print('in a =',a,'and b =',b,'\n')
    if a>b:
        print('a =',a,'is max')
    else:
        print('b =',b,'is max')

max(1,5)
a=5
b=10
max()

a=1
b=5
c=7
def test():
    global b
    a=2
    print('a in the function is',a)
    b=6
    print('b in the function is',b)
    c=8
    print('c in the function is',c)
test()
print('a =',a,'b =',b,'c =',c)
'''
#默认值，不能先定义有默认值的参数，否则无法识别输入的是哪个参数
'''
def test1(value,times=1):
    print (value*times)

test1(5)
test1(5,2)

def test2(string,times=1,value='1'):
    print(string,'\n')
    print(int(value)*times,value*times)

test2('it is')
test2('it is',5)
test2('it is',5,'5')

def test3(a,b=3,c=5):
    print ('a=',a,'b=',b,'c=',c)
test3(1)
test3(1,c=6)
test3(1,b=4)
'''
def test4():
    '''this is a test docstring.

this is the second sentence.'''
    print('docstring test')
test4()
print (test4.__doc__)

