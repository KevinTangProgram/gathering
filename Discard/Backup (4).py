import matplotlib.image as mpimg
from decimal import Decimal
import pyautogui as py
import numpy as np
import maskpass
import hashlib
import math
import time
import cv2
import os

profession = "Fishing"
speedBomb = False
walkOrRun = 1
farmTime = 7.0
leftClick = True
shields = False

sprintSpeed = 9.375
walkSpeed = 7.90
sneakSpeed = 2.37
swimSpeed = 2.442
sensitivity = 20.0/9.0
pointOfInterest = []

class Node:
	def __init__(self, coordinates, guidance = False, farmable = True, tickskipping = False, radius = 16.0, delay = 0.0):
		self.coordinates = coordinates
		self.farmable = farmable
		self.guidance = guidance
		self.delay = delay
		self.tickskipping = tickskipping
		self.radius = radius
		pointOfInterest.append(self)

if (profession == "Woodcutting"):
	Node([767.5, 96.5, -4652.5], guidance = True, radius = 9.0)
	Node([758.5, 94.5, -4655.5], guidance = True, delay = 0.5)
	Node([762.5, 98.5, -4647.5], guidance = True)
	Node([766.5, 102.5, -4638.5], guidance = True)
	Node([764.5, 105.5, -4628.5], guidance = True)
	Node([757.5, 106.5, -4624.5], guidance = True)
	Node([759.0, 105.0, -4626.0], guidance = True, farmable = False)
	Node([764.5, 104.5, -4624.5], farmable = False)
	Node([767.5, 104.5, -4616.5], radius = 4.0)
	Node([780.5, 100.5, -4639.5], guidance = True, delay = 0.5)
	#Node([776.5, 101.0, -4640.5], guidance = True)
elif (profession == "Mining"):
	Node([13697.5, 117.0, -3928.0], guidance = True, farmable = False, radius = 2.0)
	Node([13695.5, 119.0, -3928.5], tickskipping = True)
	Node([13699.5, 118, -3928.5])
	Node([13710.0, 115.0, -3947.0], farmable = False, radius = 1.0)
	Node([13707.5, 116.5, -3947.5], tickskipping = True)
	Node([13712.5, 115.5, -3946.5])
	Node([13714.5, 118.0, -3957.5], farmable = False, radius = 1.0)
	Node([13704.5, 115.0, -3960.5], farmable = False, radius = 1.0)
	Node([13703.5, 115.5, -3962.5], tickskipping = True)
	Node([13705.5, 115.5, -3958.5])
	Node([13704.0, 115.0, -3950.0], farmable = False, radius = 1.0)
	Node([13706.5, 116.5, -3949.5])
	Node([13701.5, 115.0, -3937.5], guidance = False, farmable = False, radius = 1.0)
	Node([13700.5, 115.5, -3935.5])
	Node([-170.0, -1.0, 50.0], farmable = True)
	#Node([13697.5, 123.0, -3923.5], guidance = True, farmable = False, radius = 1.0)
	#Node([13697.5, 127.0, -3922.5], tickskipping = True)
	#Node([13695.5, 123.5, -3923.5])
	#Node([13693.5, 115.0, -3958.5], farmable = False, radius = 2.0)
	#Node([13677.5, 116.0, -3963.5], guidance = True, farmable = False, radius = 2.0)
	#Node([13678.5, 115.5, -3963.5], tickskipping = True)
	#Node([13676.5, 116.5, -3965.5])
	#Node([13679.5, 115.0, -3954.5], guidance = True, farmable = False, radius = 1.0)
	#Node([13677.5, 117.0, -3955.5], guidance = True, farmable = False, radius = 0.25)
	#Node([13676.5, 115.5, -3954.5], tickskipping = True)
	#Node([13678.5, 115.5, -3955.5])
elif (profession == "Fishing"):
	Node([754.5, 134.4, -4369.0], farmable = False, radius = 1.0)
	Node([754.0, 135.0, -4372.0], tickskipping = True)
	Node([756.0, 135.0, -4367.0])
	Node([766.0, 134.4, -4367.0], guidance = True, radius = 1.0)
	Node([767.5, 134.4, -4354.0], farmable = False, radius = 1.0)
	Node([764.0, 135.0, -4356.0], tickskipping = True)
	Node([772.0, 135.0, -4353.0])
	Node([778.5, 134.4, -4358.5], farmable = False, radius = 1.0)
	Node([778.0, 135.0, -4355.0], tickskipping = True)
	Node([781.0, 135.0, -4356.0], tickskipping = True)
	Node([782.0, 135.0, -4359.0],)
	Node([783.5, 134.4, -4366.0], farmable = False, radius = 1.0)
	Node([785.0, 135.0, -4367.0])
	Node([777.0, 134.4, -4373.0], farmable = False, radius = 1.0)
	Node([778.0, 135.0, -4374.0])
	Node([770.0, 134.4, -4375.5], farmable = False, radius = 1.0)
	Node([768.0, 135.0, -4376.0])
elif (profession == "Farming"):
	Node([1340.5, 116.5, -4807.5], delay = 0.5)
	Node([1336.5, 115.0, -4801.0], farmable = False, radius = 1.0)
	Node([1338.5, 116.5, -4800.5], tickskipping = True)
	Node([1334.5, 116.5, -4801.5])
	Node([1331.0, 114.9375, -4807.5], farmable = False, radius = 1.0)
	Node([1329.5, 116.5, -4809.5], tickskipping = True)
	Node([1332.5, 116.5, -4805.5])
	Node([1325.5, 114.9375, -4807.5], farmable = False, radius = 1.0)
	Node([1324.5, 116.5, -4809.5], tickskipping = True)
	Node([1327.5, 116.5, -4808.5], tickskipping = True)
	Node([1326.5, 116.5, -4805.5])
	Node([1323.5, 115.5, -4802.5], farmable = False, radius = 1.0)
	Node([1324.5, 117.5, -4800.5], tickskipping = True)
	Node([1325.5, 116.5, -4801.5])

def password():
	while (True):
		os.system('cls')
		print("Wynncraft's Automated Resource Collector\n")
		password = maskpass.advpass(prompt="Enter the password: ", mask="\u00B7") + "sniperjake1994"
		if (hashlib.sha256(password.encode('utf-8')).hexdigest() == "9fd768728cff0070570900e65a0355a725fb7762fd8522deb094050130e164c5"):
			break
		else:
			os.system('cls')
			maskpass.askpass(prompt="Wynncraft's Automated Resource Collector\n\nPress enter to try again.", mask="")

	os.system('cls')
	key = maskpass.askpass(prompt="Wynncraft's Automated Resource Collector\n\nAuthentication Successful\n\nPress enter to begin the program.", mask="") + "Adamastor"

	if (hashlib.sha256(key.encode('utf-8')).hexdigest() == "5581a0b43e297785b843b22fed421ec6bda040d53da21c5577a60a84280b5cbd"):
		maskpass.askpass(prompt="\n\n\nThis program was written by Titan.\n\n\nPress enter to close the program.", mask="")
		exit()

def startup():
	py.hotkey('alt', 'tab')
	time.sleep(1)
	py.press('e')
	py.click(x=960, y=315)
	py.press('enter')

def giveSpeed(targetPitch = 90.0, targetYaw = -360):
	changeRotation(targetPitch = targetPitch, targetYaw = targetYaw)
	py.press('1')
	for i in range(3):
		time.sleep(0.5)
		py.click()
	time.sleep(1.5)
	py.press('2')

def startMove(sneakWalkSprint = 3, walkingStick = False):
	if (sneakWalkSprint == 1):
		py.keyDown('ctrlleft')
	if (sneakWalkSprint == 2):
		py.keyDown('shift')
	if (sneakWalkSprint < 3):
		py.keyDown('w')
	if (walkingStick):
		py.press('1')
	if (shields):
		py.click()
		time.sleep(0.05)
		py.click()
		time.sleep(0.05)
		py.rightClick()

def stopMove(sneakWalkSprint = 3, walkingStick = False):
	if (sneakWalkSprint < 3):
		py.keyUp('w')
	if (sneakWalkSprint == 1):
		py.keyUp('ctrlleft')
	if (sneakWalkSprint == 2):
		py.keyUp('shift')
	if (walkingStick):
		py.press('2')

def rotate(yaw = 0.0, pitch = 0.0, delay = 0.3):
	yaw *= sensitivity
	pitch *= sensitivity
	py.drag(yaw, pitch, delay, button = 'middle')

def farm(left = True, delay = 7):
	if (left):
		py.click()
	else:
		py.rightClick()
	if (speedBomb):
		time.sleep(delay/2.0)
	else:
		time.sleep(delay)

def getPosition(display=False, moving = 3, firstRun = True):
	try:
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
	except:
		if (not firstRun):
			if (profession == "Fishing"):
				py.keyUp('space')
			stopMove(moving)
			time.sleep(0.5)
			py.hotkey('alt', 'tab')
			maskpass.askpass(prompt="\nFailed to receive position coordinates. Press enter to resume the program.", mask="")
			startup()
			giveSpeed()
			startMove(moving)
			if (profession == "Fishing"):
				py.keyDown('space')
			return getPosition(moving = moving)
		else:
			return getPosition(moving = moving, firstRun = False)

def getDirection(display=False, moving = 3, firstRun = True):
	try:
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
				coords.append(float(number))
				number = ""
			else:
				number += i
		coords.append(float(number))

		if (display):
			print(coords)
		return coords
	except:
		if (not firstRun):
			if (profession == "Fishing"):
				py.keyUp('space')
			stopMove(moving)
			time.sleep(0.5)
			py.hotkey('alt', 'tab')
			maskpass.askpass(prompt="\nFailed to receive direction angles. Press enter to resume the program.", mask="")
			startup()
			giveSpeed()
			startMove(moving)
			if (profession == "Fishing"):
				py.keyDown('space')
			return getDirection(moving = moving)
		else:
			return getDirection(moving = moving, firstRun = False)

def getVisual(display = False, node = False, yLevel = 0.5):
	try:
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

		if (keys[0] > 10):
				text += "-"
		for i in range(len(keys)):
			text += dictionary.get(keys[i])
			if (i < len(keys) - 1):
				if (differences[i] > 15 and differences[i] < 25):
					text += " "
				elif (differences[i] > 25):
					text += " -"

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
			coords[1] += yLevel
			coords[2] += 0.5
			print(coords)
		return coords
	except:
		return []

def getHealth(display = False, moving = 3, firstRun = True):
	try:
		screenshot = py.screenshot(region=(700, 886, 220, 16))
		screenshot.save('unprocessedHealth.png')

		coords = mpimg.imread('unprocessedHealth.png')
		red = coords[..., 0]
		green = coords[..., 1]
		blue = coords[..., 2]
		convertToWhite = (red < 0.98)
		coords[convertToWhite] = 1
		convertToBlack = ((green != 1) & (blue != 1))
		coords[convertToBlack] = 0
		mpimg.imsave('processedHealth.png', coords)

		img_rgb = cv2.imread('processedHealth.png')
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

		for i in range(len(keys)):
			text += dictionary.get(keys[i])
			if (i < len(keys) - 1):
				if (differences[i] > 15):
					text += " "

		coords = []
		number = ""
		for i in text:
			if (i == ' '):
				coords.append(int(number))
				number = ""
			else:
				number += i
		coords.append(int(number))
		if (display):
			print(coords)
		return coords
	except:
		if (not firstRun):
			if (profession == "Fishing"):
				py.keyUp('space')
			stopMove(moving)
			time.sleep(0.5)
			py.hotkey('alt', 'tab')
			maskpass.askpass(prompt="\nFailed to get vitals. Press enter to resume the program.", mask="")
			startup()
			giveSpeed()
			startMove(moving)
			if (profession == "Fishing"):
				py.keyDown('space')
			return getHealth(moving = moving)
		else:
			py.press('f5')
			currentDirection = getDirection()
			changeRotation(targetPitch = 90)
			py.press('f5')
			currentHealth = getHealth(moving = moving, firstRun = False)
			changeRotation(targetPitch = currentDirection[1])
			py.press('f5')
			return currentHealth

def calculateTheta(firstPoint, secondPoint, display=False):
	dz = secondPoint[2] - firstPoint[2]
	dx = secondPoint[0] - firstPoint[0]
	angle = 90.0
	if (dz > 0):
		angle = np.degrees(np.arctan(dx/dz))
	elif (dx != 0):
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

def calculatePhi(firstPoint, secondPoint, display=False):
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

def calculateSpeed(seconds = 3.0, sprint = False, sneak = False, display=False):
	if (sprint):
		py.keyDown('ctrlleft')
	if (sneak):
		py.keyDown('shift')
	py.keyDown('w')
	firstPoint = getPosition(moving = True)
	time.sleep(seconds)
	secondPoint = getPosition(moving = True)
	py.keyUp('w')
	if (sprint):
		py.keyUp('ctrlleft')
	if (sneak):
		py.keyUp('shift')
	r2 = math.sqrt((secondPoint[0] - firstPoint[0])**2 + (secondPoint[2] - firstPoint[2])**2)
	if (display):
		print(r2/seconds)
	return r2/seconds

def calculateSensitivity(pixels = 100.0, display=False):
	py.drag(0, -1000, 0.3, button = 'middle')
	firstAngle = getDirection()
	py.drag(0, pixels, 0.3, button = 'middle')
	secondAngle = getDirection()
	if (display):
		print(pixels/(secondAngle[1] - firstAngle[1]))
	return pixels/(secondAngle[1] - firstAngle[1])

def changeRotation(destination = [0.0, 0.0, 0.0], targetPitch = -91.0, targetYaw = -360.0, roboticMovement = False, moving = 3):
	currentDirection = getDirection(moving = moving)
	currentPosition = getPosition(moving = moving)
	if (destination != [0.0, 0.0, 0.0]):
		if (targetYaw == -360.0):
			targetYaw = calculateTheta(currentPosition, destination)
		if (targetPitch == -91.0):
			targetPitch = calculatePhi(currentPosition, destination)
	if (targetYaw > 180.0):
		targetYaw -= 360.0
	yawAngle = currentDirection[0]
	pitchAngle = currentDirection[1]
	if (destination == [0.0, 0.0, 0.0]):
		if (targetYaw == -360.0):
			targetYaw = yawAngle
		if (targetPitch == -91.0):
			targetPitch = pitchAngle
	yawOffset = 0.0
	pitchOffset = 0.0
	if (yawAngle != targetYaw):
		yawOffset = targetYaw - yawAngle
		if (yawOffset < -180):
			yawOffset += 360
		elif (yawOffset > 180):
			yawOffset -= 360
	if (pitchAngle != targetPitch):
		pitchOffset = targetPitch - pitchAngle
	if (roboticMovement):
		rotate(yaw = yawOffset)
		rotate(pitch = pitchOffset)
	else:
		rotate(yawOffset, pitchOffset)
	return currentPosition

def proximity(destination, radius = 16.0, abortRadius = 10000.0, moving = 3):	
	currentPosition = getPosition(moving = moving)
	r2 = (destination[0]-currentPosition[0])**2 + (destination[1]-currentPosition[1])**2 + (destination[2]-currentPosition[2])**2
	if (r2 < radius):
		return True
	if (r2 > abortRadius):
		print("Node out of range.")
		abort()
	return False

def jump(moving = 2):
	currentPosition = getPosition(moving = moving)
	visualCoords = getVisual()
	if (visualCoords != [] and visualCoords[1] >= int(currentPosition[1])):
		py.keyDown('space')
		py.keyUp('space')

def abort(temporary = False, moving = 3):
	stopMove(moving)
	print("\nMission Aborted")
	py.press('/')
	time.sleep(0.5)
	py.write('class')
	py.press('enter')
	time.sleep(1)
	if (temporary):
		py.moveTo(850, 410)
		time.sleep(5)
		py.click()
		futureTime = time.time() + 70
		priorHealth = getHealth()[0]
		while(futureTime > time.time()):
			presentHealth = getHealth()[0]
			if (priorHealth > presentHealth):
				abort(True, moving)
				return
			else:
				priorHealth = presentHealth
		giveSpeed()
		startMove(moving)
	else:
		py.hotkey('alt', 'tab')
		exit()

def main():
	password()
	try:
		startup()
		previousPosition = getPosition()
		previousHealth = getHealth()[0]
		patience = 0
		movementSpeed = True
		while (True):
			if (movementSpeed):
				giveSpeed()
				movementSpeed = False
			elif (profession != "Mining"):
				movementSpeed = True

			if (profession == "Fishing"):
				py.keyDown('space')
			for i in range(len(pointOfInterest)):
				checkpoint = pointOfInterest[i].coordinates
				if (shields):
					startMove(walkingStick = True)
				if (checkpoint[1] == -1.0):
					giveSpeed(checkpoint[2], checkpoint[0])
				elif (i == 0 or not pointOfInterest[i].tickskipping and i != 0 and not pointOfInterest[i - 1].tickskipping):
					if (not pointOfInterest[i].guidance):
						while(not proximity(checkpoint)):
							currentHealth = getHealth()
							if (previousHealth > currentHealth[0]):
								abort(True)
								previousHealth = getHealth()
							else:
								previousHealth = currentHealth[0]
							changeRotation(checkpoint)
							starting = getPosition()
							distance = math.sqrt((checkpoint[0] - starting[0])**2 + (checkpoint[2] - starting[2])**2)
							seconds = 0.0
							if (profession == "Fishing"):
								seconds = distance / swimSpeed
							elif(walkOrRun == 0):
								seconds = distance / walkSpeed
							else:
								seconds = distance / sprintSpeed
							startMove(walkOrRun)
							time.sleep(seconds)
							stopMove(walkOrRun)
						while(profession != "Fishing " and not proximity(checkpoint, radius = pointOfInterest[i].radius)):
							currentHealth = getHealth()
							if (previousHealth > currentHealth[0]):
								abort(True)
								previousHealth = getHealth()
							else:
								previousHealth = currentHealth[0]
							changeRotation(checkpoint)
							starting = getPosition()
							distance = math.sqrt((checkpoint[0] - starting[0])**2 + (checkpoint[2] - starting[2])**2)
							seconds = distance / sneakSpeed
							startMove(2)
							time.sleep(seconds)
							stopMove(2)
					else:
						changeRotation(checkpoint, 39.0)
						startMove(walkOrRun)
						while(not proximity(checkpoint, moving = walkOrRun)):
							currentHealth = getHealth(moving = walkOrRun)
							if (previousHealth > currentHealth[0]):
								abort(True, walkOrRun)
								previousHealth = getHealth()
							else:
								previousHealth = currentHealth[0]
							currentPosition = changeRotation(checkpoint, 39.0, moving = walkOrRun)
							if (profession != "Fishing"):
								jump(walkOrRun)
							if (currentPosition[0] == previousPosition[0] and currentPosition[2] == previousPosition[2]):
								patience += 1
							else:
								patience = 0
							previousPosition = currentPosition
							if (patience > 9):
								abort(moving = walkOrRun)
						stopMove(walkOrRun)
						startMove(2)
						while(profession != "Fishing" and not proximity(checkpoint, radius = pointOfInterest[i].radius, moving = 2)):
							currentHealth = getHealth(moving = 2)
							if (previousHealth > currentHealth[0]):
								abort(True, 2)
								previousHealth = getHealth()
							else:
								previousHealth = currentHealth[0]
							currentPosition = changeRotation(checkpoint, 39.0, moving = 2)
							if (profession != "Fishing"):
								jump()
							if (currentPosition[0] == previousPosition[0] and currentPosition[2] == previousPosition[2]):
								patience += 1
							else:
								patience = 0
							previousPosition = currentPosition
							if (patience > 9):
								if (profession == "Mining"):
									stopMove(2)
									changeRotation(targetYaw = 180.0)
									startMove(0)
									time.sleep(0.5)
									stopMove(0)
									time.sleep(0.1)
									startMove(2)
								else:
									abort(walkOrRun)
						stopMove(2)
				if (shields):
					stopMove(walkingStick = True)
				if (pointOfInterest[i].farmable):
					changeRotation(checkpoint)
					time.sleep(pointOfInterest[i].delay)
					currentHealth = getHealth()
					if (previousHealth > currentHealth[0]):
						abort(True)
						previousHealth = getHealth()
					else:
						previousHealth = currentHealth[0]
					if (pointOfInterest[i].tickskipping or checkpoint[1] == -1):
						farm(leftClick, farmTime - 2)
					else:
						farm(leftClick, farmTime)
					if (checkpoint[1] == -1):
						rotate(36.0, 17.1)
						farm(leftClick, farmTime)
	except KeyboardInterrupt:
		if (profession == "Fishing"):
			py.keyUp('space')
		print("\nMission Aborted")

#startup()
main()
#getVisual(node = True, yLevel = 0.5)
#getPosition(display = True)
#getHealth(True)
"""
py.hotkey('alt', 'tab')
time.sleep(1)
py.press('enter')
calculateSpeed(display = True)
#calculateSensitivity(display = True)
#changeRotation([1324.5, 117.5, -4800.5])
py.keyUp('space')
py.press('t')
py.hotkey('alt', 'tab')
"""