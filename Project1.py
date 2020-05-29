# -*- coding: utf-8 -*-
#Nome: Éverton Luís Mendes da Silva
#N°USP: 10728171




import matplotlib.pyplot as plt
import numpy as np
from random import randint


#tipos de automatos que serao usados
a1=[[0.9,0.1],[0.9,0.1]]
a2=[[0.2,0.8],[0.2,0.8]]
a3=[[0.5,0.5],[0.5,0.5]]



#essa é a minha celula, ou seja, o lugar em que um human esta em certo ponto e seu caminho percorrido
class Celula():
	
	def __init__(self,number=0, path=[], matrix=[]):
		
		self.number=number
		self.path=path
		self.matrix=matrix

	#Registra o caminho do automato
	def ChangePath(self, A1):
		
		self.path.append(A1)

	#Muda a posição do automato
	def ChangeNumber(self, A2):
	
		self.number=A2
	
	#Calcula desvio padrão dos caminhos percorridos pelo automato 
	def DesvioP(self):
		
		Xmedia=self.Probability()
		count=0
		for i in self.path:
			count+=(i-Xmedia)**2
		return (count/(len(self.path)-1))**0.5
			
	#calcula a frequencia relativa dos caminhos dos automatos
	def Probability(self):
		
		count=0
		for i in self.path:
			if i==1:
				count+=1
		return count/len(self.path)

	def Run(self):
		
		N1=0.1*(randint(0,10))
		if(self.number==0):
			if (N1<=self.matrix[0][0]):
				self.ChangePath(0)
			else:
				self.ChangeNumber(1)
				self.ChangePath(1)
		
		else:
			if(N1<=self.matrix[1][1]):
				self.ChangePath(1)
			else:
				self.ChangeNumber(0)
				self.ChangePath(0)
		



SaveProbability1=[]
SaveProbability2=[]
SaveProbability3=[]
SaveDesvioP1=[]
SaveDesvioP2=[]
SaveDesvioP3=[]

Mlist=[]
M=500
for i in range(8):
    Mlist.append(M)
    M+=250

'''
human4=Celula(0,[0,1,1,1,0,0,1,0,1,0,1,0,1,1,0,0,0,1,0,1,1,0,1,1,0,0,1,1], a1)
print(human4.DesvioP())
print(human4.Probability())
'''

for i in Mlist:
    
    human1=Celula(0,[0],a1)
    human2=Celula(0,[0],a2)
    human3=Celula(0,[0],a3)
    
    for j in range(i):
    
    	human1.Run()
    	human2.Run()
    	human3.Run()
    
    SaveProbability1.append(human1.Probability())
    SaveDesvioP1.append(human1.DesvioP())
    SaveProbability2.append(human2.Probability())
    SaveDesvioP2.append(human2.DesvioP())
    SaveProbability3.append(human3.Probability())
    SaveDesvioP3.append(human3.DesvioP())
    
#print("Automato 1 ", human1.Probability())	
#print("Automato 2 ", human2.Probability())
#print("Automato 3 ", human3.Probability())





#------------------------------------------------FAZENDO OS GRAFICOS---------------------------------------------



#STEM, SQUARE WAVE, BARPLOT

  
  
  
        #  Plotando grafico do tipo STEM
'''
#Automato1
x=[]
for i in range(len(human1.path)):
	x.append(i)
y=human1.path
plt.xlabel('tempo')
plt.ylabel('Posição')
plt.title('Automato1(STEM)')
plt.stem(x, y, use_line_collection=True)
plt.show()

#Automato2
x=[]
for i in range(len(human2.path)):
	x.append(i)
y=human2.path
plt.xlabel('tempo')
plt.ylabel('Posição')
plt.title('Automato2(STEM)')
plt.stem(x, y, use_line_collection=True)
plt.show()

#Automato3
x=[]
for i in range(len(human3.path)):
	x.append(i)
y=human3.path
plt.xlabel('tempo')
plt.ylabel('Posição')
plt.title('Automato3(STEM)')
plt.stem(x, y, use_line_collection=True)
plt.show()
'''


        #Plotando graficos SQUARE WAVE 
'''    
#modificação da lista original para conseguir plotar certo o grafico SQUAREWAVE 

def squarewave(lista):
    
    x=[]
    y=[]
    for i in range(len(lista)):
        if lista[i]==0:
            y.append(-1)
            ySave=-1
            x.append(i)
        else:
            y.append(1)
            ySave=1
            x.append(i)
            
    
        if i<(len(lista)-1):
            if (lista[i]!=lista[i+1]):
                x.append(i)
                if ySave==1:
                    y.append(-1)
                else:
                    y.append(1)
    
    return x, y
    


#Automato1
x1=[]
y1=[]
x1, y1=squarewave(human1.path)
plt.ylabel('Posição')
plt.title('Automato1(SQUAREWAVE)')
plt.plot(x1, y1, linewidth=1.0)
plt.show()

#Automato2
x1=[]
y1=[]
x1, y1=squarewave(human2.path)
plt.ylabel('Posição')
plt.title('Automato2(SQUAREWAVE)')
plt.plot(x1, y1, linewidth=1.0)
plt.show()

#Automato3
x1=[]
y1=[]
x1, y1=squarewave(human3.path)
plt.ylabel('Posição')
plt.title('Automato3(SQUAREWAVE)')
plt.plot(x1, y1, linewidth=1.0)
plt.show()

'''

        #Plotando graficos BARPLOT
'''
#Automato1
x=[]
y=[]
for i in range(len(human1.path)):
    x.append(i)
y=human1.path
plt.xlabel('TEMPO')
plt.ylabel('POSIÇÃO')
plt.title('Automato1(BARPLOT)')
plt.bar(x, y)
plt.show()

#Automato2
x=[]
y=[]
for i in range(len(human2.path)):
    x.append(i)
y=human2.path
plt.xlabel('TEMPO')
plt.ylabel('POSIÇÃO')
plt.title('Automato2(BARPLOT)')
plt.bar(x, y)
plt.show()


#Automato3
x=[]
y=[]
for i in range(len(human3.path)):
    x.append(i)
y=human3.path
plt.xlabel('TEMPO')
plt.ylabel('POSIÇÃO')
plt.title('Automato3(BARPLOT)')
plt.bar(x, y)
plt.show()
'''

#GRAFICOS DENSIDADE DE PROBABILIDADE

#DensProbability=(1/((SaveDesvioP1[0])*(2*(np.pi))**0.5))*(np.e)**((-0.5)*((x-(SaveProbability1[0]))/(SaveDesvioP1[0])**2))

#gama=(Xi-(SaveProbability1[i]))/(SaveDesvioP1[i])
#DensProbability=(1/((SaveDesvioP1[i])*(2*(np.pi))**0.5))*(np.e)**((-0.5)*gama**2)

for i in range(len(SaveProbability1)):
    
    Xi=np.linspace(0,1,10000)
    gama=((Xi-(SaveProbability1[i]))/(SaveDesvioP1[i]))
    gama1=(1/(SaveDesvioP1[i]))
    gama2=(1/(2*(np.pi)))**0.5
    plt.plot(Xi, gama1*gama2*(np.e)**((-0.5)*gama**2), color='blue')

#plt.title('Automato1(Distribuição Normal)')
#plt.xlabel('Probabilidade')
#plt.ylabel('Distribuição')
#plt.show()

for i in range(len(SaveProbability1)):
    
    Xi=np.linspace(0,1,10000)
    gama=((Xi-(SaveProbability2[i]))/(SaveDesvioP2[i]))
    gama1=(1/(SaveDesvioP2[i]))
    gama2=(1/(2*(np.pi)))**0.5
    plt.plot(Xi, gama1*gama2*(np.e)**((-0.5)*gama**2), color='green')
#plt.title('Automato2(Distribuição Normal)')
#plt.xlabel('Probabilidade')
#plt.ylabel('Distribuição')
#plt.show()
for i in range(len(SaveProbability1)):
    
    Xi=np.linspace(0,1,10000)
    gama=((Xi-(SaveProbability3[i]))/(SaveDesvioP3[i]))
    gama1=(1/(SaveDesvioP3[i]))
    gama2=(1/(2*(np.pi)))**0.5
    plt.plot(Xi, gama1*gama2*(np.e)**((-0.5)*gama**2), color='orange')
#plt.title('Automato3(Distribuição Normal)')
plt.title('Automatos 1, 2, 3')
plt.xlabel('Probabilidade')
plt.ylabel('Distribuição')
plt.show()





  
#fazer para varios padroes(200) com o M fixo
#colocar os dados em um arquivo
#fazer os graficos do meu caderno



#preciso fazer frequencia relativa
#fazer a media 
#fazer desvio padrao
#usar a formula p(x)=(1/(sigma*raizDeDoisPi))*euler**((-0.5)*((x-media)/sigma)**2
#fazer o grafico das probabilidades


