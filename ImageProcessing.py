# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 14:01:40 2022

@author: kevin
"""

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
#import cv2

picture = mpimg.imread('halfBookSignUpdated.png')
plt.imshow(picture)
picture = picture[22:50, 13:45,...]
"""
red = picture[..., 0]
green = picture[..., 1]
blue = picture[..., 2]

convertToWhite = (red != 1) | (green < 0.332) | (green > 0.334) | (blue < 0.332) | (blue > 0.334)
picture[convertToWhite] = 1
convertToBlack = (red == 1) & (green != 1) & (blue != 1)
picture[convertToBlack] = 0
"""
plt.imshow(picture)
plt.imsave('halfBookSignUpdated.png', picture)

#number = picture[:, 286:292]
#plt.imshow(number)
#plt.imsave('(.png', picture)

"""
if (open("lobbyImage1.png", "rb").read() == open("unprocessedCoordinates.png", "rb").read()):
	print("True")
else:
	print("False")
"""