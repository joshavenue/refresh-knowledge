import getpass
import os
import random

moves = ['rock','paper','scissor']
asking = ['ai', 'a.i']

def rules_man():
	while True:
		player_one = getpass.getpass('Choose your move : ')
		if player_one.lower() not in moves:
			print('Invalid input.')
			os.system('clear')
		else:
			break

	while True:

		player_two = getpass.getpass('Choose your move : ')
		if player_two.lower() not in moves:
			print('Invalid input.')
			os.system('clear')
		else:
			break

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

def rules_bot():
	while True:
		player_one = getpass.getpass('Choose your move : ')
		if player_one.lower() not in moves:
			print('Invalid input.')
			os.system('clear')
		else:
			break

	random_it = random.randint(0,2)
	if random_it == 0:
		bot_choice = 'rock'
	elif random_it == 1:
		bot_choice = 'paper'
	else:
		bot_choice = 'scissor'

	print('Bot chose {}.'.format(bot_choice))

	if player_one.lower() == bot_choice:
		print('Same. You both chose {}.'.format(bot_choice))
	elif moves[0] in player_one.lower() and moves[1] in bot_choice:
		print('Bot wins.')
	elif moves[1] in player_one.lower() and moves[0] in bot_choice:
		print('You wins.')
	elif moves[1] in player_one.lower() and moves[2] in bot_choice:
		print('Bot wins.')
	elif moves[0] in player_one.lower() and moves[2] in bot_choice:
		print('You wins')
	elif moves[2] in player_one.lower() and moves[1] in bot_choice:
		print('Bot wins.')
	elif moves[2] in player_one.lower() and moves[0] in bot_choice:
		print('You wins.')
	else:
		print('Strange.')

print('Welcome to the Rock Paper Scissor!')

ask = str(input('Do you wish to play against human or A.I? : '))
if ask.lower() in asking:
	rules_bot()
else:
	rules_man()
