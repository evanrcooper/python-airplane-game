from PIL import Image

def convertImage(name):
    img = Image.open(name)
    img = img.convert("RGBA")
  
    datas = img.getdata()
  
    newData = []
    
    threshold = 180

    for item in datas:
        if item[0] >= threshold and item[1] >= threshold and item[2] >= threshold:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
  
    img.putdata(newData)
    img.save("./New.png", "PNG")
    print("Successful")

convertImage("imagesBefore/flower.png")