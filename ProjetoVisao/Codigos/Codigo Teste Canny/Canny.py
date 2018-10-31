import cv2
import numpy as np

print("Iniciou")

#Le uma imagem e armazena em img
img = cv2.imread('logo.jpeg',0)

#Usando o algoritmo Canny, as bordas da imagem sao detectada
edges = cv2.Canny(img,100,200)

#Mostra a imagem com as bordas
cv2.imshow('edges',edges)

#Programa espera alguma tecla ser pressionada
cv2.waitKey(0)

#Fecha todas as janelas
cv2.destroyAllWindows()

print("Terminou")
