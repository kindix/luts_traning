my_string = 'fuck you bitch'

my_list = []
for liter in my_string:
	ord_value = ord(liter)
	my_list.append(ord_value)
summation = sum(my_list)
print(summation)

my_string = 'fuck you bitch'

new_list = list(map(ord, my_string))
print(new_list)

second_list = []
for liter in my_string:
	ord_value = ord(liter)
	second_list.append(ord_value)
print(new_list)

#for i in range(50):
#	print('hello %d\n\a' % i)

my_dict = {'a': 1, 'd': 4, 'c': 3, 'b': 2 }
for key in sorted(my_dict): print(key, '=>', my_dict[key])

list_to_the_power_2 = [1,2,4,8,16,32,64,128,256]
for value in list_to_the_power_2:
	if value == 2**5:
		position = list_to_the_power_2.index(value)
		print('I find it {0} and her position is {1}'.format(value, position))

# FIRST lambda
x = 5
lambda_list = list(map(lambda x: 2**x, range(10)))
print(lambda_list)
for value in lambda_list:
	if value == 2**5:
		position = lambda_list.index(value)
		print('I find it {0} and her position is {1}'.format(value, position))
		