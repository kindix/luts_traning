#create file and write text
with open('my_file.txt', 'w') as text_file:
	text_file.write('Hello\n')
	text_file.write('kindix')
# read text
with open('my_file.txt', 'r') as text_file:
	aString = text_file.read()
	print(aString)
# read first line in txt
with open('my_file.txt', 'r') as text_file:
	aString2 = text_file.readline()
	print(aString2)
# read line by line
for line in open('my_file.txt'):
	print(line)

data = open('my_file.txt', 'rb').read() #luts c.294(9)
print(data)
print(data[0:6]) # string
print(data[0:6][0]) # 8bit 
print(bin(data[0:6][0])) # 2bit

A = 'string'
B,C,D = 1,2,3
E = [4,5,6]
F = {'a': 1, 'b': 2}

with open('my_file.txt', 'w') as text_file:
	text_file.write(A + '\n')  
	text_file.write('{0},{1},{2} \n'.format(B,C,D))
	text_file.write(str(E) + '##' + str(F) + '\n')

with open('my_file.txt', 'r') as text_file:
	#read all text
	print(text_file.read())

with open('my_file.txt', 'r') as text_file:
	#read first line
	text_file.readline()
	#read second line and convert to int
	read_two_line = text_file.readline()
	show = read_two_line.split(',')
	# generate to list
	num_in_two_line = [int(x) for x in show]
	#read 3 line
	read_tr_line = text_file.readline()
	show_tr = read_tr_line.split('##')
	#generate to list
	objects_in_tr_line = [eval(x) for x in show_tr]
	print(objects_in_tr_line)

# use module 'pickle' ('wb and rb ==> binnary')
my_dict = {'NAME': 'Andrey', 'AGE': 27}

with open('my_file_pickle.txt', 'wb') as text_file:
	import pickle
	pickle.dump(my_dict,text_file);

with open('my_file_pickle.txt', 'rb') as text_file:
	print(pickle.load(text_file))

# use module struct for binnary

with open('my_file_struct.bin', 'wb') as text_file:
	import struct
	data = struct.pack('>i4sh', 7, 'spam', 8)
	text_file.write(data)

with open('my_file_struct.bin', 'rb') as text_file:
	read_text = text_file.read()
	values = struct.unpack('>i4sh',read_text)
	print(values)

