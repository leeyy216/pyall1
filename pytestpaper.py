# 试卷生成器——该程序可以从文件中随机挑选出不同的题目生成一份试卷。每份试卷可以不一样，通过读取答案来给打分
# take random 50音图 mp3 
# 随机组合罗马音声母韵母
import os
import random

class Japanesetest(object):

	def __init__(self):
		# question resouce
		self.sheng = ['元','k','s','h','n','t','m','r','y','w','ん']
		self.yun = ['a','i','u','e','o']
		# self.question = random.choice(sheng) + random.choice(yun)

	def printques(self):
		ch = input("begin the test?")
		# while(ch == 'y' or ch == 'Y'):
		while(ch != 'n' and ch != 'N'):
			question = random.choice(self.sheng) + random.choice(self.yun)
			print (question)
			ch = input("go on?")

test = Japanesetest()
test.printques()