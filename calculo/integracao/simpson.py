
def f(x):
    return 3*(x**2)-x
	#return x**5 + x**3 + 12*x**2 + 5*x
	#return x**3 + 12*x**2 + 5*x
    #return x**2 + 2*x - 3

def simpson_1_3(f,a,b):
	return ((float(b-a)/6)*(f(a)+4*f((a+b)/2)+f(b)))

def simpson_1_3_composto(f, a, b, n=30):
    h = float(b - a) / n
    result = f(a) + f(b)

    for i in range(1, n, 2):
        result += 4 * f(a + i * h)
    for i in range(2, n-1, 2):
        result += 2 * f(a + i * h)

    return result * h / 3.0

def simpson_3_8(f,a,b):
	return (f(a)+3*f(float(2*a+b)/3)+3*f(float(2*b+a)/3)+f(b))*(float(b-a)/8.0)

def simpson_3_8_composto(f,a, b, n=100):
    h = (float(b - a) / n)
    result = f(a) + f(b);
  
    for i in range(1, n):
        if (i % 3 == 0):
            result +=  2 * f(a + i * h)
        else:
            result+= 3 * f(a + i * h)
     
    return ((float( 3 * h) / 8 ) * result )
	
print('simples13 = ',simpson_1_3(f,0,2))
print('composta13 = ',simpson_1_3_composto(f,0,2))
print('simples38 = ',simpson_3_8(f,0,2))
print('composta38 = ',simpson_3_8_composto(f,0,2))
