# DEVELOPER : Grishak
# START DATE 18/4/2018

"""
		TODO:
			- better user interface
			- a GUI

		Assumes - there are imported functions to determine whether the expression that is 
			given by the user can be tought of a mathematical expression
		
		Description - This is the main method for CalcFreeHand program.
		
	"""

from correct_chars import correct_chars
from bal_parenthesis import check_bal_parenthesis
from symbols_repeated import check_repeated_symbols
from symbols_around_pars import check_symbols_around_asymbol
# imports are in the order of which functions were created

while True:
	user_input = ''
	user_input = input('\nEnter your equasion: ')
	if (
			correct_chars(user_input) 
			and check_bal_parenthesis(user_input) 
			and check_repeated_symbols(user_input) 
			and check_symbols_around_asymbol(user_input, '(', True) 
			and check_symbols_around_asymbol(user_input, ')', True) 
			and check_symbols_around_asymbol(user_input, '(', False) 
			and check_symbols_around_asymbol(user_input, ')', False)
		):
		if len(user_input) > 1 :
			result = eval(user_input)
			print('Answer: ' + str(result))
		else:
			print('\nInput not a mathematical expression\nTry again\n')
	else:
		print('\nInput not a mathematical expression\nTry again\n')

	
