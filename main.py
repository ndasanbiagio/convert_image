import cv2
import os



# Option

images = os.listdir('images')
for image in images:
  print(image)
  gray = cv2.imread(f'images/{image}', 0)
  print(gray)
  cv2.imwrite(f'grayimages/gray-{image}', gray)



# One option
color = cv2.imread('imagenes/galaxy.jpeg', 0)
cv2.imwrite('galaxy-gray.jpeg', color)

color1 = cv2.imread('imagenes/python.jpeg', 0)
cv2.imwrite('pyhton-gray.jpeg', color1)

color2 = cv2.imread('imagenes/bear.jpeg', 0)
cv2.imwrite('bear-gray.jpeg', color2)


