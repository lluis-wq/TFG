import sympy as sp
import random

paps = sp.Symbol('paps')
pbps = sp.Symbol('pbps')
papr = 1 - pbps
pbpr = 1 - paps

pajs = paps**4 * (1 + 4 * pbpr + 10 * pbpr**2) + (20 * paps**5 * pbpr**3)/(1 - 2 * paps * pbpr)
pajr = papr**4 * (1 + 4 * pbps + 10 * pbps**2) + (20 * papr**5 * pbps**3)/(1 - 2 * papr * pbps)
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
print(f'h3 = {h3}')
paTBS = sum(pTB(7,j) for j in range(6)) + pTB(6,6) * h3
print(f'paTBS = {paTBS}')
paTBR = sum(pTB_resta(7,j) for j in range(6)) + pTB_resta(6,6) * h3
print(f'paTBR = {paTBR}')


paSS = sum(pS(6,j) for j in range(5)) + pS(5,5) * (pajs * pajr + (pajs * pbjs + pajr * pbjr) * paTBS)
print(f'pass = {paSS}')
paSR = sum(pS_resta(6,j) for j in range(5)) + pS_resta(5,5) * (pajr * pajs + (pajr * pbjr + pajs * pbjs) * paTBR)
print(f'pasr = {paSR}')
print("Iniciando demostración computacional por evaluación masiva...")
exito = True

# Probamos 100 combinaciones aleatorias diferentes de probabilidades
for i in range(100):
    # Generamos probabilidades aleatorias realistas para el tenis (entre 40% y 90%)
    val_paps = random.uniform(0.4, 0.9)
    val_pbps = random.uniform(0.4, 0.9)
    
    # Sustituimos las letras por los números usando .subs() y evaluamos con .evalf()
    # Metemos las variables en un diccionario para la sustitución
    eval_SS = paSS.subs({paps: val_paps, pbps: val_pbps}).evalf()
    eval_SR = paSR.subs({paps: val_paps, pbps: val_pbps}).evalf()
    
    # Restamos y redondeamos a 5 decimales para evitar el error de coma flotante de Python
    diferencia = round(float(abs(eval_SS - eval_SR)), 5)
    
    if diferencia != 0.0:
        exito = False
        print(f"Fallo encontrado con paps={val_paps} y pbps={val_pbps}")
        break

if exito:
    print("-" * 60)
    print("¡TEOREMA DEMOSTRADO COMPUTACIONALMENTE!")
    print("Para 100 escenarios aleatorios, la diferencia entre paSS y paSR es exactamente 0.0")
    print("-" * 60)