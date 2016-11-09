my_file = open('part4_files.txt', 'w')
my_file.write('Hello ')
my_file.write('world\n')
my_file.close()

my_file = open('part4_files.txt', 'r')
print(my_file.read())

print({x**2 for x in [1,2,3,4]})

print(set('Hello')) # del double {'e', 'l', 'o', 'H'}

#Drobu
from fractions import Fraction
f = Fraction(2,3)
print(f + 1)

#standatr ','
import decimal
d = decimal.Decimal('3.141')
print(d + 1)
# return type of value
print(type(my_file))
###
if isinstance(d, decimal.Decimal):
	print('yes')
else: 
	print('BOOM')


## Create my class======================
class IT:
	"""docstring for IT"""
	def __init__(self, name, pay):
		self.name = name
		self.pay = pay
	def last_name(self):
		return self.name.split()[-1]
	def new_pay(self, percent):
		self.pay *= (1.00 + percent)

iam = IT('Andrey kindix', 5000)

print(iam.last_name())

iam.new_pay(0.175)
print(iam.pay)
#=======================================		