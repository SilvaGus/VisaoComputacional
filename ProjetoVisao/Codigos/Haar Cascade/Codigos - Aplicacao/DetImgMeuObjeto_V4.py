#Bibliotecas
import numpy as np
import cv2

print("Iniciou")

#Cria classificador cascade com base no algoritmo treinado
pessoa_cascade = cv2.CascadeClassifier('meu_cascade.xml')

#Abre imagem e armazena
img = cv2.imread('tes.jpeg', 1)

#Converte para escalas de cinza
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Detecta o objeto que foi treinado e armazena as coordenadas do local
pessoas = pessoa_cascade.detectMultiScale(gray)

#print(pessoas)

#Colocar retângulo ao redor da pessoa detectada e repete o
#processo para o número total de pessoas detectadas
for (x,y,w,h) in pessoas:

        #Desenha retângulo na imagem e prepara para desenhar o próximo
	cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
	roi_gray = gray[y:y+h, x:x+w]
	roi_color = img[y:y+h, x:x+w]

#Redefine o tamanho da imagem que será mostrada
img = cv2.resize(img, (600,400))

#Mostra a imagem com as pessoas detectadas
cv2.imshow('img',img)

#Espera qualquer tecla ser apertada para continuar
cv2.waitKey(0)

#Fecha todas as janelas
cv2.destroyAllWindows()

print("Terminou")
