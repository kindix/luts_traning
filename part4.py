my_di = {'a': 1, 'b': 2, 'c': 3}

# old versin
mm = list(my_di.keys())
mm.sort()
for key in mm:
	print(key, '=>', my_di[key])

# NEW VERSION start 3.0
for key in sorted(my_di):
	print(key, '==>', my_di[key])

print(my_di['a']) # enter with key)

a = [2,54,7,32,12,56,56,2]
print(a.index(32))	# on place
print(a.count(2)) # how many times