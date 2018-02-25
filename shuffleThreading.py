from images import*
from copy import*

def main():


    originalImage = FileImage('play12.jpeg')
    thisImage = FileImage('play12.jpeg')
    bluescreen(originalImage,thisImage)
    raw_input("press enter to quit")

def bluescreen(originalImage,image):
    height = image.getHeight()
    width = image.getWidth()

    for y in range(height):
    	if y%14>8:
    		for x in range(width):
    			if x%14<8:
    				oldRGB = originalImage.getPixel(x,y)
    				image.setPixel(x,y,oldRGB)
    			else:
    				oldRGB = originalImage.getPixel(width-x-1,height-y-1)
    				image.setPixel(x,y,oldRGB)
    	else:
    		for x in range(width):
    			if x%14>=8:
    				oldRGB = originalImage.getPixel(x,y)
    				image.setPixel(x,y,oldRGB)
    			else:
    				oldRGB = originalImage.getPixel(width-x-1,height-y-1)
    				image.setPixel(x,y,oldRGB)


    image.show()


main()
