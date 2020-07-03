# -*- coding: utf-8 -*-
#Nome: Éverton Luís Mendes da Silva
#N°USP: 10728171


import matplotlib.pyplot as plt
import numpy as np
from random import randint
from PIL import Image
import cv2
import matplotlib.image as mpimg








'''
retina=[[0,0,1,0,0,0,0,0],
        [0,0,1,0,0,0,0,0],
        [0,0,1,0,0,0,0,0],
        [0,0,1,0,0,0,0,0],
        [0,0,1,0,0,0,0,0],
        [0,0,1,0,0,0,0,0],
        [0,0,1,0,0,0,0,0],
        [0,0,1,0,0,0,0,0]]

'''
#cortex=[]
#peso=[]




def CriaMatriz(n, m):

    matriz=[]
    for i in range(n):
        
        linha=[]
        for j in range(m):

            linha.append(0)

        matriz.append(linha)
        

    return(matriz)

def Randomnumber(lista=[]):

    for i in range(len(lista)):
        for j in range(len(lista[0])):

            lista[i][j]= 0.0001*(randint(0,10000))

    return lista







class cortex():


    def __init__(self, espaço=[], step=1):

        self.espaço=espaço
        self.step=step


    def InnerProduct(self, lista):

        
        importante=[]
        posição=[]
        
        for i in range(len(self.espaço)):
            for j in range(len(self.espaço[0])):


                lista1=lista
                lista1=np.matrix(lista1)

                espaço1=self.espaço[i][j]
                espaço1=np.matrix(espaço1)

                lista1=lista1.getA1()
                espaço1=espaço1.getA1()
                
                conta=0
                conta=np.inner(lista1,espaço1)


                importante.append(conta)
                posição.append([i,j])

        
        k=importante.index(max(importante))
                
                
                


        
        return  posição[k]        

                        


    def LearnR(self, gamma=0.2, retina=[], Nt=20):

        porra=self.InnerProduct(retina)
        n=int(porra[0])
        m=int(porra[1])
        
        for x in range(Nt):
            for i in range(len(self.espaço)):
                for j in range(len(self.espaço)):

                    r=((n-i)**2 + (m-j)**2)**0.5

                    alpha=gamma*((np.e)**((-1)*0.5*r*(self.step)/Nt))
                    
                    retina1=retina
                    retina1=np.matrix(retina1)
                    espaço1=self.espaço[i][j]
                    espaço1=np.matrix(espaço1)

                    espaço1=espaço1+alpha*(retina1-espaço1)

                    espaço1=espaço1.getA()
                    self.espaço[i][j]=espaço1


            self.step=self.step+1


    def StartSpace(self):


        for i in range(8):
            for j in range(8):
                
                matrizA=CriaMatriz(20, 20)
                matrizA=Randomnumber(matrizA)
                self.espaço[i][j]=matrizA


    def ShowNeuron(self, n, m):


        espaço1=self.espaço[n][m]
        
        #print(espaço1)
        espaço1=np.matrix(espaço1)
        espaço1=espaço1.getA()
        #print(espaço1)
        #imga = Image.fromarray(espaço1)
        plt.imshow(espaço1)
        plt.show()
        
        
        #imgplot.save('testN.png')
        #im = Image.open('testN.png')  
        #im.show() 





#recebeu o arquivo fez as mudanças e transformou em array
foto1=Image.open('E.png')
foto2=foto1.resize((20,20))
foto2.save('E1.png')

image = cv2.imread('E1.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#cv2.imshow('Original image',image)
#cv2.imshow('Gray image', gray)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


cv2.imwrite('GrayE.png', gray)

imgE = mpimg.imread('GrayE.png')


#recebeu o arquivo fez as mudanças e transformou em array
foto3=Image.open('F.png')
foto4=foto3.resize((20,20))
foto4.save('F1.png')

image1 = cv2.imread('F1.png')
gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
#cv2.imshow('Original image',image)
#cv2.imshow('Gray image', gray)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


cv2.imwrite('GrayF.png', gray1)

imgF = mpimg.imread('GrayF.png')


#recebeu o arquivo fez as mudanças e transformou em array
foto5=Image.open('I.png')
foto6=foto5.resize((20,20))
foto6.save('I1.png')

image = cv2.imread('I1.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#cv2.imshow('Original image',image)
#cv2.imshow('Gray image', gray)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


cv2.imwrite('GrayI.png', gray)

imgI = mpimg.imread('GrayI.png')

#recebeu o arquivo fez as mudanças e transformou em array
foto7=Image.open('J.png')
foto8=foto7.resize((20,20))
foto8.save('J1.png')

image = cv2.imread('J1.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#cv2.imshow('Original image',image)
#cv2.imshow('Gray image', gray)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


cv2.imwrite('GrayJ.png', gray)

imgJ = mpimg.imread('GrayJ.png')



#recebeu o arquivo fez as mudanças e transformou em array
foto1=Image.open('L.png')
foto2=foto1.resize((20,20))
foto2.save('L1.png')

image = cv2.imread('L1.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#cv2.imshow('Original image',image)
#cv2.imshow('Gray image', gray)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


cv2.imwrite('GrayL.png', gray)

imgL = mpimg.imread('GrayL.png')


#recebeu o arquivo fez as mudanças e transformou em array
foto1=Image.open('M.png')
foto2=foto1.resize((20,20))
foto2.save('M1.png')

image = cv2.imread('M1.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#cv2.imshow('Original image',image)
#cv2.imshow('Gray image', gray)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


cv2.imwrite('GrayM.png', gray)

imgM = mpimg.imread('GrayM.png')


#recebeu o arquivo fez as mudanças e transformou em array
foto1=Image.open('T.png')
foto2=foto1.resize((20,20))
foto2.save('T1.png')

image = cv2.imread('T1.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#cv2.imshow('Original image',image)
#cv2.imshow('Gray image', gray)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


cv2.imwrite('GrayT.png', gray)

imgT = mpimg.imread('GrayT.png')

#recebeu o arquivo fez as mudanças e transformou em array
foto1=Image.open('X.png')
foto2=foto1.resize((20,20))
foto2.save('X1.png')

image = cv2.imread('X1.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#cv2.imshow('Original image',image)
#cv2.imshow('Gray image', gray)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


cv2.imwrite('GrayX.png', gray)

imgX = mpimg.imread('GrayX.png')

#recebeu o arquivo fez as mudanças e transformou em array
foto1=Image.open('Z.png')
foto2=foto1.resize((20,20))
foto2.save('Z1.png')

image = cv2.imread('Z1.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#cv2.imshow('Original image',image)
#cv2.imshow('Gray image', gray)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


cv2.imwrite('GrayZ.png', gray)

imgZ = mpimg.imread('GrayZ.png')




#im = Image.open('testN.png')  
#im.show() 


#criando peso do meu cortex

space=[]
for i in range(8):
    space.append([0,0,0,0,0,0,0,0])
    

Cerebro1=cortex(space)
Cerebro1.StartSpace()

'''
#Cerebro1.LearnR(0.2, img, 8)
#Cerebro1.LearnR(0.2, imgE, 30)
#Cerebro1.LearnR(0.2, imgZ, 11)

#print(np.matrix(Cerebro1.espaço[3][3]))
Cerebro1.ShowNeuron(2,2)
print(2,2)
Cerebro1.ShowNeuron(2,4)
print(2,4)
Cerebro1.ShowNeuron(2,6)
print(2,6)
Cerebro1.ShowNeuron(4,2)
print(4,2)
Cerebro1.ShowNeuron(4,4)
print(4,4)
Cerebro1.ShowNeuron(4,6)
print(4,6)
Cerebro1.ShowNeuron(6,2)
print(6,2)
Cerebro1.ShowNeuron(6,4)
print(6,4)
Cerebro1.ShowNeuron(6,6)
print(6,6)

#print(Cerebro1.espaço)

b1=np.matrix(img)
b2=np.matrix(Cerebro1.espaço[3][3])

'''




#ParteA
'''


Cerebro1.LearnR(0.2, imgE, 4)
Cerebro1.ShowNeuron(2,2)
print(2,2)
Cerebro1.ShowNeuron(6,6)
print(6,6)
Cerebro1.LearnR(0.2, imgE, 8)
Cerebro1.ShowNeuron(2,2)
print(2,2)
Cerebro1.ShowNeuron(6,6)
print(6,6)
Cerebro1.LearnR(0.2, imgE, 12)
Cerebro1.ShowNeuron(2,2)
print(2,2)
Cerebro1.ShowNeuron(6,6)
print(6,6)

'''

#Parte B
#Joao
'''
Cerebro1.LearnR(0.2, imgE,1000)
Cerebro1.LearnR(0.2, imgI, 1000)
Cerebro1.LearnR(0.2, imgF, 1000)
Cerebro1.LearnR(0.2, imgJ, 1000)
Cerebro1.ShowNeuron(2,2)
print(2,2)
Cerebro1.ShowNeuron(2,4)
print(2,4)
Cerebro1.ShowNeuron(2,6)
print(2,6)
Cerebro1.ShowNeuron(4,2)
print(4,2)
Cerebro1.ShowNeuron(4,4)
print(4,4)
Cerebro1.ShowNeuron(4,6)
print(4,6)
Cerebro1.ShowNeuron(6,2)
print(6,2)
Cerebro1.ShowNeuron(6,4)
print(6,4)
Cerebro1.ShowNeuron(6,6)
print(6,6)

'''

#Maria


Cerebro1.LearnR(0.2, imgL,2000)
Cerebro1.LearnR(0.2, imgM, 2000)
Cerebro1.LearnR(0.2, imgT, 2000)
Cerebro1.LearnR(0.2, imgX, 2000)
Cerebro1.LearnR(0.2, imgZ, 2000)


Cerebro1.ShowNeuron(2,2)
print(2,2)
Cerebro1.ShowNeuron(2,4)
print(2,4)
Cerebro1.ShowNeuron(2,6)
print(2,6)
Cerebro1.ShowNeuron(4,2)
print(4,2)
Cerebro1.ShowNeuron(4,4)
print(4,4)
Cerebro1.ShowNeuron(4,6)
print(4,6)
Cerebro1.ShowNeuron(6,2)
print(6,2)
Cerebro1.ShowNeuron(6,4)
print(6,4)
Cerebro1.ShowNeuron(6,6)
print(6,6)











































        
        


        
    

                

        
    
















        
        
        

#print(R)

        
            

    
