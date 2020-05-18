# -*- coding: utf-8 -*-
#Nome: Éverton Luís Mendes da Silva
#N°USP: 10728171


import matplotlib.pyplot as plt
import numpy as np
from random import randint




#cria um conjunto de n pontos aleatórios dentro de um circulo de raio dado
def Points(n, radius):

    pontos=[]
    while (len(pontos)<n):

        x=0.00001*randint((-1)*radius*100000,radius*100000)
        y=0.00001*randint((-1)*radius*100000,radius*100000)
        
        dist=((x**2)+(y**2))**0.5
        if dist<radius:

            pontos.append([x, y])



    return pontos


#Plota os pontos 
def Grafics(lista):


    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('pontos')
    plt.axis([-1.1,1.1,-1.1,1.1])

        
    x=[]
    y=[]
    for i in range(len(lista)):
        x.append(lista[i][0])
        y.append(lista[i][1])
    
    
    
    for i in range(len(lista)):
        plt.plot(x, y,'.',  color='black')

    plt.show()


def Transform1(lista, transform=[]):

    
    change=[]
    for i in range(len(lista)):
        change.append([(lista[i][0])*(transform[0]),(lista[i][1])*(transform[1])])

    return change

def Transform2(lista, T=[]):

    T=np.matrix(T)
    change=[]
    for i in range(len(lista)):
        xy=np.matrix(lista[i])

        
        xylinha=np.matmul(T, xy.transpose())
        bota=xylinha.getA1()
        x=bota[0]
        y=bota[1]
        change.append([x,y])
        

    return change


#obtendo matriz de covariancia
def Covariance(lista):

    k=[]
    for i in range(len(lista)):
        zero=[]
        for j in range(len(lista)):
            zero.append(0)

        k.append(zero)

    
    
    for i in range(len(lista)):
        for j in range(len(lista)):

            mediafi=(sum(lista[i]))/(len(lista[0]))
            mediafj=(sum(lista[j]))/(len(lista[0]))

            soma=0
            for g in range(len(lista[0])):

                soma+=(lista[i][g]-mediafi)*(lista[j][g]-mediafj)

            k[i][j]=(soma)/(len(lista[0])-1)



    return k
        

#ordenando os autovalores da matriz de covariancia para o PCA
def Ordenando(matriz=[]):

    
    ordenadoValor=[]
    ordenadoVector=[]
    eigenvalues, eigenvector=np.linalg.eigh(matriz)

    
    eigenvalues1=[]
    for i in range(len(eigenvalues)):
        eigenvalues1.append(eigenvalues[i])
    
  
    
    for i in range(len(eigenvalues)):
        maior=eigenvalues1.index(max(eigenvalues1))
        ordenadoValor.append(eigenvalues1[maior])
        ordenadoVector.append(eigenvector[maior])
        eigenvalues1.pop(maior)



    return ordenadoValor, ordenadoVector
                


#verifica se a matriz colocada é simetrica
def check_symmetric(matrix):
    
    symmetric = True

    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if matrix[x][y] != matrix[y][x]:
                symmetric = False
                break # inner for
        if not symmetric:
            break # outer for

    print(f"Matrix is symmetric? {symmetric}")


#Principal component analysis          
def PCA(lista, rendimento):

    #covariancia=np.cov(lista)
    covariancia1=Covariance(lista)
    #print(covariancia==covariancia1)
    #covariancia1=np.matrix(covariancia1)
    
 
    Valor, Vector=Ordenando(covariancia1)

    Q=[]
    for i in Vector:
        Q.append(i)


    
    Q1=np.matrix(Q)
  
    lista1=np.matrix(lista)

    newFeature=np.matmul(Q1,lista1)
    newFeature=newFeature.getA()

    #analisando o rendimento dado e fornecendo um novo conjunto de dados

    '''
    somaValor=sum(Valor)

    
    divisao=0
    m=0
    soma=0
    while divisao<rendimento:

        soma+=Valor[m]
        #print(Valor[m])
        
        divisao=soma/somaValor
        #print(divisao)
        m+=1

    newFeature1=[]
    for i in range(m):
        newFeature1.append(newFeature[i])
    '''

    return newFeature





n1=Points(1000, 1)
Grafics(n1)
n2=Transform1(n1, [1,0.2])
Grafics(n2)


s=np.sin(np.pi/6)
c=np.cos(np.pi/6)

n3=Transform2(n2, [[c, s],[s, c]])
Grafics(n3)

'''
matrix=[[1,2,3],
        [2,1,4],
        [3,4,1]]
check_symmetric(matrix)

matrix=np.matrix(matrix)
print((np.linalg.eigh(matrix)))
'''
Grafics(PCA(n3, 1))
















