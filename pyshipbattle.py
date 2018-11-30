# 战船——创建两块游戏面板，玩家各占一边，在上面放置一些战船，玩家看不到对方的面板。
# 每艘船都占几个格子，玩家轮流攻击某个格子，如果格子上有船，那就命中目标，否则就是未命中。
# 当一艘船所占的所有格子都被攻击命中了，那么船就被击沉。谁先将对方战船全部击沉就获胜。

import os
from numpy import *		#module of matrix

class Game(object):

	def __init__(self, length, width, shipnum):	#shiplen
		self.length = length
		self.width = width
		self.shipnum = shipnum
		# self.shiplen = shiplen

	def makefield(self):
		# 画出游戏区域
		for range(0,self.width+1):
			for range(0,self.length):
				print('——')
		# pass


length = input("please input the length: ")
width = input("please input the width: ")
shipnum = input("please input the shipnum: ")
# shiplen = input("please input the shiplen: ")

game = Game(length, width, shipnum)
game.makefield