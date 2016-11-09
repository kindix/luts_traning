dic = (4,5,6)
dic = (1,) + dic[1:]
print(len(dic)) 

L = [0,1,2,3]
print(([1,2,3]+[4,5,6])[2:4])
L[3:1] = ['?']
print(L)

L[:0] #only first value

s = 'spam'

s = s[0] + 'l' + s[2:]
print(s)
