import cv2
import numpy as np
import glob
import matplotlib.pyplot as plt

img = cv2.imread('Clasificacion de Imagenes/Images/Lunares DS/dysplasticNevi/Training/dysplasticNevi10.jpg')
def getFeatures(img):
 gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 threshold,_ = cv2.threshold(gray,0,255,cv2.THRESH_OTSU)
 mask = np.uint8(1*(gray<threshold))
 B=(1/255)*np.sum(img[:,:,0]*mask)/np.sum(mask)
 G=(1/255)*np.sum(img[:,:,1]*mask)/np.sum(mask)
 R=(1/255)*np.sum(img[:,:,2]*mask)/np.sum(mask)
 return [B,G,R]

paths=['Clasificacion de Imagenes/Images/Lunares DS/dysplasticNevi/Training/',
 'Clasificacion de Imagenes/Images/Lunares DS/spitzNevus/Training/'
 ]
labels=[]
features=[]
for label, path in enumerate(paths): 
   for path in paths :
      for filename in glob.glob(path+'*.jpg'):
         img=cv2.imread(filename)
         feature_vector=np.array(getFeatures(img))
         x=np
         features.append(x)
         labels.append(label)





# Para el grafico de puntos en 3R
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')

for i, feature_row in enumerate(features):
    if labels[i] == -1:
        ax.scatter(feature_row[0], feature_row[1], feature_row[2], marker='*', c='k')
    else:
        ax.scatter(feature_row[0], feature_row[1], feature_row[2], marker='*', c='r')

ax.set_xlabel('B')
ax.set_ylabel('G')
ax.set_zlabel('R')

subFeatures = features[:, 1::]
loss = []

for w1 in np.linspace(-6, 6, 100):
    for w2 in np.linspace(-6, 6, 100):
        totalError = 0
        for i, feature_row in enumerate(subFeatures):
            sample_error = (w1 * feature_row[0] + w2 * feature_row[1] - labels[i]) ** 2
            totalError += sample_error
        loss.append([w1, w2, totalError])

loss = np.array(loss)

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')
ax1.plot_trisurf(loss[:, 0], loss[:, 1], loss[:, 2], cmap=cm.jet, linewidth=0)
ax1.set_xlabel('w1')
ax1.set_ylabel('w2')
ax1.set_zlabel('loss')

A = np.zeros((4, 4))
b = np.zeros((4, 1))

for i, feature_row in enumerate(features):
    x = np.append([1], feature_row)
    x = x.reshape((4, 1))
    y = labels[i]
    A = A + x * x.T
    b = b + x * y

invA = np.linalg.inv(A)
W = np.dot(invA, b)

X = np.arange(0, 1, 0.1)
Y = np.arange(0, 1, 0.1)
X, Y = np.meshgrid(X, Y)
Z = -(W[1] * X + W[2] * Y + W[0]) / W[3]





# Para el grafico 3d de la superficie de decision

import matplotlib.cm as cm

ax.plot_surface(X, Y, Z, cmap=cm.Blues)

prediction = 1 * (W[0] + np.dot(features, W[1::])) >= 0
prediction = 2 * prediction - 1
error = np.sum(prediction != labels.reshape(-1, 1)) / len(labels)
efectividad = 1 - error

path_img = 'Clasificacion de Imagenes/Images/Lunares DS/spitzNevus/Training/spitzNevus5.jpg'
img = cv2.imread(path_img)
feature_vector = np.array(getFeatures(img))
result = np.sign(W[0] + np.dot(feature_vector, W[1::]))
if result == -1:
    print("es un dysplasticNevi")
else:
    print("es un spitzNevus")
