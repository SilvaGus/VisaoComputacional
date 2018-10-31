import numpy as np
import cv2



print("Iniciou")

#Cria classificador cascade com base no algoritmo treinado
pessoa_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')

#Abre o video e armazena
cap = cv2.VideoCapture('videopessoa2.mp4')

#Codigo se repete ate que seja interrompido
while True:

        #Ler frame atual do video armazena 
	ret, img = cap.read()

	#Converte para escalas de cinza
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	#Detecta o objeto que foi treinado e armazena as coordenadas do local
	pessoas = pessoa_cascade.detectMultiScale(gray, 1.3, 5)

        #Colocar retângulo ao redor da pessoa detectada e repete o
        #processo para o número total de pessoas detectadas
	for (x,y,w,h) in pessoas:

                #Desenha retângulo na imagem e prepara para desenhar o próximo
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = img[y:y+h, x:x+w]
		
        #Mostra a imagem com as pessoas detectadas
	cv2.imshow('img',img)

	#Interrompe o código	
	if cv2.waitKey(25) & 0xFF == ord('q'):
		break

#Para de ler o video
cap.release()

#Espera qualquer tecla ser apertada para continuar
cv2.waitKey(0)

#Fecha todas as janelas
cv2.destroyAllWindows()

print("Terminou")



