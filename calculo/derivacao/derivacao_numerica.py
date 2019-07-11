from math import sin

def _derivada_1(f,a,h=0.001): #O(h)
	return (f(a+h)-f(a))/(h)

def __derivada_1(f,a,h=0.01):  #O(h^2)
	return (f(a+h)-f(a-h))/(2*h)

def ___derivada_1(f,a,h=0.1):  #O(h^4)
	return (-f(a+2*h)+8*f(a+h)-8*f(a-h)+f(a-2*h))/(12*h)

def derivada_2(f,x,Dx=0.01):	#usando 4 pontos, O(h^4)
	return (( 16.0*( f(x+Dx) + f(x-Dx)) ) - ( f(x+2.0*Dx) + f(x-2.0*Dx) ) - ( 30.0*f(x)) ) / (12.0*(Dx*Dx))

def f(x):
	return sin(x)

print(_derivada_1(f,0))