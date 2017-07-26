from __future__ import print_function # case python 2
import time # for adding some fake but fun loading screen
import random

run_first_time = 1 # helps welcoming the player only on every new game

toe_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9] # keep track of possible left positions
printed_toe_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9] # keep track of table moves


def check_win():
	'''Checks whether there are 3 tangent 'X' or 'O', which means game is over,
	since we have a winner.'''
	
	global printed_toe_numbers
	global toe_numbers
	
	#check if user won
	if (printed_toe_numbers[0] == 'X' and  printed_toe_numbers[1] == 'X' and printed_toe_numbers[2] == 'X') or (printed_toe_numbers[3] == 'X' and printed_toe_numbers[4] == 'X' and printed_toe_numbers[5] == 'X') or (printed_toe_numbers[6] == 'X' and printed_toe_numbers[7] == 'X' and printed_toe_numbers[8] == 'X') or (printed_toe_numbers[0] == 'X' and printed_toe_numbers[3] == 'X' and printed_toe_numbers[6] == 'X') or (printed_toe_numbers[1] == 'X' and printed_toe_numbers[4] == 'X' and printed_toe_numbers[7] == 'X') or (printed_toe_numbers[2] == 'X' and printed_toe_numbers[5] == 'X' and printed_toe_numbers[8] == 'X') or (printed_toe_numbers[0] == 'X' and printed_toe_numbers[4] == 'X' and printed_toe_numbers[8] == 'X') or (printed_toe_numbers[2] == 'X' and printed_toe_numbers[4] == 'X' and printed_toe_numbers[6] == 'X'):
		return 0 # if it returns 0, user wins!
		
	#check if computer won
	elif (printed_toe_numbers[0] == 'O' and  printed_toe_numbers[1] == 'O' and printed_toe_numbers[2] == 'O') or (printed_toe_numbers[3] == 'O' and printed_toe_numbers[4] == 'O' and printed_toe_numbers[5] == 'O') or (printed_toe_numbers[6] == 'O' and printed_toe_numbers[7] == 'O' and printed_toe_numbers[8] == 'O') or (printed_toe_numbers[0] == 'O' and printed_toe_numbers[3] == 'O' and printed_toe_numbers[6] == 'O') or (printed_toe_numbers[1] == 'O' and printed_toe_numbers[4] == 'O' and printed_toe_numbers[7] == 'O') or (printed_toe_numbers[2] == 'O' and printed_toe_numbers[5] == 'O' and printed_toe_numbers[8] == 'O') or (printed_toe_numbers[0] == 'O' and printed_toe_numbers[4] == 'O' and printed_toe_numbers[8] == 'O') or (printed_toe_numbers[2] == 'O' and printed_toe_numbers[4] == 'O' and printed_toe_numbers[6] == 'O'):
		return 1 # if it returns 1, computer wins!
	
	elif len(toe_numbers) == 0:
		return 2 # game over, tie
	else:
		return 3 # keep playing

def computer_move():
	'''An algorithm for the computer to play smart (try hard not to lose by the user).
	
	if [(1,2), (2,3), (3,6), (6,9), (9,8), (8,7), (7,4), (4,1), (4,5), (5,6), (2,5), (5,8), (5,1), (5,3), (5,7), (5,9), (1,3), (3,9), (9,7), (7,1), (1,9), (3,7), (2,8), (4,6)]
	any of these pairs or numbers is both 'X', then the computer must take an action to avoid losing the game too early.'''
	
	global toe_numbers
	global printed_toe_numbers
	
	# check if computer can win or protect from losing in next move
	if (printed_toe_numbers[0] == 'O' and printed_toe_numbers[1]  == 'O') or (printed_toe_numbers[0] == 'X' and printed_toe_numbers[1]  == 'X'):
		if 3 in toe_numbers:
			printed_toe_numbers[2] = 'O'
			toe_numbers.remove(3)
			return 
	elif (printed_toe_numbers[1] == 'O' and printed_toe_numbers[2] == 'O') or (printed_toe_numbers[1] == 'X' and printed_toe_numbers[2] == 'X'):
		if 1 in toe_numbers:
			printed_toe_numbers[0] = 'O'
			toe_numbers.remove(1)
			return 
	elif (printed_toe_numbers[2] == 'O' and printed_toe_numbers[5] == 'O') or (printed_toe_numbers[2] == 'X' and printed_toe_numbers[5] == 'X'):
		if 9 in toe_numbers:
			printed_toe_numbers[8] = 'O'
			toe_numbers.remove(9)
			return 
	elif (printed_toe_numbers[5] == 'O' and printed_toe_numbers[8] == 'O') or (printed_toe_numbers[5] == 'X' and printed_toe_numbers[8] == 'X'):
		if 3 in toe_numbers:
			printed_toe_numbers[2] = 'O'
			toe_numbers.remove(3)
			return 
	elif (printed_toe_numbers[8] == 'O' and printed_toe_numbers[7] == 'O') or (printed_toe_numbers[8] == 'X' and printed_toe_numbers[7] == 'X'):
		if 7 in toe_numbers:
			printed_toe_numbers[6] = 'O'
			toe_numbers.remove(7)
			return 
	elif (printed_toe_numbers[7] == 'O' and printed_toe_numbers[6] == 'O') or (printed_toe_numbers[7] == 'X' and printed_toe_numbers[6] == 'X'):
		if 9 in toe_numbers:
			printed_toe_numbers[8] = 'O'
			toe_numbers.remove(9)
			return 
	elif (printed_toe_numbers[6] == 'O' and printed_toe_numbers[3] == 'O') or (printed_toe_numbers[6] == 'X' and printed_toe_numbers[3] == 'X'):
		if 1 in toe_numbers:
			printed_toe_numbers[0] = 'O'
			toe_numbers.remove(1)
			return 
	elif (printed_toe_numbers[3] == 'O' and printed_toe_numbers[0] == 'O') or (printed_toe_numbers[3] == 'X' and printed_toe_numbers[0] == 'X'):
		if 7 in toe_numbers:
			printed_toe_numbers[6] = 'O'
			toe_numbers.remove(7)
			return 
	elif (printed_toe_numbers[3] == 'O' and printed_toe_numbers[4] == 'O') or (printed_toe_numbers[3] == 'X' and printed_toe_numbers[4] == 'X'):
		if 6 in toe_numbers:
			printed_toe_numbers[5] = 'O'
			toe_numbers.remove(6)
			return 
	elif (printed_toe_numbers[4] == 'O' and printed_toe_numbers[5] == 'O') or (printed_toe_numbers[4] == 'X' and printed_toe_numbers[5] == 'X'):
		if 4 in toe_numbers:
			printed_toe_numbers[3] = 'O'
			toe_numbers.remove(4)
			return 
	elif (printed_toe_numbers[1] == 'O' and printed_toe_numbers[4] == 'O') or (printed_toe_numbers[1] == 'X' and printed_toe_numbers[4] == 'X'):
		if 8 in toe_numbers:
			printed_toe_numbers[7] = 'O'
			toe_numbers.remove(8)
			return 
	elif (printed_toe_numbers[4] == 'O' and printed_toe_numbers[7] == 'O') or (printed_toe_numbers[4] == 'X' and printed_toe_numbers[7] == 'X'):
		if 2 in toe_numbers:
			printed_toe_numbers[1] = 'O'
			toe_numbers.remove(2)
			return 
	elif (printed_toe_numbers[4] == 'O' and printed_toe_numbers[0] == 'O') or (printed_toe_numbers[4] == 'X' and printed_toe_numbers[0] == 'X'):
		if 9 in toe_numbers:
			printed_toe_numbers[8] = 'O'
			toe_numbers.remove(9)
			return 
	elif (printed_toe_numbers[4] == 'O' and printed_toe_numbers[2] == 'O') or (printed_toe_numbers[4] == 'X' and printed_toe_numbers[2] == 'X'):
		if 7 in toe_numbers:
			printed_toe_numbers[6] = 'O'
			toe_numbers.remove(7)
			return 
	elif (printed_toe_numbers[4] == 'O' and printed_toe_numbers[6] == 'O') or (printed_toe_numbers[4] == 'X' and printed_toe_numbers[6] == 'X'):
		if 3 in toe_numbers:
			printed_toe_numbers[2] = 'O'
			toe_numbers.remove(3)
			return 
	elif (printed_toe_numbers[4] == 'O' and printed_toe_numbers[8] == 'O') or (printed_toe_numbers[4] == 'X' and printed_toe_numbers[8] == 'X'):
		if 1 in toe_numbers:
			printed_toe_numbers[0] = 'O'
			toe_numbers.remove(1)
			return 
	elif (printed_toe_numbers[0] == 'O' and printed_toe_numbers[2] == 'O') or (printed_toe_numbers[0] == 'X' and printed_toe_numbers[2] == 'X'):
		if 2 in toe_numbers:
			printed_toe_numbers[1] = 'O'
			toe_numbers.remove(2)
			return 
	elif (printed_toe_numbers[2] == 'O' and printed_toe_numbers[8] == 'O') or (printed_toe_numbers[2] == 'X' and printed_toe_numbers[8] == 'X'):
		if 6 in toe_numbers:
			printed_toe_numbers[5] = 'O'
			toe_numbers.remove(6)
			return 
	elif (printed_toe_numbers[8] == 'O' and printed_toe_numbers[6] == 'O') or (printed_toe_numbers[8] == 'X' and printed_toe_numbers[6] == 'X'):
		if 8 in toe_numbers:
			printed_toe_numbers[7] = 'O'
			toe_numbers.remove(8)
			return 
	elif (printed_toe_numbers[6] == 'O' and printed_toe_numbers[0] == 'O') or (printed_toe_numbers[6] == 'X' and printed_toe_numbers[0] == 'X'):
		if 4 in toe_numbers:
			printed_toe_numbers[3] = 'O'
			toe_numbers.remove(4)
			return 
	elif (printed_toe_numbers[0] == 'O' and printed_toe_numbers[8] == 'O') or (printed_toe_numbers[0] == 'X' and printed_toe_numbers[8] == 'X'):
		if 5 in toe_numbers:
			printed_toe_numbers[4] = 'O'
			toe_numbers.remove(5)
			return 
	elif (printed_toe_numbers[2] == 'O' and printed_toe_numbers[6] == 'O') or (printed_toe_numbers[2] == 'X' and printed_toe_numbers[6] == 'X'):
		if 5 in toe_numbers:
			printed_toe_numbers[4] = 'O'
			toe_numbers.remove(5)
			return 
	elif (printed_toe_numbers[1] == 'O' and printed_toe_numbers[7] == 'O') or (printed_toe_numbers[1] == 'X' and printed_toe_numbers[7] == 'X'):
		if 5 in toe_numbers:
			printed_toe_numbers[4] = 'O'
			toe_numbers.remove(5)
			return 
	elif (printed_toe_numbers[3] == 'O' and printed_toe_numbers[5] == 'O') or (printed_toe_numbers[3] == 'X' and printed_toe_numbers[5] == 'X'):
		if 5 in toe_numbers:
			printed_toe_numbers[4] = 'O'
			toe_numbers.remove(5)
			return
			
	# check if any corner is a available
	available_corners = []
	if 1 in toe_numbers:
		available_corners.append(1)
	if 3 in toe_numbers:
		available_corners.append(3)
	if 7 in toe_numbers:
		available_corners.append(7)
	if 9 in toe_numbers:
		available_corners.append(9)
	if len(available_corners) != 0:
		pc_move = random.choice(available_corners)
		printed_toe_numbers[pc_move - 1] = 'O'
		toe_numbers.remove(pc_move)
		return
		
	# check if center is available
	if 5 in toe_numbers:
		printed_toe_numbers[4] = 'O'
		toe_numbers.remove(5)
		return
	
	# move in one of the sides
	available_sides = []
	if 2 in toe_numbers:
		available_sides.append(2)
	if 4 in toe_numbers:
		available_sides.append(4)
	if 6 in toe_numbers:
		available_sides.append(6)
	if 8 in toe_numbers:
		available_sides.append(8)
	if len(available_sides) != 0:
		pc_move = random.choice(available_sides)
		printed_toe_numbers[pc_move - 1] = 'O'
		toe_numbers.remove(pc_move)
		return
	

def table_view():
	'''Prints the table view for the game.'''
	
	global toe_numbers
	global printed_toe_numbers
	
	print('\n' * 50)
	
	if run_first_time:
		print('Welcome to the PyToe Game.')
	print('\n\n|-----------|')
	print('|', printed_toe_numbers[0],'|', printed_toe_numbers[1], '|', printed_toe_numbers[2], '|')
	print('|', printed_toe_numbers[3],'|', printed_toe_numbers[4], '|', printed_toe_numbers[5], '|')
	print('|', printed_toe_numbers[6],'|', printed_toe_numbers[7], '|', printed_toe_numbers[8], '|')
	print('|-----------|')


def new_game():
	'''Starts a new game.'''
	
	global printed_toe_numbers
	global toe_numbers
	global run_first_time
	
	toe_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	printed_toe_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	
	while True:
		table_view()
		will_start_new_game = input('\nTo start a new game, type: play\n')
		
		if will_start_new_game == 'play':
			reduce_sleep = 0
			for x in range(0,101):
				print('\n' * 20, 'L  O  A  D  I  N  G :\n', '=' * int(x / 2.5), str(x)+'%')
				time.sleep(0.05 - reduce_sleep)
				reduce_sleep += 0.0005
			run_first_time = 0
			play_game()
		else:
			print('\n\nWrong command!')
			time.sleep(2)
	

def play_game():
	'''Main loop which keeps the game alive.'''
	
	global printed_toe_numbers
	global toe_numbers
	
	table_view()
	
	while True:
		
		print('\nWhere would you like to put your mark?\nPossible Positions: ', end = '')
		possible_pos = 0
		while possible_pos < len(toe_numbers):
			print(toe_numbers[possible_pos], end=' ')
			possible_pos += 1
		
		user_number = int(input('\nYour choice: '))
		if user_number in list(toe_numbers):
			toe_numbers.remove(user_number)
			printed_toe_numbers[user_number-1] = 'X'
		else:
			print('\n\nThis choice in not available.')
			time.sleep(2)
			table_view()
			continue
			
		posible_win = check_win()
		if posible_win == 0:
			table_view()
			print('Game is over. You win!')
			time.sleep(5)
			break
		elif posible_win == 2:
			table_view()
			print('Game is over. It was a tie!')
			time.sleep(5)
			break
		elif posible_win == 3:
			pass # keep playing
			
		computer_move()
		
		posible_win = check_win()
		if posible_win == 1:
			table_view()
			print('Game is over. Computer wins!')
			time.sleep(5)
			break
		elif posible_win == 2:
			table_view()
			print('Game is over. It was a tie!')
			time.sleep(5)
			break
		elif posible_win == 3:
			pass # keep playing
		
		table_view()
	new_game()

new_game()
