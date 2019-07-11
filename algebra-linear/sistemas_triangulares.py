		
def superior(A, b):
	x = []
	n = len(A)

	for i in range(0,n):
		x.append(0)

	for i in reversed(range(0,n)):
		s = 0
		for j in range(i+1,n):
			s += A[i][j] * x[j]
		x[i] = (b[i] - s) / A[i][i]
	
	return x

def inferior(A, b):
	x = []
	n = len(A)

	for i in range(0,n):
		x.append(0)

	x[0] = b[0] / A[0][0]
	for i in range(1,n):
		s = 0
		for j in range(0,i):
			s += A[i][j] * x[j]
		x[i] = (b[i] - s) / A[i][i]
	
	return x

def main():
	A = [[1,2,3],
	 	 [0,2,3],
	 	 [0,0,3]]   

	b = [6,6,9]

	A2 = [[1,0,0],
	 	  [1,2,0],
	 	  [1,2,3]]

	print(superior(A,b))
	print(inferior(A2,b))

if __name__ == "__main__":
    main()