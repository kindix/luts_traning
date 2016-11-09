#create list with Unicode num
string = 'spam'
my_list = list(map(ord, string))
print(my_list)

#come back to list
for x in my_list:
	print(chr(x), end = '') #end = '' very importend
print('\n')

#generators
res = [x*2 for x in string] #return list
print(res)

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix[0]) # first row

#slicing
L = ['spam', 'Spam', 'SPAM!']
L[2] = 'lozer'
L[0:1] = ['ha-ha', 'Boom']

# methods
L.append('apple')
L.sort()
L.reverse()
L.sort(key = str.lower) # must be same first letter in element of list, if != first of all capital sort after small
L.sort(key = str.lower, reverse = True)
sorted(L, key = str.lower, reverse = True) # work if on top non methods for L 
print(L)
print('='*15)

#[1,2,'spam'].sort()  ===>  # don't do this str() < int()
L.pop(-2) #remove [-2]
L.insert(1, 'kindix')
L.remove('ha-ha')
del L[1:3]
print('We have %s apple(s)' % L.count('apple')) #how many apples we have in list
print(L)

#find somethig, but luts don't write about thiss
for item in L:
	if item == 'apple':
		print('We have an %s' %item)
		print('We have an {0}'.format(item)) # two ways to format string (see p.7)