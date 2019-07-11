
def f(x):
	return x**2 + 2*x
	#return x**3 + 12*x**2 + 5*x
    #return x**2 + 2*x - 3

def trapezio_simples(f, a, b):
	return float(b-a)*((f(a)+f(b))/2)
	
def sub_trapezio(f, a, b, n=100):

    result = (f(a)+f(b))/2.0
    h = float(b - a) / n

    for i in range(1,n):
        result = result + f(a+h*i)

    return result * h


print("Composto = ", sub_trapezio(f,0,4))
print("Simples = ", trapezio_simples(f,0,4))
