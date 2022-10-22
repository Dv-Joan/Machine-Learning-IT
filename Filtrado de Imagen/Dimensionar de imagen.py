import cv2
import numpy as np

imagen = cv2.imread('Filtrado de Imagen/bananos.jpg')
alturaImagen = imagen.shape[0]  # Filas
anchoImagen = imagen.shape[1]  # Columnas

# Mostrar una parte de la imagen
piezaImagen = imagen[0:int(alturaImagen/2), 0:int(anchoImagen/2)]
pieza2Imagen = imagen[100:500, 500:700]


# Matriz para la traslacion de una imagen
# (Coordenada de traslacion en X ,Coordenada de traslacion en Y)
MatrizT = np.float32([[1, 0, 50], [0, 1, 100]])
imagenTrasladada = cv2.warpAffine(imagen, MatrizT, (anchoImagen, alturaImagen))


# Matriz para la rotacion de la imagen
# (Centro de Rotacion, grado de inclinacion, escala)
MatrizR = cv2.getRotationMatrix2D((anchoImagen/2, alturaImagen/2), 15, 1)
imagenRotada = cv2.warpAffine(imagen, MatrizR, (anchoImagen, alturaImagen))

# Escalado de una imagen
imagenEscalada = cv2.resize(
    imagen, (500, 500), interpolation=cv2.INTER_CUBIC)

# Salidas
cv2.imshow('Traslacion de la imagen', imagenTrasladada)
cv2.imshow('Rotacion de la imagen', imagenRotada)
cv2.imshow('Escalado de la imagen', imagenEscalada)
cv2.imshow('Recorte de Imagen', np.hstack([piezaImagen, pieza2Imagen]))
cv2.imshow('Imagen Original', imagen)
print('Imagen Shape', imagen.shape)
cv2.waitKey(0)
cv2.destroyAllWindows()
