from images import*
from copy import*
import random

def main():


    originalImage = FileImage('Albert Dubois-Pillet - The Eminence in Winter, 1889 copy.jpg')
    thisImage = FileImage('Albert Dubois-Pillet - The Eminence in Winter, 1889 copy.jpg')
    scramble(originalImage,thisImage,20)
    raw_input("press enter to quit") 
    
def scramble(originalImage,image,number):          
    height = image.getHeight()
    width = image.getWidth()
    allPixels = range((width*height)/(number*number))
    random.shuffle(allPixels)
    print allPixels
    
    for y in range(height/number):
    	#converts y row to proper entry in list (by row)
    	rowConv = y*width/number
    	print rowConv
    	for x in range(width/number):
    		pixelConv = allPixels[rowConv+x]
    		print pixelConv
    		tileCount = width/number
    		pixelConv = (pixelConv%tileCount)*number + (pixelConv/tileCount)*(width*number)
    		for i in range(number):
    			for j in range(number):
    				oldRGB = originalImage.getPixel(pixelConv%width+i,pixelConv/width+j)
    				image.setPixel(x*number+i,y*number+j,oldRGB)
    image.show()
    

main() 