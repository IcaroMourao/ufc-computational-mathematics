def lu(A, b):
	n = len(A)
	L = []

	for i in range(n):
		L.append( [0] * n )
		L[i][i] = 1

	for k in range (0, n-1):        
		for i in range (k+1, n):            
			if (abs(A[k][k]) < abs(A[i][k])):
				for j in range (0,n):
					aux=A[k][j]
					A[k][j]=A[i][j]
					A[i][j]=aux
				aux = b[k]
				b[k]=b[i]
				b[i]=aux
			m = -A[i][k]/A[k][k]
			L[i][k] = -m
			A[i][k] = 0
			for j in range (k+1, n):
					A[i][j] = A[i][j] + m*A[k][j]
			b[i] = b[i] + m*b[k]
   
	return(L,A,b)

def dot_prod(L,U):
	n = len(L)
	P = []

	for i in range(n):
		P.append( [0] * n )

	for i in range(0,n):
		for j in range(0,n):
			value=0
			for k in range(0,n):
				value = value + L[i][k]*U[k][j]
			P[i][j]=value
	return P

def detLU(M):
	n = len(M)
	prod = 1
	for i in range(0,n):
		prod = prod * M[i][i]
	return prod

def main():
	A = [[6.0, 0.0, -3.0, 0.0, 0.0],
		[3.0, -3.0, 0.0, 0.0, 0.0],
		[0.0, -1.0, 9.0, 0.0, 0.0],
		[0.0, 1.0, 8.0, -11.0, 2.0],
		[3.0, 1.0, 0.0, 0.0, -4.0]]

	b = [50.0, 0.0, 160.0, 0.0, 0.0]

	m = lu(A,b)
	print('L = ', m[0][0])
	for i in range(1,len(m[0])):
		print('    ',m[0][i])

	print('\nU = ', m[1][0])
	for i in range(1,len(m[1])):
		print('    ',m[1][i])

	print('\nb = {}\n'.format(m[2]))

	A = dot_prod(m[0],m[1])
	print('A = ', A[0])
	for i in range(1,len(A)):
		print('    ',A[i])

	print("\n",detLU(m[1]))

if __name__ == "__main__":
		main()