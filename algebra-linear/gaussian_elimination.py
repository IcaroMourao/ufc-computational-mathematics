
def gaussian(A, b):
	n = len(A)

	for k in range(0,n-1):
		for i in range(k+1,n):
			m = A[i][k]/A[k][k]
			A[i][k] = 0
			for j in range(k+1,n):
				A[i][j] = A[i][j] - m * A[k][j]
			b[i] = b[i] - m * b[k]

	return (A,b)

def gaussian_piv(A,b):
	n = len(A)

	for k in range(0,n-1):
		pivot = A[k][k]
		row_pivot= k

		#pivoteamento
		for i in range(k+1, n):
			if abs(A[i][k]) > abs(pivot):
				pivot = A[i][k]
				row_pivot = i
		if pivot == 0:
			break
		if row_pivot != k:
			for j in range(0,n):
				aux = A[k][j]
				A[k][j] = A[row_pivot][j]
				A[row_pivot][j] = aux
			aux = b[k]
			b[k] = b[row_pivot]
			b[row_pivot] = aux

		#Eliminação
		for i in range(k+1, n):
			m = A[i][k]/A[k][k]
			A[i][k] = 0
			for j in range(k+1, n):
				A[i][j] = A[i][j] - m * A[k][j]
			b[i] = b[i] - m * b[k]

	return (A,b)


def main():
	A = [[1,-2,1],
	 	 [2,-1,4],
	 	 [3,-2,2]]

	b = [7,17,14]

	m = gaussian_piv(A,b)
	print('A = ', m[0][0])
	for i in range(1,len(m[0])):
		print('    ',m[0][i])

	print('\nb = ', m[1])

if __name__ == "__main__":
    main()