# with return changer work always
def multiple(x):
	x = 2
	y =[1,3]
	return x # this is turple

x = 1
y = [1,2]
x = multiple(x)
print(x)
# def f(name)
def func(a,b,c):
	print(a,b,c)

func(1,2,3)

# def f(name = value)
def func2(a = 3, b = 4, c = 5):
	print(a,b,c)

func2()

# def ...
def func3(a, b = 6, c = 7):
	print(a,b,c)

func3(1)

# def f(*m)
def func4(*args): # to tuple
	print(args)

func4(1)
func4(2,3)
func4(4,5,6)

# def f(**m)
def func4(**args): # to dict
	print(args)

func4(a=1)
func4(a=2,b=3)
func4(a=4,b=5,c=6)

### unpack
def func5(a,b,c,d):
	print(a,b,c,d)

args = (1,2)
args += (3,4)
func5(*args)

args = {'a': 1, 'b': 2, 'c': 3}
args['d'] = 4
func5(**args)

#Exp
func5(*(1,2), **{'d': 4, 'c':3})

#Exp
func5(1, *(2,3), **{'d': 4})

#Exp
func5(1, *(2,3), d = 4)

#Exp
func5(1, *(2,), c = 3, **{'d': 4})

#Exp
def crouli(a,*b,c):
	print(a,b,c)

crouli(1,2,c = 3)

#Exp
def crouli2(a,*,b,c=3):
	print(a,b,c)

crouli(1,2,c=3)


def min_value(*args):
	tmp = list(args)
	tmp.sort()
	return tmp[0]

print(min_value(1,4,4,32))

