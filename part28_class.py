class MixedNames:
	data = 'spam'
	def __init__(self,value):
		self.data = value
	def display(self):
		print(self.data, MixedNames.data)

x = MixedNames(1)
y = MixedNames(2)
x.display()
y.display()



class NextClass:
	def printer(self, text):
		self.text = text
		print(self.text)

d = NextClass()
d.printer('inctance call')
NextClass.printer(x, 'class call')
x.text


class Super:
	def method(self):
		print('in SUPER method')

class Sub(Super):
	def method(self):
		print('starting SUB method')
		Super.method(self)
		print('end SUB method')

s = Super()
s.method()

a = Sub()
a.method()