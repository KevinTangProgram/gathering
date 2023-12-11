import matplotlib.image as mpimg
from decimal import Decimal
#import pytesseract as tess
import pyautogui as py
import numpy as np
import math
import time
import cv2

pointOfInterest = [1.123, 0.0, 1.0]
currentPosition = [0.0, 0.0, 0.0]
currentDirection = [0.0, 0.0]

#negative Z = >90
#positive Z = < 90
#negative X = +angle
#positive X = -angle

#tess.pytesseract.tesseract_cmd = r'C:\Users\kevin\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

#white = mpimg.imread('white.jpg')
py.hotkey('alt', 'tab')
time.sleep(1)

def getPosition(display=False):
	screenshot = py.screenshot(region=(50, 158, 358, 16))
	screenshot.save('unprocessedCoordinates.png')

	"""
	dictionary = {}
	letter = '.'
	for i in range(12):
		if (i < 10):
			letter = str(i)
		elif (i == 10):
			letter = '~'
		elif (i == 11):
			letter = '-'
		for pos in py.locateAllOnScreen(letter + '.png', region=(50, 158, 358, 16)):
			dictionary[pos.left] = letter
	listOfKeys = sorted(dictionary)


	text = ""
	for i in range(len(listOfKeys)):
		text += dictionary.get(listOfKeys[i])

	print(text)
	coords = []
	for i in range(len(text)):
		number = ""
		if (text == '~'):
			coords.append(int(number))
		else:
			number += text[i]
		
	print(coords)
	"""

	coords = mpimg.imread('unprocessedCoordinates.png')
	red = coords[..., 0]
	green = coords[..., 1]
	blue = coords[..., 2]
	convertToBlack = ((red > 0.878) & (red < 0.879) & (green > 0.878) & (green < 0.879) & (blue >= 0.878) & (blue < 0.879))
	coords[convertToBlack] = 0
	convertToWhite = ((red != 0) & (green != 0) & (blue != 0))
	coords[convertToWhite] = 1
	mpimg.imsave("processedCoordinates.png", coords)

	img_rgb = cv2.imread('processedCoordinates.png')
 
	img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

	dictionary = {}
	for i in range(10):
		letter = str(i)
		template = cv2.imread(letter + '.png', 0)
		res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
		threshold = 0.9999
		loc = np.where(res >= threshold)
		lists = loc[1].tolist()
		for j in lists:
			dictionary[j] = letter

	keys = sorted(dictionary)
	differences = []
	for i in range(1, len(keys)):
		differences.append(keys[i] - keys[i - 1])
	text = ""
	if (keys[0] > 10):
			text += "-"
	for i in range(len(keys)):
		text += dictionary.get(keys[i])
		if (i < len(keys) - 1):
			if (differences[i] > 14 and differences[i] < 20):
				text += "."
			elif (differences[i] > 35 and differences[i] < 45):
				text += " "
			elif (differences[i] > 46):
				text += " -"
	#print(text)

	coords = []
	number = ""
	for i in text:
		if (i == ' '):
			coords.append(float(number))
			number = ""
		else:
			number += i
	coords.append(float(number))
	if (display):
		print(coords)
	return coords

	"""
	background = white.copy()

	coordsShape = coords.shape
	startingY = 50 - int(coordsShape[0] / 2)
	startingX = 350 - int(coordsShape[1] / 2)
	background[startingY:startingY + coordsShape[0], startingX:startingX + coordsShape[1], :] = coords

	mpimg.imsave('testdata.png', background)
	text = tess.image_to_string(background)
	text = text[:-1]

	print(text)

	coords = []
	number = ""
	for i in text:
		if (i == '/'):
			coords.append(float(number))
			number = ""
		else:
			if (i == '@'):
				number += '0'
			else:
				number += i
	coords.append(float(number))

	print(coords)
	"""
	"""
	try:
		number = int(text)
	except:
		mpimg.imsave(mythics[i] + '.png', background)
		print(mythics[i]  + ": " + text)
	"""

def getDirection(display=False):
	screenshot = py.screenshot(region=(78, 212, 447, 16))
	screenshot.save('unprocessedDirection.png')

	direction = mpimg.imread('unprocessedDirection.png')
	red = direction[..., 0]
	green = direction[..., 1]
	blue = direction[..., 2]
	convertToBlack = ((red > 0.878) & (red < 0.879) & (green > 0.878) & (green < 0.879) & (blue >= 0.878) & (blue < 0.879))
	direction[convertToBlack] = 0
	convertToWhite = ((red != 0) & (green != 0) & (blue != 0))
	direction[convertToWhite] = 1
	mpimg.imsave("processedDirection.png", direction)

	img_rgb = cv2.imread('processedDirection.png')
 
	img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

	dictionary = {}
	for i in range(11):
		letter = str(i)
		if (i == 10):
			letter = '('
		template = cv2.imread(letter + '.png', 0)
		res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
		threshold = 0.9999
		loc = np.where(res >= threshold)
		lists = loc[1].tolist()
		for j in lists:
			dictionary[j] = letter

	keys = sorted(dictionary)
	differences = []
	for i in range(1, len(keys)):
		differences.append(keys[i] - keys[i - 1])
	#print(keys)
	#print(differences)
	text = ""
	if (differences[1] > 10):
		text += "-"
	for i in range(len(keys)):
		if (dictionary.get(keys[i]) != '('):
			text += dictionary.get(keys[i])
		if (i < len(keys) - 1 and i > 0):
			if (differences[i] > 14 and differences[i] < 20):
				text += "."
			elif (differences[i] > 35 and differences[i] < 45):
				text += " "
			elif (differences[i] > 46):
				text += " -"
	coords = []
	number = ""
	for i in text:
		if (i == ' '):
			#print(number)
			coords.append(float(number))
			number = ""
		else:
			number += i
	#print(number)
	coords.append(float(number))

	if (display):
		print(coords)
	return coords

def calculateDirection(firstPoint, secondPoint, display=False):
	dz = secondPoint[2] - firstPoint[2]
	dx = secondPoint[0] - firstPoint[0]
	angle = 90.0
	if (dz != 0):
		angle = np.degrees(np.arctan(dx/dz))
	if (angle < 0):
		angle *= -1
	if (dz < 0):
		angle += 90
	if (dx > 0):
		angle *= -1
	if (dx == 0 and dz < 0):
		angle = 180.0
	preciseAngle = Decimal(str(angle))
	roundedAngle = round(preciseAngle, 1)
	if (display):
		print(roundedAngle)
	return float(roundedAngle)
	"""
	dz = endingPosition[2] - startingPosition[2]
	dx = endingPosition[0] - startingPosition[0]
	absdz = dz
	absdx = dx
	if (dz < 0):
		absdz = dz * -1
	if (dx < 0):
		absdx = dx * -1
	angle = 0.0
	if (absdz != 0):
		angle = np.degrees(np.arctan(absdx/absdz))
	if (dz > 0 and dx > 0):
		angle *= -1
	#elif (dz > 0 and dx < 0):
	#	angle = angle
	elif (dz < 0 and dx > 0):
		angle += 90
		angle *= -1
	elif (dz < 0 and dx < 0):
		angle += 90
	elif (dx == 0 and dz < 0):
		angle = 180.0
	elif (dz == 0 and dx > 0):
		angle = -90.0
	elif (dz == 0 and dx < 0):
		angle = 90.0
	preciseAngle = Decimal(str(angle))
	roundedAngle = round(preciseAngle, 1)
	print(angle)
	print(roundedAngle)
	"""
	"""
	print(dx, dz)
	if (absdx != 0):
		angle = np.degrees(np.arctan(absdz/absdx))
	if (dz < 0):
		angle += 90
	if (dx > 0):
		angle *= -1
	preciseAngle = Decimal(str(angle))
	roundedAngle = round(preciseAngle, 1)
	print(angle)
	print(roundedAngle)
	"""

def calibrate():
	currentPosition = getPosition()
	currentDirection = getDirection()

def turn(pixels, time = 0.3):
	py.drag(pixels, 0, time, button = 'middle')		#90
"""
	if (adjustment == 1):
		py.drag(1, 0, 0.1, button='middle')
	elif (adjustment == 2):
		py.drag(10, 0, 0.1, button='middle')	#1.5
	elif (adjustment == 3):
		py.drag(20, 0, 0.1, button='middle')
	elif (adjustment == 3):
		py.drag(100, 0, 0.1, button='middle')	#15
"""


def moveForward(delay):
	py.keyDown('w')
	time.sleep(delay)
	py.keyUp('w')

def proximity():
	r2 = (pointOfInterest[0]-currentPosition[0])**2 + (pointOfInterest[2]-currentPosition[2])**2
	if (r2 < 9):
		return True
	return False

def makeAdjustments():
	targetDirection = calculateDirection(currentPosition, pointOfInterest)
	print(targetDirection)
	currentDirection = getDirection()
	if (currentDirection[0] != targetDirection):
		angle = currentDirection[0]
		offset = 0.0
		if (currentDirection[0] < 0):
			angle += 360
		if (angle > targetDirection):
			if (angle - targetDirection < 180):
				offset = targetDirection - angle				#left
			else:
				offset = 360 - angle + targetDirection			#right
		else:
			if (targetDirection - angle < 180):
				offset = targetDirection - angle - 360			#left
			else:
				offset = targetDirection - angle				#right
		offset *= 20
		offset /= 9
		turn(offset)

	currentDirection = getDirection()
	if (currentDirection[0] > 179 and targetDirection < -179 or currentDirection[0] < -179 and targetDirection > 179):
		angle = currentDirection[0]
		while (currentDirection[0] != targetDirection):
			if (angle > targetDirection):
				turn(1, 0.1)										#right
			else:
				turn(-1, 0.1)										#left
			currentDirection = getDirection()
	else:
		while (currentDirection[0] != targetDirection):
			angle = currentDirection[0]
			if (angle > targetDirection):
				turn(-1, 0.1)										#left
			else:
				turn(1, 0.1)										#right	
			currentDirection = getDirection()

def checkAlightment():
	currentDirection = getDirection()
	if (currentDirection[0] != calculateDirection(currentPosition, pointOfInterest)):
		makeAdjustments()
	
def move():
	py.keyDown('w')

#calibrate()
#time.sleep(5)
#calculateDirection()
#panLeft(100)
#getPosition()
#getDirection()
#moveForward(10)
#calculateDirection(currentPosition, pointOfInterest, True)
#turnRight(2)
makeAdjustments()
#turnRight(1200)
#getDirection(True)
print("\nCompleted\n")
py.hotkey('alt', 'tab')