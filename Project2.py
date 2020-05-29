# -*- coding: utf-8 -*-
#Nome: Éverton Luís Mendes da Silva
#N°USP: 10728171

import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
from random import randint




class Automato():


    #definições gerais para qualquer tipo de automato; nós, matriz com as probabilidade, caminho percorrido, posição atual
    def __init__(self, nodes=[], matrix=[], position=0, path=[]):

        self.nodes=nodes
        self.matrix=matrix
        self.position=position
        self.path=path


    '''------------------------'''

                    

    #Faz a escolha do proximo caminho , usando o método de Monte Carlo, através das probabilidades da matriz 'matrix'
    def MonteCarlo(self, j, Rnumber):
        
        #---------Monte-Carlo probabilidade---------
        i=0
        prbs=[]
        prbs.extend(self.matrix[j])
        p=prbs[0]
            
        while (Rnumber>p):
            
            i+=1
            p+=prbs[i]

        return i


        '''--------------------------'''


    #Calculando a media dos valores de uma lista
    def Average(self, lista=[]):

        soma=0
        for i in range(len(lista)):
            soma+=lista[i]

        return (soma/(len(lista)))



        '''--------------------------'''
                


    #Calculando o desvio padrâo dos valores de uma lista
    def StandardDeviation(self, lista=[]):

        soma=0
        for i in range(len(lista)):
            soma+=(lista[i]-(self.Average(lista)))**2

        return ((soma/(len(lista)-1))**0.5)



        '''--------------------------'''

                

    #Fazendo split sginal em todos os nós
    def SplitSignal(self):

        answerMatriz=[]
        for i in self.nodes:

            answerLista=[]
            for j in self.path:
                
                if j==i:
                    answerLista.append(1)
                else:
                    answerLista.append(0)

            answerMatriz.append(answerLista)


        return answerMatriz
    


        '''--------------------------'''



    #Encontrando os Bursts dos valores de uma lista
    def ScanBursts(self, lista):
        
        i = 0
        Ls=[]
        M=len(lista)-1
        while (i <= M):
            
            if (lista[i] == 1):
                
                io = i
                while (lista[i] == 1)and(i < M):
                    i+=1
                if (i == M)and(lista[i] == 1):
                    i=M+1
                bs = i-io
                if (bs > 0):
                    Ls.append(bs)

            i+=1

        return Ls
    


        '''--------------------------'''
                


    #Encontrando as distancias entre simbolos de um conjunto de dados
    def ScanIntersymbols(self, lista):

        i=0
        Ls=[]
        M=len(lista)-1

        while(i<M):

            if(lista[i]==1):

                io=i
                i+=1
                bs=0

                while(lista[i]==0 and i<M):
                    i+=1

                if(i==M and lista[i]==1):
                    bs= M-io

                if(i<M and lista[i]==1):
                    bs= i-io

                if(bs>0):

                    Ls.append(bs)
                    i-=1

            i+=1

        return Ls


        '''--------------------------'''


                    
    #metodo da visibilidade
    def Visibility(self, lista):

        #criando uma matriz MxM de zeros
        matriz=[]
        for i in range(len(lista)):
            linha1=[]
            for  j in range(len(lista)):
                linha1.append(0)
            matriz.append(linha1)

        j=2
        while(j<len(lista)):
            
            i=1
            while(i<(j-1)):

                flag=1
                k=i+1
                while(k<=(j-1) and flag==1):
                    aux=lista[j]+(lista[i]-lista[j])*(j-k)/(j-i)
                    if(lista[k]>=aux):
                        flag=0
                    k+=1
                if(flag==1):
                    matriz[i][j]=1
                    matriz[j][i]=1

                i+=1

            j+=1


        #Plotando a matriz de visibilidade    
        
        for i in range(len(self.path)):
            for j in range(len(self.path)):

                if(matriz[i][j] == 1):

                    plt.plot(len(Automato1.path)-i, j,'s', color='black')     
            
            
        plt.show()
        


        return matriz



        '''--------------------------'''
                


    #função que cria uma lista de integração de um dado sinal colocado
    def Integration(self, lista):

        Integration1=[]
        deltaT=1
        soma=0
        for i in range(len(lista)):

            soma+=lista[i]
            Integration1.append(deltaT*soma)

        return Integration1


    def FastFourier(self, lista):

        fhat= np.fft.fft(lista, len(lista))
        PSD= fhat*np.conj(fhat)

        #Plota o grafico da tranformada de fourier
        
        freq=(1/len(lista))*np.arange(len(lista))
        L=np.arange(1, np.floor(len(lista)/2), dtype='int')
        plt.title('FFT')
        plt.xlabel('Frequency')
        plt.ylabel('Power Espectrum')
        plt.stem(freq[L], PSD[L], use_line_collection=True)
        plt.xlim(freq[L[0]], freq[L[-1]])
        plt.show()
        
        
        return PSD


        '''--------------------------'''


    
    #Função que retorna os graus de cada nó de uma matriz de adjacência
    def Degree(self, matriz):

        matrizB=np.matrix(matriz)
        G=nx.from_numpy_matrix(matrizB)
        listaDegree=[]
        for i in range(len(matriz[0])):
            listaDegree.append(G.degree[i])


        return listaDegree
    


        '''--------------------------'''


    #Função que retorna os coeficientes de aglomeração dos nós dada uma matriz de adjacência
    def ClusteringCoef(self, matriz):

        matrizB=np.matrix(matriz)
        G=nx.from_numpy_matrix(matrizB)
        listaClusteringCoef=[]
        for i in range(len(matriz[0])):
            listaClusteringCoef.append(nx.clustering(G,i))

        return listaClusteringCoef



        '''--------------------------'''


                
    #detrend fluctuation analysis
    def DFA(self, lista):

        Xa=[]
        W=0
        for i in range(len(lista)):
           W+=lista[i]-self.Average(lista)
           Xa.append(W)

        m=10
        Fm=[]
        while(m<len(Xa)):

            Z=[]
            for k in range(int(len(lista)/m)):
                x=[]
                y=[]
                for i in range(m):

                    x.append(i+k*m)
                    y.append(Xa[i+k*m])


                #aproximção poligonal
                
                P=self.MeanSquare(x, y)
                c=float(P[0])
                a=float(P[1])
                for i in range(m):
                    
                    Z.append(c+(i+k*m)*a)

            
            #fazendo a conta da função Fm
            soma1=0
            for i in range(len(Z)):
                soma1+=(Xa[i]-Z[i])**2
            conta=(1/len(Z))*(soma1)
            Fm.append(conta**0.5)

            m+=10

            
            
            #fazendo o grafico da integral de sinal
            if(m==20):

                x=[]
                for i in range(len(Xa)):
                    x.append(i)
                plt.title('m=20')
                plt.xlabel('Time')
                plt.ylabel('Integrated Signal')
                plt.plot(x, Xa, LineWidth=1.1, color='black')

                x=[]
                for i in range(len(Z)):
                    x.append(i)
                plt.plot(x, Z, LineWidth=1.5, color='yellow')
                plt.show()

            if(m==40):

                x=[]
                for i in range(len(Xa)):
                    x.append(i)
                plt.title('m=40')
                plt.xlabel('Time')
                plt.ylabel('Integrated Signal')
                plt.plot(x, Xa, LineWidth=1.1, color='black')

                x=[]
                for i in range(len(Z)):
                    x.append(i)
                plt.plot(x, Z, LineWidth=1.5, color='yellow')
                plt.show()


            if(m==80):

                x=[]
                for i in range(len(Xa)):
                    x.append(i)
                plt.title('m=80')
                plt.xlabel('Time')
                plt.ylabel('Integrated Signal')
                plt.plot(x, Xa, LineWidth=1.1, color='black')

                x=[]
                for i in range(len(Z)):
                    x.append(i)
                plt.plot(x, Z, LineWidth=1.5, color='yellow')
                plt.show()
                    
            
        
        xp=[]
        t=0
        for i in range(len(Fm)):
            xp.append(10+t)
            t+=10
            
        for i in range(len(Fm)):
            Fm[i]=np.log10(Fm[i])
            xp[i]=np.log10(xp[i])

        P=self.MeanSquare(xp, Fm)
        b=float(P[0])
        d=float(P[1])
        alpha=d
        
        
        
        
        #fazendo o grafico do DFA
        plt.title('DFA')
        plt.xlabel('log(m)')
        plt.ylabel('log(F(m))')
        plt.plot(xp, Fm, LineWidth=1.5, color='orange')
        u=np.linspace(xp[0], xp[len(Fm)-1], 200)
        plt.plot(u, b+u*d, LineWidth=2, color='green')
        plt.show()
        
        

        
        return alpha



        '''--------------------------'''


                    

    #Calculando a entropia de Shannon a partir de uma lista com probabilidades
    def Entropy(self, lista):

        soma=0
        for i in lista:
            soma+=i*(np.log2(i))

        return -soma
    


        '''--------------------------'''
                
                

    #Calculando a entropia de evenness
    def Evenness(self, lista):

        e=self.Entropy(lista)
        n=2**e

        return n



        '''--------------------------'''

        
      

    #Função que faz Minimos Quadrados e retorna dois valores que sao c(coflin) e m(cofang)            
    def MeanSquare(self, x=[], y=[]):

        p=[]
        A=[]
        Y1=[]
        for i in range(len(x)):
            A.append([1,x[i]])
            Y1.append([y[i]])
            

        A=np.matrix(A)
        Y1=np.matrix(Y1)
        P=np.matrix(p)
        S=np.matmul((A.transpose()), A)
        P=np.matmul((np.matmul(np.linalg.inv(S), A.transpose())), Y1)
        
        return P
        

        '''--------------------------'''


                     
    #Faz a passagem para a proxima posição e registra o caminho realizado
    def Run(self):

        R= 0.0001*(randint(0,10000))
        
        Nnext= self.MonteCarlo(self.position, R)
        self.path.append(self.nodes[Nnext])
        self.position=Nnext









#---------------------- RODANDO O PROGRAMA ------------------------------

#matriz1=[[0.9,0.1],[0.9,0.1]]
#node1=[0,1]
#Automato1=Automato(node1, matriz1, 0, [0])


#matriz1=[[0.2, 0.8],[0.2,0.8]]
#node1=[0,1]
#Automato1=Automato(node1, matriz1, 0, [0])


#matriz1=[[0.5, 0.5],[0.5, 0.5]]
#node1=[0, 1]
#Automato1=Automato(node1, matriz1, 0, [0])


#matriz1=[[0.9,0.1,0,0,0,0],[0.882,0.098,0.02,0,0,0],[0,0,0.2,0.8,0,0],[0,0,0.194,0.776,0.03,0],[0,0,0,0,0.5,0.5],[0.01,0,0,0,0.495,0.495]]
#node1=[0,1,2,3,4,5]
#Automato1=Automato(node1, matriz1, 0, [0])


#matriz1=[[0.9,0.1,0,0,0,0],[0.882,0.098,0.02,0,0,0],[0,0,0.2,0.8,0,0],[0,0,0.194,0.776,0.03,0],[0,0,0,0,0.5,0.5],[0.01,0,0,0,0.495,0.495]]
#node1=[0,1,0,1,0,1]
#Automato1=Automato(node1, matriz1, 0, [0])


matriz1=[[0.5, 0.5, 0, 0],[0, 0.1, 0.9, 0],[0, 0, 0.6, 0.4],[0.7, 0, 0, 0.3]]
node1=[0, 1, 2, 3]
Automato1=Automato(node1, matriz1, 0, [0])

time=1000
for i in range(time):
    Automato1.Run()














#print(Automato1.path)
#print(Automato1.Average(Automato1.path))
#print(Automato1.StandardDeviation(Automato1.path))
#print(Automato1.SplitSignal())
#print(Automato1.ScanBursts(Automato1.path))
#print(Automato1.ScanIntersymbols(Automato1.path))

'''
Split=Automato2.SplitSignal()
Automato2.FastFourier(Split[1])
'''    
#Automato2.DFA(Automato2.path)












#---------------------- FAZENDO OS GRAFICOS ------------------


def Dist(lista):

    resp=[]
    resp2=[]
    for i in lista:
        if i not in resp:
            resp.append(i)

    for j in resp:

        conta=lista.count(j)
        resp2.append(conta/(len(lista)))


    return resp2
        
        
        
        
            

        






#Primeiro conjunto de medidas

x=[]
for i in range(len(Automato1.path)):
    x.append(i)

plt.title("Autômato E(1000)")
plt.xlabel('Time')
plt.ylabel('Position')
plt.bar(x, Automato1.path)
plt.show()


y1=[]
y2=[]
y1=Automato1.SplitSignal()
for i in range(len(Automato1.nodes)):
    
    plt.title('Split Signal')
    plt.xlabel('Time')
    plt.ylabel('Position')
    plt.bar(x,y1[i])
    plt.show()



    
    y2=Automato1.ScanBursts(y1[i])
    media=Automato1.Average(y2)
    Standard=Automato1.StandardDeviation(y2)
    Entropia=Automato1.Entropy(Dist(y2))
    Evenn=Automato1.Evenness(Dist(y2))

    print('numero de bursts: ',len(y2))
    print('media: ', media)
    print('desvio padrao: ', Standard)
    print('entropia: ', Entropia)
    print('eveness: ', Evenn)



#segundo conjuntos de medidaa


for i in range(len(Automato1.nodes)):

    y3=Automato1.ScanIntersymbols(y1[i])
    media=Automato1.Average(y3)
    Standard=Automato1.StandardDeviation(y3)
    Entropia=Automato1.Entropy(Dist(y3))
    Evenn=Automato1.Evenness(Dist(y3))

    print('numero de Distancias: ',len(y2))
    print('media: ', media)
    print('desvio padrao: ', Standard)
    print('entropia: ', Entropia)
    print('eveness: ', Evenn)        



#terceiro conjunto de medidas

for i in range(len(Automato1.nodes)):

    y4=Automato1.FastFourier(y1[i])
    media=Automato1.Average(y4)
    Standard=Automato1.StandardDeviation(y4)

    print("media: ",media)
    print("Standard: ", Standard)


#Automato1.FastFourier(y1[0])
#Automato1.FastFourier(y1[1])


#quarto conjunto de medidas


matriz=Automato1.Visibility(Automato1.path)
Degre=Automato1.Degree(matriz)
Coef=Automato1.ClusteringCoef(matriz)
media1=Automato1.Average(Degre)
media2=Automato1.Average(Coef)
Stand1=Automato1.StandardDeviation(Degre)
Stand2=Automato1.StandardDeviation(Coef)

print('MediaDegre: ', media1)
print('Standard : ', Stand1)
print('MediaCoef: ', media2)
print('Standard : ', Stand2)


#quinto conjunto de medidas

alpha1=Automato1.DFA(Automato1.path)
print('Alpha: ', alpha1)



  
    



    
        

















             

















                
