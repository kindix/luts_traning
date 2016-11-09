'''
I don't now 
what happend
'''

seplen = 60
sepchr = '='

def listing(module, verbose = True):
	sepline = seplen*sepchr
	if verbose:
		print(sepline)
		print('name: ', module.__name__, 'file: ', module.__file__)
		print(sepline)

	counter = 0
	for attr in module.__dict__:
		print('{0:02d}) {1}'.format(counter, attr), end = '')
		if attr.startswith('__'):
			print('<built-in name')
		else:
			print(getattr(module, attr))
		counter += 1

	if verbose:
		print(sepline)
		print(module.__name__, 'has {0:d} names'.format(counter))
		print(sepline)	


if __name__ == '__main__':
	import part24_module3
	listing(part24_module3)

	print(__doc__)