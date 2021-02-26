#!/usr/bin/env python3
columns = int(input("Digite a quantidade de colunas da tabela: "))
rows = int(input("Digite a quantidade de linhas da tabela: "))


matrix = []
for i in range(rows):
    matrix.append([0]*columns)

for i in range(rows):
    for j in range(columns):
        matrix[i][j] = input()

print(matrix)

new_file = open('new_file2.txt','w')
for rows in matrix:
    for i in rows:
        new_file.write(i +" ")
    new_file.write("\n")



