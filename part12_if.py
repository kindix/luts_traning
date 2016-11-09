if not 1:
	print('False')
else:
	print('True')

# Exp
string = 'ran forest, ran'
if string == 'fuck off':
	print(string)
elif string == 'mmmm':
	print(string)
else:
	print('ran fucking forest, ran')

# Exp
choise = 'ham'
print({'spam': 23,
		'ham': 1.99,
		'fuck': 2.2}[choise])

#same Exp 
my_di = {'spam': 23,
		'ham': 1.99,
		'fuck': 2.2}
print(my_di.get('ham', 'Bad choise'))

# same Exp
x = 'ham'
if x in my_di:
	print(my_di[x])
else:
	print('Bad choise')

#Exp
string_value = 'SPAM'
if 'kind' in 'kindix':
	print(string_value * 8)
	string_value += 'NI'
	if string_value.endswith('NI'): # word end = 'NI'
		string_value *= 2
		print(string_value)

#Exp
if X:
	A = X
else:
	A = Z
#Exp
A = Y if X else Z
#Exp
print(['Y', 'Z'][bool('')])
print(['Y', 'Z'][bool('spam')])
