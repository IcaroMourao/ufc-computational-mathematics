
def f(x):
	return 1/x

def lagrange(x,y,p):
	n = len(x)
	s = 0
	for i in range(0,n):
		l = 1
		for j in range(0,n):
			if j != i:
				l *= (p-x[j])/(x[i]-x[j])
		s += y[i] * l
	return s

def main():
	pontos = []
	y_dos_pontos = []

	while True:
		ponto = input('Digite os pontos [Para parar digite x]\n')
		if ponto == 'x':
			break

		ponto = float(ponto)

		pontos.append(ponto)
		y_dos_pontos.append(f(ponto))

	p = 1.5
	print('f({}) = {}'.format(p, f(p)))
	print('pl({}) = {}'.format(p, lagrange(pontos, y_dos_pontos, p)))

if __name__ == "__main__":
    main()