from math import sin

def f(x):
	return sin(x) - 1

def calc(a,b,fa,fb):
	return a+(fa*(a-b))/(fb-fa)

epsilon = 0.1

def pos_false(f,a,b):
	if(abs(b-a) <= epsilon or abs(f(a)) <= epsilon or abs(f(b)) <= epsilon):
	     return b
	while True:
		p = calc(a,b,f(a),f(b))

		if(abs(f(p)) <= epsilon):
		    return p
		if(f(a) * f(p) > 0):
			a = p
		else:
			b = p
		if(abs(b-a) <= epsilon):
			return a
	return p

print(pos_false(f,1,2))
