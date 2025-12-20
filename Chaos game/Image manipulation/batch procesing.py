import os
from PIL import Image
from tqdm import tqdm


# File manipulation
fileDir = r"D:\Chaos game\50k"
saveDir = r"D:\Chaos game\50k_jpg"
os.makedirs(saveDir, exist_ok=True)
os.chdir(fileDir) # changes directory
fileList = os.listdir() # list of files we have in directory 

for imageFile in tqdm(fileList, desc="Converting EPS -> JPG"):
    if os.path.isfile(imageFile):
        filePath = os.path.join(fileDir, imageFile)
        # print(filePath)
        f, e = os.path.splitext(imageFile)
        if e.lower() == ".eps":
            # image manipulation 
            im = Image.open(filePath)
            if im.mode != "RGB":
                im = im.convert("RGB")
            outFile = f + ".jpg"
            outPath = os.path.join(saveDir, outFile)
            print(outFile)

            im.save(outPath, quality=95, dpi=(300,300))
            print("Saved: ", outPath)
            





