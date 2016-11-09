import time
reps = 1000
reps_list = range(reps)

def timer(func, *pargs, **kargs):
	start = time.clock()
	for i in reps_list:
		ret = func(*pargs, **kargs)
	elapsed = time.clock() - start
	return (elapsed, ret)