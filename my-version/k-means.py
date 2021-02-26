#!/usr/bin/env python3
import math
from random import randint
def line_count():
    return sum(1 for line in  open("new_file.txt",'r'))

"""
    Abrindo o arquivo de texto
"""
file =  open("new_file.txt",'r')

"""
    Vetor que irá armazenar todos os valores do arquivo txt
"""
vetor = []

nLinhas = line_count()

colunas = 0
linhas = 0

"""
    For que armazena os valores do arquivo no vetor e calcula a quantidade de colunas presentes nas tabelas
"""
for line in file:
       linhas += 1
       for n in line.split(' '):
           if n != '\n' and n != 'setosa' and n!= 'virginica' and n !='versicolor' and n !='':
                colunas += 1
                vetor.append(float(n))

           if linhas != nLinhas :
                colunas= 0

"""
    Criação e preenchimento de uma matriz com os dados do arquivo txt
"""               
matrix = []
for i in range(linhas):
    matrix.append([0]*colunas)

cont = 0
for i in range(linhas):
    for j in range(colunas):
        matrix[i][j] = vetor[cont]
        cont+=1

k = int(input("Digite a quantidade de grupos que deseja formar "))
pontos_iniciais = []
for i in range(k):
    matrix.append([0]*colunas)
for i in range(k):
    r = randint(0,linhas)
    pontos_iniciais.append( matrix[r])

print(pontos_iniciais)


"""
    Calculo da distancia euclidiana
"""
E = []
comp = []
x = 0

for l in range(k):
    for i in range(linhas):
        for j in range(colunas):
            valor = pow(pontos_iniciais[l][j] - matrix[i][j], 2)
            x += valor
            if(j == (colunas-1)):
                E.append(math.sqrt(x))
        x=0
    comp.append(E)
    E = []


indices = []
for i in range(linhas):
    indices.append(-1)

for i in range(linhas):
    x = -1
    for j in range(k):
        if(comp[j][i] > x ):
            print(j)
            print(comp[j][i])
            x = comp[j][i]
            indices[i] = j

print(indices)

ids = []

ponto_medio = []
for p in range(k):
    ponto_medio.append([0]*colunas)

for p in range(k):
    for d in range(colunas):
        ponto_medio[p][d] = 0
        

for n in range(k):
    for t in range(linhas):
        if( n == indices[k]):
            ids[n].append(k)
    
    for f in range(len(ids)):
        for d in range(colunas):
            ponto_medio[n][d] += matrix[f][d]

print( ponto_medio)
        




       
        


    
        
"""
N = sorted(E)


ids = []
for i in range(k):
    for j in range(linhas):
        if( N[i] == E[j]):
            ids.append(j)


    for i in range(k):
    print(matrix[ids[i]][colunas-1])

"""







 





