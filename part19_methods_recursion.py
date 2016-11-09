# recursion
def sum_func(L):
	print(L)
	if not L:
		return 0
	else:
		return L[0] + sum_func(L[1:])

print(sum_func([1,2,3,4,5]))
print(sum([1,2,3,4,5]))

#exp two
def sum_version2(L):
	if not L: return 0 
	return xz_func(L)

def xz_func(L):
	return L[0] + sum_func(L[1:])

print(sum_version2([1,5,10,14,15]))

# recursion summation strong list
def sumtree(L):
	rezult = 0
	for value in L:
		if not isinstance(value, list):
			rezult += value
		else:
			rezult += sumtree(value)
	return rezult

my_strong_list = [1, [2, [3,4], 5], 6, [7,8]]

print(sumtree(my_strong_list))

#annotation __annotations__

def new_func(a: 'spam' = 1, b = 1, c: 99 = 99): #luts c547
	return a + b + c

print(new_func(1,2,3))
print(new_func.__annotations__)

for arg in new_func.__annotations__:
	print(arg, '==>', new_func.__annotations__[arg])

print(new_func())

# lambda exp
lambda_func = lambda x,y,z: x**2 + y + z
print(lambda_func(10,2,3))

# lambda list?
lambda_list = [lambda x: x**2,
				lambda x: x**3,
				lambda x: x**4]
for item in lambda_list:
	print(item(2))

# map exp
couters = [1,2,3,5,6,7,8,9,10] # luts c554
def func_count(x):
	return x + 10

print(list(map(func_count, couters)))
#same exp
print(list(map(lambda x: x + 10, couters)))

print(list(map(pow, couters, couters)))

#filter
print(list(filter(lambda x: x > 0, range(-5,5))))

#reduce 
from functools import reduce
print(reduce(lambda x,y: x + y, [1,2,3,4,5,6,7]))
print(reduce(lambda x,y: x + y, [1,2]))
