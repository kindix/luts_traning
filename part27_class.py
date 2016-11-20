from part27_classtools import AttrDisplay

class Person(AttrDisplay):
	def __init__(self, name, job = None, pay = 0):
		self.name = name
		self.job = job
		self.pay = pay
	#def __str__(self):
	#	return '[Person: {0} has {1} $]'.format(self.name,self.pay)
	def last_name(self):
		return self.name.split()[-1]
	def give_raise(self, percent):
		self.pay = float(self.pay * (1 + percent))

class Manager(Person):
	def __init__(self, name, pay):
		Person.__init__(self, name, 'mgr', pay)
	def give_raise(self, percent, bonus = 0.1):
		Person.give_raise(self, percent + bonus)


if __name__ == '__main__':

	bob = Person('Bob Smith')
	sue = Person('Sue Jones', job = 'dev', pay = 10)
	print(bob.name, '==', bob.job)
	print(sue.name, '==', sue.job)
	print(bob)
	print(sue)
	print(bob.last_name())
	sue.give_raise(0.01)
	print(sue.pay)
	print(sue)

	phil = Manager('Phil Adams', pay = 1000)
	print(phil)
	phil.give_raise(0.1)
	print(phil.pay, phil.job)

