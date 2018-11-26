#Authour : sanu k yadav
#Email: sanukyadav@gmail.com



"""

import functools as ft 
import itertools as it 

OPERATORS = '+','-','*','/'
EXIT_COMMANDS = 'exit' , 'quit'

def can_calculate(state):
	if len(state) < 3:
		return False
	#extended iterator unpacking
	*_, i1,op, i2 = state
	return isinstance(i1, float) and op in OPERATORS and isinstance(i2, float)

def calculate(state):
	*_,i1,op,i2= state
	if op == '+':
		result = i1 + i2
	elif op == '-':
		result = i1 - i2
	elif op == '/':
		result = i1 / i2
	elif op == '*':
		result = i1 * i2
	else:
		raise ValueError('Invalid OPERATORS!!!')
	print('%f %s %f = %f' %(i1,op,i2,result))
	return result

def process_input(state, update):
	state.append(update)
	if can_calculate(state):
		result = calculate(state)
		state.append(result)
	return state

#Decorators are used 
def validate_input(fnc):
	def inner():
		i = fnc()
		try:
			i = float(i)
		except ValueError:
			pass
		if isinstance(i,float) or i in OPERATORS or i in EXIT_COMMANDS:
			return i
		return None
	return inner

@validate_input
def get_input():
	return input()

#Used Generators
def input_loop():
	while True:
		i = get_input()
		if i in EXIT_COMMANDS:
			break
		if i is None:
			print("Please enter a number or an OPERATOR")
			continue
		yield i


def calculator():
	#Reduce function from functools
	ft.reduce(process_input, input_loop(), [0])


calculator()


"""

import functools as ft 
import itertools as it 

OPERATORS = '+','-','*','/'
EXIT_COMMANDS = 'exit' , 'quit'

def can_calculate(state):
	if len(state) < 3:
		return False
	#extended iterator unpacking
	*_, i1,op, i2 = state
	return isinstance(i1, float) and op in OPERATORS and isinstance(i2, float)

def calculate(state):
	*_,i1,op,i2= state
	if op == '+':
		result = i1 + i2
	elif op == '-':
		result = i1 - i2
	elif op == '/':
		result = i1 / i2
	elif op == '*':
		result = i1 * i2
	else:
		raise ValueError('Invalid OPERATORS!!!')
	print('%f %s %f = %f' %(i1,op,i2,result))
	return result



#Decorators are used 
def validate_input(fnc):
	def inner():
		i = fnc()
		try:
			i = float(i)
		except ValueError:
			pass
		if isinstance(i,float) or i in OPERATORS or i in EXIT_COMMANDS:
			return i
		return None
	return inner

@validate_input
def get_input():
	return input()

#Used Generators
def input_loop():
	while True:
		i = get_input()
		if i in EXIT_COMMANDS:
			break
		if i is None:
			print("Please enter a number or an OPERATOR")
			continue
		yield i

def process_input():
	state = []
	while  True:
		update = yield
		state.append(update)
		if can_calculate(state):
			result = calculate(state)
			state.append(result)

def calculator():
	g = process_input()
	g.send(None)
	while True:
		i = get_input()
		if i in None:
			print("Please Enter a number or an OPERATOR")
			continue
		if i in EXIT_COMMANDS:
			break
		g.send(i)

calculator()
