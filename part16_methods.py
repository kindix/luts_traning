def items(x,y):
	return x*y

print(items('gg',5))

first_list = [21,234,13,345,56,234,6,34,12]
second_list = [234,13,235,123,56,23,1,6,12,56,123]


def same_values(x,y):
	rezult = [] # local value
	for key in x:
		if key in y:
			rezult.append(key)
			rezult.sort()
	return(rezult)
print(same_values(first_list,second_list))

# same
res = [x for x in first_list if x in second_list]
print(res)