# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 23:58:19 2022

@author: kevin
"""

#import pytesseract as tess
#from PIL import Image
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
#import time

img = mpimg.imread('君の名は.jpg')
copy = img.copy()
plt.imshow(copy)
r = copy[..., 0]
g = copy[..., 1]
b = copy[..., 2]
print(img.shape)

mask = ((r < 255) & (g < 255) & (b < 255))
copy[mask] = 255

plt.imshow(copy)
a = copy.shape
white = copy[0:100, 0:700, :]
print(white.shape)
plt.imshow(white)
#plt.imshow(carbonCopy)
mpimg.imsave('white.jpg', white)
# image = Image.open('white.png')
# newImage = image.resize((a[1]*10, a[0]*10))
# newImage.show()
# newImage.save('white.png')