
n = 5 
m = 3
folgas = 2

def printTable(tabela):
    for i in range(0,m):
        for j in range(0,n):
            print("{}\t".format(round(tabela[i][j]), 2), end="")
        print()
    print()


def minColum(tabela):
    minimo = 10000000
    c = -1

    for i in range(0,n-folgas-1):
        if tabela[0][i] < minimo and tabela[0][i]>0:
            minimo = tabela[0][i]
            c = i
    return c


def findLines(c, tabela):
    minimo = tabela[1][n - 1] / tabela[1][c]
    l = 1

    for j in range(2,m):
        if tabela[j][c] > 0:
            if ((tabela[j][n - 1] / tabela[j][c]) < minimo and (tabela[j][n - 1] / tabela[j][c]) > 0):
                minimo = tabela[j][n - 1] / tabela[j][c]
                l = j
    return l

def line_calc(linha, colunaPiv, tabela):
    if (tabela[linha][colunaPiv] != 0):
        piv = tabela[linha][colunaPiv]
        for i in range(0,n):
            tabela[linha][i] /= piv

def buildTable(linha, colunaPiv, tabela):

    p2 = tabela[linha][colunaPiv]

    for l in range(0,m):
        p1 = tabela[l][colunaPiv]
        p3 = abs(p1)

        if l != linha:
            for c in range(0,n):
                if (p1 > 0 and p2 > 0):
                    tabela[l][c] = (tabela[l][c] * p2) - (tabela[linha][c] * p3)
                elif (p1 > 0 and p2 < 0):
                    tabela[l][c] = (tabela[l][c] * p2) + (tabela[linha][c] * p3)
                elif (p1 < 0 and p2 > 0):
                    tabela[l][c] = (tabela[l][c] * p2) + (tabela[linha][c] * p3)
                else:
                    tabela[l][c] = (tabela[l][c] * p2) - (tabela[linha][c] * p3)

def Simplex(tabela):
    while(minColum(tabela)!=-1):
        coluna_piv = minColum(tabela)
        linha = findLines(coluna_piv,tabela)
        line_calc(linha,coluna_piv,tabela)
        buildTable(linha,coluna_piv,tabela)
    
    print()
    printTable(tabela)

def main():
    tabela = [[2, 4, 0, 0, 0],
              [1, 1, 1, 0, 5],
              [0, 1, 0, 1, 4]]

    print("\tModelo Simplex\n")
    Simplex(tabela);

if __name__ == "__main__":
		main()