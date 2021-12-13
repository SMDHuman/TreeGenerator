from graphics import *
import random
import math

class Branch():
	def __init__(self, pos, degree, width, height):
		self.posA = pos
		self.degree = degree
		self.width = width
		self.height = height

		self.posB = [self.posA[0] + math.cos(math.radians(self.degree)) * self.height, self.posA[1] + math.sin(math.radians(self.degree)) * self.height]

	def lerp(self, t):
		x = (self.posB[0] - self.posA[0]) * t + self.posA[0]
		y = (self.posB[1] - self.posA[1]) * t + self.posA[1]
		return([x, y])
strHeight = 150
strWidth =  10   #Başlangıçtaki gövdenin kalınlığı
wDecrease = 2     #Her dal büyüdüğünde ne kada kısalıcak
hDecrease = 20
branchNum = strWidth // wDecrease   #Kaç kere dal büyütücek
branchRange = [2, 4]  #Min ve Max dal çıkarma sayısı
rotation = 40 #Dönüş açısı


winX = 600
winY = 600
win =  GraphWin("Tree Generator", 600, 600, autoflush = False)
win.setCoords(-winX/2, 0, winX/2, winY)
win.setBackground("gray")



while(win.isClosed() == 0):
	win.clear()
	win.update()
	
	colorT = 1/3
	treeColor = [int(92 * colorT), int(55 * colorT), int(27 * colorT)]
	colorChange = 8

	tree = [[Branch([0, 0], 90, strWidth, strHeight)]]

	width = strWidth
	height = strHeight
	#Dalları oluştur
	for i in range(branchNum):
		width -= wDecrease
		height -= hDecrease

		bufBranchs = []
		for branch in tree[i]:

			for n in range(random.randint(branchRange[0], branchRange[1])):

				bufBranchs.append(Branch(branch.lerp(random.randint(0, 100)/100), branch.degree + random.randint(-rotation, rotation), width, height))
		tree.append(bufBranchs)


	#Dalları çiz
	for branchs in tree:
		for i in range(3):
			treeColor[i] += colorChange
			if(treeColor[i] < 0):
				treeColor[i] = 0
			elif(treeColor[i] > 255):
				treeColor[i] = 255
		for branch in branchs:
			line = Line(Point(branch.posA[0], branch.posA[1]), 
						Point(branch.posB[0], branch.posB[1]))
			line.setWidth(branch.width)
			line.setFill(color_rgb(treeColor[0], treeColor[1], treeColor[2]))
			line.draw(win)
	win.update()
	win.getMouse()