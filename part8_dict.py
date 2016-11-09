D = dict(name2 = 'PHIL', age2 = 30) # all keys must be equal 'str'
#same...
D = {'name': 'BOB', 'age': 25}
#same...
D = dict(zip(['name', 'age', 'work'], ['BOB', 27, 'IT'])) # keys and value crate with lists

#generqator
my_gen_dict = {i: j for (i,j) in zip(['name', 'age', 'work'], ['BOB', 27, 'IT'])}
print(my_gen_dict)
#sort dict
for key in sorted(my_gen_dict): print('{0} => {1}'.format(key, my_gen_dict[key]))

dict_fromkeys = dict.fromkeys(['a','b'], 0) # if keys eaquls one item (here {'a': 0, 'b': 0})
dict_fromkeys = {i:0 for i in ['a','b']}
print('='*50)
print(dict_fromkeys)
print('='*20)

print(D.keys()) #show only keys
for key in D.keys(): print(key)
for key in D: print(key)


print(list(D.values())) # show onle values on list
print(list(D.items())) # show all dict in () on list
print(D['name']) #show value with key='name'

print(list(D.keys())) # show only keys on list

#print(D.pop('name')) #remove value with key='name' === 
print(D.get('name', 'not here')) # check present key and return value in dict 
del D['name'] # delete name

print('='*20)

print(len(D))
print('name' in D) #check

# rename  value 
D['age'] = 28

# key may have same value
D['name'] = ['PHIL', 'ANDREY']
print(D) 

D2 = {'kill': 'BILL', 'yma': 'turman'}
print('='*20)
print(D2.update(D)) #xz don't work((
