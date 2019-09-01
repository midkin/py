# Tic-Tac-Toe Game
# midkin 01.09.2019 (dd.mm.yyyy)
# no copyrights

import itertools


# Prints the welcome message
# Only printed in the first round
for _ in range(40):
	print()
print('Tic-Tac-Toe implementation by midkin.\n\nThis is the first round, so you can play first.\nWinner plays first in the next rounds.\n')

# List to hold cell values
cells = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# List to help with computer logic
cell_logic = [6 , 1, 8, 7, 5, 3, 2, 9, 4]

# Keep track of game activity
end_game = False

# Keep track of who plays first
user_first = True

# List to keep track user choice
user_choices = []

# List to keep track computer choice
computer_choices = []

# Keep track of the score
score = [0, 0]

# Grid printing method
def print_grid():
	for _ in range(13):
		print('-', end='')
	print()
	for i in range(0, 7, 3):
		print('| ' + str(cells[i]) + ' | '+ str(cells[i+1]) + ' | ' + str(cells[i+2]) + ' |')
		for _ in range(13):
			print('-', end='')
		print()
		
# Informs the user for his/her next move
def user_turn():
	global cells, cell_logic, user_choices
	while True:
		for _ in range(40):
			print()
		print_grid()
		choice = input('You may type 1-9 corresponding to the position you want to draw.\n')
		try:
			choice = int(choice)
			if choice < 1 or choice > 9:
				continue
			else:
				user_choices.append(cell_logic[choice-1])
				cells[choice-1] = 'X'
				cell_logic[choice-1] = 'X'
				break
		except:
			continue
	
def computer_turn():
	if cells[4] == 5:
		cells[4] = 'O'
		cell_logic[4] = 'O'
		computer_choices.append(5)
		return
		
	for pair in itertools.combinations(computer_choices,2):
		checker = 15 - sum(pair)
		if checker in cell_logic:
			computer_choices.append(checker)
			cells[cell_logic.index(checker)] = 'O'
			cell_logic[cell_logic.index(checker)] = 'O'
		
	for pair in itertools.combinations(user_choices, 2):
		checker = 15 - sum(pair)
		if checker in cell_logic:
			computer_choices.append(checker)
			cells[cell_logic.index(checker)] = 'O'
			cell_logic[cell_logic.index(checker)] = 'O'
			return
	
	for i in computer_choices:
		for pair in itertools.combinations(cell_logic, 2):
			try:
				int(pair[0]) + int(pair[1])
				if sum(pair+i) == 15:
					computer_choices.append(pair[0])
					cells[cell_logic.index(pair[0])] = 'O'
					cell_logic[cell_logic.index(pair[0])] = 'O'
					return
			except:
				pass
				
	for i in cell_logic:
		if isinstance(i, int):
			computer_choices.append(i)
			cells[cell_logic.index(i)] = 'O'
			cell_logic[cell_logic.index(i)] = 'O'
			return

def check_end_game():
	global  end_game, user_first
	
	for comb in itertools.combinations(user_choices, 3):
		if sum(comb) == 15:
			end_game = True
			user_first = True
			for _ in range(40):
				print()
			print('You win!\n')
			score[0] += 1
			return
	
	for comb in itertools.combinations(computer_choices, 3):
		if sum(comb) == 15:
			end_game = True
			user_first = False
			for _ in range(40):
				print()
			print('You lose!\n')
			score[1] += 1
			return
	
	if len(user_choices) + len(computer_choices) == 9:
		end_game = True
		for _ in range(40):
			print()
		print('This is a tie.\n')
		score[0] += 1
		score[1] += 1
		return
		
def reset():
	global cells, cell_logic, end_game, user_choices, computer_choices
	end_game = False
	cells = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	cell_logic = [6 , 1, 8, 7, 5, 3, 2, 9, 4]
	user_choices = []
	computer_choices = []
	
def start_new():
		while True:
			choice = input('Wanna start a new game? (y/n)\n')
			if choice != 'y' and choice != 'n':
				continue
			else:
				return choice
	
if __name__ == '__main__':
	while True:
		if user_first:
			user_turn()
			computer_turn()
		else:
			computer_turn()
			user_turn()
		for _ in range(40):
			print()
		check_end_game()
		if end_game:
			print('Score:', score[0], ':', score[1])
			if start_new() == 'y':
				reset()
				continue
			else:
				print('Goodbye!')
				break
			
