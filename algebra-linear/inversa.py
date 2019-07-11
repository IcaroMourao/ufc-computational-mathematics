
def inversa(A):
	n = len(A)
	b = []

	for i in range(n):
		b.append( [0] * n )

	for i in range(0,n):
		j = i
		pivote = A[i][j]
		b[i][j] = 1/pivote

		for m in range(0,n):
			if(m != i):
				b[i][m] = A[i][m]/pivote

		for m in range(0,n):
			if(m != j):
				b[m][j] = -A[m][j]/pivote;

		for x in range(0,n):
			for y in range(0,n):
				if(x!=i and y!=j):
					b[x][y] = A[x][y]-(A[i][y]*A[x][j])/pivote

		for k in range(0,n):
			for l in range(0,n):
				A[k][l] = b[k][l];

		return b

def main():
	A = [[2,3,1],
		 [1,0,4],
		 [2,3,4]]

	A_inv = inversa(A)

	for i in A_inv:
		print(i)

if __name__ == "__main__":
		main()