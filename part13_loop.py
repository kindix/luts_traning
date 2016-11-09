# immprtal loop
#while True:
#	print('Type Ctrl+C to exit')

string = 'spam'
while string:
	print(string, end = ',')
	string = string[1:]

a = 0; b = 10
while a < b:
	print(a, end=',')
	a += 1

#while 1: pass

#Exp
x = 10
while x:
	x -=1
	if x % 2 !=0: continue
	print(x)
#same Exp
x = 10
while x:
	x -=1
	if x % 2 ==0: 
		print(x)
#Exp
while True:
	name = input('Enter your name: ')
	if name == 'stop': break
	age = input('How old are you?')
	print('Hello {0}, your are {1} years old man'.format(name,age))

#Exp
y = int(input('Enter y: '))
x = y//2
while x > 1:
	if y % x == 0:
		print('asffd')
		break
	x -= 1
else: 
	print(y, 'is prime')

# Exp 'for'
items = ['aaa', 111, (4,5), 2.01]
tests = [(4,5), 3.14]
for test in tests:
	for item in items:
		if test == item:
			print(test, 'was found')
			break
	else:
		print(test, 'not found')

# same Exp 'for'
for key in tests:
	if key in items:
		print(key, 'was found')
	else:
		print(key, 'not found')

# EXP find same value
string_one = 'spam'
string_two = 'sram'

same_value = []
for word in string_one:
	if word in string_two:
		same_value.append(word)
print(same_value)

#Exp
new_list = [1,2,3,4,5]
for i in range(len(new_list)):
	new_list[i] += 1

#Exp 'zip'
for (x,y) in zip(string_two,string_one):
	print(x,'+',y, '=', x+y)

#Exp
for (i,j) in enumerate(string_one):
	print(i, ':', j)