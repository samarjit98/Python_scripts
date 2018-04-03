from PIL import Image

#load image using Pillow (PIL)

img = Image.open('suman.png').convert('1') # '1' mode for bkack and white image
pixels = img.load()

#pixel[x, y] == 0 for black/dark

xlist = []
ylist = []
for y in range(img.size[1]):
    for x in range(img.size[0]):
        if pixels[x, y] == 0:
            xlist.append(x)
            ylist.append(y)

'''
list of x and y coordiantes of all black/dark pixels
'''

#4 corners of the black square
xleft = min(xlist)
xright = max(xlist)
ytop = min(ylist)
ybot = max(ylist)

#print(xlist)
#print(ylist)

print("Coordinates from top left corner are:")

print(xleft, ytop)
print(xright, ytop)
print(xleft, ybot)
print(xright, ybot)
