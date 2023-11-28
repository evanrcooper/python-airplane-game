from PIL import Image
from rembg import remove

def convertImageRemove(path, name, filetype):
    img = Image.open(path+name+filetype)
    img = remove(img)
    img.save("./imagesAfter/"+name+"_NEW.png", "PNG")
    print("Successfully Edited: ", name)

convertImageRemove("imagesBefore/", "flower", ".png")
convertImageRemove("imagesBefore/", "fish", ".png")
# convertImageRemove("imagesBefore/", "person", ".png")
convertImageRemove("imagesBefore/", "shoes", ".png")