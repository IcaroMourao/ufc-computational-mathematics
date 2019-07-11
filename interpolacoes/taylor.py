
def f(x):
	return 3*(x**2)+2*x-1

def g(x):
	return 2*(x**3)

def derivada_1(f,x,Dx=0.0001): #usando expansao de taylor
	return ( 8.0*( f(x+Dx) - f(x-Dx) ) - (( f(x+2.0*Dx) - f(x-2.0*Dx) )) ) / (12.0*Dx)

def derivada_2(f,x,Dx=0.0001):
	return (( 16.0*( f(x+Dx) + f(x-Dx)) ) - ( f(x+2.0*Dx) + f(x-2.0*Dx) ) - ( 30.0*f(x)) ) / (12.0*(Dx*Dx))

def taylor(f,x0,x):
    return f(x0) + derivada_1(f,x0)*(x-x0) + (derivada_2(f,x0)/2.0)*((x-x0)**2)

result = taylor(g,3,0)
print("Função = ", g(3))
print("Interpolacao = ", result)
print("Erro = ", float(g(3) - result))
#print ("Derivada segunda de g(3) = ",derivada_2(g,3))