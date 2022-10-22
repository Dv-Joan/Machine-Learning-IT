import cv2
import cv2
import numpy as np

imagen = cv2.imread('Procesamiento de Imagenes/bananos.jpg')
_, binarioUMBRAL = cv2.threshold(imagen, 230, 255, cv2.THRESH_BINARY)
_, binarioInvertidoUMBRAL = cv2.threshold(
    imagen, 100, 255, cv2.THRESH_BINARY_INV)
_, truncadoUMBRAL = cv2.threshold(imagen, 155, 255, cv2.THRESH_TRUNC)
_, toZeroUMBRAL = cv2.threshold(imagen, 155, 255, cv2.THRESH_TOZERO)
_, toZeroInvertidoUMBRAL = cv2.threshold(
    imagen, 155, 255, cv2.THRESH_TOZERO_INV)


cv2.imshow('Imagen Original', imagen)
cv2.imshow('Umbrales Aplicados', np.hstack(
    [binarioUMBRAL, binarioInvertidoUMBRAL, truncadoUMBRAL, toZeroUMBRAL, toZeroInvertidoUMBRAL]))
cv2.waitKey(0)
cv2.destroyAllWindows()
