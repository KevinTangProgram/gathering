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

profession = "Fishing"
level = 110
character = "Assassin"

speedBomb = False
sprint = True
farmTime = 6.5
leftClick = False
shields = False
waterLevel = 0.0
vitals = True

sprintSpeed = 23.03 #(Assassin slider)		#23.37(Assassin slider)			#22.472(Assassin weathered)		#9.375(Archer)
walkSpeed = 17.978 #(Assassin slider)		#18.0 (Assassin weathered)		#7.90(Archer)
sneakSpeed = 5.393 #(Assassin slider)		#5.188(Assassin weathered)		#2.37(Archer)
swimSpeed = 2.442
sensitivity = 20.0/9.0
pointOfInterest = []
directory = os.getcwd() + '\\Images\\'

class Node:
	def __init__(self, coordinates, guidance = False, farmable = True, tickskipping = False, radius = 16.0, delay = 0.0, rapidClick = False, rooted = False):
		self.coordinates = coordinates
		self.farmable = farmable
		self.guidance = guidance
		self.delay = delay
		self.tickskipping = tickskipping
		self.radius = radius
		self.rapidClick = rapidClick
		self.rooted = rooted
		self.previousTime = 0.0
		if (coordinates[1] > 0):
			pointOfInterest.append(self)
		elif (coordinates[1] == -1 and character == "Archer"):
			pointOfInterest.append(self)
		elif (coordinates[1] == -2 and character == "Assassin"):
			pointOfInterest.append(self)

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
	if (level == 100):
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
		Node([779.0, 148.0, -993.0], guidance = True, farmable = False, radius = 1.0)
		Node([776.0, 148.0, -993.0], tickskipping = True)
		Node([779.0, 148.0, -995.0], tickskipping = True)
		Node([783.0, 148.0, -993.0])
		Node([778.0, 148.0, -985.0], guidance = True, farmable = False, radius = 1.0)
		Node([775.0, 148.0, -985.0], tickskipping = True)
		Node([776.0, 148.0, -987.0], tickskipping = True)
		Node([778.5, 148.0, -988.5], tickskipping = True)
		Node([781.0, 148.0, -986.0], tickskipping = True)
		Node([781.0, 148.0, -984.0])
		Node([776.0, 149.0, -970.0], guidance = True, farmable = False, radius = 1.0)
		Node([779.0, 149.0, -970.0], tickskipping = True)
		Node([776.0, 149.0, -967.0], tickskipping = True)
		Node([773.0, 149.0, -969.0], tickskipping = True)
		Node([772.5, 126.0, -971.0])
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
	py.moveTo(850, 410)
	time.sleep(0.5)
	py.click()
	py.press('backspace', presses = 2)
	py.moveTo(960, 315)
	time.sleep(0.5)
	py.click()
	py.press('enter')

password()
startup()

def server(movementStatus = 0, swim = [False]):
	stopMove(movementStatus)
	if (swim[0] == True):
		py.keyUp('space')
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
					startMove(movementStatus)
					if (swim[0] == True):
						py.keyDown('space')
					abort(True, movementStatus, swim = swim)
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

def lobby(movementStatus = 0, swim = [False]):
	print("\nKicked to lobby.", end = "")
	while (True):
		check = py.locateOnScreen(directory + 'craftingTable.png', region=(1080, 390, 40, 40))
		try:
			check.left
			startMove(movementStatus)
			if (swim[0] == True):
				py.keyDown('space')
			abort(True, movementStatus, swim = swim)
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

def checkVitals(previousHealth = [1, 1], movementStatus = 0, swim = [False]):
	currentHealth = getHealth(previousHealth, movementStatus)
	if (vitals and previousHealth[0] > currentHealth[0]):
		print("\nHealth dropped from ", previousHealth[0], " to ", currentHealth[0], end = ".")
		abort(True, movementStatus, swim = swim)
		currentHealth = getHealth(currentHealth)
	elif (currentHealth[0]/currentHealth[1] < 0.1):
		print("\nHealth dropped to below 10%.")
		abort(movementStatus = movementStatus, swim = swim)
	return currentHealth

def eta(destination, speed, movementStatus = 0, swim = [False]):
	currentPosition = getPosition(movementStatus = movementStatus, swim = swim)
	distance = math.sqrt((destination[0] - currentPosition[0])**2 + (destination[2] - currentPosition[2])**2)
	return distance / speed

def movementSpell(targetPitch = 90.0, targetYaw = -360, swim = [False]):
	if (character == "Archer"):
		changeRotation(targetPitch = targetPitch, targetYaw = targetYaw)
		py.press('1')
		py.click(clicks = 3, interval = 0.1)
		time.sleep(1)
		previousY = getPosition(swim = swim)[1]
		currentY = 0.0
		while(True):
			currentY = getPosition(swim = swim)[1]
			if (currentY == previousY):
				currentY = getPosition(swim = swim)[1]
				if (currentY == previousY):
					break
			previousY = currentY
		if (not shields):
			py.press('2')
	elif (character == "Assassin"):
		py.press('1')
		previousPosition = getPosition(swim = swim)
		py.click(button = 'right', clicks = 3, interval = 0.1)
		while(True):
			currentPosition = getPosition(swim = swim)
			if (previousPosition == currentPosition):
				py.rightClick()
			else:
				break
		previousY = getPosition(swim = swim)[1]
		currentY = 0.0
		while(True):
			currentY = getPosition(swim = swim)[1]
			if (currentY == previousY):
				currentY = getPosition(swim = swim)[1]
				if (currentY == previousY):
					break
			previousY = currentY

def startMove(movementStatus = 0, walkingStick = False, shield = False):	# 0 = not moving | 1 = walking | 2 = sneaking | 3 = sprinting
	if (movementStatus == 3):
		py.keyDown('ctrlleft')
	elif (movementStatus == 2):
		py.keyDown('shift')
	if (movementStatus > 0):
		py.keyDown('w')
	if (walkingStick or shield):
		py.press('1')
	if (shield):
		py.click()
		time.sleep(0.1)
		py.click()
		time.sleep(0.1)
		py.rightClick()

def stopMove(movementStatus = 0, walkingStick = False, shield = False):
	if (movementStatus > 0):
		py.keyUp('w')
	if (movementStatus == 2):
		py.keyUp('shift')
	elif (movementStatus == 3):
		py.keyUp('ctrlleft')
	if (walkingStick or shield):
		py.press('2')

def rotate(yaw = 0.0, pitch = 0.0, delay = 0.3):
	yaw *= sensitivity
	pitch *= sensitivity
	py.drag(yaw, pitch, delay, button = 'middle')

def farm(left = True, delay = 7.0, autoClicker = False):
	py.press('2')
	if (speedBomb):
		delay /= 2.0
	num = random.random()
	if (num < 0.5):
		py.keyDown("shift")
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

def getPosition(display=False, movementStatus = 0, iterations = 0, swim = [False]):
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
		if (swim[0] == False and positionCoordinates[1] < waterLevel):
			swim[0] = True
			py.keyDown('space')
		elif (swim[0] == True and positionCoordinates[1] > waterLevel):
			swim[0] = False
			py.keyUp('space')
		return positionCoordinates
	except:
		if (iterations > 1):
			if (swim[0] == True):
				print("\nFailed to receive position coordinates.", end = "")
				abort(False, movementStatus, swim = swim)
			else:
				stopMove(movementStatus)
				time.sleep(0.5)
				py.hotkey('alt', 'tab')
				print("\nFailed to receive position coordinates on", time.ctime(time.time()), end = ". ")
				maskpass.askpass(prompt="Press enter to resume the program.", mask="")
				startup()
				if (character == "Archer"):
					movementSpell(swim = swim)
				startMove(movementStatus)
			return getPosition(movementStatus = movementStatus, swim = swim)
		else:
			if (open(directory + "lobbyImage1.png", "rb").read() == open(directory + "unprocessedCoordinates.png", "rb").read()):
				stopMove(movementStatus)
				if (swim[0] == True):
					py.keyUp('space')
				time.sleep(30)
				screenshot = py.screenshot(region=(50, 158, 358, 16))
				screenshot.save(directory + 'unprocessedCoordinates.png')
				if (open(directory + "lobbyImage3.png", "rb").read() == open(directory + "unprocessedCoordinates.png", "rb").read() or open(directory + "lobbyImage5.png", "rb").read() == open(directory + "unprocessedCoordinates.png", "rb").read()):
					startMove(movementStatus)
					if (swim[0] == True):
						py.keyDown('space')
				else:
					lobby(movementStatus, swim)
					return getPosition(movementStatus = movementStatus, swim = swim)
			if (open(directory + "lobbyImage3.png", "rb").read() == open(directory + "unprocessedCoordinates.png", "rb").read() or open(directory + "lobbyImage5.png", "rb").read() == open(directory + "unprocessedCoordinates.png", "rb").read()):
				server(movementStatus, swim)
				return getPosition(movementStatus = movementStatus, swim = swim)
			return getPosition(movementStatus = movementStatus, iterations = iterations + 1, swim = swim)

def getDirection(display=False, movementStatus = 0, iterations = 0, swim = [False]):
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
		if (iterations > 1):
			if (swim[0] == True):
				print("\nFailed to receive direction angles.", end = "")
				abort(False, movementStatus, swim = swim)
			else:
				stopMove(movementStatus)
				time.sleep(0.5)
				py.hotkey('alt', 'tab')
				print("\nFailed to receive direction angles on", time.ctime(time.time()), end = ". ")
				maskpass.askpass(prompt="Press enter to resume the program.", mask="")
				startup()
				if (character == "Archer"):
					movementSpell(swim = swim)
				startMove(movementStatus)
			return getDirection(movementStatus = movementStatus, swim = swim)
		else:
			if (open(directory + "lobbyImage2.png", "rb").read() == open(directory + "unprocessedDirection.png", "rb").read()):
				stopMove(movementStatus)
				if (swim[0] == True):
					py.keyUp('space')
				time.sleep(30)
				screenshot = py.screenshot(region=(78, 212, 447, 16))			#1.12
				screenshot.save(directory + 'unprocessedDirection.png')
				if (open(directory + "lobbyImage4.png", "rb").read() == open(directory + "unprocessedDirection.png", "rb").read() or open(directory + "lobbyImage6.png", "rb").read() == open(directory + "unprocessedDirection.png", "rb").read()):
					startMove(movementStatus)
					if (swim[0] == True):
						py.keyDown('space')
				else:
					lobby(movementStatus, swim)
					return getDirection(movementStatus = movementStatus, swim = swim)
			if (open(directory + "lobbyImage4.png", "rb").read() == open(directory + "unprocessedDirection.png", "rb").read() or open(directory + "lobbyImage6.png", "rb").read() == open(directory + "unprocessedDirection.png", "rb").read()):
				server(movementStatus, swim)
				return getDirection(movementStatus = movementStatus, swim = swim)
			return getDirection(movementStatus = movementStatus, iterations = iterations + 1, swim = swim)

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
			if (waterLevel == 0.0):
				coords[1] += yLevel
			else:
				coords[1] = waterLevel + yLevel
			coords[2] += 0.5
			print("Node(", coords, ")")
		return coords
	except:
		return []

def getHealth(previousHealth = [1, 1], movementStatus = 0, iterations = 0, display = False):
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

def calculateSpeed(seconds = 3.0, movementStatus = 0, display=False, swim = [False]):
	if (movementStatus == 3):
		py.keyDown('ctrlleft')
	elif (movementStatus == 2):
		py.keyDown('shift')
	if (movementStatus > 0):
		py.keyDown('w')
	firstPoint = getPosition(movementStatus = movementStatus, swim = swim)
	time.sleep(seconds)
	secondPoint = getPosition(movementStatus = movementStatus, swim = swim)
	if (movementStatus > 0):
		py.keyUp('w')
	if (movementStatus == 3):
		py.keyUp('ctrlleft')
	if (movementStatus == 2):
		py.keyUp('shift')
	r2 = math.sqrt((secondPoint[0] - firstPoint[0])**2 + (secondPoint[2] - firstPoint[2])**2)
	if (display):
		print(r2/seconds)
	return r2/seconds

def calculateSensitivity(pixels = 100.0, display=False, swim = [False]):
	py.drag(0, -1000, 0.3, button = 'middle')
	firstAngle = getDirection(swim = swim)
	py.drag(0, pixels, 0.3, button = 'middle')
	secondAngle = getDirection(swim = swim)
	if (display):
		print(pixels/(secondAngle[1] - firstAngle[1]))
	return pixels/(secondAngle[1] - firstAngle[1])

def changeRotation(destination = [0.0, 0.0, 0.0], targetPitch = -91.0, targetYaw = -360.0, roboticMovement = False, movementStatus = 0, swim = [False]):
	currentDirection = getDirection(movementStatus = movementStatus, swim = swim)
	currentPosition = getPosition(movementStatus = movementStatus, swim = swim)
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

def proximity(destination, radius = 16.0, abortRadius = 2500.0, movementStatus = 0, swim = [False]):	
	currentPosition = getPosition(movementStatus = movementStatus, swim = swim)
	r2 = (destination[0]-currentPosition[0])**2 + (destination[1]-currentPosition[1])**2 + (destination[2]-currentPosition[2])**2
	if (r2 < radius):
		return True
	if (r2 > abortRadius):
		destination = [295.5, 34.0, 321.5]
		r2 = (destination[0]-currentPosition[0])**2 + (destination[1]-currentPosition[1])**2 + (destination[2]-currentPosition[2])**2
		if (r2 < 10000.0):
			stopMove(movementStatus)
			if (swim[0] == True):
				py.keyUp('space')
			lobby(movementStatus, swim)
		else:
			print("Node out of range.")
			abort(False, movementStatus, swim = swim)
	return False

def jump(movementStatus = 2, check = True, swim = [False]):
	currentPosition = getPosition(movementStatus = 2, swim = swim)
	visualCoords = getVisual()
	if ((visualCoords != [] and visualCoords[1] >= int(currentPosition[1])) or not check):
		if (swim[0] == True):
			swim[0] = False
			py.keyUp('space')
		py.keyDown('space')
		py.keyUp('space')

def leap(destination, swim = [False]):
	currentPosition = getPosition(swim = swim)
	distance = math.sqrt((destination[0]-currentPosition[0])**2 + (destination[2]-currentPosition[2])**2)
	jumpAngle = 90.0
	if (distance > 8.75):
		return
	elif (distance > 7.9):
		polynomial = [-0.0035843480, -0.1192294472, 7.7966948006]
		#polynomial = [-0.0001627924, -0.0095179927, -0.2007563758, 6.0709137802]
		polynomial[2] -= distance
		answers = np.roots(polynomial)
		for i in answers:
			if (i > -20.0 and i < 0.0):
				jumpAngle = i
				break
	elif (distance > 3.0):
		polynomial = [-0.0000112392, -0.0030250284, -0.0913002657, 8.0828211019]
		#polynomial = [-0.0000108678, -0.0028506290, -0.0929670533, 6.7921445423]
		polynomial[3] -= distance
		answers = np.roots(polynomial)
		for i in answers:
			if (i > -75.0 and i < -20.0):
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
	changeRotation(targetPitch = jumpAngle, targetYaw = directionAngle, swim = swim)
	movementSpell(swim = swim)

def abort(temporary = False, movementStatus = 0, iterations = 0, swim = [False]):
	if (swim[0] == True):
		py.keyUp('space')
	stopMove(movementStatus)
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
		if (swim[0] == True):
			py.keyDown('space')
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
			if (character == "Archer" and int(futureTime - time.time()) % 14 == 0):
				startMove(shield = True)
				time.sleep(1)
			if (priorHealth[0] > presentHealth[0]):
				if (iterations > 9):
					print("Damage taken too many times.", end = "")
					abort(swim = swim)
				else:
					print("\nHealth dropped from ", priorHealth[0], " to ", presentHealth[0], end = ".")
					abort(True, movementStatus, iterations + 1, swim = swim)
				return
			else:
				priorHealth = presentHealth
		if (character == "Archer"):
			movementSpell(swim = swim)
		startMove(movementStatus)
		print("Program resumed on", time.ctime(time.time()))
	else:
		py.hotkey('alt', 'tab')
		exit()

def calculateDistance(targetPitch, targetYaw, display = False):
	distance = -0.002*((targetPitch + 20.0)**2) + 7.5
	print("Predicted Distance: ", distance)
	pointOne = getPosition()
	changeRotation(targetPitch = targetPitch, targetYaw = targetYaw)
	movementSpell()
	time.sleep(3)
	pointTwo = getPosition()
	r2 = math.sqrt((pointTwo[0] - pointOne[0])**2 + (pointTwo[2] - pointOne[2])**2)
	if (display):
		print("(", targetPitch,  ", ",  r2, ")")
	return r2

def main():
	swim = [False]
	try:
		previousPosition = getPosition(swim = swim)
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
			movementSpell(swim = swim)
		else:
			escapeSpell = False
		if (sprint):
			movementChoice = 3
			speed = sprintSpeed
		if (waterLevel != 0.0):
			speed = swimSpeed
		while (True):
			if (movementSpeed and escapeSpell):
				time.sleep(0.5)
				movementSpell(swim = swim)
				movementSpeed = False
			elif (escapeSpell):
				movementSpeed = True

			for i in range(len(pointOfInterest)):
				checkpoint = pointOfInterest[i].coordinates
				if (checkpoint[1] == -1.0):
					movementSpell(checkpoint[2], checkpoint[0], swim = swim)
				elif (checkpoint[1] == -2.0):
					movementSpell(checkpoint[2], checkpoint[0], swim = swim)
				elif ((i == 0 or not pointOfInterest[i].tickskipping and i != 0 and not pointOfInterest[i - 1].tickskipping) and not pointOfInterest[i].rooted):
					if (not pointOfInterest[i].guidance):
						if (character == "Assassin" and not proximity(checkpoint, radius = pointOfInterest[i].radius, swim = swim)):
							leap(checkpoint, swim)
						while(not proximity(checkpoint, swim = swim)):
							previousHealth = checkVitals(previousHealth, swim = swim)
							changeRotation(checkpoint, swim = swim)
							#if (character == "Assassin"):
							#	movementSpell(swim = swim)
							seconds = eta(checkpoint, speed, swim = swim)
							startMove(movementChoice)
							time.sleep(seconds)
							stopMove(movementChoice)
						while(not proximity(checkpoint, radius = pointOfInterest[i].radius, swim = swim)):
							previousHealth = checkVitals(previousHealth, swim = swim)
							changeRotation(checkpoint, swim = swim)
							#if (character == "Assassin"):
							#	movementSpell(swim = swim)
							if (swim):
								seconds = eta(checkpoint, speed, swim = swim)
								startMove(movementChoice)
								time.sleep(seconds)
								stopMove(movementChoice)
							else:
								seconds = eta(checkpoint, sneakSpeed, swim = swim)
								startMove(2)
								time.sleep(seconds)
								stopMove(2)
					else:
						offTarget = False
						if (character == "Assassin" and not proximity(checkpoint, radius = pointOfInterest[i].radius, swim = swim)):
							leap(checkpoint, swim)
						if (not proximity(checkpoint, swim = swim)):
							changeRotation(checkpoint, 39.0, swim = swim)
							startMove(movementChoice)
							offTarget = True
						while(not proximity(checkpoint, movementStatus = movementChoice, swim = swim)):
							previousHealth = checkVitals(previousHealth, movementStatus = movementChoice, swim = swim)
							currentPosition = changeRotation(checkpoint, 39.0, movementStatus = movementChoice, swim = swim)
							if (swim[0] == False):
								jump(movementChoice, swim = swim)
							if (currentPosition[0] == previousPosition[0] and currentPosition[2] == previousPosition[2]):
								patience += 1
							else:
								patience = 0
							previousPosition = currentPosition
							if (patience > 9):
								print("Character in a trapped condition.", end = "")
								abort(movementStatus = movementChoice, swim = swim)
						if (offTarget):
							stopMove(movementChoice)

						slowMovement = 0
						if (not proximity(checkpoint, radius = pointOfInterest[i].radius, swim = swim)):
							slowMovement = 2
							if (swim):
								slowMovement = movementChoice
							changeRotation(checkpoint, 39.0, swim = swim)
							startMove(slowMovement)
						currentTime = time.time()
						while(not proximity(checkpoint, radius = pointOfInterest[i].radius, movementStatus = slowMovement, swim = swim)):
							if (currentTime + 5 < time.time() and swim[0] == False):
								jump(slowMovement, False, swim = swim)
								currentTime = time.time()
							previousHealth = checkVitals(previousHealth, slowMovement, swim = swim)
							currentPosition = changeRotation(checkpoint, 39.0, movementStatus = slowMovement, swim = swim)
							if (swim[0] == False):
								jump(slowMovement, swim = swim)
							if (currentPosition[0] == previousPosition[0] and currentPosition[2] == previousPosition[2]):
								patience += 1
							else:
								patience = 0
							previousPosition = currentPosition
							if (patience > 9):
								print("Character in a trapped condition.", end = "")
								abort(movementStatus = slowMovement, swim = swim)
						if (slowMovement != 0):
							stopMove(slowMovement)
				if (pointOfInterest[i].farmable):
					changeRotation(checkpoint, swim = swim)
					if (speedBomb):
						if (time.time() - 30.0 - farmTime/2.0 < pointOfInterest[i].previousTime):
							time.sleep(30.0 + farmTime/2.0 - time.time() + pointOfInterest[i].previousTime)
					else:
						if (time.time() - 60.0 - farmTime < pointOfInterest[i].previousTime):
							time.sleep(60.0 + farmTime - time.time() + pointOfInterest[i].previousTime)
					pointOfInterest[i].previousTime = time.time()
					if (not speedBomb):
						time.sleep(pointOfInterest[i].delay)
					if (shields):
						stopMove(shield = True)
					previousHealth = checkVitals(previousHealth, swim = swim)
					if (pointOfInterest[i].tickskipping):
						farm(leftClick, farmTime - 2, pointOfInterest[i].rapidClick)
					else:
						farm(leftClick, farmTime, pointOfInterest[i].rapidClick)
					if (shields):
						startMove(shield = True)
	except KeyboardInterrupt:
		if (swim[0] == True):
			py.keyUp('space')
		print("\nMission Aborted")

#distanceList = []
#directionsList = []

main()
#getVisual(node = True, yLevel = 0.0)
#getPosition(display = True)
#getDirection(True)
#getVisual(True)
#getHealth(display = True)
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