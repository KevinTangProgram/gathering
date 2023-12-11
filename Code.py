from cryptography.fernet import Fernet
import matplotlib.image as mpimg
import pydirectinput as pydirect
from decimal import Decimal
import pyautogui as py
import numpy as np
import maskpass
import requests
import hashlib
import random
import math
import time
import json
import cv2
import os

profession = "Mining"
level = 110
character = "Assassin"
blindCheck = False

sprint = True
farmTime = 4.5
leftClick = True
shields = False
waterLevel = 0.0
vitals = True

sprintSpeed = 23.03 #(Assassin slider)		#23.37(Assassin slider)			#22.472(Assassin weathered)		#9.375(Archer)
walkSpeed = 17.978 #(Assassin slider)		#18.0 (Assassin weathered)		#7.90(Archer)
sneakSpeed = 5.393 #(Assassin slider)		#5.188(Assassin weathered)		#2.37(Archer)
swimSpeed = 2.442
sensitivity = 20.0/3.0
pointOfInterest = []
gps = []
admins = ["Salted", "Grian", "Jumla", "Crunkle", "HeyZeer0", "Nepmia"]
managers = ["Naraka00", "Viridian"]
moderators = ["____________birb", "_purplegiraffe_", "Aerrihn", "AmbassadorDazz", "BTK2000", "Chigo_", "ditsario", "Fiery_Mystery", "Ichikaaa", "ItzAzura", "Lysmod", "Julinho", "Magicmakerman", "MigatteNoGokuii", "MilkeeW", "PraetorianWolf", "ShadowShift", "Slime1480"]
directory = os.getcwd() + '\\Images\\'

positionScreenshot = (50, 188, 358, 16)
directionScreenshot = (78, 242, 447, 16)
visualScreenshot = (1680, 224, 238, 16)
streamAndSpeed = (780, 25, 470, 70)
healthScreenshot = (700, 896, 250, 16)
durabilityScreenshot = (150, 925, 20, 20)
eHealthScreenshot = (775, 60, 370, 60)		#unsure

#server and lobby
locateHeart = (775, 950, 25, 25)
locateTable = (1085, 395, 40, 40)
locateLogo = (650, 85, 80, 80)
locatePlainBook = (990, 485, 40, 35)

#fixTool and bank
locatePickaxeh = (830, 700, 40, 35)
locateBackArrow = (1085, 360, 40, 35)
locateBackArrow2 = (1085, 395, 40, 35)
locateCheck = (975, 430, 40, 35)
locateBook = (1060, 1000, 40, 40)
locateConfirm = (1000, 400, 400, 200)
locateBackArrow3 = (1085, 430, 40, 35)
locatePickaxeh2 = (830, 680, 40, 40)
locatePickaxe = (830, 395, 185, 40)
locateScrap = (940, 430, 40, 35)
locateRepair = (1020, 330, 85, 25)
locateBlank = (795, 355, 40, 40)
locateArrow = (1085, 340, 35, 35)
locateBlank2 = (980, 585, 40, 40)

class Node:
	def __init__(self, coordinates, guidance = False, farmable = True, tickskipping = False, radius = 16.0, delay = 0.0, rapidClick = False, rooted = False, movement = False):
		self.coordinates = coordinates
		self.farmable = farmable
		self.guidance = guidance
		self.delay = delay
		self.tickskipping = tickskipping
		self.radius = radius
		self.rapidClick = rapidClick
		self.rooted = rooted
		self.previousTime = 0.0
		self.movement = movement
		if (coordinates[1] > 0):
			pointOfInterest.append(self)
		elif (coordinates[1] == -1 and character == "Archer"):
			pointOfInterest.append(self)
		elif (coordinates[1] <= -2 and coordinates[1] >= -8 and character == "Assassin"):
			pointOfInterest.append(self)

class Waypoint:
	def __init__(self, coordinates, radius = 25.0, horse = True, interact = 0):
		self.coordinates = coordinates
		self.radius = radius
		self.horse = horse
		self.interact = interact
		gps.append(self)

if (profession == "Woodcutting"):
	if (level == 100):
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
	elif (level == 110):
		Node([985.5, 76.0, -606.0], farmable = False, radius = 1.0)
		Node([985.5, 76.5, -607.5])
		Node([982.5, 77.0, -586.5], farmable = False, radius = 1.0)
		Node([979.5, 78.5, -586.5])
		Node([52.5, -1.0, 50.0], farmable = False)
		Node([52.5, -1.0, 50.0], farmable = False)
		Node([1012.0, 79.0, -608.4], guidance = True, farmable = False)
		Node([1017.5, 79.0, -612.5], farmable = False, radius = 1.0)
		Node([1019.5, 79.5, -612.5])
		Node([1020.0, 80.0, -623.0], guidance = True, farmable = False)
		Node([1020.0, 80.0, -634.0], farmable = False, radius = 1.0)
		Node([1021.5, 81.5, -634.5])
		Node([1020.0, 80.0, -623.0], farmable = False)
		Node([1000.0, 75.0, -623.0], farmable = False, radius = 9.0)
		Node([1001.5, 75.5, -624.5])
		Node([1001.0, 77.0, -606.0], guidance = True, farmable = False)
		#Node([999.5, 75.5, -626.5], guidance = True)
		#Node([990.0, 77.0, -601.5], guidance = True, farmable = False)
		#Node([985.5, 76.5, -609.5], guidance = True)
		#Node([978.5, 79.5, -586.5], guidance = True)
		#Node([1022.5, 83.5, -633.5], guidance = True)
		#Node([1021.5, 81.5, -613.5], guidance = True)
		#Node([1000.5, 77.0, -618.5], guidance = True, farmable = False)
elif (profession == "Mining"):
	if (level == 60):
		Node([-1446.5, 48.5, -5374.5], guidance = True)
		Node([-1442.5, 46.5, -5380.5], guidance = True)
		Node([-1447.5, 49.5, -5383.5], guidance = True)
		Node([-1438.5, 49.5, -5382.5], guidance = True)
		Node([-30.0, -1.0, 0.0], farmable = False)
		Node([-1439.5, 50.5, -5373.5], guidance = True)
		Node( [-1437.5, 50.5, -5376.5], guidance = True)
		Node([-1441.5, 48.5, -5372.5], guidance = True, radius = 3.0)
		Node([-1447.0, 49.0, -5379.0], farmable = False, guidance = True)
		Node([-1448.0, 49.5, -5378.0], guidance = True)
		Node([-1443.194, 48.0, -5375.737], guidance = True, farmable = False)
	elif (level == 70):
		#Node([-792.5, 111.0, -5643.5], guidance = True,  farmable = False, radius = 1.0)
		#Node([-795.5, 112.0, -5642.5], tickskipping = True)
		#Node([-793.5, 115.0, -5645.5])
		#Node([-777.5, 114.0, -5653.5], guidance = True)
		#Node([-777.5, 113.0, -5643.5], guidance = True)
		#Node([-762.5, 112.0, -5649.5], guidance = True)
		#Node([-768.0, 110.0, -5642.0], guidance = True, farmable = False, radius = 1.0)
		#Node([-771.5, 113.0, -5641.5], tickskipping = True)
		#Node([-767.5, 114.0, -5638.5])
		#Node([-777.5, 110.0, -5648.5], guidance = True, farmable = False)
		Node( [-789.0, 50.0, -5389.0], guidance = True, farmable = False, radius = 1.0)
		Node( [-788.5, 51.5, -5391.5], movement = False)
		Node( [-791.5, 52.5, -5390.5], rooted = True)
		Node( [-796.0, 50.0, -5389.0], guidance = True, farmable = False, radius = 1.0)
		Node ([10.0, -6.0, 60.0], farmable = False)
		Node( [-802.5, 50.5, -5387.5], rooted = True)
		Node( [-803.5, 51.5, -5385.5], rooted = True)
		Node( [-801.5, 50.0, -5384.5], farmable = False, radius = 1.0, guidance = True)
		Node ([0.0, -7.0, 0.0], farmable = False)
		Node( [-801.5, 54.5, -5377.5], rooted = True)
		Node( [-60.0, -7.0, -65.0], farmable = False)
		Node( [-798.5, 55.5, -5375.5], rooted = True)
		Node( [-797.0, 53.0, -5376.0], farmable = False, guidance = True, radius = 1.0)
		Node ([-30.0, -7.0, -53.0], farmable = False)
		Node( [-791.5, 55.5, -5368.5], rooted = True)
		Node([-792.0, 53.0, -5372.0], farmable = False, guidance = True, radius = 1.0)
		Node([5.0, -7.0, -165.0], farmable = False)
		Node( [-5.0, -6.0, -165.0], farmable = False)
	elif (level == 80):
		Node([14220.0, 62.0, 28059.0], guidance = True, farmable = False, radius = 1.0)
		Node([14220.5, 66.5, 28057.5], rooted = True)
		Node([14217.5, 65.5, 28059.5], rooted = True)
		Node([14223.0, 61.0, 28064.0], guidance = True, farmable = False)
		Node([14225.0, 61.0, 28065.0], guidance = True, farmable = False, radius = 1.0)
		Node([14223.5, 63.5, 28065.5], tickskipping = True)
		Node([14226.5, 64.5, 28066.5], rooted = True)
		Node([14233.0, 61.0, 28064.0], guidance = True, farmable = False, radius = 1.0)
		Node([14235.5, 64.5, 28065.5], rooted = True)
		Node([24.0, -2.0, -85.2], farmable = False)
		Node([14245.0, 60.0, 28065.0], guidance = True, farmable = False, radius = 1.0)
		Node([14245.5, 63.5, 28065.5])
		Node([2.0, -2.0, -130.0], farmable = False)
		Node([14255.5, 61.5, 28052.5], rooted = True)
		Node([14254.0, 62.5, 28054.5], rooted = True)
		Node([2.0, -2.0, 50.0], farmable = False)
		Node([14249.0, 60.0, 28058.0], guidance = True, farmable = False, radius = 1.0)
		#Node([14251.5, 60.0, 28057.0], guidance = True, farmable = False, radius = 1.0)
		#Node([14245.5, 63.5, 28065.5], guidance = True)
		Node([14251.5, 62.5, 28056.5], tickskipping = True, rooted = True)
		Node([14247.5, 63.5, 28056.5], rooted = True)
		Node([8.0, -2.0, 88.0], farmable = False)
		Node([8.0, -2.0, 88.0], farmable = False)
	elif (level == 90):
		Node([14228.0, 61.0, 28057.0], guidance = True, farmable = False, radius = 1.0)
		Node([14226.5, 64.5, 28056.5], rooted = True)
		Node([33.0, -2.0, 60.9], farmable = False)
		Node([14218.5, 65.5, 28063.5], rooted = True)
		Node([45.0, -2.0, -83.7], farmable = False)
		#Node([14228.0, 60.5, 28063.0], guidance = True, farmable = False, radius = 1.0)
		Node([14230.0, 61.0, 28064.0], guidance = True, farmable = False, radius = 1.0)
		Node([14230.5, 62.5, 28066.5], rooted = True)
		Node([20.0, -2.0, -100.0], farmable = False)
		Node([14242.0, 60.0, 28064.0], guidance = True, farmable = False, radius = 1.0)
		Node([14241.5, 63.5, 28066.5], rooted = True)
		Node([14247.0, 60.0, 28064.0], guidance = True, farmable = False, radius = 1.0)
		Node([14249.0, 60.0, 28064.0], guidance = True, farmable = False, radius = 1.0)
		Node([14250.5, 64.5, 28065.5], rooted = True)
		Node([5.0, -2.0, -104.0], farmable = False)
		Node([14267.0, 60.0, 28059.0], guidance = True, farmable = False, radius = 1.0)
		Node([14265.5, 60.5, 28057.5], rooted = True)
		Node([14275.5, 60.0, 28059.0], guidance = True, farmable = False, radius = 1.0)
		Node([14275.5, 64.5, 28056.5], rooted = True)
		Node([20.0, -2.0, -90.0], farmable = False)
		#Node([14283.0, 61.0, 28059.0], guidance = True, farmable = False, radius = 1.0)
		Node([14289.0, 61.0, 28058.0], guidance = True, farmable = False, radius = 1.0)
		Node([14289.5, 64.5, 28055.5], rooted = True)
		Node([14289.0, 61.0, 28064.0], guidance = True, farmable = False, radius = 1.0)
		Node([14290.5, 64.5, 28065.5], tickskipping = True, rooted = True)
		Node([14286.5, 61.5, 28064.5], rooted = True)
		Node([14287.0, 61.0, 28062.0], guidance = True, farmable = False, radius = 1.0)
		Node([14282.0, 61.0, 28066.0], guidance = True, farmable = False, radius = 1.0)
		Node([14281.5, 64.5, 28067.5], rooted = True)
		#Node([17.5, -2.0, 122.5], farmable = False)
		Node([14239.0, 62.0, 28057.0], guidance = True, farmable = False, radius = 1.0)
		Node([14237.5, 66.5, 28054.5], tickskipping = True, rooted = True)
		Node([14236.5, 64.5, 28054.5], rooted = True)
		Node([14230.0, 61.0, 28057.0], guidance = True, farmable = False, radius = 1.0)
	elif (level == 100):
		Node([857.0, 51.0, -4312.0], guidance = True, farmable = False, radius = 1.0)
		Node([855.5, 53.5, -4315.5], tickskipping = True, rooted = True)
		Node([857.5, 51.5, -4314.5], tickskipping = True, rooted = True)
		Node([859.5, 52.5, -4312.5], tickskipping = True, rooted = True)
		Node([858.5, 51.5, -4308.5])
		Node([861.0, 53.0, -4307.0], guidance = True, farmable = False, radius = 1.0)
		Node([860.0, 53.0, -4305.0], guidance = True, farmable = False, radius = 1.0)
		Node([859.0, 53.0, -4303.0], guidance = True, farmable = False, radius = 1.0)
		Node([861.5, 53.5, -4305.5], tickskipping = True, rooted = True)
		Node([858.5, 52.5, -4301.5], tickskipping = True, rooted = True)
		Node([860.0, 54.5, -4298.0])
		Node([856.0, 52.5, -4297.0], guidance = True, farmable = False, radius = 1.0)
		Node([854.0, 52.5, -4297.0], guidance = True, farmable = False, radius = 1.0)
		Node([851.5, 53.5, -4295.5], tickskipping = True, rooted = True)
		Node([853.5, 52.5, -4298.5], tickskipping = True, rooted = True)
		Node([853.0, 55.5, -4300.5])
		Node([854.0, 52.0, -4305.0], guidance = True, farmable = False)
		Node([850.0, 52.0, -4306.0], guidance = True, farmable = False, radius = 1.0)
		Node([847.5, 53.5, -4305.5], tickskipping = True, rooted = True)
		Node([848.5, 51.5, -4307.5])
		Node([855.0, 51.0, -4311.0], guidance = True, farmable = False, radius = 1.0)
		#Node([25.0, -2.0, -168.7], farmable = False)
		"""
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
		Node([13701.5, 115.0, -3938.5], guidance = False, farmable = False, radius = 1.0)
		Node([13700.5, 115.5, -3935.5])
		Node([-165.0, -1.0, 55.0], farmable = False)
		Node([13697.5, 127.0, -3922.5], tickskipping = True, rooted = True)
		Node([13695.5, 123.5, -3923.5], rooted = True)
		"""
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
	elif (level == 110):
		Node([482.5, 95.0, -518.0], farmable = False, guidance = True, radius = 1.0)
		Node([481.5, 95.5, -515.5], tickskipping = True, rooted = True)
		Node([483.5, 95.0, -514.5], tickskipping = True, rooted = True)
		Node([483.5, 94.5, -518.5], rooted = True)
		Node([476.0, 95.0, -522.0], farmable = False, guidance = True)
		#Node([477.0, 95.0, -522.0], farmable = False, guidance = True)
		Node([474.5, 95.5, -524.5], tickskipping = True, rooted = True)
		Node([477.5, 94.5, -523.5], rooted = True)
		Node([10.0, -2.0, 126.0], farmable = False)
		#Node([476.0, 95.0, -524.0], farmable = False, guidance = True)
		#Node([0.0, -7.0, 144.5], farmable = False)
		Node([471.0, 96.0, -531.0], farmable = False, guidance = True, radius = 1.0)
		Node([471.5, 95.5, -532.5], tickskipping = True, movement = True, rooted = True)
		Node([472.5, 96.5, -530.5], rooted = True)
		Node([10.0, -2.0, -167.0], farmable = False)
		Node([474.2, 96.0, -545.5], farmable = False, guidance = True, radius = 1.0)
		Node([474.1, -3.0, -170.0], farmable = False)
		Node([477.5, 95.5, -547.5], tickskipping = True, rooted = True)
		Node([475.5, 96.5, -548.5], tickskipping = True, rooted = True)
		Node([475.5, 94.5, -545.5], tickskipping = True, rooted = True)
		Node([470.5, 98.5, -544.5], tickskipping = True, rooted = True)
		Node([472.5, 96.5, -543.5], rooted = True)
		Node([23.0, -2.0, -50.0], farmable = False)
		Node([483.5, 91.5, -536.5], guidance = True, delay = 0.5)
		Node([20.0, -2.0, 0.0], farmable = False)
		Node([-30.0, -4.0, 0.0], farmable = False)
		#Node([-20.0, -2.0, 0.0], farmable = False)
		#Node([-70.0, -4.0, 0.0], farmable = False)

		#Waypoint([989.5, 73.0, -663.5], radius = 1.0, horse = False)
		#Waypoint([989.5, 74.5, -663.5], horse = False, interact = 1)
		Waypoint([997.0, 73.0, -685.0], radius = 1.0, horse = False)
		Waypoint([998.0, 73.0, -705.0], radius = 1.0, horse = False)
		Waypoint([998.5, 75.0, -711.5], radius = 1.0, horse = False)
		Waypoint([998.5, 76.5, -711.5], horse = False, interact = 1)
		Waypoint([998.0, 73.0, -705.0], radius = 1.0, horse = False)
		Waypoint([997.0, 73.0, -685.0], radius = 1.0, horse = False)
		Waypoint([980.0, 73.0, -686.0], radius = 1.0, horse = False)
		Waypoint([979.5, 74.5, -688.5], horse = False, interact = 2)
		Waypoint([978.0, 73.85, -671.0])
		Waypoint([979.0, 76.85, -602.0])
		Waypoint([1005.0, 81.85, -560.0])
		Waypoint([980.0, 78.85, -512.0])
		Waypoint([897.0, 78.85, -491.0])
		Waypoint([856.0, 76.85, -432.0])
		Waypoint([856.0, 72.85, -383.0])
		Waypoint([807.0, 78.85, -348.0])
		#Waypoint([732.0, 88.85, -357.0])
		Waypoint([716.0, 86.85, -327.0])
		Waypoint([698.0, 90.85, -389.0])
		Waypoint([650.0, 88.85, -482.0])
		Waypoint([548.0, 89.85, -505.0])
		Waypoint([526.0, 88.85, -526.0])
		Waypoint([526.5, 88.0, -525.5], radius = 1.0, horse = False)
		Waypoint([488.5, 93.0, -525.5], horse = False)
		Waypoint([487.0, 93.0, -519.0], radius = 1.0, horse = False)
		Waypoint([-55.3, -1.0, 45.0], horse = False)
		Waypoint([482.5, -2.0, -517.65], horse = False)

		"""
		Node([474.2, 96.0, -545.5], farmable = False, guidance = True, radius = 1.0)
		Node([474.1, -3.0, -165.0], farmable = False)
		Node([477.5, 95.5, -547.5], tickskipping = True)
		Node([475.5, 94.5, -545.5], tickskipping = True)
		Node([475.5, 96.5, -548.5], tickskipping = True)
		Node([470.5, 98.5, -544.5], tickskipping = True)
		Node([472.5, 96.5, -543.5], delay = 0.0)
		Node([17.0, -2.0, 15.0], farmable = False) #12.7
		Node([471.0, 96.0, -531.0], farmable = False, guidance = True, radius = 1.0)
		Node([471.5, 95.5, -532.5], tickskipping = True)
		Node([472.5, 96.5, -530.5])
		#Node([67.5, -2.0, -63.4], farmable = False)
		Node([45.0, -2.0, -38.7], farmable = False)
		#Node([475.0, 95.0, -526.0], farmable = False, guidance = True, radius = 1.0)
		Node([476.0, 95.0, -524.0], farmable = False, guidance = True, radius = 1.0)
		Node([477.0, 95.0, -522.0], farmable = False, guidance = True, radius = 1.0)
		Node([474.5, 95.5, -524.5], tickskipping = True)
		Node([477.5, 94.5, -523.5])
		#Node([482.5, 95.0, -516.5], farmable = False, guidance = True, radius = 1.0)
		#Node([484.0, 95.0, -516.0], farmable = False, guidance = True, radius = 1.0)
		Node([483.0, 95.0, -517.0], farmable = False, guidance = True, radius = 1.0)
		Node([483.5, 94.5, -514.5], tickskipping = True)
		Node([481.5, 95.5, -515.5], tickskipping = True)
		Node([483.5, 93.5, -518.5], delay = 0.0)
		Node([10.0, -2.0, 163.1], farmable = False)
		Node([10.0, -2.0, 163.1], farmable = False)
		"""
		"""
		Node([478.5, 94.0, -540.5], farmable = False, radius = 1.0)
		Node([476.5, 94.5, -538.5], tickskipping = True)
		Node([477.5, 94.5, -542.5])
		Node([-85.0, -1.0, 50.0], farmable = False)
		Node([471.0, 97.0, -542.0], guidance = True, farmable = False, radius = 1.0)
		Node([470.5, 98.5, -544.5], tickskipping = True)
		Node([472.5, 97.0, -543.5])
		Node([468.0, 99.0,-537.0], guidance = True, farmable = False, radius = 1.0)
		Node([466.0, 101.0, -534.5])
		Node([473.5, 95.0, -532.5], farmable = False, radius = 2.0)
		#Node([471.0, 96.0, -531.0], farmable = False, radius = 1.0)
		Node([472.5, 96.5, -530.5], tickskipping = True)
		Node([471.5, 95.5, -532.5])
		Node([477.0, 94.0, -535.0], farmable = False)
		Node([161.0, -1.0, 39.0], farmable = False)
		#Node([473.0, 95.0, -534.0], farmable = False)
		#Node([480.0, 93.0, -533.0], farmable = False)
		#Node([168.0, -1.0, 45.0], farmable = False)
		#Node([149.0, -1.0, 39.0], farmable = False)
		#Node([140.0, -1.0, 39.0], farmable = False)
		Node([484.0, 95.0, -516.0], guidance = True, farmable = False, radius = 1.0)
		Node([483.5, 94.0, -518.5], tickskipping = True)
		Node([481.5, 95.5, -515.5], tickskipping = True)
		Node([483.5, 95.0, -514.5], delay = 0.5)
		Node([-13.0, -1.0, 10.0], farmable = False)
		"""
		#[148.2, -1.0, 42.3]
elif (profession == "Fishing"):
	if (level == 70):
		Node([-199.5, 27.5, -5214.5], guidance = True, rapidClick = True)
		Node([-203.5, 27.5, -5202.5], guidance = True, rapidClick = True)
		Node([-206.5, 27.5, -5196.5], guidance = True, rapidClick = True)
		Node([-206.5, 27.5, -5189.5], guidance = True, rapidClick = True)
		Node([-206.5, 27.5, -5183.5], guidance = True, rapidClick = True)
		Node([-206.5, 27.5, -5177.5], guidance = True, rapidClick = True)
		Node([-203.5, 27.5, -5172.5], guidance = True, rapidClick = True)
		#Node([-196.0, 26.4, -5173.5], guidance = True, farmable = False, radius = 1.0)
		#Node([-194.5, 27.5, -5171.5], tickskipping = True)
		#Node([-197.5, 27.5, -5175.5])
	elif (level == 80):
		Node([-1872.0, 33.4, -2189.0], guidance = True, farmable = False, radius = 1.0)
		Node([-1869.5, 34.0, -2187.5], tickskipping = True)
		Node([-1870.5, 34.0, -2190.5], rapidClick = True)
		Node([-1872.0, 33.4, -2181.0], guidance = True, farmable = False, radius = 1.0)
		Node([-1871.5, 34.0, -2178.5], tickskipping = True)
		Node([-1870.5, 34.0, -2182.5])
		Node([-1871.0, 33.4, -2172.0], guidance = True, farmable = False, radius = 1.0)
		#Node([-1870.0, 33.4, -2167.0], guidance = True, farmable = False, radius = 1.0)
		Node([-1869.5, 34.0, -2169.5], tickskipping = True)
		Node([-1871.5, 34.0, -2174.5])
		Node( [-1870.0, 33.4, -2164.0], guidance = True, farmable = False, radius = 1.0)
		Node([-1868.5, 34.0, -2165.5])
		Node( [-1866.0, 33.4, -2160.0], guidance = True, farmable = False, radius = 1.0)
		Node([-1863.5, 34.0, -2160.5], tickskipping = True)
		Node([-1866.5, 34.0, -2162.5])
	elif (level == 90):
		Node([14266.0, 63.0, 28007.0], farmable = False, radius = 1.0)
		#Node([14266.7, 63.0, 28006.3], farmable = False, radius = 1.0)
		Node([14263.5, 63.0, 28004.5], tickskipping = True)
		Node([14262.5, 63.0, 28006.5])
		Node([14266.0, 63.0, 28009.0], farmable = False, radius = 1.0)
		Node([14264.0, 63.0, 28010.0], farmable = False, radius = 1.0)
		Node([14261.5, 63.0, 28008.5], tickskipping = True)
		Node([14260.5, 63.0, 28011.5])
		#Node([14262.0, 63.0, 28018.0], farmable = False, radius = 1.0)
		Node([14261.0, 63.0, 28016.0], farmable = False, radius = 1.0)
		Node([14258.5, 63.0, 28017.0], tickskipping = True)
		Node([14259.5, 63.0, 28014.5])
		#Node([14258.0, 63.0, 28018.0] , farmable = False, radius = 1.0)
		#Node([14254.0, 63.0, 28020.0], farmable = False, radius = 1.0)
		#Node([14255.5, 63.0, 28018.0], farmable = False, radius = 1.0)
		Node([14254.0, 63.0, 28020.0], farmable = False, radius = 1.0)
		Node([14254.5, 63.0, 28016.5], tickskipping = True)
		Node([14251.5, 63.0, 28017.5])
		Node([14255.0, 63.0, 28012.0], farmable = False, radius = 1.0)
		Node([14251.5, 63.0, 28011.0], tickskipping = True)
		Node([14255.5, 63.0, 28009.5])
		Node([14263.0, 63.0, 28011.5], farmable = False, radius = 1.0)
		Node([14265.0, 63.0, 28009.5], farmable = False, radius = 1.0)
	elif (level == 100):
		#Node([753.5, 134.4, -4368.5], farmable = False, radius = 1.0)
		#Node([753.5, 135.0, -4371.5], tickskipping = True)
		#Node([755.5, 135.0, -4366.5])
		#Node([100.0, -1.0, 70.0], farmable = False)
		#Node([765.5, 134.4, -4366.5], radius = 1.0)
		#Node([65.0, -1.0, 70.0], farmable = False)
		#Node([777.0, 134.4, -4373.0], farmable = False, radius = 1.0)
		#Node([777.5, 135.0, -4373.5])
		#Node([175.0, -1.0, 65.0], farmable = False)
		#Node([778.0, 134.4, -4358.0], farmable = False, radius = 1.0)
		#Node([777.5, 135.0, -4354.5], tickskipping = True, rapidClick = True)
		#Node([780.5, 135.0, -4355.5], tickskipping = True, rapidClick = True)
		#Node([781.5, 135.0, -4358.5], rapidClick = True)
		#Node([-110.0, -1.0, 70.0], farmable = False)
		#Node([767.5, 134.4, -4354.0], farmable = False, radius = 1.0)
		#Node([763.5, 135.0, -4355.5], tickskipping = True,  rapidClick = True)
		#Node([771.5, 135.0, -4352.5], rapidClick = True)
		#Node([-40.0, -1.0, 50.0], farmable = False)
		Node([1437.0, 126.0, -4576.0], guidance = True, farmable = False, radius = 1.0)
		Node([1439.0, 126.0, -4575.0], guidance = True, farmable = False, radius = 1.0)
		Node([1439.5, 126.0, -4572.0], tickskipping = True)
		Node([1441.0, 126.0, -4573.0], tickskipping = True)
		Node([1442.0, 126.0, -4575.5], tickskipping = True)
		Node([1440.0, 126.0, -4578.5], delay = 0.5)
		Node([1433.0, 126.0, -4581.0], guidance = True, farmable = False, radius = 1.0)
		Node([1434.0, 126.0, -4583.0], guidance = True, farmable = False, radius = 1.0)
		Node([1437.5, 126.0, -4582.0], tickskipping = True)
		Node([1435.0, 126.0, -4584.0], tickskipping = True)
		Node([1433.0, 126.0, -4585.0], tickskipping = True)
		Node([1430.5, 126.0, -4583.5], delay = 0.5)
		Node([1427.5, 126.0, -4577.5], guidance = True, farmable = False, radius = 1.0)
		#Node([1429.0, 126.0, -4580.0], guidance = True, farmable = False, radius = 1.0)
		Node([1426.5, 126.0, -4579.5], guidance = True, farmable = False, radius = 1.0)
		Node([1426.5, 126.0, -4582.5], tickskipping = True)
		Node([1424.0, 126.0, -4581.0], tickskipping = True)
		Node([1424.0, 126.0, -4579.0], tickskipping = True)
		Node([1424.5, 126.0, -4576.5], delay = 0.5)
		Node([1432.0, 126.0, -4573.0], guidance = True, farmable = False, radius = 1.0)
		Node([1430.0, 126.0, -4572.0], guidance = True, farmable = False, radius = 1.0)
		Node([1426.5, 126.0, -4573.0], tickskipping = True)
		Node([1427.0, 126.0, -4570.5], tickskipping = True)
		Node([1428.0, 126.0, -4569.0], tickskipping = True)
		Node([1430.0, 126.0, -4568.5], delay = 0.5)
		#Node([1425.0, 126.0, -4579.0], guidance = True, farmable = False, radius = 1.0)
	elif (level == 110):
		Node([778.0, 148.0, -985.0], guidance = True, farmable = False, radius = 1.0)
		Node([775.0, 148.0, -985.0], tickskipping = True)
		Node([776.0, 148.0, -987.0], tickskipping = True)
		Node([778.5, 148.0, -988.5], tickskipping = True)
		Node([781.0, 148.0, -986.0], tickskipping = True, delay = 1.0)
		Node([781.0, 148.0, -984.0], delay = 1.0)
		Node([5.0, -2.0, 7.6], farmable = False)
		Node([776.0, 149.0, -970.0], guidance = True, farmable = False, radius = 1.0)
		Node([779.0, 149.0, -970.0], tickskipping = True)
		Node([776.0, 149.0, -967.0], tickskipping = True)
		Node([773.0, 149.0, -969.0], tickskipping = True)
		Node([772.5, 149.0, -971.0], delay = 1.5)
		Node([7.0, -2.0, -172.6], farmable = False)
		#Node([779.0, 148.0, -993.0], guidance = True, farmable = False, radius = 1.0)
		Node([774.0, 148.0, -991.0], guidance = True, farmable = False, radius = 1.0)
		Node([772.0, 148.0, -992.0], tickskipping = True)
		Node([775.0, 148.0, -994.0])
		Node([780.0, 148.0, -992.0], guidance = True, farmable = False, radius = 1.0, delay = 3.0)
		Node([779.0, 148.0, -995.0], tickskipping = True)
		Node([782.5, 148.0, -993.0])

		Waypoint([989.5, 73.0, -663.5], radius = 1.0, horse = False)
		Waypoint([989.5, 74.5, -663.5], horse = False, interact = 1)
		Waypoint([980.0, 73.0, -686.0], radius = 1.0, horse = False)
		Waypoint([979.5, 74.5, -688.5], horse = False, interact = 2)
		Waypoint([968.0, 73.0, -690.0], radius = 1.0, horse = False)
		Waypoint([969.0, 73.0, -701.0], radius = 1.0, horse = False)
		Waypoint([982.5, 73.0, -721.0], radius = 1.0, horse = False)
		Waypoint([979.0, 76.85, -737.0])
		Waypoint([982.0, 76.85, -770.5])
		Waypoint([951.0, 72.85, -815.0])
		Waypoint([953.5, 70.85, -855.5])
		Waypoint([933.0, 76.85, -866.0])
		Waypoint([917.5, 84.85, -869.5])
		Waypoint([905.0, 89.85, -883.0])
		Waypoint([890.5, 93.85, -883.5])
		Waypoint([886.0, 96.85, -907.0])
		Waypoint([879.5, 107.85, -939.5])
		Waypoint([859.0, 111.85, -957.5])
		Waypoint([825.5, 118.85, -931.5])
		Waypoint([816.5, 121.35, -954.5])
		Waypoint([823.0, 127.85, -975.0])
		Waypoint([841.5, 132.85, -1000.5])
		Waypoint([806.5, 142.35, -1003.5])
		Waypoint([788.0, 148.85, -983.0])
		Waypoint([788.0, 148.0, -983.0], horse = False)
		Waypoint([89.0, -1.0, 59.0], horse = False)
		Waypoint([788.0, -2.0, -983.0], horse = False)
		Waypoint([781.0, -2.0, -978.0], horse = False)
		Waypoint([90.0, -3.0, 45.0], horse = False)
		Waypoint([792.0, 152.0, -943.0], radius = 1.0, horse = False)
		Waypoint([90.0, -4.0, 0.0], horse = False)
		Waypoint([778.0, 148.0, -983.0], radius = 1.0, horse = False)

		#Node([966.0, 124.0, -1094.75], guidance = True, farmable = False, radius = 2.0)
		#Node([968.5, 125.0, -1093.5], tickskipping = True)
		#Node([966.5, 125.0, -1097.5], tickskipping = True)
		#Node([963.5, 125.0, -1093.5])
		#Node([960.0, 124.0, -1094.5], guidance = True, farmable = False, radius = 2.0)
		#Node([957.5, 125.0, -1092.5], tickskipping = True)
		#Node([962.5, 125.0, -1096.5])
		#Node([965.806, 124.0, -1087.419], guidance = True, farmable = False, radius = 2.0)
		#Node([963.5, 125.0, -1085.5], tickskipping = True)
		#Node([966.5, 125.0, -1084.5])
		#Node([976.5, 124.0, -1089.0], guidance = True, farmable = False, radius = 2.0)
		#Node([973.5, 125.0, -1087.5], tickskipping = True)
		#Node([979.5, 125.0, -1090.5])
		#Node([981.0, 124.0, -1103.0], guidance = True, farmable = False, radius = 2.0)
		#Node([983.5, 125.0, -1104.5], tickskipping = True)
		#Node([978.5, 125.0, -1101.5])
		#Node([974.0, 125.0, -1105.0], guidance = True, farmable = False)
elif (profession == "Farming"):
	if (level == 100):
		Node([1340.5, 116.5, -4807.5], delay = 1.0)
		Node([1336.5, 115.0, -4801.0], farmable = False, radius = 1.0)
		Node([1338.5, 116.5, -4800.5], tickskipping = True)
		Node([1334.5, 116.5, -4801.5])
		Node([1331.0, 114.9375, -4807.5], farmable = False, radius = 1.0)
		Node([1332.5, 116.5, -4805.5], tickskipping = True)
		Node([1329.5, 116.5, -4809.5])
		Node([1325.5, 114.9375, -4807.5], farmable = False, radius = 1.0)
		Node([1324.5, 116.5, -4809.5], tickskipping = True)
		Node([1327.5, 116.5, -4808.5], tickskipping = True)
		Node([1326.5, 116.5, -4805.5])
		Node([1323.5, 115.5, -4802.5], farmable = False, radius = 1.0)
		Node([1324.5, 117.5, -4800.5], tickskipping = True)
		Node([1325.5, 116.5, -4801.5])
	elif (level == 110):
		Node([1086.857, 135.0, -1136.214], farmable = False, radius = 1.0)
		Node([1087.5, 136.5, -1138.5], tickskipping = True)
		Node([1084.5, 136.5, -1136.5], tickskipping = True)
		Node([1088.5, 136.5, -1134.5], delay = 0.5)

		Node([90.0, -1.0, 68.0], farmable = False)

		Node([1096.5, 135.0, -1136.0], farmable = False, radius = 1.0)
		Node([1093.5, 136.5, -1135.5], tickskipping = True)
		Node([1096.5, 136.5, -1137.5], tickskipping = True)
		Node([1099.5, 136.5, -1136.5], delay = 0.5)

		Node([70.0, -1.0, 75.0], farmable = False)
		#Node([1100.0, 135.0, -1134.0], farmable = False, radius = 1.0)

		Node([1103.5, 135.0,-1138.5], farmable = False, radius = 1.0)
		Node([1105.5, 135.5, -1136.5], tickskipping = True, delay = 0.5)
		Node([1101.5, 136.5, -1140.5])

		Node([1095.5, 135.0, -1138.5], farmable = False, radius = 2.0)

		Node([1093.273, 136.0, -1143.182], farmable = False, radius = 1.0)
		Node([1095.5, 137.5, -1141.5], tickskipping = True)
		Node([1092.5, 137.5, -1140.5], tickskipping = True)
		Node([1090.5, 137.5, -1143.5], delay = 0.5)

		Node([1089.5, 136.0, -1141.5], farmable = False, radius = 1.0)
		
		Node([1085.0, 136.0, -1141.0], farmable = False, radius = 2.0)
		Node([1086.5, 137.5, -1142.5], tickskipping = True)
		Node([1083.5, 136.5, -1139.5])

def password():
	password = ""
	os.system('cls')
	print("Wynncraft's Automated Resource Collector\n\nAwaiting Server Connection...", end="")
	serverCheck = json.loads(requests.get("https://wynncraft-kf68.onrender.com/startup").text)
	while (True):
		try:
			os.system('cls')
			print("Wynncraft's Automated Resource Collector\n")
			password = maskpass.advpass(prompt="Enter the password: ", mask="\u00B7") + "Adamastor"
			if (hashlib.sha256(password.encode('utf-8')).hexdigest() == "559f1112003dcde49fb59dfee6d839c80344f58131861f22ac9763e9899996fa"):
				break
			else:
				os.system('cls')
				maskpass.askpass(prompt="Wynncraft's Automated Resource Collector\n\nPress enter to try again.", mask="")
		except:
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
	#print(fernet.decrypt(b'gAAAAABjGGY7yTCJJRMzPIRMawDAFRF-evMtC2ne6PmJ-Jf9aOya3GrXNYHY_C3PxWkKTmkB2tDRabKeplN-ATJMfBhS_HEMXVDGjfroMnklNZzgj065PTw=').decode())

	exitCode = False
	if (serverCheck == 1):
		print("Data out of sync")
		exitCode = True
	try:
		key = maskpass.askpass(prompt="\nPress enter to begin the program.", mask="") + "Warp"
		if (hashlib.sha256(key.encode('utf-8')).hexdigest() == "39865892e074fb33d5505fe64ab05b695ffeb9f142f7eb84d0c869b4c8779668"):
			key += "Spring"
			key = hashlib.sha256(key.encode('utf-8')).hexdigest()
			key = key[:-21] + '='
			fernet = Fernet(key)
			key = fernet.decrypt(b'gAAAAABi4wdn6UEOXcY9gE-ET_xg-lJhbOSw6YG3SaVSucOOZavoPQfj4pAGLaaYAg4ZvTmHvCis0lCTS4U4_9iTS9Vd2_MKl8cq42W8Un5osJX7jR9LS8VvGNa8GHMNH090SVuU3rL-').decode()
			print(key)
			exitCode = True
			#print("\n\nPress enter to close the program.", end = "")
			#maskpass.askpass(prompt="", mask="")
	except:
		pass
	if (exitCode):
		exit()
	print("Program started on", time.ctime(time.time()))

def imageProcessor(picture, health = False, doubleSpeed = 0, dura = False, eHealth = False):
	red = picture[..., 0]
	green = picture[..., 1]
	blue = picture[..., 2]
	if (health):
		convertToWhite = (red < 0.98)
		picture[convertToWhite] = 1
		convertToBlack = ((green != 1) & (blue != 1))
		picture[convertToBlack] = 0
	elif (doubleSpeed == 1):
		convertToWhite = (red != 0) | (green < 0.658) | (green > 0.66) | (blue < 0.658) | (blue > 0.66)
		picture[convertToWhite] = 1
		convertToBlack = ((red != 1) & (green != 1) & (blue != 1))
		picture[convertToBlack] = 0
	elif (doubleSpeed == 2):
		convertToBlack = ((red > 0.988) & (red < 0.989) & (green > 0.988) & (green < 0.989) & (blue > 0.988) & (blue < 0.989))
		picture[convertToBlack] = 0
		convertToWhite = ((red != 0) | (green != 0) | (blue != 0))
		picture[convertToWhite] = 1
	elif (dura):
		convertToWhite = (red < 0.654) | (red > 0.659) | (green != 0) | (blue != 0)
		picture[convertToWhite] = 1
		convertToBlack = (red != 1) & (green != 1) & (blue != 1)
		picture[convertToBlack] = 0
	elif (eHealth):
		convertToWhite = (red < 0.988) | (red > 0.989) | (green < 0.329) | (green > 0.330) | (blue < 0.329) | (blue > 0.330)
		picture[convertToWhite] = 1
		convertToBlack = (red == 1) & (green != 1) & (blue != 1)
		picture[convertToBlack] = 0
	else:
		convertToBlack = ((red > 0.866) & (red < 0.868) & (green > 0.866) & (green < 0.868) & (blue > 0.866) & (blue < 0.868))
		picture[convertToBlack] = 0
		convertToWhite = ((red != 0) & (green != 0) & (blue != 0))
		picture[convertToWhite] = 1
	return picture

def numberProcessor(img_rgb):
	img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
	dictionary = {}
	for i in range(12):
		letter = str(i)
		if (i == 10):
			letter = '('
		if (i == 11):
			letter = 'k'
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
	if ((functionCallNumber == 0 and keys[0] > 10) or (functionCallNumber == 1 and differences[1] > 10) or (functionCallNumber == 2 and differences[0] > 28)):
		text += "-"
	for i in range(len(keys)):
		if (((dictionary.get(keys[i]) != '(') and (dictionary.get(keys[i]) != 'k'))):
			text += dictionary.get(keys[i])
		if (i < len(keys) - 1 and (functionCallNumber != 1 and functionCallNumber != 2 or i > 0)):
			if ((functionCallNumber < 2 and differences[i] > 35 and differences[i] < 45) or (functionCallNumber > 1 and differences[i] > 15 and (functionCallNumber != 2 or differences[i] < 32))):
				text += " "
			elif ((functionCallNumber < 2 and differences[i] > 46) or (functionCallNumber == 2 and differences[i] > 32)):
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

def checkStream():
	screenshot = py.screenshot(region=streamAndSpeed)
	screenshot.save(directory + 'unprocessedStream.png')

	coords = mpimg.imread(directory + 'unprocessedStream.png')
	mpimg.imsave(directory + "processedStream.png", imageProcessor(coords, eHealth = True))
	img_rgb = cv2.imread(directory + 'processedStream.png')
	template = cv2.imread(directory + 'enabled.png', 0)
	img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
	res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
	threshold = 0.9999
	loc = np.where(res >= threshold)
	lists = loc[1].tolist()

	if (len(lists) > 0):
		return True
	return False

def processModerators(names):
	names = names.replace(", ", "\", \"")
	names = "\"" + names + "\""
	print(names)

def startup():
	py.hotkey('alt', 'tab')
	time.sleep(1)
	py.press('e')
	py.moveTo(960, 315)
	time.sleep(0.5)
	py.click()
	py.press('backspace', presses = 2)
	py.press('enter')
	if (not checkStream()):
		py.press('/')
		time.sleep(0.5)
		py.write('stream')
		py.press('enter')

#password()
#startup()

def server(keyPress):
	movementStatus = keyPress.copy()
	stopMove(keyPress)
	print("\nKicked out of server", end = "")
	while (True):
		try:
			#check = py.locateOnScreen(directory + 'heart.png', region=locateHeart)
			#check.left
			#py.press('f3')
			#time.sleep(5)
			confirm = py.locateOnScreen(directory + 'craftingTable.png', region=locateTable)
			confirm.left
			startMove(movementArray = movementStatus, keyPress = keyPress)
			abort(True, keyPress = keyPress)
			return
			#while (True):
			#	try:
			#		confirm = py.locateOnScreen(directory + 'craftingTable.png', region=locateTable)
			#		confirm.left
			#		startMove(movementArray = movementStatus, keyPress = keyPress)
			#		abort(True, keyPress = keyPress)
			#		return
			#	except:
			#		py.press('1')
			#		time.sleep(2)
			#		py.click(clicks = 2, interval = 2)
			#		time.sleep(30)
		except:
			lobbyStartTime = time.time() + 60
			while (True):
				py.moveTo(1900, 900)
				time.sleep(0.5)
				try:
					verify = py.locateOnScreen(directory + 'logo.png', region=locateLogo)
					verify.left
					break
				except:
					py.moveTo(960, 575)
					time.sleep(0.5)
					py.click()
					time.sleep(5)
					if (time.time() > lobbyStartTime):
						break
			if (time.time() < lobbyStartTime):
				py.moveTo(1040, 1000)
				time.sleep(0.5)
				py.click()
				time.sleep(5)
				py.moveTo(960, 125)
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
		try:
			check = py.locateOnScreen(directory + 'craftingTable.png', region=locateTable)
			check.left
			startMove(movementArray = movementStatus, keyPress = keyPress)
			abort(True, keyPress = keyPress)
			return
		except:
			try:
				location = py.locateOnScreen(directory + 'book.png', region=locatePlainBook)
				location.left
				py.press('e')
			except:
				pass
			py.press('1')
			time.sleep(2)
			py.click(clicks = 2, interval = 2)
			time.sleep(30)
	#case fails if logging in causes crash

def checkVitals(dangerString, previousHealth = [1, 1], keyPress = [False, False, False, False]):
	currentHealth = getHealth(previousHealth)
	if (vitals and previousHealth[0] > currentHealth[0]):
		print("Health dropped from", previousHealth[0], "to", currentHealth[0], "at", time.ctime(time.time()))
		if (character == "Assassin" and level == 110 and profession == "Fishing"):
			currentHealth[1] -= 1
		else:
			abort(True, keyPress = keyPress)
			currentHealth = getHealth(currentHealth)
	elif (currentHealth[0]/currentHealth[1] < 0.5):
		print("\nHealth dropped to below 50%.")
		dangerString = repair(keyPress, dangerString)
		return [1, 1]
	return [currentHealth, dangerString]

def eta(destination, speed, keyPress):
	currentPosition = getPosition(keyPress = keyPress)
	distance = math.sqrt((destination[0] - currentPosition[0])**2 + (destination[2] - currentPosition[2])**2)
	return distance / speed

def movementSpell(dangerString, targetPitch = 90.0, targetYaw = -360, keyPress = [False, False, False, False]):
	if (character == "Archer"):
		changeRotation(targetPitch = targetPitch, targetYaw = targetYaw)
		py.press('1')
		py.click(clicks = 3, interval = 0.1)
		time.sleep(1)
		previousY = getPosition(keyPress = keyPress)[1]
		currentY = 0.0
		while(True):
			currentY = getPosition(keyPress = keyPress)[1]
			if (currentY == previousY):
				currentY = getPosition(keyPress = keyPress)[1]
				if (currentY == previousY):
					break
			previousY = currentY
		if (not shields):
			py.press('2')
	elif (character == "Assassin"):
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
		finishTime = time.time() + 10
		dangerString = checkModerators(keyPress, dangerString)
		while(True):
			currentY = getPosition(keyPress = keyPress)[1]
			if (currentY == previousY):
				currentY = getPosition(keyPress = keyPress)[1]
				if (currentY == previousY):
					break
			if (time.time() > finishTime):
				break
			previousY = currentY
	return dangerString

def startMove(movementStatus = 0, keyPress = [False, False, False, False], movementArray = [False, False, False, False], walkingStick = False, shield = False):	# 0 = not moving | 1 = walking | 2 = sneaking | 3 = sprinting
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
	if (walkingStick or shield):
		py.press('1')
		if (shield):
			py.click()
			time.sleep(0.1)
			py.click()
			time.sleep(0.1)
			py.rightClick()

def stopMove(keyPress, walkingStick = False, shield = False, swim = False):
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
	#if (walkingStick or shield):
	#	py.press('2')

def rotate(yaw = 0.0, pitch = 0.0, delay = 0.3):
	yaw *= sensitivity
	pitch *= sensitivity
	pydirect.drag(int(yaw + 0.5), int(pitch + 0.5), delay, relative=True, button="middle")

def checkSpeed(display = False):
	screenshot = py.screenshot(region=streamAndSpeed)
	screenshot.save(directory + 'unprocessedSpeed.png')

	coords = mpimg.imread(directory + 'unprocessedSpeed.png')
	mpimg.imsave(directory + "processedSpeed.png", imageProcessor(coords, doubleSpeed = 1))
	img_rgb = cv2.imread(directory + 'processedSpeed.png')
	template = cv2.imread(directory + 'speed.png', 0)
	img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
	res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
	threshold = 0.9999
	loc = np.where(res >= threshold)
	lists = loc[1].tolist()

	if (len(lists) == 0):
		if (display):
			print(-1)
		return -1

	coords = mpimg.imread(directory + 'unprocessedSpeed.png')
	mpimg.imsave(directory + "processedSpeedNumber.png", imageProcessor(coords, doubleSpeed = 2))
	img_rgb = cv2.imread(directory + 'processedSpeedNumber.png')
	dictionary = numberProcessor(img_rgb)
	
	for i in dictionary:
		if (display):
			print(int(dictionary[i]))
		return int(dictionary[i])

def checkDurability():
	screenshot = py.screenshot(region=durabilityScreenshot)
	screenshot.save(directory + 'unprocessedDurability.png')

	coords = mpimg.imread(directory + 'unprocessedDurability.png')
	mpimg.imsave(directory + "processedDurability.png", imageProcessor(coords, dura = True))
	img_rgb = cv2.imread(directory + 'processedDurability.png')
	dictionary = numberProcessor(img_rgb)

	if (len(dictionary) == 1):
		return True
	return False

def enemyHealth():
	screenshot = py.screenshot(region=eHealthScreenshot)
	screenshot.save(directory + 'unprocessedEnemy.png')

	coords = mpimg.imread(directory + 'unprocessedEnemy.png')
	mpimg.imsave(directory + "processedEnemy.png", imageProcessor(coords, eHealth = True))
	img_rgb = cv2.imread(directory + 'processedEnemy.png')
	dictionary = numberProcessor(img_rgb)
	healthReading = dictionaryProcessor(dictionary, 3)
	if (healthReading == ''):
		return 0
	return int(healthReading)

def randomRotation(keyPress):
	num = random.random()
	if (num < 0.5):
		currentDirection = getDirection(keyPress = keyPress)
		randomPitch = random.randint(0, 45)
		randomYaw = random.randint(-45, 45)
		if (currentDirection[1] > 0):
			rotate(randomYaw, -randomPitch)
		else:
			rotate(randomYaw, randomPitch)

def getInitialModList():
	modTimeOut = []
	dangerString = ""

	responseObject = json.loads(requests.get("https://wynncraft-kf68.onrender.com/moderators").text)
	if (len(responseObject) == 0):
		print("Error with inital call")
	for i in responseObject:
		if (i[1] > 0): #and i[0] != "Salted"):
			if (i[1] > 29 and i[1] < 100):
				dangerString += ('|' + i[0] + '|')
			else:
				if (i[1] > 100):
					i[1] -= 100
					print(i[0] +  " vanished at " + time.ctime())
				modTimeOut.append([i[0], i[1]])

	responseObject = json.loads(requests.get("https://weak-lime-drill-fez.cyclic.app/get/friends").text)
	utcTime = time.gmtime(responseObject[len(responseObject) - 1]["update"])
	utcMinutes = utcTime.tm_hour * 60 + utcTime.tm_min + 1
	if (utcMinutes < 30):
		responseObject = json.loads(requests.get("https://weak-lime-drill-fez.cyclic.app/get/all").text)
		utcMinutes += 41760
		for i in responseObject:
			try:
				i["today"] = i["month"] + i["today"]
			except:
				pass
	
	for i in responseObject:
		try:
			timeStampString = stringToBool(i["today"])[utcMinutes - 30:utcMinutes]
			if ('1' in timeStampString and (i["user"] != "azarashiouo" and i["user"] != "Awesome_AA_" and i["user"] != "Awesome_AA" and i["user"] != "Zyreon")):
				if (('|' + i["user"] + '|' not in dangerString) and (i["user"] != "Salted")):
					for j in modTimeOut:
						if (j[0] == i["user"]):
							break
					else:
						print(i["user"])
						if (timeStampString.rindex('1') == 29):
							dangerString += ('|' + i["user"] + '|')
						else:
							modTimeOut.append([i["user"], timeStampString.rindex('1') + 1])
		except:
			pass
	return [dangerString, modTimeOut]

def farm(previousHealth, durability, speedBomb, speedClock, left = True, delay = 7.0, autoClicker = False, keyPress = [False, False, False, False], dangerString = ""):
	py.press('2')
	if (speedBomb[0]):
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
		stopTime = time.time() + delay
		if (not speedBomb[0]):
			minutes = checkSpeed()
			if (minutes > -1):
				speedBomb[0] = True
				speedClock[0] = time.time() + ((minutes + 1) * 60)
				print("Speed bomb detected on", time.ctime(time.time()), "with", minutes, "minutes remaining")
		elif (speedClock[0] < time.time() and speedBomb[0]):
			speedBomb[0] = False
			print("Speed bomb finished on", time.ctime(time.time()))
		heartDanger = checkVitals(dangerString, previousHealth, keyPress = keyPress)
		previousHealth = heartDanger[0]
		dangerString = heartDanger[1]
		lagTime = []
		if (delay != farmTime):
			returnData = getInitialModList()
			dangerString = returnData[0]
			lagTime = returnData[1]
		dangerString = checkModerators(keyPress, dangerString, initialTimeOut=lagTime)
		durability[0] = checkDurability()
		randomRotation(keyPress)
		difference = stopTime - time.time()
		if (difference > 0):
			time.sleep(difference)
	if (num < 0.5):
		py.keyUp('shift')
		keyPress[1] = False
	return [previousHealth, dangerString]

def getPosition(display=False, keyPress = [False, False, False, False], iterations = 0):
	try:
		screenshot = py.screenshot(region=positionScreenshot)			#1.17
		#screenshot = py.screenshot(region=(50, 158, 358, 16))			#1.12
		screenshot.save(directory + 'unprocessedCoordinates.png')

		coords = mpimg.imread(directory + 'unprocessedCoordinates.png')
		mpimg.imsave(directory + "processedCoordinates.png", imageProcessor(coords))

		img_rgb = cv2.imread(directory + 'processedCoordinates.png')
		dictionary = numberProcessor(img_rgb)

		text = dictionaryProcessor(dictionary, 0)

		positionCoordinates = textProcessor(text, display, 0)
		if (keyPress[2] == False and positionCoordinates[1] < waterLevel):
			keyPress[2] = True
			py.keyDown('space')
		elif (keyPress[2] == True and positionCoordinates[1] > waterLevel):
			keyPress[2] = False
			py.keyUp('space')
		return positionCoordinates
	except:
		movementStatus = keyPress.copy()
		if (iterations > 1):
			if (keyPress[2] == True):
				print("\nFailed to receive position coordinates.", end = "")
				abort(False, keyPress)
			else:
				stopMove(keyPress)
				py.screenshot('evidence1.png')
				py.press('f5')
				py.screenshot('evidence2.png')
				py.press('f5')
				py.screenshot('evidence3.png')
				time.sleep(0.5)
				py.hotkey('alt', 'tab')
				print("\nFailed to receive position coordinates on", time.ctime(time.time()), end = ". ")
				maskpass.askpass(prompt="Press enter to resume the program.", mask="")
				startup()
				if (character == "Archer"):
					dangerString = movementSpell(dangerString = "", keyPress = keyPress)
				startMove(movementArray = movementStatus, keyPress = keyPress)
			return getPosition(keyPress = keyPress)
		else:
			try:
				check = py.locateOnScreen(directory + 'craftingTable.png', region=locateTable)
				check.left
				lobby(keyPress)
				return getPosition(keyPress = keyPress)
			except:
				pass
			if (open(directory + "lobbyImage1.png", "rb").read() == open(directory + "unprocessedCoordinates.png", "rb").read()):
				stopMove(keyPress)
				time.sleep(30)
				screenshot = py.screenshot(region=positionScreenshot)
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
		screenshot = py.screenshot(region=directionScreenshot)			#1.12
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
				py.screenshot('evidence1.png')
				py.press('f5')
				py.screenshot('evidence2.png')
				py.press('f5')
				py.screenshot('evidence3.png')
				time.sleep(0.5)
				py.hotkey('alt', 'tab')
				print("\nFailed to receive direction angles on", time.ctime(time.time()), end = ". ")
				maskpass.askpass(prompt="Press enter to resume the program.", mask="")
				startup()
				if (character == "Archer"):
					dangerString = movementSpell(dangerString = "", keyPress = keyPress)
				startMove(movementArray = movementStatus,  keyPress = keyPress)
			return getDirection(keyPress = keyPress)
		else:
			try:
				check = py.locateOnScreen(directory + 'craftingTable.png', region=locateTable)
				check.left
				lobby(keyPress)
				return getDirection(keyPress = keyPress)
			except:
				pass
			if (open(directory + "lobbyImage2.png", "rb").read() == open(directory + "unprocessedDirection.png", "rb").read()):
				stopMove(keyPress)
				time.sleep(30)
				screenshot = py.screenshot(region=directionScreenshot)			#1.12
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
		screenshot = py.screenshot(region=visualScreenshot)			#1.12 #164
		screenshot.save(directory + 'unprocessedVisual.png')

		coords = mpimg.imread(directory + 'unprocessedVisual.png')
		mpimg.imsave(directory + "processedVisual.png", imageProcessor(coords))

		img_rgb = cv2.imread(directory + 'processedVisual.png')
		dictionary = numberProcessor(img_rgb)

		text = dictionaryProcessor(dictionary, 2)

		coords = textProcessor(text, display, 2)
		if (node):
			coords[0] += 0.5
			if (waterLevel == 0.0):
				coords[1] += yLevel
			else:
				coords[1] = waterLevel + yLevel
			coords[2] += 0.5
			print("Node(", coords, ")")
		return coords
	except:
		return []

def getHealth(previousHealth = [1, 1], iterations = 0, display = False):
	try:
		screenshot = py.screenshot(region=healthScreenshot)
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
	elif (dx != 0 and dz != 0):
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

def calculateSpeed(seconds = 3.0, movementStatus = 0, display=False):
	keyPress = [False, False, False, False]
	startMove(movementStatus, keyPress)
	firstPoint = getPosition(keyPress = keyPress)
	time.sleep(seconds)
	secondPoint = getPosition(keyPress = keyPress)
	stopMove(keyPress)
	r2 = math.sqrt((secondPoint[0] - firstPoint[0])**2 + (secondPoint[2] - firstPoint[2])**2)
	if (display):
		print(r2/seconds)
	return r2/seconds

def calculateSensitivity(pixels = 100.0, display=False):
	keyPress = [False, False, False, False]
	pydirect.drag(0, -1000, 0.3, relative=True, button="middle")
	firstAngle = getDirection(keyPress = keyPress)
	pydirect.dragRel(0, int(pixels), 0.3, relative=True, button="middle")
	secondAngle = getDirection(keyPress = keyPress)
	if (display):
		print(pixels/(secondAngle[1] - firstAngle[1]))
	return pixels/(secondAngle[1] - firstAngle[1])

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
		lobbyCoordinates = [295.5, 34.0, 321.5]
		r2 = (lobbyCoordinates[0]-currentPosition[0])**2 + (lobbyCoordinates[1]-currentPosition[1])**2 + (lobbyCoordinates[2]-currentPosition[2])**2
		if (r2 < 10000.0):
			lobby(keyPress)
		else:
			print("Node out of range.")
			print("Last recoreded position: ", currentPosition)
			print("Failed to reach: ", destination)
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

def leap(destination, dangerString, keyPress = [False, False, False, False]):
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
	dangerString = movementSpell(dangerString = dangerString, keyPress = keyPress)
	return dangerString

def hop(keyPress, dangerString):
	py.keyDown('space')
	py.keyUp('space')
	time.sleep(0.05)
	py.keyDown('space')
	time.sleep(0.5)
	py.keyUp('space')
	futureTime = time.time() + 0.5
	dangerString = checkModerators(keyPress, dangerString)
	if (time.time() < futureTime):
		time.sleep(futureTime - time.time())
	return dangerString

def abort(temporary = False, keyPress = [False, False, False, False], iterations = 0):
	movementStatus = keyPress.copy()
	stopMove(keyPress)
	if (not temporary):
		py.screenshot('evidence1.png')
		py.press('f5')
		py.screenshot('evidence2.png')
		py.press('f5')
		py.screenshot('evidence3.png')
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
		futureTime = time.time() + 10
		#if (speedBomb[0]):
		#	futureTime -= 30
		time.sleep(1)
		py.press('/')
		time.sleep(0.5)
		py.write('stream')
		py.press('enter')
		priorHealth = getHealth()
		while(futureTime > time.time()):
			presentHealth = getHealth(priorHealth)
			if (character == "Archer" and int(futureTime - time.time()) % 14 == 0):
				startMove(keyPress = keyPress, shield = True)
				time.sleep(1)
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
		if (character == "Archer"):
			dangerString = movementSpell(dangerString = "", keyPress = keyPress)
		startMove(movementArray = movementStatus, keyPress = keyPress)
		print("Program resumed on", time.ctime(time.time()))
	else:
		stopMove(keyPress)
		py.hotkey('alt', 'tab')
		exit()

def stringToList(dangerString):
	currentIndex = 0
	dangerList = []
	while (True):
		nextBreak = dangerString.find('|', currentIndex + 1)
		if (nextBreak == -1):
			break
		modName = dangerString[currentIndex + 1: nextBreak]
		if (dangerString[currentIndex: currentIndex + 5] == "|$#!%"):
			modName = dangerString[currentIndex + 5: nextBreak]
		dangerList.append(modName)
	return dangerList

def checkModerators(keyPress, dangerString, initialTimeOut=[], onHorse = False):
	response = {}
	shiftStatus = False
	if (not blindCheck):
		response = requests.post("https://wynncraft-kf68.onrender.com/check", json={"previous": dangerString})
	else:
		response = requests.get("https://wynncraft-kf68.onrender.com/blindcheck")
	if (len(response.text) != 2 or len(initialTimeOut) > 0): #and len(response.text) != 3):
		if (not blindCheck):
			if (len(response.text) > 1 and response.text[1] == '|' and len(initialTimeOut) == 0):
				dangerString = response.text[1: -1]
			else:
				movementStatus = keyPress.copy()
				modList = []
				timeOut = []
				if (len(initialTimeOut) > 0):
					for i in initialTimeOut:
						modList.append(i[0])
						timeOut.append(time.time() + (i[1] * 60))
				else:
					print(response.text.replace("\"", "") + " at " + time.ctime(time.time()))
				if (len(initialTimeOut) > 0):
					stopMove(keyPress)
					py.press('/')
					time.sleep(0.5)
					py.write('class')
					py.press('enter')
					time.sleep(1)
					
					mousePositionList = [890, 925, 960, 1000]
					py.moveTo(mousePositionList[int(random.random() * 4)], 410)
					time.sleep(5)
					py.click()
				elif (" detected in world " in response.text):
					abort(False, keyPress = keyPress)
					#teleport(keyPress)
					#abort(False, keyPress = keyPress)
				elif (" went offline" in response.text):
					modOfInterest = response.text[1: response.text.index(" went offline")]
					modList.append(modOfInterest)
					timeOut.append(time.time() + 1800)
					dangerString = dangerString.replace('|' + modOfInterest + '|', "")

					stopMove(keyPress)
					py.press('/')
					time.sleep(0.5)
					py.write('class')
					py.press('enter')
					time.sleep(1)
					
					mousePositionList = [890, 925, 960, 1000]
					py.moveTo(mousePositionList[int(random.random() * 4)], 410)
					time.sleep(5)
					py.click()

				elif ("User not found" in response.text):
					stopMove(keyPress)
					time.sleep(30)
					try:
						check = py.locateOnScreen(directory + 'craftingTable.png', region=locateTable)
						check.left
						mousePositionList = [890, 925, 960, 1000]
						py.moveTo(mousePositionList[int(random.random() * 4)], 410)
						time.sleep(5)
						py.click()
					except:
						time.sleep(60)
						server(keyPress)
					returnData = getInitialModList()
					dangerString = checkModerators(keyPress, returnData[0], returnData[1])
				else:
					stopMove(keyPress)
					py.press('/')
					time.sleep(0.5)
					py.write('class')
					py.press('enter')
					time.sleep(1)
					if ("Error with axios call" in response.text):
						print(dangerString)
						dangerString = getInitialModList()[0]
				while (True):
					response = requests.post("https://wynncraft-kf68.onrender.com/check", json={"previous": dangerString})
					if (len(response.text) > 1 and response.text[1] == '|' or len(response.text) == 2):
						dangerString = response.text[1: -1]
						loopIndex = 0
						while (loopIndex < len(modList)):
							if ((time.time() > timeOut[loopIndex]) or ('|' + modList[loopIndex] + '|' in dangerString)):
								if ('|' + modList[loopIndex] + '|' in dangerString):
									print(modList[loopIndex] + " back in service at " + time.ctime())
								else:
									print(modList[loopIndex] + " no longer being tracked at " + time.ctime())
								del timeOut[loopIndex]
								del modList[loopIndex]
							else:
								loopIndex += 1
						if (len(modList) == 0):
							break						
					elif (len(response.text) != 2):
						print(response.text.replace("\"", "") + " at " + time.ctime(time.time()))
						if (" went offline" in response.text):
							modOfInterest = response.text[1: response.text.index(" went offline")]
							modList.append(modOfInterest)
							timeOut.append(time.time() + 1800)
							dangerString = dangerString.replace('|' + modOfInterest + '|', "")
						elif (" detected in world " in response.text):
							abort(False, keyPress = keyPress)
						elif ("User not found" in response.text):
							time.sleep(30)
							try:
								check = py.locateOnScreen(directory + 'craftingTable.png', region=locateTable)
								check.left
								mousePositionList = [890, 925, 960, 1000]
								py.moveTo(mousePositionList[int(random.random() * 4)], 410)
								time.sleep(5)
								py.click()
							except:
								time.sleep(60)
								server(keyPress)
							returnData = getInitialModList()
							dangerString = checkModerators(keyPress, returnData[0], returnData[1])
						else:
							stopMove(keyPress)
							time.sleep(50)				
							if ("Error with axios call" in response.text):
								print(dangerString)
								returnData = getInitialModList()
								dangerString = checkModerators(keyPress, returnData[0], returnData[1])			
					time.sleep(5)

				py.press('m')
				time.sleep(30)
				returnData = getInitialModList()
				dangerString = checkModerators(keyPress, returnData[0], returnData[1])
				print("Program resumed on", time.ctime(time.time()), '\n')
				getPosition()

				py.press('/')
				time.sleep(0.5)
				py.write('class')
				py.press('enter')
				time.sleep(1)
				py.moveTo(850, 410)
				time.sleep(5)
				py.click()
				if (movementStatus[2] == True):
					py.keyDown('space')
					keyPress[2] = True
				time.sleep(1)
				py.press('/')
				time.sleep(0.5)
				py.write('stream')
				py.press('enter')
				if (onHorse):
					mountHorse(keyPress)
				startMove(movementArray = movementStatus, keyPress = keyPress)
		else:
			print(response.text.replace("\"", "") + " at " + time.ctime(time.time()))
			#teleport(keyPress)
			abort(False, keyPress = keyPress)
	return dangerString

def calculateDistance(targetPitch, targetYaw, display = False):
	distance = -0.002*((targetPitch + 20.0)**2) + 7.5
	print("Predicted Distance: ", distance)
	pointOne = getPosition()
	changeRotation(targetPitch = targetPitch, targetYaw = targetYaw)
	movementSpell(dangerString = "")
	time.sleep(3)
	pointTwo = getPosition()
	r2 = math.sqrt((pointTwo[0] - pointOne[0])**2 + (pointTwo[2] - pointOne[2])**2)
	if (display):
		print("(", targetPitch,  ", ",  r2, ")")
	return r2

def mountHorse(keyPress):
	finishTime = time.time() + 10
	while (True):
		py.press('6')
		changeRotation(targetPitch = 90.0, keyPress = keyPress)
		py.click(button = 'right', clicks = 2, interval = 1.0)
		currentPosition = getPosition(keyPress = keyPress)
		checkHeight = currentPosition[1] - int(currentPosition[1])
		if (((checkHeight > 0.84) and (checkHeight <= 0.85)) or ((checkHeight > 0.51) and (checkHeight <= 0.52))):
			break
		elif (finishTime < time.time()):
			py.press('/')
			time.sleep(0.5)
			py.write('class')
			py.press('enter')
			time.sleep(1)
			py.moveTo(850, 410)
			time.sleep(5)
			py.click()
			time.sleep(1)
			py.press('/')
			time.sleep(0.5)
			py.write('stream')
			py.press('enter')	

def dismountHorse(keyPress):
	finishTime = time.time() + 30
	while (True):
		py.press('q')
		currentPosition = getPosition(keyPress = keyPress)
		if (((currentPosition[1]) - int(currentPosition[1]) == 0.0) or ((currentPosition[1]) - int(currentPosition[1]) == 0.5)):
			break
		elif (finishTime < time.time()):
			break

def teleport(keyPress):
	futureTime = time.time() + 30
	while (True):
		py.press('5')
		changeRotation(targetPitch = -45.0, targetYaw = -90.0, keyPress = keyPress)
		py.rightClick()
		if (proximity([978.0, 73.0, -671.0], radius = 999, abortRadius = 499999)):
			break
		elif (futureTime < time.time()):
			print("Failed to teleport")
			abort(keyPress = keyPress)

def checkProgress(caseNumber):
	passes = 0
	while True:
		try:
			location = ()
			if (caseNumber == 0):
				location = py.locateOnScreen(directory + 'pickaxeh.png', region=locatePickaxeh)
			elif (caseNumber == 1):
				location = py.locateOnScreen(directory + 'backArrow.png', region=locateBackArrow)
			elif (caseNumber == 2):
				location = py.locateOnScreen(directory + 'backArrow.png', region=locateBackArrow2)
			elif (caseNumber == 3):
				location = py.locateOnScreen(directory + 'check.png', region=locateCheck)
			elif (caseNumber == 4):
				location = py.locateOnScreen(directory + 'questBook.png', region=locateBook)
			elif (caseNumber == 5):
				location = py.locateOnScreen(directory + 'confirm20.png', region=locateConfirm)
			elif (caseNumber == 6):
				location = py.locateOnScreen(directory + 'backArrow.png', region=locateBackArrow3)
			elif (caseNumber == 7):
				location = py.locateOnScreen(directory + 'pickaxeh.png', region=locatePickaxeh2)
			location.left
			return True
		except:
			passes += 1
			if (passes > 300):
				return False

def fixTool(checkpoint, keyPress):
	changeRotation(checkpoint, keyPress = keyPress)
	if (True):
		proceed = True
		finalCheck = False
		
		if (proceed):
			py.rightClick()
			proceed = checkProgress(0)			#diamond pickaxe
		
		if (proceed):
			py.moveTo(x=1105, y=540)			#emerald Sign
			py.click()
			proceed = checkProgress(1)			#back green sign

		if (proceed):
			py.moveTo(x=995, y=410)				#blank Sign
			py.click()
			proceed = checkProgress(2)			#back green Sign

		if (proceed):
			py.moveTo(x=850, y=665)				#diamond pickaxe
			py.click()
			proceed = checkProgress(3)			#check sign

		if (proceed):
			py.moveTo(x=925, y=450)				#le Sign
			py.click()
			proceed = checkProgress(4)			#bookSign

		if (proceed):
			py.press('t')
			time.sleep(0.5)
			py.write("1000000")
			py.press("enter")
			proceed = checkProgress(3)			#check sign

		if (proceed):
			py.moveTo(x=995, y=450)
			proceed = checkProgress(5)			#confirm sign
			finalCheck = True

		if (proceed):
			#py.moveTo(x=995, y=450)			#checkmark
			py.click()
			proceed = checkProgress(1)			#back green Sign

		if (proceed):
			py.moveTo(x=100, y=100)
			time.sleep(0.5)
			pickaxeLocation = py.locateCenterOnScreen(directory + 'pickaxe.png', region=locatePickaxe)
			py.moveTo(x=pickaxeLocation[0], y=pickaxeLocation[1])					#diamond pickaxe
			py.click()
			proceed = checkProgress(6)			#back green sign

		if (proceed):
			py.moveTo(x=1070, y=450)			#red x
			py.click()
			proceed = checkProgress(1)			#back green sign

		if (not checkProgress(7) and finalCheck):
			print("Lost pickaxe")
			abort(False, keyPress = keyPress)
			

	else:
		futureTime = time.time() + 30
		while (True):
			py.rightClick()
			try:
				location = py.locateOnScreen(directory + 'scrap.png', region=locateScrap)
				location.left
				futureTime = time.time() + 30
				while (True):
					py.moveTo(x=1030, y = 445)
					py.click()
					try:
						location = py.locateOnScreen(directory + 'repair.png', region=locateRepair)
						location.left
						futureTime = time.time() + 30
						while (True):
							py.moveTo(x = 820, y = 380)
							py.click()
							py.moveTo(x = 100, y = 100)
							try:
								location = py.locateOnScreen(directory + 'blank.png', region=locateBlank)
								location.left
								break
							except:
								if (futureTime < time.time()):
									break
						break
					except:
						if (futureTime < time.time()):
							break
				break
			except:
				if (futureTime < time.time()):
					break
	futureTime = time.time() + 30
	while (True):
		py.press('e')
		time.sleep(1)
		try:
			location = py.locateOnScreen(directory + 'questBook.png', region=locateBook)
			location.left
			break
		except:
			pass

def depositInBank(checkpoint, keyPress):
	futureTime = time.time() + 30
	changeRotation(checkpoint, keyPress = keyPress)
	while (True):
		py.rightClick()
		try:
			location = py.locateOnScreen(directory + 'arrow.png', region=locateArrow)
			location.left
			futureTime = time.time() + 30
			while (True):
				py.moveTo(x=1100, y=540)
				py.rightClick()
				try:
					location = py.locateOnScreen(directory + 'blank.png', region=locateBlank2)
					location.left
					break
				except:
					if (futureTime < time.time()):
						break
			break
		except:
			if (futureTime < time.time()):
				break
	futureTime = time.time() + 30
	while (True):
		py.press('e')
		time.sleep(1)
		try:
			location = py.locateOnScreen(directory + 'questBook.png', region=locateBook)
			location.left
			break
		except:
			if (futureTime < time.time()):
				pass

def attack(keyPress, coords = [0.0, 0.0, 0.0]):
	previousPosition = [0.0, 0.0, 0.0]
	startTime = time.time()
	currentTime = time.time()
	py.press('1')
	changeRotation(targetPitch = 90.0, targetYaw = 45.0, keyPress = keyPress)
	while (True):
		if (currentTime < time.time()):
			currentTime += 3.0
			py.click(button = 'right', clicks = 2, interval = 0.1)
		if (coords[0] == 0.0 and coords[1] == 0.0 and coords[2] == 0.0):
			time.sleep(0.1)
		else:
			sleepTime = time.time() + 0.1
			flag = False
			if (not proximity(coords, radius = 1.0, keyPress = keyPress)):
				changeRotation(coords, 39.0, keyPress = keyPress)
				startMove(2, keyPress)
				flag = True
			trackTime = time.time()
			while(not proximity(coords, radius = 1.0, keyPress = keyPress)):
				flag = True
				if (trackTime + 5 < time.time() and keyPress[2] == False):
					jump(False, keyPress = keyPress)
					trackTime = time.time()
				#previousHealth = checkVitals(previousHealth, keyPress = keyPress)
				currentPosition = changeRotation(coords, 39.0, keyPress = keyPress)
				if (keyPress[2] == False):
					jump(keyPress = keyPress)
				if (currentPosition[0] == previousPosition[0] and currentPosition[2] == previousPosition[2]):
					patience += 1
					stopMove(keyPress)
					startMove(2, keyPress)
				else:
					patience = 0
				previousPosition = currentPosition
				if (patience > 9):
					print("Character in a trapped condition.", end = "")
					abort(keyPress = keyPress)
			stopMove(keyPress)
			if (flag):
				changeRotation(targetPitch = 90.0, targetYaw = 0.0, keyPress = keyPress)
			difference = sleepTime - time.time()
			if (difference > 0.0):
				time.sleep(difference)
		py.click()
		if (startTime + 15 < time.time() and enemyHealth() == 0):
			break
	
def repair(keyPress, dangerString, deposit = True):
	stopMove(keyPress)
	previousPosition = [0.0, 0.0, 0.0]
	if (not proximity([978.0, 73.0, -671.0], radius = 999, abortRadius = 499999, keyPress = keyPress)):
		teleport(keyPress)
		print("Recess taken on", time.ctime(time.time()))
	py.press('9')
	for i in range(len(gps)):
		checkpoint = gps[i].coordinates
		if (checkpoint[1] == -1):
			changeRotation(targetPitch = checkpoint[0], targetYaw = checkpoint[2], keyPress = keyPress)
			dangerString = movementSpell(dangerString = dangerString, keyPress = keyPress)
		elif (checkpoint[1] == -2):
			dangerString = leap(checkpoint, dangerString = dangerString, keyPress = keyPress)
		elif (checkpoint[1] == -3):
			changeRotation(targetPitch = checkpoint[0], targetYaw = checkpoint[2], keyPress = keyPress)
			startMove(1, keyPress)
			attack(keyPress = keyPress)
			stopMove(keyPress)
		elif (checkpoint[1] == -4):
			changeRotation(targetPitch = checkpoint[0], targetYaw = checkpoint[2], keyPress = keyPress)
			attack(keyPress, gps[i - 1].coordinates)
			stopMove(keyPress)
		elif (deposit or i > 7):
			if (not gps[i].horse and i != 0 and gps[i - 1].horse):
				dismountHorse(keyPress)
				py.press('1')
				dangerString = checkModerators(keyPress, dangerString)
			elif (gps[i].horse and not gps[i - 1].horse):
				mountHorse(keyPress)
			offTarget = False
			if (not proximity(checkpoint, 25, 99999, keyPress = keyPress)):
				if (i == 0 or i == 2):
					currentPosition = changeRotation(checkpoint, 60.0, keyPress = keyPress)
				else:
					currentPosition = changeRotation(checkpoint, 39.0, keyPress = keyPress)
				startMove(1, keyPress)
				dangerString = checkModerators(keyPress, dangerString, onHorse = gps[i].horse)
				offTarget = True
			while(not proximity(checkpoint, 25, 99999, keyPress = keyPress)):
				#previousHealth = checkVitals(previousHealth, keyPress = keyPress)
				if (i == 0 or i == 2):
					currentPosition = changeRotation(checkpoint, 60.0, keyPress = keyPress)
				else:
					currentPosition = changeRotation(checkpoint, 39.0, keyPress = keyPress)
				if (keyPress[2] == False):
					jump(keyPress = keyPress)
				if (currentPosition[0] == previousPosition[0] and currentPosition[2] == previousPosition[2]):
					patience += 1
					dangerString = hop(keyPress, dangerString)
				else:
					patience = 0
				previousPosition = currentPosition
				if (patience > 9):
					print("Character in a trapped condition.", end = "")
					abort(keyPress = keyPress)
			if (offTarget):
				stopMove(keyPress, swim = True)

			if (not gps[i].horse):
				slowMovement = 0
				if (not proximity(checkpoint, radius = gps[i].radius, keyPress = keyPress)):
					slowMovement = 2
					if (keyPress[2] == True):
						slowMovement = movementChoice
					if (i == 0 or i == 2):
						currentPosition = changeRotation(checkpoint, 60.0, keyPress = keyPress)
					else:
						currentPosition = changeRotation(checkpoint, 39.0, keyPress = keyPress)
					startMove(slowMovement, keyPress)
				currentTime = time.time()
				while(not proximity(checkpoint, radius = gps[i].radius, keyPress = keyPress)):
					if (currentTime + 5 < time.time() and keyPress[2] == False):
						jump(False, keyPress = keyPress)
						currentTime = time.time()
					#previousHealth = checkVitals(previousHealth, keyPress = keyPress)
					if (i == 0 or i == 2):
						currentPosition = changeRotation(checkpoint, 60.0, keyPress = keyPress)
					else:
						currentPosition = changeRotation(checkpoint, 39.0, keyPress = keyPress)
					if (keyPress[2] == False):
						jump(keyPress = keyPress)
					if (currentPosition[0] == previousPosition[0] and currentPosition[2] == previousPosition[2]):
						patience += 1
						dangerString = hop(keyPress, dangerString)
					else:
						patience = 0
					previousPosition = currentPosition
					if (patience > 9):
						print("Character in a trapped condition.", end = "")
						abort(keyPress = keyPress)
				if (slowMovement != 0):
					stopMove(keyPress, swim = True)

			if (gps[i].interact == 1):
				fixTool(checkpoint, keyPress)
			elif (gps[i].interact == 2):
				depositInBank(checkpoint, keyPress)
	print("Resumed work on", time.ctime(time.time()), "\n")
	return dangerString

def stringToBool(characterString):
	binary = [128, 64, 32, 16, 8, 4, 2, 1]
	booleanArray = ""
	for i in characterString:
		num = ord(i)
		for j in range(8):
			if (num - binary[j] >= 0):
				booleanArray += '1'
				num -= binary[j]
			else:
				booleanArray += '0'
	return booleanArray

def main():
	keyPress = [False, False, False, False]					# 0 = ctrl | 1 = shift | 2 = space | 3 = w
	durability = [False]
	speedBomb = [False]
	speedClock = [0.0]
	tryAttack = False
	enemyHealthRead = 1

	responseData = getInitialModList()
	dangerString = responseData[0]
	modTimeOut = responseData[1]

	dangerString = checkModerators([False, False, False, False], dangerString, modTimeOut)

	try:
		previousPosition = getPosition(keyPress = keyPress)
		previousHealth = getHealth()
		patience = 0
		escapeSpell = True
		movementSpeed = False
		speed = walkSpeed
		movementChoice = 1
		if (character == "Archer"):
			for i in range(len(pointOfInterest)):
				if (pointOfInterest[i].coordinates[1] == -1):
					escapeSpell = False
			dangerString = movementSpell(dangerString = dangerString, keyPress = keyPress)
		else:
			escapeSpell = False
		if (sprint):
			movementChoice = 3
			speed = sprintSpeed
		if (waterLevel != 0.0):
			speed = swimSpeed
		if (level == 110 and proximity([978.0, 73.0, -671.0], radius = 999, abortRadius = 499999, keyPress = keyPress)):
			dangerString = repair(keyPress = keyPress, dangerString = dangerString, deposit = False)
		while (True):
			if (movementSpeed and escapeSpell):
				time.sleep(0.5)
				dangerString = movementSpell(dangerString = dangerString, keyPress = keyPress)
				movementSpeed = False
			elif (escapeSpell):
				movementSpeed = True
			for i in range(len(pointOfInterest)):
				if (durability[0] and level == 110):
					dangerString = repair(keyPress, dangerString = dangerString)
					durability[0] = False
					break
				checkpoint = pointOfInterest[i].coordinates
				if (checkpoint[1] == -1.0):														#Archer escape spell
					dangerString = movementSpell(dangerString, checkpoint[2], checkpoint[0], keyPress = keyPress)
				elif (checkpoint[1] == -2.0):													#Assassin vanish + hop
					changeRotation(targetPitch = checkpoint[0], targetYaw = checkpoint[2])
					dangerString = movementSpell(dangerString = dangerString, keyPress = keyPress)
					dangerString = hop(keyPress, dangerString)
				elif (checkpoint[1] == -3.0):													#Assassin sneak for fine adjustment
					changeRotation(targetYaw = checkpoint[2])
					currentPosition = getPosition(keyPress = keyPress)
					if (currentPosition[0] < checkpoint[0]):
						startMove(movementStatus = 2, keyPress = keyPress)
					while (currentPosition[0] < checkpoint[0]):
						currentPosition = getPosition(keyPress = keyPress)
					stopMove(keyPress = keyPress)
				elif (checkpoint[1] == -4.0):													#Assassin vanish predetermined
					changeRotation(destination = [482.5, 95.0, -518.0], targetPitch = checkpoint[0])
					dangerString = movementSpell(dangerString = dangerString, keyPress = keyPress)
				elif (checkpoint[1] == -5.0):													#Assassin quick vanish + hop
					changeRotation(targetPitch = checkpoint[0], targetYaw = checkpoint[2])
					dangerString = movementSpell(dangerString = dangerString, keyPress = keyPress)
					py.press('2')
					dangerString = hop(keyPress, dangerString)
				elif (checkpoint[1] == -6.0):													#Assassin vanish
					changeRotation(targetPitch = checkpoint[0], targetYaw = checkpoint[2])
					dangerString = movementSpell(dangerString = dangerString, keyPress = keyPress)
				elif (checkpoint[1] == -7.0):													#Assassin hop
					changeRotation(targetPitch = checkpoint[0], targetYaw = checkpoint[2])
					dangerString = hop(keyPress, dangerString)
				elif (not pointOfInterest[i].rooted):
					if (not pointOfInterest[i].guidance):
						if (character == "Assassin" and not proximity(checkpoint, radius = pointOfInterest[i].radius, keyPress = keyPress)):
							dangerString = leap(checkpoint, dangerString, keyPress)
						while(not proximity(checkpoint, keyPress = keyPress)):
							healthDanger = checkVitals(dangerString, previousHealth, keyPress = keyPress)
							previousHealth = healthDanger[0]
							dangerString = healthDanger[1]
							dangerString = checkModerators(keyPress, dangerString)
							if (previousHealth[1] == 1):
								break
							changeRotation(checkpoint, keyPress = keyPress)
							#if (character == "Assassin"):
							#	movementSpell(swim = swim)
							seconds = eta(checkpoint, speed, keyPress = keyPress)
							startMove(movementChoice, keyPress)
							time.sleep(seconds)
							stopMove(keyPress, swim = True)
						if (previousHealth[1] == 1):
							break
						while(not proximity(checkpoint, radius = pointOfInterest[i].radius, keyPress = keyPress)):
							healthDanger = checkVitals(dangerString, previousHealth, keyPress = keyPress)
							previousHealth = healthDanger[0]
							dangerString = healthDanger[1]
							dangerString = checkModerators(keyPress, dangerString)
							if (previousHealth[1] == 1):
								break
							changeRotation(checkpoint, keyPress = keyPress)
							#if (character == "Assassin"):
							#	movementSpell(swim = swim)
							if (keyPress[2] == True):
								seconds = eta(checkpoint, speed, keyPress = keyPress)
								startMove(movementChoice, keyPress)
								time.sleep(seconds)
								stopMove(keyPress, swim = True)
							else:
								seconds = eta(checkpoint, sneakSpeed, keyPress = keyPress)
								startMove(2, keyPress)
								time.sleep(seconds)
								stopMove(keyPress, swim = True)
						if (previousHealth[1] == 1):
							break
					else:
						offTarget = False
						if (character == "Assassin" and not proximity(checkpoint, radius = pointOfInterest[i].radius, keyPress = keyPress)):
							dangerString = leap(checkpoint, dangerString, keyPress)
						if (not proximity(checkpoint, keyPress = keyPress)):
							changeRotation(checkpoint, 39.0, keyPress = keyPress)
							startMove(movementChoice, keyPress)
							offTarget = True
						while(not proximity(checkpoint, keyPress = keyPress)):
							healthDanger = checkVitals(dangerString, previousHealth, keyPress = keyPress)
							previousHealth = healthDanger[0]
							dangerString = healthDanger[1]
							dangerString = checkModerators(keyPress, dangerString)
							if (previousHealth[1] == 1):
								break
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
						if (previousHealth[1] == 1):
							break
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
							healthDanger = checkVitals(dangerString, previousHealth, keyPress = keyPress)
							previousHealth = healthDanger[0]
							dangerString = healthDanger[1]
							dangerString = checkModerators(keyPress, dangerString)
							if (previousHealth[1] == 1):
								break
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
						if (previousHealth[1] == 1):
							break
						if (slowMovement != 0):
							stopMove(keyPress, swim = True)
				if (pointOfInterest[i].farmable):
					changeRotation(checkpoint, keyPress = keyPress)
					if (speedBomb[0]):
						if (time.time() - 30.0 - farmTime/2.0 < pointOfInterest[i].previousTime):
							time.sleep(30.0 + farmTime/2.0 - time.time() + pointOfInterest[i].previousTime)
					else:
						if (time.time() - 60.0 - farmTime < pointOfInterest[i].previousTime):
							time.sleep(60.0 + farmTime - time.time() + pointOfInterest[i].previousTime)
					pointOfInterest[i].previousTime = time.time()
					#if (not speedBomb[0]):
					#	time.sleep(pointOfInterest[i].delay)
					if (shields):
						stopMove(keyPress, shield = True, swim = True)
					if (pointOfInterest[i].movement):
						py.keyDown('s')
						time.sleep(0.1)
						upcomingTime = time.time() + 5
						while (not proximity([470.3, 96.0, -530.3], radius = 0.0002, keyPress = keyPress)):
							if (time.time() > upcomingTime):
								break
						py.keyUp('s')
						changeRotation(checkpoint, keyPress = keyPress)
					drawBlood = previousHealth.copy()
					
					healthDanger = farm(previousHealth, durability, speedBomb, speedClock, leftClick, farmTime + pointOfInterest[i].delay, pointOfInterest[i].rapidClick, keyPress = keyPress, dangerString = dangerString)
					previousHealth = healthDanger[0]
					dangerString = healthDanger[1]
					if (previousHealth[1] == 1):
						break
					if (previousHealth[1] + 1 == drawBlood[1]):
						tryAttack = True
						enemyHealthRead = enemyHealth()
					if (tryAttack and enemyHealthRead < 100000):
						py.press('1')
						py.click(clicks = 3, interval = 0.1)
						enemyHealthRead = enemyHealth()
						if (enemyHealthRead > 0 and enemyHealthRead < 100000):
							attack(keyPress = keyPress)
						tryAttack = False
						enemyHealthRead = 1

					if (shields):
						startMove(keyPress = keyPress, shield = True)
				if (not speedBomb[0]):
					time.sleep(pointOfInterest[i].delay)
	except KeyboardInterrupt:
		stopMove(keyPress)
		print("\nMission Aborted")

#distanceList = []
#directionsList = []
#server([False, False, False, False])
#main()
#calculateTheta([476.0, 95.0, -524.0], [471.0, 96.0, -531.0], True)
#getVisual(node = True)
#getPosition(display = True)
#getDirection(True)
#getVisual(True)
#getHealth(display = True)
#calculateSpeed(movementStatus = 1, display = True)
#repair([False, False, False, False], "", deposit = True)
#print(enemyHealth())
#print(checkStream())
#print(checkModerators([False, False, False, False], ""))
#fixTool([998.5, 76.5, -711.5], [False, False, False, False])
#calculateSensitivity(display = True)

"""
up = True
for a in range(91):
	angleNumber = a * 1.0
	downAngle = 0.0
	if (up):
		downAngle = 180.0
		up = False
	else:
		up = True
	distance = calculateDistance(angleNumber, downAngle)
	distanceList.append(distance)
	angle = getDirection()
	directionsList.append(angle[1])

for b in range(len(distanceList)):
	print(distanceList[b])

for c in range(len(directionsList)):
	print(directionsList[c])
"""
"""
py.hotkey('alt', 'tab')
time.sleep(1)
py.press('enter')
movementSpell()
calculateSpeed(display = True, movementStatus = 1)
#calculateSensitivity(display = True)
py.keyUp('space')
py.press('t')
py.hotkey('alt', 'tab')
"""