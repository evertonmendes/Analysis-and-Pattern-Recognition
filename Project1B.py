# -*- coding: utf-8 -*-
#Nome: Éverton Luís Mendes da Silva
#N°USP: 10728171

import matplotlib.pyplot as plt
import numpy as np
from random import randint





matriz1=[[0.9,0.1], [0.882, 0.098]]
#0.02
matriz2=[[0.2,0.8], [0.194, 0.776]]
#0.03
matriz3=[[0.5,0.5], [0.495, 0.495]]
#0.01




#definindo celulas pequenas de dois lugares
class Celula():
    
    
    def __init__(self, a=0, b=0, matriz=[], pulo=0):
        
        self.a=a
        self.b=b
        self.matriz=matriz
        self.pulo=pulo   #probabilidade da transição de celula
        
        



#definindo o Automato, possui tres celulas nele
class Automato():
    
    
    def __init__(self, posicao=0, posicaoCel=Celula(), n1=Celula(), n2=Celula(), n3=Celula(), path=[]):
        
        self.posicao=posicao
        self.posicaoCel=posicaoCel
        self.path=path
        self.n1=n1
        self.n2=n2
        self.n3=n3
        
        
    #funçao para mudar de celula   
    def ChangeCel(self, Cel1):
        
        self.posicaoCel=Cel1
        
        
    
    
    def Run(self):
        
        Rnumber=0.0001*(randint(0,10000))
        
        
        
        #se ele estiver em 'a' ele nao ira mudar de celula e possui uma açao simples de movimentação na mesma celula
        if (self.posicaoCel.a==self.posicao):
            
            if (Rnumber<=self.posicaoCel.matriz[0][0]):
                
                self.path.append(self.posicao)
                
            else:
                
                self.posicao=self.posicaoCel.b
                self.path.append(self.posicao)
        
        
        #estando em 'b' ele podera ter movimentos complicados de troca de celula
        else:
            
            #---------Monte-Carlo probabilidade---------
            i=0
            prbs=[]
            prbs.append(self.posicaoCel.pulo)
            prbs.extend(self.posicaoCel.matriz[1])
            p=prbs[0]
            
            while (Rnumber>p):
                
                i+=1
                p+=prbs[i]
                
            #--------------------------------------------
                
            if(i==1):
                
                self.posicao=self.posicaoCel.a
                self.path.append(self.posicao)
            
            elif(i==2):
                
                self.path.append(self.posicao)
                
            else:
                
                if(self.posicaoCel==self.n1):
                    
                    self.ChangeCel(self.n2)
                    self.posicao=self.posicaoCel.a
                    self.path.append(self.posicao)
                    
                elif(self.posicaoCel==self.n2):
                    
                    self.ChangeCel(self.n3)
                    self.posicao=self.posicaoCel.a
                    self.path.append(self.posicao)
                    
                else:
                    
                    self.ChangeCel(self.n1)
                    self.posicao=self.posicaoCel.a
                    self.path.append(self.posicao)
                    
                
                
            
                
                
                
            
            
        
        
        
#-------------------RODANDO O PROGRAMA--------------------------------


#definindo as celulas
leg1=Celula(0, 1, matriz1, 0.02)
leg2=Celula(2, 3, matriz2, 0.03)
leg3=Celula(4, 5, matriz3, 0.01)
leg4=Celula(0, 1, matriz1, 0.02)
leg5=Celula(0, 1, matriz2, 0.03)
leg6=Celula(0, 1, matriz3, 0.01)

        
        
#definindo os automatos
body1=Automato(0, leg1, leg1, leg2, leg3, [0])
body2=Automato(0, leg4, leg4, leg5, leg6, [0])
    
        



tempo=1500
for j in range(tempo):
    
    body1.Run()
    body2.Run()
    
    
print(body1.path)
print(body2.path)







#--------------------------- FAZENDO OS GRAFICOS -------------------------------------------


#STEM, BARPLOT


        #Plotando graficos do tipo STEM
        

#body1     
x=[]
for i in range(len(body1.path)):
    x.append(i)
y=body1.path
plt.xlabel('Tempo')
plt.ylabel('Posição')
plt.title('Body1(STEM)')
plt.stem(x, y, use_line_collection=True)
plt.show()


#body2
x=[]
for i in range(len(body2.path)):
    x.append(i)
y=body2.path
plt.xlabel('Tempo')
plt.ylabel('Posição')
plt.title('Body2(STEM)')
plt.stem(x, y, use_line_collection=True)
plt.show()



    
        #Plotando graficos do tipo BARPLOT
        
#Body1
x=[]
y=[]
for i in range(len(body1.path)):
    x.append(i)
y=body1.path
plt.xlabel('TEMPO')
plt.ylabel('POSIÇÃO')
plt.title('Body1(BARPLOT)')
plt.bar(x, y)
plt.show()
        
        
#Body2
x=[]
y=[]
for i in range(len(body2.path)):
    x.append(i)
y=body2.path
plt.xlabel('TEMPO')
plt.ylabel('POSIÇÃO')
plt.title('Body2(BARPLOT)')
plt.bar(x, y)
plt.show()

    
    
    
    
    
    
    
    
    
    


