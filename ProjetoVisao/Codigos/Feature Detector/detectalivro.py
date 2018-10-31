import cv2
import numpy as np
#from matplotlib import pyplot as plt




print("Comecou")

img1 = cv2.imread('livro.jpeg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('livrof.jpeg',cv2.IMREAD_GRAYSCALE)

#sift = cv2.xfeatures2d.SIFT_create()

#surf = cv2.xfeatures2d.SURF_create()

orb = cv2.ORB_create()

keypoints1, descriptors1 = orb.detectAndCompute(img1, None)

keypoints2, descriptors2 = orb.detectAndCompute(img2, None)


img1 = cv2.drawKeypoints(img1, keypoints1, None)

img2 = cv2.drawKeypoints(img2, keypoints2, None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

matches = bf.match(descriptors1,descriptors2)

matches = sorted(matches, key = lambda x:x.distance)

mat_result = cv2.drawMatches(img1, keypoints1, img2, keypoints2,matches, None)

cv2.namedWindow('img1',cv2.WINDOW_NORMAL)

cv2.imshow('img1',img1)

cv2.namedWindow('img2',cv2.WINDOW_NORMAL)

cv2.imshow('img2',img2)

cv2.namedWindow('mat_result',cv2.WINDOW_NORMAL)

cv2.imshow('mat_result',mat_result)


'''

hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)


va = hsv[:,:,2]
sa = hsv[:,:,1]
hu = hsv[:,:,0]


tamcol=len(hsv[:,1])
tamrow=len(hsv[1,:])

idx0=np.zeros((tamcol,tamrow))


for i in range(tamcol):
	for j in range(tamrow):
		if hu[i,j]>51:
			newhu[i,j]=0
			
		else:
			newhu[i,j]=hu[i,j]
			


print(idx2)


fogo=cv2.merge([newhu,newsa,newva])

fogo2=cv2.cvtColor(fogo,cv2.COLOR_HSV2BGR)


cv2.imshow('img',img)
cv2.imshow('fogo2',fogo2)
'''
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Terminou")
