'''sdfsdfsdf
	dsfsdfsdf
	dsfdsfsf''' # same, but we can use it __doc__

print(__doc__) # return string 

import sys

print('for sys','='*20)
print(dir(sys))
print('for list','='*20)
print(dir([]))
print('for str','='*20)
print(dir(''))
print('for num','='*20)
print(dir(4))
print('='*50)

print(map.__doc__)
#info
print(help(map)) #same 
print(help(dict))

import part8_dict

print(help(part8_dict)) #info 