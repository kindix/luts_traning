# global
X = 99

def func(Y):
	#local
	Z = X + Y
	return Z

print(func(1))

def func():
	#local
	global X 
	X = 101

func()
print(X)

x,y = 1,2

def all_global():
	global z
	z = x + y

all_global()
print(z)


var = 99

def local():
	var = 0

def glob1():
	global var
	var += 1

def glob2():
	var = 0
	import part17_methods
	var += 1

def glob3():
	var = 0
	import sys
	glob = sys.modules['part17_methods']
	glob.var += 1

def test():
	print(var)
	local(); glob1(); glob2(); glob3()
	print(var)

print('-'*50)
#test()  = comment, but doubling all rezults

# read next line
def maker(x):
	def action(n):
		return x**n
	return action

f = maker(3) # return action
print(f(3)) # return x**n

#lambda
def to_the_power():
	rezult = []
	for i in range(5):
		rezult.append(lambda x, i=i: i**x)
	return rezult

my_res = to_the_power()
print(my_res[1](2)) # show the 1 to the power 2
print(my_res[2](4)) # show the 2 to the power 4

#nonlocal

def tester(start):
	state = start
	def nested(label):
		nonlocal state
		print(label,'==', state)
		state += 1
	return nested

F = tester(0)
F(3)
F('dddd')
