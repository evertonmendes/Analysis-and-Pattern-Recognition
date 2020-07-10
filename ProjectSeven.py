# -*- coding: utf-8 -*-
#Nome: Éverton Luís Mendes da Silva
#N°USP: 10728171


import matplotlib.pyplot as plt
import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
from sklearn.decomposition import PCA
from sklearn import datasets
from sklearn.metrics import plot_confusion_matrix
from sklearn.metrics import confusion_matrix
import seaborn as sn
import pandas as pd
from PIL import Image
import cv2
import matplotlib.image as mpimg
from scipy.cluster.hierarchy import dendrogram, linkage

iris = datasets.load_iris()
X = iris.data[:, :4]

arquivo=open('Iris.dat','w')
arquivo.writelines(str(X))
arquivo.close()

arquivo=open('IrisTarget.dat','w')
arquivo.writelines(str(iris.target))
arquivo.close()




#print(X)




#plt.title('Ward')
Z = linkage(X, 'ward')
fig = plt.figure(figsize=(25, 10))
dn = dendrogram(Z)

#plt.title('single')
Z = linkage(X, 'single')
fig = plt.figure(figsize=(25, 10))
dn = dendrogram(Z)

#plt.title('average')
Z = linkage(X, 'average')
fig = plt.figure(figsize=(25, 10))
dn = dendrogram(Z)


#plt.title('complete')
Z = linkage(X, 'complete')
fig = plt.figure(figsize=(25, 10))
dn = dendrogram(Z)


plt.show()


#print(len(Z))
#print(Z)
#print(len(iris.target))
#print(iris.target)
'''
y=iris.target
y1=[]
for i in range(len(y)-1):
    y1.append(y[i])



    
    




df_cm=confusion_matrix(y1, Z)

df_cm = pd.DataFrame(df_cm, range(3), range(3))
# plt.figure(figsize=(10,7))
sn.set(font_scale=1.4) # for label size
sn.heatmap(df_cm, annot=True, annot_kws={"size": 16}) # font size

#plt.imshow(MatrizConf, cmap='binary')
plt.show()

'''




