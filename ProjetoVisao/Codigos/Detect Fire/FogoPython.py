import cv2
import numpy as np

print("Iniciou")

#Le a imagem e armazena
img = cv2.imread('car-fire.jpg',1)
#edges = cv2.Canny(img,100,200)

#Transforma a imagem para o dominio HSV
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#Cria uma copia 
newhsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

#Separa a imagem nos tres dominios Value, Saturation, Hue
va = hsv[:,:,2]
sa = hsv[:,:,1]
hu = hsv[:,:,0]

#Faz o mesmo para a copia
newva = newhsv[:,:,2]
newsa = newhsv[:,:,1]
newhu = newhsv[:,:,0]


#Pega os valores dos tamanhos das matrizes
tamcol=len(hsv[:,1])
tamrow=len(hsv[1,:])

#Cria trez matrizes auxiliares de zeros do tamanho da imagem
idx0=np.zeros((tamcol,tamrow))
idx1=np.zeros((tamcol,tamrow))
idx2=np.zeros((tamcol,tamrow))

#Agora 3 novas matrizes serao criadas, em que os valores de HSV
#correspondentes a cor fogo e fumaca serao separados, para que eles
#possam ser isolados do resto da imagem

for i in range(tamcol):
	for j in range(tamrow):
		if hu[i,j]>51:
			newhu[i,j]=0
			
		else:
			newhu[i,j]=hu[i,j]
			
#print(idx0)

for i in range(tamcol):
	for j in range(tamrow):
		if sa[i,j]<76:
			newsa[i,j]=0
		else:
			
			newsa[i,j]=sa[i,j]
			
#print(idx1)

for i in range(tamcol):
	for j in range(tamrow):
		if va[i,j]<127:
			
			newva[i,j]=0

		else:
			newva[i,j]=va[i,j]

#print(idx2)

#Juntas as matrizes para que elas formem uma nova imagem
fogo=cv2.merge([newhu,newsa,newva])

#Converte a imagem novamente para o dominio RGB
fogo2=cv2.cvtColor(fogo,cv2.COLOR_HSV2BGR)

#Mostra a imagem antes e depois do processamento
cv2.imshow('img',img)
cv2.imshow('fogo2',fogo2)

#Espera alguma tecla ser pressionada
cv2.waitKey(0)

#Encerra todas as janelas
cv2.destroyAllWindows()

print("Terminou")

