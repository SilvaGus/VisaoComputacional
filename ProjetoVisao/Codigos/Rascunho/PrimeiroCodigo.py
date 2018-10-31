import cv2

image = cv2.imread('lena.png',0)
x=10
print("Testando")

cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
