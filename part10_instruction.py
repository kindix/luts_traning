#while True:
#	user_info = input('Put your info: \n')
#	if user_info == 'stop':
#		break
#	elif not user_info.isdigit():
#		print('BAD!!!'*5)
#	else:
#		print(int(user_info)**2)
#print('Bye')

#while True:
#	user_info = input('Put your info: \n')
#	if user_info.isdigit():
#		print(int(user_info)**2)
#		continue
#	elif user_info == 'stop':
#		break
#	else:
#		print('BAD!!!'*5)
#print('Bye')

#while True:
#	user_info = input('Put your info: \n')
#	if user_info == 'stop': 
#		break
#	try:
#		int(user_info)**2
#	except: 
#		print('ERROR')
#	else:
#		print(int(user_info)**2)
#print('Bye')

while True:
	user_info = input('Put your info: \n')
	if user_info.isdigit():
		num = int(user_info)
		if num < 20:
			print('To low')
		else:
			print(num**2)
		continue
	elif user_info == 'stop':
		break
	else:
		print('BAD!!!'*5)
print('Bye')