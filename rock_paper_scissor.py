import getpass
import os
import random

moves = ['rock','paper','scissor']
asking = ['ai', 'a.i']

def check_move_1():
	while True:
		player_one = getpass.getpass('Choose your move : ')
		if player_one.lower() not in moves:
			print('Invalid input.')
			os.system('clear')
		else:
			print('OK.')
			break
		
def check_move_2():
	while True:

		player_two = getpass.getpass('Choose your move : ')
		if player_two.lower() not in moves:
			print('Invalid input.')
			os.system('clear')
		else:
			print('OK.')
			break

def bot():
	random_it = random.randint(0,2)
	if random_it == 0:
		bot_choice = moves[0]
	elif random_it == 1:
		bot_choice = moves[1]
	else:
		bot_choice = moves[2]

def rules_man(p1,p2):
	if player_one.lower() == player_two.lower():
		print('It is the same.')
	elif moves[0] in player_one.lower() and moves[1] in player_two.lower():
		print('Player two wins.')
	elif moves[1] in player_one.lower() and moves[0] in player_two.lower():
		print('Player One wins.')
	elif moves[1] in player_one.lower() and moves[2] in player_two.lower():
		print('Player two wins.')
	elif moves[0] in player_one.lower() and moves[2] in player_two.lower():
		print('Player one wins')
	elif moves[2] in player_one.lower() and moves[1] in player_two.lower():
		print('Player two wins.')
	elif moves[2] in player_one.lower() and moves[0] in player_two.lower():
		print('Player one wins.')
	else:
		print('Strange.')

def rules_bot(p1,p3):
	if player_one.lower() == bot_choice:
		print('It is the same.')
	elif moves[0] in player_one.lower() and moves[1] in bot_choice:
		print('Bot wins.')
	elif moves[1] in player_one.lower() and moves[0] in bot_choice:
		print('Player One wins.')
	elif moves[1] in player_one.lower() and moves[2] in bot_choice:
		print('Bot wins.')
	elif moves[0] in player_one.lower() and moves[2] in bot_choice:
		print('Player one wins')
	elif moves[2] in player_one.lower() and moves[1] in bot_choice:
		print('Bot wins.')
	elif moves[2] in player_one.lower() and moves[0] in bot_choice:
		print('Player one wins.')
	else:
		print('Strange.')

print('Welcome to the Rock Paper Scissor!')

ask = str(input('Do you want to play against human or A.I? : '))
if ask.lower() in asking:
	bot()
	check_move_1()
	rules_bot(player_one,bot)
else:
	check_move_1()
	check_move_2()
	rules_man(player_one,player_two)


