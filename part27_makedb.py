from part27_class import Person, Manager
	
bob = Person('Bob Smith')
sue = Person('Sue Jones', job = 'dev', pay = 10)
phil = Manager('Phil Adams', pay = 1000)

import shelve

db = shelve.open('persondb')
for obj in (bob,sue,phil):
	db[obj.name] = obj
db.close()

if __name__ == '__main__':

	db = shelve.open('persondb')
	for key in sorted(db):
		print(key, '=>', db[key])