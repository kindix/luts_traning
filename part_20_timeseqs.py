import sys
import part_20_mytimer

reps = 10000
replist = range(reps)

def for_loop():
	res = []
	for x in replist:
		res.append(x + 1)
	return res

def list_comp():
	return [x + 1  for x in replist]

def map_call():
	return list(map(lambda x: x + 1, replist))

def gen_expr():
	return list(x + 1 for x in replist)

def gen_func():
	def gen():
		for x in replist:
			yield x + 10 
	return list(gen())

print(sys.version)

for test in (for_loop, list_comp, map_call, gen_expr, gen_func):
	elapsed, rezult = mytimer.timer(test)
	print('='*50)
	print('{0}: {1:0.6f} ==> [{2}...{3}]'.format(test.__name__,elapsed, rezult[0],rezult[-1]))