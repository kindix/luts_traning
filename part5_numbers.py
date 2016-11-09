
import decimal 
decimal.getcontext().prec = 4   # 4 times after ','
current_value = decimal.Decimal(1) / decimal.Decimal(7)
print(current_value)
########################
import fractions
fractions.Fraction(1,3) 
#########################
a = 8
b = 3
c = a**b**a
print(len(str(c)))
#########################
import math
print(math.floor(2.5))
print(math.floor(-2.5))
print(math.trunc(2.5))
print(math.trunc(-2.5))
print('===============')
print(round(-2.5))
print(round(2.5))
print('{0:.48f}'.format(math.pi)) # 48 max after ','
print(1/3)

# generate 'set'
s = set('spam')
s.add('ss')
s.remove('p')
print(s)
my_list = [1,2,3,4]
my_set = set(my_list)
print(my_set)

# new set
my_set2 = {1,2,3,4}

#check how many link on object
import sys
print(sys.getrefcount(my_set))

