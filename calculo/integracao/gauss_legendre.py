def f(x):
	return x**4 + 2*x + 1
	#return x**3 + 2*x + 1
	#return x**4 + 7*x -1
	#return x**3 + 1

ordem2 = [[-0.577350269, 1.0],
		  [ 0.577350269, 1.0]]

ordem3 = [[ 0,           0.888888889],
		  [-0.774596669, 0.555555556],
		  [ 0.774596669, 0.555555556]]

ordem4 = [[-0.339981043, 0.652145155],
		  [ 0.339981043, 0.652145155],
		  [-0.861136312, 0.347854845],
		  [ 0.861136312, 0.347854845]]

def gauss_legendre(f,a,b,n=2):

	mz = float(b+a)/2
	mx = float(b-a)/2

	result = 0.0

	for i in range(0,n):
		if n == 2:
			xi = ordem2[i][0]
			wi = ordem2[i][1]

		elif n == 3:
			xi = ordem3[i][0]
			wi = ordem3[i][1]

		elif n == 4:
			xi = ordem4[i][0]
			wi = ordem4[i][1]	

		result += wi*f((xi*mx + mz))

	return result*mx

print(gauss_legendre(f,2,4))
