import cv2
import numpy as np
 
# Read the main image
img_rgb = cv2.imread('processedCoords2.png')
 
# Convert it to grayscale
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
 
# Read the template
# template = cv2.imread('5.png',0)
dictionary = {}
for i in range(10):
	letter = str(i)
	template = cv2.imread(letter + '.png', 0)
	res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
	threshold = 0.9999
	loc = np.where( res >= threshold)
	lists = loc[1].tolist()
	for j in lists:
		dictionary[j] = letter

keys = sorted(dictionary)
print(dictionary)
print(keys)
differences = []
for i in range(1, len(keys)):
	differences.append(keys[i] - keys[i - 1])

print(differences)
text = ""
if (keys[0] > 10):
		text += "-"
for i in range(len(keys)):
	print(dictionary.get(keys[i]), end=" ")
	text += dictionary.get(keys[i])
	if (i < len(keys) - 1):
		if (differences[i] > 14 and differences[i] < 20):
			text += "."
		elif (differences[i] > 35 and differences[i] < 45):
			text += " "
		elif (differences[i] > 50):
			text += " -"
print()
print(text)
# Store width and height of template in w and h
# w, h = template.shape[::-1]
 
# Perform match operations.
# res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)

# Specify a threshold
# threshold = 0.9999
 
# Store the coordinates of matched area in a numpy array

# loc = np.where( res >= threshold)
 
# Draw a rectangle around the matched region.
# for pt in zip(*loc[::-1]):
#     cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
 
# Show the final image with the matched area.
# cv2.imshow('Detected',img_rgb)