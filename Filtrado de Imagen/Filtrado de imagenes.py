# Configurar como directorio de trabajo D:/Universidad/UNCP/Innovacion de TI/Practicas"
# Tools -> Preferences / Working Directory
# Tools -> Run / Working Directory

from msilib.schema import CreateFolder
import cv2
import numpy as np

bananos = cv2.imread('Filtrado de Imagen/bananos.jpg')

# Crear imagen original
cv2.imshow('original', bananos)
cv2.waitKey(5)

# Crear filtro de 2x2 . Creacion de matriz de 2x2 de 1s
filtro_2x2 = np.ones((2, 2))/(2*2)
outputFiltro_2x2 = cv2.filter2D(bananos, -1, filtro_2x2)
cv2.imshow('Filtrado de Imagen 2x2', outputFiltro_2x2)
cv2.waitKey(5)

# Crear filtro 5x5. Creacion de matriz de 5x5 de 1s
filtro_5x5 = np.ones((5, 5))/((5*5))
outputFiltro_5x5 = cv2.filter2D(bananos, -1, filtro_5x5)
cv2.imshow('Filtrado de Imagen 5x5', outputFiltro_5x5)
cv2.waitKey(5)


# Crear filtro 11x11. Creacion de matriz de 11 x 11 de 1s
filtro_11x11 = np.ones((11, 11))/(11*11)
outputFiltro_11x11 = cv2.filter2D(bananos, -1, filtro_11x11)
cv2.imshow('Imagen con Filtro 11x11', outputFiltro_11x11)
cv2.waitKey(5)

# Crear filtro 30x30. Creacion de matriz de 30 x 30 de 1s
filtro_30x30 = np.ones((30, 30))/(30*30)
outputFiltro_30x30 = cv2.filter2D(bananos, -1, filtro_30x30)
cv2.imshow('Imagen con Filtro 30x30', outputFiltro_30x30)
cv2.waitKey(5)

# Crear filtro 40x40. Creacion de matriz de 40 x 40 de 1s
filtro_40x40 = np.ones((40, 40))/(40*40)
outputFiltro_40x40 = cv2.filter2D(bananos, -1, filtro_40x40)
cv2.imshow('Imagen con Filtro 40x40 ', outputFiltro_40x40)
cv2.waitKey(0)
