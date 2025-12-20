import os
from PIL import Image
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor

# File manipulation
fileDir = r"D:\Chaos game\50k"
saveDir = r"D:\Chaos game\50k_jpg"
os.makedirs(saveDir, exist_ok=True)
os.chdir(fileDir) # changes directory
fileList = os.listdir() # list of files we have in directory 

def convert_eps(imageFile):
    filePath = os.path.join(fileDir, imageFile)
    
    if not os.path.isfile(imageFile):
        return
        
    f, e = os.path.splitext(imageFile)
    
    if e.lower() == ".eps":
        try:
            # image manipulation 
            im = Image.open(filePath)
            if im.mode != "RGB":
                im = im.convert("RGB")
            outFile = f + ".jpg"
            outPath = os.path.join(saveDir, outFile)
            im.save(outPath, quality=95, dpi=(300,300))
        except Exception as err:
            print(f"Error converting {imageFile}: {err}")
            
with ThreadPoolExecutor(max_workers=6) as executor:
    list(tqdm(executor.map(convert_eps, fileList), total=len(fileList), desc="Converting EPS -> JPG"))
        





