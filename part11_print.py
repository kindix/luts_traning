num = 2
wink = 1
A,B = num, wink # tuple
print(A)
[c,d] = [num, wink] # list

a,b,c = list(range(3))
print(a,c)

A = 'a fuck'
a, *b = A
print(b) # list [' ', 'f','u','c','k']

B = [1,2,3,4]
*a,b = B # a = [1,2,3], b = 4

L = [1,2,3,4]
while L:
	front, *L = L
	print(front, L)


new_list = [1,2,3,4]
new_list += [5,6] # work as extend()

# print to file
log_print = open('log.txt', 'a')
print(new_list, file = log_print)
log_print.close()

# ERRORS

import sys
print('BAD!!!'*8, file = sys.stderr)
