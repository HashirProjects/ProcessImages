import os
import cv2
import pickle

class processImgs():

	def __init__(self, colorCode , directory):
		self.colorCode = colorCode
		self.directory = directory

	def Fetch(self):

		self.processedImgs = []

		for img in os.listdir(self.directory):

			imgArrayForm = cv2.imread(os.path.join(self.directory,img),self.colorCode)
			self.processedImgs.append(imgArrayForm)

	def Resize(self, resolution):

		for img in self.processedImgs:

			try:

				self.processedImgs = cv2.resize(img, resolution)

			except Exception as e:

				raise e
				print ("One of your images was invalid")

	def Save(self):

		with open(os.path.join(self.directory,"ImgData"), "wb") as file:
			pickle.dump(self.processedImgs, file)

	def Load(self):

		with open(os.path.join(self.directory,"ImgData"), "rb") as file:
			self.processedImgs = pickle.load(file)

#shortcuts

def SaveAsArray(colorCode =1, directory):
	imgProcessor=processImgs(colorCode, directory)
	imgProcessor.Fetch()
	imgProcessor.Save()

def ResizeAndSaveAsArray(resolution = (100,100), colorCode =1, directory):
	imgProcessor=processImgs(colorCode, directory)
	imgProcessor.Fetch()
	imgProcessor.Resize(resolution)
	imgProcessor.Save()
