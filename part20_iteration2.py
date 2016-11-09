res = [x + y for x in [0,1,2] for y in [10,11,12]]
print(res)

M = [[1,2,3],
	[4,5,6],
	[7,8,9]]

N = [[10,20,30],
	[40,50,60],
	[70,80,90]]

multy = [[M[row][col] * N[row][col] for col in range(3)] for row in range(3)]
print(multy)

list_of_turple = [('bob', 35, 'mgr'), ('mel', 29, 'dev')]
age = [age for (name, age, job) in list_of_turple]
print(age)

#yield
def gensquares(N):
	for value in range(N):
		yield value**2

for value in gensquares(5):
	print(value, end = ' ')

#use lambda 
for i in map(lambda i : i**2, range(5)):
	print(i, end = ' ')

squared = [x**2 for x in range(5)]
print(squared, end = ' ')

#send
def gen():
	for i in range(10):
		x = yield i
		print(x)

g = gen()
next(g)
g.send(77)

print([x*4 for x in 'SPAM'])

# yield
def timesfour(items):
	for item in items:
		yield item*4

print(list(timesfour('SPAM')))

# created my func 'map'
def mymap(func, *args):
	res = []
	for arg in zip(*args):
		res.append(func(*arg))
	return res

print(mymap(abs, [-2,-1,0,1,2]))

# same
def mymap2(func, *args):
	return [func(*arg) for arg in zip(*args)]

print(mymap2(abs, [-2,-1,0,1,2]))

#generation dict {} and set {}
my_dict = {x: x*x for x in range(5)}
my_set = {x for x in range(5)}
print(my_dict, '|||', my_set)