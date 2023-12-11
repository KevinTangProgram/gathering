import matplotlib.image as mpimg
from decimal import Decimal
import pyautogui as py
import numpy as np
import math
import time
import cv2

pointOfInterest = []

class Node:
	def __init__(self, coordinates, farmable = True):
		self.coordinates = coordinates
		self.farmable = farmable
		pointOfInterest.append(self)

Node([767.5, 96.5, -4652.5])
Node([758.5, 94.5, -4655.5])
Node([762.5, 98.5, -4647.5])
Node([766.5, 102.5, -4638.5])
Node([764.5, 105.5, -4628.5])
Node([757.5, 106.5, -4624.5])
Node([780.5, 100.5, -4639.5])

def absoluteValue(n):
	if (n < 0):
		return -n
	return n

def turn(pixels, time = 0.3):
	py.drag(pixels, 0, time, button = 'middle')

def rotate(pixels, time = 0.3):
	py.drag(0, pixels, time, button = 'middle')		#90

def farm(left = True, delay = 7):
	if (left):
		py.click()
	else:
		py.rightClick()
	time.sleep(delay)

def getPosition(display=False):
	#screenshot = py.screenshot(region=(50, 194, 358, 16))			#1.17
	screenshot = py.screenshot(region=(50, 158, 358, 16))			#1.12
	screenshot.save('unprocessedCoordinates.png')

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

def getDirection(display=False):
	screenshot = py.screenshot(region=(78, 212, 447, 16))			#1.12
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

def getVisual(display = False, node = False):
	screenshot = py.screenshot(region=(116, 284, 175, 16))			#1.12 #164
	screenshot.save('unprocessedVisual.png')

	coords = mpimg.imread('unprocessedVisual.png')
	red = coords[..., 0]
	green = coords[..., 1]
	blue = coords[..., 2]
	convertToBlack = ((red > 0.878) & (red < 0.879) & (green > 0.878) & (green < 0.879) & (blue >= 0.878) & (blue < 0.879))
	coords[convertToBlack] = 0
	convertToWhite = ((red != 0) & (green != 0) & (blue != 0))
	coords[convertToWhite] = 1
	mpimg.imsave("processedVisual.png", coords)

	img_rgb = cv2.imread('processedVisual.png')
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
	#print(keys)
	#print(differences)

	if (len(keys) == 0):
		return []
	if (keys[0] > 10):
			text += "-"
	for i in range(len(keys)):
		text += dictionary.get(keys[i])
		if (i < len(keys) - 1):
			if (differences[i] > 15 and differences[i] < 25):
				text += " "
			elif (differences[i] > 25):
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
	if (node):
		coords[0] += 0.5
		coords[1] += 0.5
		coords[2] += 0.5
		print(coords)
	return coords

def calculateDirection(firstPoint, secondPoint, display=False):
	dz = secondPoint[2] - firstPoint[2]
	dx = secondPoint[0] - firstPoint[0]
	angle = 90.0
	if (dz != 0):
		if (dz > 0):
			angle = np.degrees(np.arctan(dx/dz))
		else:
			angle = np.degrees(np.arctan(dz/dx))
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

def calculateRotation(firstPoint, secondPoint, display=False):
	firstLength = math.sqrt((secondPoint[0] - firstPoint[0])**2 + (secondPoint[2] - firstPoint[2])**2)
	secondLength = (secondPoint[1]) - (firstPoint[1] + 1.6)
	if (firstLength == 0):
		if (secondLength > 0):
			return -90.0
		return 90.0
	angle = np.degrees(np.arctan(secondLength/firstLength))
	angle *= -1
	preciseAngle = Decimal(str(angle))
	roundedAngle = round(preciseAngle, 1)
	if (display):
		print(roundedAngle)
	return float(roundedAngle)

def proximity(destination, radius = 16.0, abort = 10000.0):
	currentPosition = getPosition()
	r2 = (destination[0]-currentPosition[0])**2 + (destination[1]-currentPosition[1])**2 + (destination[2]-currentPosition[2])**2
	if (r2 < radius):
		return True
	if (r2 > abort):
		print("Mission Aborted")
		py.press('t')
		py.hotkey('alt', 'tab')
		exit()
	return False

def jump():
	currentPosition = getPosition()
	visualCoords = getVisual()
	if (visualCoords != [] and visualCoords[1] >= int(currentPosition[1])):
		py.keyDown('space')
		py.keyUp('space')

def courseCorrection(destination = [0.0, 0.0, 0.0], targetDirection = 360.0):
	currentDirection = getDirection()
	if (destination != [0.0, 0.0, 0.0]):
		currentPosition = getPosition()
		targetDirection = calculateDirection(currentPosition, destination)
	elif (targetDirection > 180.0):
		targetDirection -= 360.0
	angle = currentDirection[0]
	if (angle != targetDirection):
		offset = 0.0
		firstOption = angle - targetDirection
		clockwise = False
		if (firstOption < 0):
			clockwise = True
			firstOption *= - 1
		secondOption = 360 - firstOption
		if (firstOption < secondOption):
			if (clockwise):
				offset = firstOption
			else:
				offset = -firstOption
		else:
			if (clockwise):
				offset = -secondOption
			else:
				offset = secondOption
		offset *= 20
		offset /= 9
		turn(offset)

def visualRotation(destination = [0.0, 0.0, 0.0], targetAngle = 39.0):
	currentDirection = getDirection()
	if (destination != [0.0, 0.0, 0.0]):
		currentPosition = getPosition()
		targetAngle = calculateRotation(currentPosition, destination)
	angle = currentDirection[1]
	if (angle != targetAngle):
		offset = targetAngle - angle
		offset *= 20
		offset /= 9
		rotate(offset)
		
def startMove():
	py.keyDown('w')
	py.press('1')

def stopMove():
	py.keyUp('w')
	py.press('2')

def main():
	try:
		py.hotkey('alt', 'tab')
		time.sleep(1)
		py.press('enter')

		speed = True
		while (True):
			if (speed):
				visualRotation(targetAngle = 90.0)
				py.press('1')
				for i in range(3):
					time.sleep(0.5)
					py.click()
				time.sleep(1.5)
				py.press('2')
				speed = False
			else:
				speed = True

			for i in range(len(pointOfInterest)):
				checkpoint = pointOfInterest[i].coordinates
				courseCorrection(checkpoint)
				visualRotation()
				startMove()
				while(not proximity(checkpoint)):
					courseCorrection(checkpoint)
					jump()
				stopMove()
				if (pointOfInterest[i].farmable):
					courseCorrection(checkpoint)
					visualRotation(checkpoint)
					farm(True, 5)
	except KeyboardInterrupt:
		print("Mission Aborted")

main()
#getVisual(node = True)