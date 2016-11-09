my_tuple = tuple('spam'); print(my_tuple)
one_value_in_tuple = (0,)
T = 0, 'No', 1, 'Yes'; print(T)
print(my_tuple[1:])
print(len((my_tuple)))
print(my_tuple + T)

#generator
ge_list = [x*2 for x in my_tuple] #use tuple() to convert 

my_tuple.index('s')
my_tuple.count('yes')

sort_list = sorted(my_tuple); print(sort_list)
sort_tuple = tuple(sort_list); print(sort_tuple)