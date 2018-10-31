import cv2
import numpy as np
#from matplotlib import pyplot as plt




print("Comecou")

img = cv2.imread('car-fire.jpg',1)
#edges = cv2.Canny(img,100,200)

hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
newhsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)


va = hsv[:,:,2]
sa = hsv[:,:,1]
hu = hsv[:,:,0]

newva = newhsv[:,:,2]
newsa = newhsv[:,:,1]
newhu = newhsv[:,:,0]



tamcol=len(hsv[:,1])
tamrow=len(hsv[1,:])

idx0=np.zeros((tamcol,tamrow))
idx1=np.zeros((tamcol,tamrow))
idx2=np.zeros((tamcol,tamrow))


for i in range(tamcol):
	for j in range(tamrow):
		if hu[i,j]>51:
			newhu[i,j]=0
			
		else:
			newhu[i,j]=hu[i,j]
			

print(idx0)

for i in range(tamcol):
	for j in range(tamrow):
		if sa[i,j]<76:
			newsa[i,j]=0
		else:
			
			newsa[i,j]=sa[i,j]
print(idx1)

for i in range(tamcol):
	for j in range(tamrow):
		if va[i,j]<127:
			
			newva[i,j]=0

		else:
			newva[i,j]=va[i,j]

print(idx2)


fogo=cv2.merge([newhu,newsa,newva])

fogo2=cv2.cvtColor(fogo,cv2.COLOR_HSV2BGR)

#fogo2=cv2.cvtColor(fogo,cv2.COLOR_HSV2BGR)

#fogo2=cv2.cvtColor(fogo,cv2.COLOR_HSV2BGR)

cv2.imshow('img',img)
cv2.imshow('fogo2',fogo2)



'''	
for i in range(15):
	for j in range(15):
		if mat1[i,j]<76:
			mat0[i,j]=mat1[i,j]
			
for i in range(15):
	for j in range(15):
		if mat1[i,j]<127:
			mat0[i,j]=mat1[i,j]
	
'''



'''


lower_def = np.array([51,0,0])
upper_def = np.array([255,76,127])

fogo = cv2.inRange(hsv,lower_def,upper_def)


cv2.imshow('img',img)
cv2.imshow('fogo',fogo)


print(fogo)
'''
'''
cv2.imshow('hsv',hsv)
cv2.imshow('hu',hu)
cv2.imshow('san',sa)
cv2.imshow('va',va)
'''


'''
red = img[:,:,2]
green = img[:,:,1]
blue = img[:,:,0]

#cv2.imshow('img',img)
#cv2.imshow('red',red)
#cv2.imshow('green',green)
#cv2.imshow('blue',blue)
'''

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Terminou")
