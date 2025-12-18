import os
from PIL import Image


fileDir = "D:/Chaos game/50k"
os.chdir(fileDir) # changes directory
fileList = os.listdir() # list of files we have in directory 

print(len(fileList))

# https://www.youtube.com/watch?v=tJxcKyFMTGo



# im= Image.open(r"D:\Chaos game\50k\3 sides  50000 - iterations  ratio 0.1")



# print(im.format, im.size, im.mode)
