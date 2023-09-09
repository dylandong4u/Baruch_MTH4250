def gcd(a,b):
	'''
	Input positive integers a and b with a >= b
	Return gcd of a,b.
	'''
	r = [a,b] # a list to keep track of the remainders 
	
	while r[-1] > 0:
		quo = r[-2] // r[-1] # we use negative indexs cuz we are adding numbers to the list
		rem = r[-2] % r[-1]
		
		r += [rem]
		print(r)
		print('%d = %d * %d + %d'%(r[-2],r[-1],quo,rem))
	
	return r[0]

a = 726
b = 252
print(gcd(a,b))
