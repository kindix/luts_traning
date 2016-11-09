import part5_numbers
print('How many %s' % len(str(part5_numbers)))

S = 's\np\ta\x00m\0' #\x00 == 'space' \0 'space' too (table 7.2 Luts)
print(S)


# five line with \n
text = '''dkghodghlkdf
gdfghdfjkghdfl
jhgdfhgdfg
dfgdf
gdfghdfjkghdflgdf
gdfghdfjkghdflgdf'''
print(text)

# one line with space
text2 = 'asdsadsad \
asdasdsadsad \
adsadsadsad\
sddsadasd'
print(text2)

# no format with \ maybe noformat always...
S = r'\temp\spam'
print(S) #\temp\spam

#double '\' use with \n )))
html = 'hltv.org\\news'
print(html)

value = 'a'
ord_value = ord(value)
print(eval(str(ord_value)))

# Luts 229 table 7.3
#replace
string = 'spammy'
string = string.replace('mm','xx')
print(string)

string_two = 'xxxxSPAMxxxxSPAM'
where = string_two.find('SPAM')
string_two = string_two[:where] + 'EGGS' +string_two[where+4:]
print(string_two) 

# light version )))
string_two = 'xxxxSPAMxxxxSPAM'
new_string = string_two.replace('SPAM','EGGS', 1) # change one(two) arg of 'SPAM'
print(new_string)

#format str
import sys
string3 = 'My %(spam)s runs in %(platform)s' % {'spam' : 'PC', 'platform': sys.platform }
print(string3)

# second 
string4 = 'My {1[spam]} runs in {0.platform}'.format(sys, {'spam': 'PC'})
print(string4)
