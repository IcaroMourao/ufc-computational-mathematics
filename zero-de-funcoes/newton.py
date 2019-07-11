
def f(x):
    return 3*(x**2) + 2*x-1

def g(x):
	return 5*(x**5)-2*(x**4)+3*(x**2) -8*x-10

def h(x):
	return x**3 - 8

def derivada(f, x, Dx=0.0001):
	return ( 8.0*( f(x+Dx) - f(x-Dx) ) - (( f(x+2.0*Dx) - f(x-2.0*Dx) )) ) / (12.0*Dx) 

def newton(g, x0, epsilon=0.001):
    x = x0
    i = 0
    while i < 150:
        valor_func = g(x)
        valor_deri = derivada(g,x)
        x = x - valor_func / valor_deri
        if abs(valor_func / valor_deri) <= epsilon:
        	break
        i += 1
    return x

print(newton(h, 5))