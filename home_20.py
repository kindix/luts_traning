# 1
def show_value(x):
	return x
#3
def adder(**pargs):
	if type(pargs[0]) == type(0):
		summation = 0
	else:
		summation = pargs[0][:0]
	for arg in pargs:
		summation = summation + arg
	return summation	
#4
def adder4(good = 1, bad = 2, ugly = 3):
	return good + bad + ugly
# next 4
def adder4a(**kargs):
	arg_keys = list(kargs.keys())
	tot = kargs[arg_keys[0]]
	for key in arg_keys[1:]:
		tot += kargs[key]
	return tot
# 5
def copy_dict(old_dict):
	new_dict = {}
	for key in old_dict.keys():
		new_dict[key] = old_dict[key]
	return new_dict
# 6
def add_dict(first_dict, second_dict):
	new_dict = {}
	if type(first_dict) and type(second_dict) == type({}):
		for key in first_dict.keys():
			new_dict[key] = first_dict[key]
		for key in second_dict.keys():
			new_dict[key] = second_dict[key]
	return new_dict
#8
def prime_mod(y):
	if y <= 1: 
		print(y, 'not prime')
	else:
		x = y//2
		while x > 1:
			if y % x == 0:
				print(y, 'has factor', x)
				break
			x -= 1
		else: 
			print(y, 'is prime')
#9

my_list = [2,4,9,16,25]

def sqrt(sqrt_list):
	import math
	for value in sqrt_list:
		sqrt_list.append(math.sqrt(value))
	return sqrt_list

import math
sqrt_list = [math.sqrt(x) for x in my_list]
map_sqrt_list = list(map(math.sqrt, my_list))
lambda_sqrt_list = list(map(lambda x: math.sqrt(x), my_list))

#10
import mytimer
import sys

reps = 1000
replist = range(reps)

def func_pow():
	for x in replist:
		res = pow(x, 0.5)
	return res

def func_math():
	import math
	for x in replist:
		res = math.sqrt(x)
	return res

def shift_eight():
	for x in replist:
		res = x**0.5
	return res

print(sys.version)

with open('test.txt', 'a') as test_file:
	for test in (func_math, func_pow, shift_eight):
		elapsed, rezult = mytimer.timer(test)
		print('='*50)
		print('{0:s}: {1:6f} ==> {2:6f}'.format(test.__name__,elapsed, rezult), file = test_file)

