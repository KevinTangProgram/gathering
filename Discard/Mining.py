from cryptography.fernet import Fernet
import matplotlib.image as mpimg
from decimal import Decimal
import pyautogui as py
import numpy as np
import maskpass
import hashlib
import random
import math
import time
import cv2
import os

speedBomb = False
farmTime = 3.5
leftClick = True

sensitivity = 20.0/9.0
pointOfInterest = []
directory = os.getcwd() + '\\Images\\'

class Node:
	def __init__(self, coordinates, guidance = False, farmable = True, tickskipping = False, radius = 16.0, delay = 0.0, rapidClick = False, movement = False):
		self.coordinates = coordinates
		self.farmable = farmable
		self.guidance = guidance
		self.delay = delay
		self.tickskipping = tickskipping
		self.radius = radius
		self.rapidClick = rapidClick
		self.previousTime = 0.0
		self.movement = movement
		pointOfInterest.append(self)


Node([482.5, 95.0, -518.0], farmable = False, guidance = True, radius = 1.0)
Node([483.5, 95.0, -514.5], tickskipping = True)
Node([481.5, 95.5, -515.5], tickskipping = True)
Node([483.5, 94.0, -518.5], delay = 1.0)
Node([476.0, 95.0, -522.0], farmable = False, guidance = True)
Node([474.5, 95.5, -524.5], tickskipping = True)
Node([477.5, 94.5, -523.5])
Node([10.0, -2.0, 126.0], farmable = False)
Node([471.0, 96.0, -531.0], farmable = False, guidance = True, radius = 1.0)
Node([471.5, 95.5, -532.5], tickskipping = True, movement = True)
Node([472.5, 96.5, -530.5])
Node([10.0, -2.0, -167.0], farmable = False)
Node([474.2, 96.0, -545.5], farmable = False, guidance = True, radius = 1.0)
Node([474.1, -3.0, -170.0], farmable = False)
Node([477.5, 95.5, -547.5], tickskipping = True)
Node([475.5, 94.5, -545.5], tickskipping = True)
Node([475.5, 96.5, -548.5], tickskipping = True)
Node([470.5, 98.5, -544.5], tickskipping = True, delay = 1.0)
Node([472.5, 96.5, -543.5], delay = 1.0)
Node([23.0, -1.0, -50.0], farmable = False)
Node([483.5, 91.5, -536.5], guidance = True)
Node([20.0, -2.0, 0.0], farmable = False)
Node([-30.0, -4.0, 0.0], farmable = False)
#Node([-20.0, -2.0, 0.0], farmable = False)
#Node([-70.0, -4.0, 0.0], farmable = False)

def password():
	password = ""
	while (True):
		os.system('cls')
		print("Wynncraft's Automated Resource Collector\n")
		password = maskpass.advpass(prompt="Enter the password: ", mask="\u00B7") + "Adamastor"
		if (hashlib.sha256(password.encode('utf-8')).hexdigest() == "559f1112003dcde49fb59dfee6d839c80344f58131861f22ac9763e9899996fa"):
			break
		else:
			os.system('cls')
			maskpass.askpass(prompt="Wynncraft's Automated Resource Collector\n\nPress enter to try again.", mask="")

	os.system('cls')
	password += "Weathered"
	password = hashlib.sha256(password.encode('utf-8')).hexdigest()
	password = password[:-21] + '='
	fernet = Fernet(password)
	print(fernet.decrypt(b'gAAAAABjGGaQxaEUEWXzYCuPmgYqJrN_rNervKZ7777nRCMkZeI00mf7daE6kem6WW3rvlWylnDzVs74oH1Ums3lh4U5cmBctLzOhf4M8CMAUkxvIkceEssagaIg__itvE4y7VL8KlCi').decode())
	print(fernet.decrypt(b'gAAAAABjGGa7MZ-BfCTy_lQEQJxxPfbFLfvNrJOa4etdPTxUr0ZxocG6qiuCSY1IuyOXbVGwJ9oB7doW0IikfVzDRfvnlKvcXwL5VO4IKkS44eo6GZmXbXw=').decode())
	print(fernet.decrypt(b'gAAAAABjGGSz0wzgZUtaISoUAhj-cVrA8HMyBEmvnS1INexXrFYTBLpo1QVSwIX1sfEMeXsyDdarYVO3v2DIdJqQWhJMoYxBbvxbz3NOi_xdqegahZPdybY=').decode())
	print(fernet.decrypt(b'gAAAAABjGGUKGDVT9jMaHZDI-Nvt3AYrrkGvlPI2Gp7acI3Vks_2qCZjGM0pLRkSnossQdvDIvV3Lhm1aTuvEeDC-bcHd4otkWUUquWaKn_WZWkO01jTngE=').decode())
	print(fernet.decrypt(b'gAAAAABjGGWKxWaZ4D42LVUvgHK3USxlP7nCQwtAPenEvUzPYXMInOM-z1XoHVfDIl-BYc1dyEyx09_XkPHnB3enBfD5Ip-CQDmQg7TsF6Vdpzbhy7IOGm-i0MKOINl5i63HwS160eog').decode())
	print(fernet.decrypt(b'gAAAAABjGGXGPMN2Rba1Y8e7KDkjEaCEr2--sIdK7B1WVLS4fCpbSuBEbGEDg-ny3qHqva5H3gDI41ZhSVlRPr1s3A82h_YmHeJoUg97iBp1qqzKhS5a3MBrHEF1L5h3eIuTJ0QCalBH').decode())
	print(fernet.decrypt(b'gAAAAABjGGY7yTCJJRMzPIRMawDAFRF-evMtC2ne6PmJ-Jf9aOya3GrXNYHY_C3PxWkKTmkB2tDRabKeplN-ATJMfBhS_HEMXVDGjfroMnklNZzgj065PTw=').decode())
	key = maskpass.askpass(prompt="Press enter to begin the program.", mask="") + "Warp"

	if (hashlib.sha256(key.encode('utf-8')).hexdigest() == "39865892e074fb33d5505fe64ab05b695ffeb9f142f7eb84d0c869b4c8779668"):
		key += "Spring"
		key = hashlib.sha256(key.encode('utf-8')).hexdigest()
		key = key[:-21] + '='
		fernet = Fernet(key)
		key = fernet.decrypt(b'gAAAAABi4wdn6UEOXcY9gE-ET_xg-lJhbOSw6YG3SaVSucOOZavoPQfj4pAGLaaYAg4ZvTmHvCis0lCTS4U4_9iTS9Vd2_MKl8cq42W8Un5osJX7jR9LS8VvGNa8GHMNH090SVuU3rL-').decode()
		print(key)
		#print("\n\nPress enter to close the program.", end = "")
		#maskpass.askpass(prompt="", mask="")
		exit()
	print("Program started on", time.ctime(time.time()))

def startup():
	py.hotkey('alt', 'tab')
	time.sleep(1)
	py.press('e')
	py.moveTo(960, 315)
	time.sleep(0.5)
	py.click()
	py.press('backspace', presses = 2)
	py.press('enter')

password()
startup()

def server(keyPress):
	movementStatus = keyPress.copy()
	stopMove(keyPress)
	print("\nKicked out of server", end = "")
	while (True):
		check = py.locateOnScreen(directory + 'heart.png', region=(775, 950, 25, 25))
		try:
			check.left
			py.press('f3')
			time.sleep(5)
			while (True):
				confirm = py.locateOnScreen(directory + 'craftingTable.png', region=(1080, 390, 40, 40))
				try:
					confirm.left
					startMove(movementArray = movementStatus, keyPress = keyPress)
					abort(True, keyPress = keyPress)
					return
				except:
					py.press('1')
					time.sleep(2)
					py.click(clicks = 2, interval = 2)
					time.sleep(30)
		except:
			while (True):
				py.moveTo(1900, 900)
				time.sleep(0.5)
				verify = py.locateOnScreen(directory + 'logo.png', region=(650, 310, 80, 80))
				try:
					verify.left
					break
				except:
					py.moveTo(960, 575)
					time.sleep(0.5)
					py.click()
					time.sleep(5)
			py.moveTo(1040, 1000)
			time.sleep(0.5)
			py.click()
			time.sleep(5)
			py.moveTo(960, 575)
			py.click()
			time.sleep(5)
			py.moveTo(750, 950)
			py.click()
			time.sleep(10)

def lobby(keyPress):
	movementStatus = keyPress.copy()
	stopMove(keyPress)
	print("\nKicked to lobby.", end = "")
	while (True):
		check = py.locateOnScreen(directory + 'craftingTable.png', region=(1080, 390, 40, 40))
		try:
			check.left
			startMove(movementArray = movementStatus, keyPress = keyPress)
			abort(True, keyPress = keyPress)
			return
		except:
			location = py.locateOnScreen(directory + 'book.png', region=(990, 485, 40, 35))
			try:
				location.left
				py.press('e')
			except:
				pass
			py.press('1')
			time.sleep(2)
			py.click(clicks = 2, interval = 2)
			time.sleep(30)
	#case fails if logging in causes crash

def imageProcessor(picture, health = False):
	red = picture[..., 0]
	green = picture[..., 1]
	blue = picture[..., 2]
	if (health):
		convertToWhite = (red < 0.98)
		picture[convertToWhite] = 1
		convertToBlack = ((green != 1) & (blue != 1))
		picture[convertToBlack] = 0
	else:
		convertToBlack = ((red > 0.878) & (red < 0.879) & (green > 0.878) & (green < 0.879) & (blue >= 0.878) & (blue < 0.879))
		picture[convertToBlack] = 0
		convertToWhite = ((red != 0) & (green != 0) & (blue != 0))
		picture[convertToWhite] = 1
	return picture

def numberProcessor(img_rgb):
	img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
	dictionary = {}
	for i in range(11):
		letter = str(i)
		if (i == 10):
			letter = '('
		template = cv2.imread(directory + letter + '.png', 0)
		res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
		threshold = 0.9999
		loc = np.where(res >= threshold)
		lists = loc[1].tolist()
		for j in lists:
			dictionary[j] = letter
	return dictionary

def dictionaryProcessor(dictionary, functionCallNumber):
	keys = sorted(dictionary)
	differences = []
	for i in range(1, len(keys)):
		differences.append(keys[i] - keys[i - 1])
	text = ""
	if (((functionCallNumber == 0 or functionCallNumber == 2) and keys[0] > 10) or (functionCallNumber == 1 and differences[1] > 10)):
		text += "-"
	for i in range(len(keys)):
		if (functionCallNumber != 1 or (dictionary.get(keys[i]) != '(')):
			text += dictionary.get(keys[i])
		if (i < len(keys) - 1 and (functionCallNumber != 1 or i > 0)):
			if ((functionCallNumber < 2 and differences[i] > 35 and differences[i] < 45) or (functionCallNumber > 1 and differences[i] > 15 and (functionCallNumber != 2 or differences[i] < 25))):
				text += " "
			elif ((functionCallNumber < 2 and differences[i] > 46) or (functionCallNumber == 2 and differences[i] > 25)):
				text += " -"
			elif (functionCallNumber < 2 and differences[i] > 14 and differences[i] < 20):
				text += "."
	return text

def textProcessor(text, display = False, functionCallNumber = -1):
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
		if (functionCallNumber == 0):
			print("Position:", end = " ")
		elif (functionCallNumber == 1):
			print("Direction:", end = " ")
		elif (functionCallNumber == 2):
			print("Looking at:", end = " ")
		elif (functionCallNumber == 3):
			print("Health:", end = " ")
		print(coords)
	return coords

def checkVitals(previousHealth = [1, 1], keyPress = [False, False, False, False]):
	currentHealth = getHealth(previousHealth)
	#if (previousHealth[0] > currentHealth[0]):
		#print("\nHealth dropped from ", previousHealth[0], " to ", currentHealth[0], end = ".")
	if (currentHealth[0]/currentHealth[1] < 0.5):
		print("\nHealth dropped to below 50%.")
		abort(keyPress = keyPress)
	return currentHealth

def movementSpell(targetPitch = 90.0, targetYaw = -360, keyPress = [False, False, False, False]):
	py.press('1')
	previousPosition = getPosition(keyPress = keyPress)
	py.click(button = 'right', clicks = 3, interval = 0.1)
	finishTime = time.time() + 30
	while(True):
		currentPosition = getPosition(keyPress = keyPress)
		if (previousPosition == currentPosition):
			py.rightClick()
			if (time.time() > finishTime):
				break
		else:
			break
	previousY = getPosition(keyPress = keyPress)[1]
	currentY = 0.0
	while(True):
		currentY = getPosition(keyPress = keyPress)[1]
		if (currentY == previousY):
			currentY = getPosition(keyPress = keyPress)[1]
			if (currentY == previousY):
				break
		previousY = currentY

def startMove(movementStatus = 0, keyPress = [False, False, False, False], movementArray = [False, False, False, False]):	# 0 = not moving | 1 = walking | 2 = sneaking | 3 = sprinting
	if (movementStatus == 3 or movementArray[0] == True):
		py.keyDown('ctrlleft')
		keyPress[0] = True
	elif (movementStatus == 2 or movementArray[1] == True):
		py.keyDown('shift')
		keyPress[1] = True
	if (movementArray[2] == True):
		py.keyDown('space')
		keyPress[2] = True
	if (movementStatus > 0 or movementArray[3] == True):
		py.keyDown('w')
		keyPress[3] = True

def stopMove(keyPress, swim = False):
	if (keyPress[3] == True):
		py.keyUp('w')
		keyPress[3] = False
	if (keyPress[2] == True and (not swim)):
		py.keyUp('space')
		keyPress[2] = False
	if (keyPress[1] == True):
		py.keyUp('shift')
		keyPress[1] = False
	elif (keyPress[0] == True):
		py.keyUp('ctrlleft')
		keyPress[0] = False

def rotate(yaw = 0.0, pitch = 0.0, delay = 0.3):
	yaw *= sensitivity
	pitch *= sensitivity
	py.drag(yaw, pitch, delay, button = 'middle')

def farm(left = True, delay = 7.0, autoClicker = False, keyPress = [False, False, False, False]):
	py.press('2')
	if (speedBomb):
		delay /= 2.0
	num = random.random()
	if (num < 0.5):
		py.keyDown("shift")
		keyPress[1] = True
	if (autoClicker):
		futureTime = time.time() + delay
		while (futureTime > time.time()):
			if (left):
				py.click()
			else:
				py.rightClick()
			time.sleep(0.5)
	else:
		if (left):
			py.click()
		else:
			py.rightClick()
		time.sleep(delay)
	if (num < 0.5):
		py.keyUp('shift')
		keyPress[1] = False

def getPosition(display=False, keyPress = [False, False, False, False], iterations = 0):
	try:
		#screenshot = py.screenshot(region=(50, 194, 358, 16))			#1.17
		screenshot = py.screenshot(region=(50, 158, 358, 16))			#1.12
		screenshot.save(directory + 'unprocessedCoordinates.png')

		coords = mpimg.imread(directory + 'unprocessedCoordinates.png')
		mpimg.imsave(directory + "processedCoordinates.png", imageProcessor(coords))

		img_rgb = cv2.imread(directory + 'processedCoordinates.png')
		dictionary = numberProcessor(img_rgb)

		text = dictionaryProcessor(dictionary, 0)

		positionCoordinates = textProcessor(text, display, 0)
		return positionCoordinates
	except:
		movementStatus = keyPress.copy()
		if (iterations > 1):
			if (keyPress[2] == True):
				print("\nFailed to receive position coordinates.", end = "")
				abort(False, keyPress)
			else:
				stopMove(keyPress)
				time.sleep(0.5)
				py.hotkey('alt', 'tab')
				print("\nFailed to receive position coordinates on", time.ctime(time.time()), end = ". ")
				maskpass.askpass(prompt="Press enter to resume the program.", mask="")
				startup()
				startMove(movementArray = movementStatus, keyPress = keyPress)
			return getPosition(keyPress = keyPress)
		else:
			if (open(directory + "lobbyImage1.png", "rb").read() == open(directory + "unprocessedCoordinates.png", "rb").read()):
				stopMove(keyPress)
				time.sleep(30)
				screenshot = py.screenshot(region=(50, 158, 358, 16))
				screenshot.save(directory + 'unprocessedCoordinates.png')
				startMove(movementArray = movementStatus, keyPress = keyPress)
				if (open(directory + "lobbyImage3.png", "rb").read() == open(directory + "unprocessedCoordinates.png", "rb").read() or open(directory + "lobbyImage5.png", "rb").read() == open(directory + "unprocessedCoordinates.png", "rb").read()):
					pass
				else:
					lobby(keyPress)
					return getPosition(keyPress = keyPress)
			if (open(directory + "lobbyImage3.png", "rb").read() == open(directory + "unprocessedCoordinates.png", "rb").read() or open(directory + "lobbyImage5.png", "rb").read() == open(directory + "unprocessedCoordinates.png", "rb").read()):
				server(keyPress)
				return getPosition(keyPress = keyPress)
			return getPosition(keyPress = keyPress, iterations = iterations + 1)

def getDirection(display=False, keyPress = [False, False, False, False], iterations = 0):
	try:
		screenshot = py.screenshot(region=(78, 212, 447, 16))			#1.12
		screenshot.save(directory + 'unprocessedDirection.png')

		direction = mpimg.imread(directory + 'unprocessedDirection.png')
		mpimg.imsave(directory + "processedDirection.png", imageProcessor(direction))

		img_rgb = cv2.imread(directory + 'processedDirection.png')
		dictionary = numberProcessor(img_rgb)

		text = dictionaryProcessor(dictionary, 1)

		return textProcessor(text, display, 1)
	except:
		movementStatus = keyPress.copy()
		if (iterations > 1):
			if (keyPress[2] == True):
				print("\nFailed to receive direction angles.", end = "")
				abort(False, keyPress = keyPress)
			else:
				stopMove(keyPress)
				time.sleep(0.5)
				py.hotkey('alt', 'tab')
				print("\nFailed to receive direction angles on", time.ctime(time.time()), end = ". ")
				maskpass.askpass(prompt="Press enter to resume the program.", mask="")
				startup()
				startMove(movementArray = movementStatus,  keyPress = keyPress)
			return getDirection(keyPress = keyPress)
		else:
			if (open(directory + "lobbyImage2.png", "rb").read() == open(directory + "unprocessedDirection.png", "rb").read()):
				stopMove(keyPress)
				time.sleep(30)
				screenshot = py.screenshot(region=(78, 212, 447, 16))			#1.12
				screenshot.save(directory + 'unprocessedDirection.png')
				startMove(movementArray = movementStatus, keyPress = keyPress)
				if (open(directory + "lobbyImage4.png", "rb").read() == open(directory + "unprocessedDirection.png", "rb").read() or open(directory + "lobbyImage6.png", "rb").read() == open(directory + "unprocessedDirection.png", "rb").read()):
					pass
				else:
					lobby(keyPress)
					return getDirection(keyPress = keyPress)
			if (open(directory + "lobbyImage4.png", "rb").read() == open(directory + "unprocessedDirection.png", "rb").read() or open(directory + "lobbyImage6.png", "rb").read() == open(directory + "unprocessedDirection.png", "rb").read()):
				server(keyPress)
				return getDirection(keyPress = keyPress)
			return getDirection(keyPress = keyPress, iterations = iterations + 1)

def getVisual(display = False, node = False, yLevel = 0.5):
	try:
		screenshot = py.screenshot(region=(116, 284, 175, 16))			#1.12 #164
		screenshot.save(directory + 'unprocessedVisual.png')

		coords = mpimg.imread(directory + 'unprocessedVisual.png')
		mpimg.imsave(directory + "processedVisual.png", imageProcessor(coords))

		img_rgb = cv2.imread(directory + 'processedVisual.png')
		dictionary = numberProcessor(img_rgb)

		text = dictionaryProcessor(dictionary, 2)

		coords = textProcessor(text, display, 2)
		if (node):
			coords[0] += 0.5
			coords[1] += yLevel
			coords[2] += 0.5
			print("Node(", coords, ")")
		return coords
	except:
		return []

def getHealth(previousHealth = [1, 1], iterations = 0, display = False):
	try:
		screenshot = py.screenshot(region=(700, 886, 250, 16))
		screenshot.save(directory + 'unprocessedHealth.png')

		coords = mpimg.imread(directory + 'unprocessedHealth.png')
		mpimg.imsave(directory + 'processedHealth.png', imageProcessor(coords, True))

		img_rgb = cv2.imread(directory + 'processedHealth.png')
		dictionary = numberProcessor(img_rgb)

		text = dictionaryProcessor(dictionary, 3)

		healthArray = textProcessor(text, display, 3)
		healthArray[1]
		return healthArray
	except:
		print("\nFailed to get vitals on", time.ctime(time.time()))
		return previousHealth

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

def changeRotation(destination = [0.0, 0.0, 0.0], targetPitch = -91.0, targetYaw = -360.0, roboticMovement = False, keyPress = [False, False, False, False]):
	currentDirection = getDirection(keyPress = keyPress)
	currentPosition = getPosition(keyPress = keyPress)
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

def proximity(destination, radius = 16.0, abortRadius = 2500.0, keyPress = [False, False, False, False]):	
	currentPosition = getPosition(keyPress = keyPress)
	r2 = (destination[0]-currentPosition[0])**2 + (destination[1]-currentPosition[1])**2 + (destination[2]-currentPosition[2])**2
	if (r2 < radius):
		return True
	if (r2 > abortRadius):
		destination = [295.5, 34.0, 321.5]
		r2 = (destination[0]-currentPosition[0])**2 + (destination[1]-currentPosition[1])**2 + (destination[2]-currentPosition[2])**2
		if (r2 < 10000.0):
			lobby(keyPress)
		else:
			print("Node out of range.")
			abort(False, keyPress)
	return False

def jump(check = True, keyPress = [False, False, False, False]):
	currentPosition = getPosition(keyPress = keyPress)
	visualCoords = getVisual()
	if ((visualCoords != [] and visualCoords[1] >= int(currentPosition[1])) or not check):
		if (keyPress[2] == True):
			keyPress[2] = False
			py.keyUp('space')
		py.keyDown('space')
		py.keyUp('space')

def leap(destination, keyPress = [False, False, False, False]):
	currentPosition = getPosition(keyPress = keyPress)
	distance = math.sqrt((destination[0]-currentPosition[0])**2 + (destination[2]-currentPosition[2])**2)
	jumpAngle = 90.0
	if (distance > 8.75):
		return
	elif (distance > 7.8):
		polynomial = [-0.0035843480, -0.1192294472, 7.7966948006]
		#polynomial = [-0.0001627924, -0.0095179927, -0.2007563758, 6.0709137802]
		polynomial[2] -= distance
		answers = np.roots(polynomial)
		for i in answers:
			if (i > -20.0 and i < 0.0):
				jumpAngle = i
				break
	elif (distance > 3.0):
		polynomial = [0.0000537626, -0.0056456382, -0.1000183618, 7.8237279321]
		#polynomial = [-0.0000112392, -0.0030250284, -0.0913002657, 8.0828211019]
		#polynomial = [-0.0000108678, -0.0028506290, -0.0929670533, 6.7921445423]
		polynomial[3] -= distance
		answers = np.roots(polynomial)
		for i in answers:
			if (i > 0.0 and i < 24.0):
			#if (i > -75.0 and i < -20.0):
				jumpAngle = i
				break
	else:
		polynomial = [0.0000023118, -0.0006601857, 0.0045007334, 3.2527696370]
		#polynomial = [0.0000019194, -0.0005594382, 0.0033288429, 2.8263366120]
		polynomial[3] -= distance
		answers = np.roots(polynomial)
		for i in answers:
			if (i > 10.0 and i < 90.0):
				jumpAngle = i
				break
	directionAngle = calculateTheta(currentPosition, destination)
	changeRotation(targetPitch = jumpAngle, targetYaw = directionAngle, keyPress = keyPress)
	movementSpell(keyPress = keyPress)

def hop():
	py.keyDown('space')
	py.keyUp('space')
	time.sleep(0.05)
	py.keyDown('space')
	time.sleep(0.5)
	py.keyUp('space')
	time.sleep(0.5)

def abort(temporary = False, keyPress = [False, False, False, False], iterations = 0):
	movementStatus = keyPress.copy()
	stopMove(keyPress)
	print("\nMission Aborted on", time.ctime(time.time()))
	py.press('/')
	time.sleep(0.5)
	py.write('class')
	py.press('enter')
	time.sleep(1)
	if (temporary):
		py.moveTo(850, 410)
		time.sleep(5)
		py.click()
		if (movementStatus[2] == True):
			py.keyDown('space')
			keyPress[2] = True
		futureTime = time.time() + 70
		if (speedBomb):
			futureTime -= 30
		time.sleep(1)
		py.press('/')
		time.sleep(0.5)
		py.write('stream')
		py.press('enter')
		priorHealth = getHealth()
		while(futureTime > time.time()):
			presentHealth = getHealth(priorHealth)
			if (priorHealth[0] > presentHealth[0]):
				if (iterations > 3):
					print("Damage taken too many times.", end = "")
					abort(keyPress = keyPress)
				else:
					print("\nHealth dropped from ", priorHealth[0], " to ", presentHealth[0], end = ".")
					startMove(movementArray = movementStatus, keyPress = keyPress)
					abort(True, keyPress = movementStatus, iterations = iterations + 1)
				return
			else:
				priorHealth = presentHealth
		startMove(movementArray = movementStatus, keyPress = keyPress)
		print("Program resumed on", time.ctime(time.time()))
	else:
		py.hotkey('alt', 'tab')
		exit()

def main():
	keyPress = [False, False, False, False]					# 0 = ctrl | 1 = shift | 2 = space | 3 = w
	try:
		previousPosition = getPosition(keyPress = keyPress)
		previousHealth = getHealth()
		patience = 0
		movementChoice = 3
		while (True):
			for i in range(len(pointOfInterest)):
				checkpoint = pointOfInterest[i].coordinates
				if (checkpoint[1] == -1.0):
					changeRotation(targetPitch = checkpoint[0], targetYaw = checkpoint[2])
					movementSpell(keyPress = keyPress)
					py.press('2')
					hop()
				elif (checkpoint[1] == -2.0):
					changeRotation(targetPitch = checkpoint[0], targetYaw = checkpoint[2])
					movementSpell(keyPress = keyPress)
					hop()
				elif (checkpoint[1] == -3.0):
					changeRotation(targetYaw = checkpoint[2])
					currentPosition = getPosition(keyPress = keyPress)
					if (currentPosition[0] < checkpoint[0]):
						startMove(movementStatus = 2, keyPress = keyPress)
					while (currentPosition[0] < checkpoint[0]):
						currentPosition = getPosition(keyPress = keyPress)
					stopMove(keyPress = keyPress)
				elif (checkpoint[1] == -4.0):
					changeRotation(destination = [482.5, 95.0, -518.0], targetPitch = checkpoint[0])
					movementSpell(keyPress = keyPress)
				elif ((i == 0 or not pointOfInterest[i].tickskipping and i != 0 and not pointOfInterest[i - 1].tickskipping)):
					offTarget = False
					if (not proximity(checkpoint, radius = pointOfInterest[i].radius, keyPress = keyPress)):
						leap(checkpoint, keyPress)
					if (not proximity(checkpoint, keyPress = keyPress)):
						changeRotation(checkpoint, 39.0, keyPress = keyPress)
						startMove(movementChoice, keyPress)
						offTarget = True
					while(not proximity(checkpoint, keyPress = keyPress)):
						previousHealth = checkVitals(previousHealth, keyPress = keyPress)
						currentPosition = changeRotation(checkpoint, 39.0, keyPress = keyPress)
						if (keyPress[2] == False):
							jump(keyPress = keyPress)
						if (currentPosition[0] == previousPosition[0] and currentPosition[2] == previousPosition[2]):
							patience += 1
						else:
							patience = 0
						previousPosition = currentPosition
						if (patience > 9):
							print("Character in a trapped condition.", end = "")
							abort(keyPress = keyPress)
					if (offTarget):
						stopMove(keyPress, swim = True)

					slowMovement = 0
					if (not proximity(checkpoint, radius = pointOfInterest[i].radius, keyPress = keyPress)):
						slowMovement = 2
						if (keyPress[2] == True):
							slowMovement = movementChoice
						changeRotation(checkpoint, 39.0, keyPress = keyPress)
						startMove(slowMovement, keyPress)
					currentTime = time.time()
					while(not proximity(checkpoint, radius = pointOfInterest[i].radius, keyPress = keyPress)):
						if (currentTime + 5 < time.time() and keyPress[2] == False):
							jump(False, keyPress = keyPress)
							currentTime = time.time()
						previousHealth = checkVitals(previousHealth, keyPress = keyPress)
						currentPosition = changeRotation(checkpoint, 39.0, keyPress = keyPress)
						if (keyPress[2] == False):
							jump(keyPress = keyPress)
						if (currentPosition[0] == previousPosition[0] and currentPosition[2] == previousPosition[2]):
							patience += 1
						else:
							patience = 0
						previousPosition = currentPosition
						if (patience > 9):
							print("Character in a trapped condition.", end = "")
							abort(keyPress = keyPress)
					if (slowMovement != 0):
						stopMove(keyPress, swim = True)
				if (pointOfInterest[i].farmable):
					changeRotation(checkpoint, keyPress = keyPress)
					if (speedBomb):
						if (time.time() - 30.0 - farmTime/2.0 < pointOfInterest[i].previousTime):
							time.sleep(30.0 + farmTime/2.0 - time.time() + pointOfInterest[i].previousTime)
					else:
						if (time.time() - 60.0 - farmTime < pointOfInterest[i].previousTime):
							time.sleep(60.0 + farmTime - time.time() + pointOfInterest[i].previousTime)
					pointOfInterest[i].previousTime = time.time()
					#if (not speedBomb):
					#	time.sleep(pointOfInterest[i].delay)
					previousHealth = checkVitals(previousHealth, keyPress = keyPress)
					if (pointOfInterest[i].movement):
						py.keyDown('s')
						time.sleep(0.1)
						upcomingTime = time.time() + 10
						while (not proximity([470.3, 96.0, -530.3], radius = 0.0002, keyPress = keyPress)):
							if (time.time() > upcomingTime):
								break
						py.keyUp('s')
						changeRotation(checkpoint, keyPress = keyPress)
					if (pointOfInterest[i].tickskipping):
						farm(leftClick, farmTime - 2, pointOfInterest[i].rapidClick, keyPress = keyPress)
					else:
						farm(leftClick, farmTime, pointOfInterest[i].rapidClick, keyPress = keyPress)
				if (not speedBomb):
					time.sleep(pointOfInterest[i].delay)
	except KeyboardInterrupt:
		stopMove(keyPress)
		print("\nMission Aborted")

#distanceList = []
#directionsList = []
main()
#calculateTheta([484.576, 93.0, -520.435], [482.5, 95.0, -518.0], True)
#getVisual(node = True, yLevel = 0.5)
#getPosition(display = True)
#getDirection(True)
#getVisual(True)
#getHealth(display = True)