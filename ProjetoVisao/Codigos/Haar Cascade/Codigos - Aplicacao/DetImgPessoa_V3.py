import numpy as np
import cv2

print("Iniciou")

#Cria classificador cascade com base no algoritmo treinado
pessoa_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')

upb_cascade = cv2.CascadeClassifier('haarcascade_upperbody.xml')

lob_cascade = cv2.CascadeClassifier('haarcascade_lowerbody.xml')

#Abre imagem e armazena
img = cv2.imread('pessoas2.jpg', 1)

#Converte para escalas de cinza
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Detecta pessoas que foi treinado e armazena as coordenadas do local
pessoas = pessoa_cascade.detectMultiScale(gray)

#print(pessoas)

#Colocar retângulo ao redor da pessoa detectada e repete o
#processo para o número total de pessoas detectadas
for (x,y,w,h) in pessoas:

        #Desenha retângulo na pessoa e prepara para desenhar o próximo
	cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
	roi_gray = gray[y:y+h, x:x+w]
	roi_color = img[y:y+h, x:x+w]

#Detecta pessoas com a parte de corpo de cima que foi treinado e armazena
#as coordenadas do local
upb = upb_cascade.detectMultiScale(gray)
#print(upb)

#Detecta pessoas com a parte de corpo de baixo que foi treinado e armazena
#as coordenadas do local
lob = lob_cascade.detectMultiScale(gray)
#print(lob)

#Colocar retângulo ao redor da pessoa detectada e repete o
#processo para o número total de pessoas detectadas
for (ex,ey,ew,eh) in upb:

        #Desenha retângulo na pessoa com metade do corpo acima
        #e prepara para desenhar o próximo
	cv2.rectangle(img,(ex,ey),(ex+ew,ey+eh),	(0,255,0),2)

#Colocar retângulo ao redor da pessoa detectada e repete o
#processo para o número total de pessoas detectadas
for (ex,ey,ew,eh) in lob:
        
        #Desenha retângulo na pessoa com metade do corpo abaixo
        #e prepara para desenhar o próximo
	cv2.rectangle(img,(ex,ey),(ex+ew,ey+eh),	(0,255,0),2)

#Redefine o tamanho da imagem que será mostrada
img = cv2.resize(img, (600,400))

#Mostra a imagem com as pessoas detectadas
cv2.imshow('img',img)

#Espera qualquer tecla ser apertada para continuar
cv2.waitKey(0)

#Fecha todas as janelas
cv2.destroyAllWindows()

print("Terminou")
