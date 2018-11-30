import curses
from random import randrange, choice
from collections import defaultdict

actions = ['Up', 'Left', 'Down', 'Right', 'Restart', 'Exit']

letter_codes = [ord(ch) for ch in 'WASDRQwasdrq']

actions_dict = dict(zip(letter_codes, actions * 2))

state_actions = {
	'Init': init,
	'Win': lambda: not_game('Win') 
	'Gameover': lambda: not_game('Gameover'),
	'Game': game
}

def get_user_action(keyboard):
	char = 'N'
	while char not in actions_dict:
		char = keyboard.getch()
	return actions_dict[char]

# 矩阵转置
def transpose(field):
	return [list(row) for row in zip(*field)]

# 矩阵逆转
def invert(field):
	return [row[::-1] for row in field]

# 棋盘
class GameField(object):
	"""docstring for GameField"""
	def __init__(self, height=4, width=4, win=2048):
		self.height = height		#高
		self.width = width			#宽
		self.win_value = 2048		#过关分数
		self.score = 0				#当前分数
		self.highscore = 0			#最高分
		self.reset()				#棋盘重置

def init():
	pass

def game():
	# Game
	# Win
	# Gameover
	# Exit
	pass

def 
