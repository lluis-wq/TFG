import sympy as sp

paps = sp.Symbol('paps')
pbps = sp.Symbol('pbps')
papr = 1 - pbps
pbpr = 1 - paps

pajs = sp.Symbol('pajs')
pajr = sp.Symbol('pajr')
pbjs = 1 - pajr
pbjr = 1 - pajs

def pS(i,j):
    if i == 0 and j == 0:
        return 1

    if (i + j) % 2 == 1:
        if j==0 and 1 <= i <= 6:
            return pajs * pS(i-1,j)
        if i==0 and 1 <= j <= 6:
            return pbjr * pS(i,j-1)
        if 1 <= i <= 5 and 1 <= j <= 5:
            return pajs * pS(i-1,j) + pbjr * pS(i,j-1)
        if i == 6 and 1 <= j <= 4:
            return pajs * pS(i-1,j)
        if j == 6 and 1 <= i <= 4:
            return pbjr * pS(i,j-1)

    if (i + j) % 2 == 0:
        if j==0 and 1 <= i <= 6:
            return pajr * pS(i-1,j)
        if i==0 and 1 <= j <= 6:
            return pbjs * pS(i,j-1)
        if 1 <= i <= 5 and 1 <= j <= 5:
            return pajr * pS(i-1,j) + pbjs * pS(i,j-1)
        if i == 6 and 1 <= j <= 4:
            return pajr * pS(i-1,j)
        if j == 6 and 1 <= i <= 4:
            return pbjs * pS(i,j-1)
    
    return 0


def pS_resta(i,j):
    if i == 0 and j == 0:
        return 1

    if (i + j) % 2 == 1: 
        if j==0 and 1 <= i <= 6:
            return pajr * pS_resta(i-1,j)
        if i==0 and 1 <= j <= 6:
            return pbjs * pS_resta(i,j-1)
        if 1 <= i <= 5 and 1 <= j <= 5:
            return pajr * pS_resta(i-1,j) + pbjs * pS_resta(i,j-1)
        if i == 6 and 1 <= j <= 4:
            return pajr * pS_resta(i-1,j)
        if j == 6 and 1 <= i <= 4:
            return pbjs * pS_resta(i,j-1)

    if (i + j) % 2 == 0: 
        if j==0 and 1 <= i <= 6:
            return pajs * pS_resta(i-1,j)
        if i==0 and 1 <= j <= 6:
            return pbjr * pS_resta(i,j-1)
        if 1 <= i <= 5 and 1 <= j <= 5:
            return pajs * pS_resta(i-1,j) + pbjr * pS_resta(i,j-1)
        if i == 6 and 1 <= j <= 4:
            return pajs * pS_resta(i-1,j)
        if j == 6 and 1 <= i <= 4:
            return pbjr * pS_resta(i,j-1)
    
    return 0


def pTB(i,j):
    if i == 0 and j == 0:
        return 1
    
    if (i + j + 4) % 4 == 0 or (i + j + 4) % 4 == 1:
        if j==0 and 1 <= i <= 7:
            return paps * pTB(i-1,j)
        if i==0 and 1 <= j <= 7:
            return pbpr * pTB(i,j-1)
        if 1 <= i <= 6 and 1 <= j <= 6:
            return paps * pTB(i-1,j) + pbpr * pTB(i,j-1)
        if i == 7 and 1 <= j <= 5:
            return paps * pTB(i-1,j)
        if j == 7 and 1 <= i <= 5:
            return pbpr * pTB(i,j-1)
    
    if (i + j + 4) % 4 == 2 or (i + j + 4) % 4 == 3:
        if j==0 and 1 <= i <= 7:
            return papr * pTB(i-1,j)
        if i==0 and 1 <= j <= 7:
            return pbps * pTB(i,j-1)
        if 1 <= i <= 6 and 1 <= j <= 6:
            return papr * pTB(i-1,j) + pbps * pTB(i,j-1)
        if i == 7 and 1 <= j <= 5:
            return papr * pTB(i-1,j)
        if j == 7 and 1 <= i <= 5:
            return pbps * pTB(i,j-1)

    return 0

def pTB_resta(i,j):
    if i == 0 and j == 0:
        return 1
    
    if (i + j + 4) % 4 == 0 or (i + j + 4) % 4 == 1:
        if j==0 and 1 <= i <= 7:
            return papr * pTB_resta(i-1,j)
        if i==0 and 1 <= j <= 7:
            return pbps * pTB_resta(i,j-1)
        if 1 <= i <= 6 and 1 <= j <= 6:
            return papr * pTB_resta(i-1,j) + pbps * pTB_resta(i,j-1)
        if i == 7 and 1 <= j <= 5:
            return papr * pTB_resta(i-1,j)
        if j == 7 and 1 <= i <= 5:
            return pbps * pTB_resta(i,j-1)
    
    if (i + j + 4) % 4 == 2 or (i + j + 4) % 4 == 3:
        if j==0 and 1 <= i <= 7:
            return paps * pTB_resta(i-1,j)
        if i==0 and 1 <= j <= 7:
            return pbpr * pTB_resta(i,j-1)
        if 1 <= i <= 6 and 1 <= j <= 6:
            return paps * pTB_resta(i-1,j) + pbpr * pTB_resta(i,j-1)
        if i == 7 and 1 <= j <= 5:
            return paps * pTB_resta(i-1,j)
        if j == 7 and 1 <= i <= 5:
            return pbpr * pTB_resta(i,j-1)

    return 0

h3 = (paps * papr) / (1 - (paps * pbps + papr * pbpr)) # = h3'
paTBS = sum(pTB(7,j) for j in range(6)) + pTB(6,6) * h3
paTBR = sum(pTB_resta(7,j) for j in range(6)) + pTB_resta(6,6) * h3

diferencia_tbs = paTBS - paTBR
print("Diferencia entre paTBS y paTBR (debería ser 0):")
print(diferencia_tbs.simplify())



paSSDirecto = sum(pS(6,j) for j in range(5)) + pS(5,5)
paSRDirecto = sum(pS_resta(6,j) for j in range(5)) + pS_resta(5,5)

diferencia_directa = paSSDirecto - paSRDirecto
print("Diferencia directa entre paSSDirecto y paSRDirecto (debería ser 0):")
print(diferencia_directa.simplify())

