import re

my_text = 'This is my text, created by kindix'
# find with 
match = re.match('This is my text, created by (.*)', my_text)
#print(match.group(1))

my_list = [[1,2,3], [4,5,6], [7,8,9]]

my_list.append(2)
#print(my_list)

#col2 = []
#for row in my_list:
#	col2 = row[1]
	#print(col2)

diag = []
for i in range(3):
	diag = my_list[i][i]
	print(diag)

#for word in my_text.split(' '):
#	print(word)

a = {}
for i in range(3):
	a = {i:my_list[i]}
	print(a)

my_hesh = {'a': 1, 'b': 2, 'c': 3}
my_keys = list(my_hesh.keys())

my_keys.sort()
print(my_keys)

for key in my_keys:
	print(key,'=>', my_hesh[key])