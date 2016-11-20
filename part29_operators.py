class Number:
	def __init__(self,start):
		self.data = start
	def __sub__(self, other):
		return Number(self.data - other)

X = Number(5)
Y = X - 2
print(Y.data)

class Indexer:
	def __getitem__(self, index):
		return index ** 2

C = Indexer()
print(C[2])

for i  in range(5):
	print(C[i])

class Slicing:
	data = [1,2,3,4,5,6,7,8,9,10]
	def __getitem__(self, index):
		print('getitem:', index)
		return self.data[index]

A = Slicing()
print(A[2:5])

for i  in range(10):
	print(A[i], end = ' ')

class Stepper:
	def __getitem__(self,index):
		return self.data[index]

X = Stepper()
X.data = 'Spam'
print(X[1])

for item in X:
	print(item, end = ' ')
