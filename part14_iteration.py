# Exps for files
# Exp

my_file = open('part9_files.py')
print(my_file.readline())
print(my_file.readline())
print(my_file.readline())
print(my_file.readline())

# .__next__() = next() = .readline()
print(my_file.__next__())
print(next(my_file))

# iterator 'for' return __next__()
#for line in my_file:
#	print(line.upper(), end = '') # end = '' # del one \n

# use iter
new_list = [1,4,8,2,4]
iter_list = iter(new_list)
print(next(iter_list))
print(next(iter_list))

#generator
my_list = [1,3,5,7,9]
gen_list = [x**2 for x in my_list]
print(gen_list)

#gen
xz_list = [lines.rstrip() for lines in open('part9_files.py') if lines[0] == 'p'] # line start 'p'

#same gen
xz_list2 = list(map(str, open('part9_files.py')))

#sort
A = sorted(new_list)

#max,min
min(open('part9_files.py'))
max(open('part9_files.py'))

print(set(new_list))

