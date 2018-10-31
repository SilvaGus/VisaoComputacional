#Bibliotecas
import cv2
import numpy as np

#######################PARTE 1#######################

#Definindo Funcoes

#Esta funcao pega o contorno de findContours
#entao a saida sera os centroides das coordenadas
def x_cord_contour(contour):
    
    M = cv2.moments(contour)
    return (int(M['m10']/M['m00']))

#Esta funcao pega uma imagem e determina as dimensoes dos quadrados
#Adicioa margens pretas onde necessario   
def makeSquare(not_square):

    BLACK = [0,0,0]
    img_dim = not_square.shape
    height = img_dim[0]
    width = img_dim[1]
    if (height == width):
        square = not_square
        return square
    else:
        doublesize = cv2.resize(not_square,(2*width, 2*height), interpolation = cv2.INTER_CUBIC)
        height = height * 2
        width = width * 2
        if (height > width):
            pad = (height - width)/2
            doublesize_square = cv2.copyMakeBorder(doublesize,0,0,int(pad),\
                                                   int(pad),cv2.BORDER_CONSTANT,value=BLACK)
        else:
            pad = (width - height)/2

            doublesize_square = cv2.copyMakeBorder(doublesize,int(pad),int(pad),0,0,\
                                                   cv2.BORDER_CONSTANT,value=BLACK)
    doublesize_square_dim = doublesize_square.shape

    return doublesize_square

#Esta funcao redefine o tamanho da imagem para uma diensao especifica
def resize_to_pixel(dimensions, image):
    
    buffer_pix = 4
    dimensions  = dimensions - buffer_pix
    squared = image
    r = float(dimensions) / squared.shape[1]
    dim = (dimensions, int(squared.shape[0] * r))
    resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
    img_dim2 = resized.shape
    height_r = img_dim2[0]
    width_r = img_dim2[1]
    BLACK = [0,0,0]
    if (height_r > width_r):
        resized = cv2.copyMakeBorder(resized,0,0,0,1,cv2.BORDER_CONSTANT,value=BLACK)
    if (height_r < width_r):
        resized = cv2.copyMakeBorder(resized,1,0,0,0,cv2.BORDER_CONSTANT,value=BLACK)
    p = 2
    ReSizedImg = cv2.copyMakeBorder(resized,p,p,p,p,cv2.BORDER_CONSTANT,value=BLACK)
    img_dim = ReSizedImg.shape
    height = img_dim[0]
    width = img_dim[1]
    return ReSizedImg

#######################PARTE 2#######################

#Abri digitos que serao utilizados
image = cv2.imread('images/digits.png')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
small = cv2.pyrDown(image)

cv2.waitKey(0)
cv2.destroyAllWindows()

#Separa a imagem em 5000 celulas, cada uma com um tamanho de 20x20
#Isto nos da um array de 4 dimensoes: 50 x 100 x 20 x 20
cells = [np.hsplit(row,100) for row in np.vsplit(gray,50)]

#Converte os dados para Numpy Array (50,100,20,20)
x = np.array(cells)

#Separa todos os dados dentro de dois segmentos
#Um sera usado para treinamento e o outro para testes
train = x[:,:70].reshape(-1,400).astype(np.float32) # Tamanho = (3500,400)
test = x[:,70:100].reshape(-1,400).astype(np.float32) # Tamanho = (1500,400)

#Nomeia dados para treinamento e dados
k = [0,1,2,3,4,5,6,7,8,9]
train_labels = np.repeat(k,350)[:,np.newaxis]
test_labels = np.repeat(k,150)[:,np.newaxis]

#Inicia KNN, treina os dados, e entao testa com os dados para k=3
knn = cv2.ml.KNearest_create()
knn.train(train, cv2.ml.ROW_SAMPLE, train_labels)
ret, result, neighbors, distance = knn.findNearest(test, k=3)

#Agora verifica-se a precisao da classificacao
matches = result == test_labels
correct = np.count_nonzero(matches)
#accuracy = correct * (100.0 / result.size)
#print("Precisao de %.2f" % accuracy + "%")


#######################PARTE 3#######################

#Agora que os dados foram treinados o algoritmo de leitura de numeros sera executado
image = cv2.imread('images/numbers5.jpeg')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("image", image)


#A imagem sera borrada e o algoritmo canny de deteccao de borda sera utilizado 
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(blurred, 30, 150)

#Encontra contornos
_, contours, _ = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#Ordena os contornos da esquerda para a direita usando suas coordenadas x
contours = sorted(contours, key=x_cord_contour, reverse = False)

#Cria um array vazio
full_number = []

#Laco de repeticao para contornos
for c in contours:
    (x, y, w, h) = cv2.boundingRect(c)    

    if w >= 5 and h >= 25:
        roi = blurred[y:y + h, x:x + w]
        ret, roi = cv2.threshold(roi, 127, 255,cv2.THRESH_BINARY_INV)
        
        squared = makeSquare(roi)
        final = resize_to_pixel(20, squared)
        cv2.imshow("final", final)
        final_array = final.reshape((1,400))
        final_array = final_array.astype(np.float32)
        ret, result, neighbours, dist = knn.findNearest(final_array, k=1)
        number = str(int(float(result[0])))
        full_number.append(number)
        #Desenha um retangulo sobre o digito e mosta o que o digito classificou
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.putText(image, number, (x , y + 155),
            cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 0), 2)
        cv2.waitKey(0) 
        
cv2.destroyAllWindows()

#Resultado final mostrado no terminal
print ("O numero eh: " + ''.join(full_number))





