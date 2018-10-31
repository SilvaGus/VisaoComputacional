#Bibliotecas
import urllib.request
import cv2
import numpy as np
import os

#Funcao que copia o link de cada imagem do site imagenet e armazena no computador com tamanho alterado. Essas imagens serao utilizadas como positivo 
def armazena_imagens():
    neg_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n07942152'   
    neg_image_urls = urllib.request.urlopen(neg_images_link).read().decode()
    pic_num = 1
    

    if not os.path.exists('neg'):
        os.makedirs('neg')
        
    for i in neg_image_urls.split("\n"):
        try:
            print(i)
            urllib.request.urlretrieve(i, "neg/"+str(pic_num)+".jpg")
            img = cv2.imread("neg/"+str(pic_num)+".jpg",cv2.IMREAD_GRAYSCALE)
            resized_image = cv2.resize(img, (100, 100))
            cv2.imwrite("neg/"+str(pic_num)+".jpg",resized_image)
            pic_num += 1
            
        except Exception as e:
            print(str(e)) 

#Funcao para eliminar imagens que ocorreram problemas
def encontra_defeito():
	match = False
	for file_type in ['pos']:
		for img in os.listdir(file_type):
			for ugly in os.listdir('ugly'):
				try:
					current_image_path = str(file_type)+'/'+str(img)
					ugly = cv2.imread('ugly/'+str(ugly))
					question = cv2.imread(current_image_path)
					print(question.shape)
					if ugly.shape == question.shape and not(np.bitwise_xor(ugly,question).any()):
						print('That is one ugly pic! Deleting!')
						print(current_image_path)
						os.remove(current_image_path)
				except Exception as e:
					print(str(e))

#Funcao que armazena as imagens positivas 
def armazena_imagens_p():
    neg_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n02958343'   
    neg_image_urls = urllib.request.urlopen(neg_images_link).read().decode()
    pic_num = 1
    

    if not os.path.exists('pos'):
        os.makedirs('pos')
        
    for i in neg_image_urls.split("\n"):
        try:
            print(i)
            urllib.request.urlretrieve(i, "pos/"+str(pic_num)+".jpg")
            img = cv2.imread("pos/"+str(pic_num)+".jpg",cv2.IMREAD_GRAYSCALE)
            resized_image = cv2.resize(img, (100, 100))
            cv2.imwrite("pos/"+str(pic_num)+".jpg",resized_image)
            pic_num += 1
            
        except Exception as e:
            print(str(e)) 


#Cria o arquivo descritor de negativas 
def criar_pos_neg():
    for file_type in ['neg']:
        
        for img in os.listdir(file_type):

            if file_type == 'pos':
                line = file_type+'/'+img+' 1 0 0 50 50\n'
                with open('info.dat','a') as f:
                    f.write(line)
            elif file_type == 'neg':
                line = file_type+'/'+img+'\n'
                with open('bg.txt','a') as f:
                    f.write(line)

#Funcao para reduzir o tamanho da imagem que sera objeto alvo
def redu():
	img = cv2.imread("tesoura.jpeg",cv2.IMREAD_GRAYSCALE)
	resized_image = cv2.resize(img, (50, 50))
	cv2.imwrite("teste.jpg",resized_image)


#A partir de agora as funcoes podem ser chamadas para que o treinamento possa ocorrer
