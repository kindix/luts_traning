class FirstClass:
	"""docstring for FirstClass"""

	def setdata(self, value):
		self.data = value
	def display(self):
		print(self.data)
		
x = FirstClass()
y = FirstClass()
x.setdata('Andrey kindix')
y.setdata(27)
x.display()
y.display()	


class SecondClass(FirstClass):
	"""docstring for SecondClass"FirstClass" """
	def display(self):
		print('Current value = {0}'.format(self.data))

z = SecondClass()
z.setdata(200)
z.display()	


class ThirdClass(SecondClass):
	"""docstring for ThirdClass"SecondClass" """
	def __init__(self, value):
		self.data = value
	def __add__(self, other):
		return ThirdClass(self.data + other)
	def __str__(self):
		return '[ThirdClass: {0}]'.format(self.data)
	def mul(self, other):
		self.data *= other

a = ThirdClass('abc')
a.display()
print(a)
b = a + 'xyz'
b.display()
a.mul(3)
print(a)
