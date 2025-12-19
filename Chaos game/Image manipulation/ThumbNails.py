import os
from PIL import Image
# https://www.youtube.com/watch?v=tJxcKyFMTGo


fileDir = "D:/Chaos game"
os.chdir(fileDir) # changes directory
fileList = os.listdir() # list of files we have in directory 

# print(fileList)
# print(len(fileList))

imageFile = fileList[1]
print(imageFile)
print(os.stat(imageFile))

# im= Image.open(r"D:\Chaos game\50k\3 sides  50000 - iterations  ratio 0.1")



# print(im.format, im.size, im.mode)
