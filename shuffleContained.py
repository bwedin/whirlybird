from images import*
from copy import*
import random

def main():


    originalImage = FileImage('play13.jpeg')
    thisImage = FileImage('play13.jpeg')
    scramble(originalImage,thisImage,20,5)
    raw_input("press enter to quit")

def fillPixels(originalImage,image,tile,oldNumber,newNumber):
	height = image.getHeight()
	width = image.getWidth()
	tileWidth = width/tile
	tileHeight = height/tile
	oldX = (oldNumber%tileWidth)*tile
	oldY = (oldNumber/tileWidth)*tile
	newX = (newNumber%tileWidth)*tile
	newY = (newNumber/tileWidth)*tile
	for i in range(tile):
		for j in range(tile):
			oldRGB = originalImage.getPixel(oldX+i,oldY+j)
			image.setPixel(newX+i,newY+j,oldRGB)

def scramble(originalImage,image,tile,distance):
    height = image.getHeight()
    width = image.getWidth()
    numberOfTiles = (width*height)/(tile*tile)
    usedPixels = [0]*numberOfTiles
    newRange = ((2*distance)+1)**2/2
    print newRange
    tileShift = 2*distance+1
    tileWidth = width/tile
    tileHeight = height/tile
    image.show()

    for y in range(tileHeight):
    	#converts y row to proper entry in list (by row)
    	rowConv = y*tileWidth
    	for x in range(tileWidth):
    		notFound=1
    		gettingFilled = rowConv+x
    		spotCheck = gettingFilled - (tileWidth*distance+distance)
    		if spotCheck > -1 and usedPixels[spotCheck]==0:
    			fillPixels(originalImage,image,tile,spotCheck,gettingFilled)
    		else:
    			tried = range(-newRange,newRange+1)
    			while notFound:
    				if len(tried)==0:
    					newShift=gettingFilled
    					break
    				myRandom = random.choice(tried)
    				tried.remove(myRandom)
    				if myRandom>0:
    					random1 = (myRandom+distance)/tileShift
    					random2 = myRandom-(random1*tileShift)
    				if myRandom<0:
    					myRandom = abs(myRandom)
    					random1 = (myRandom+distance)/tileShift
    					random2 = -(myRandom-(random1*tileShift))
    					random1 = -random1
    				if myRandom==0:
    					random1=0
    					random2=0
    				newShift = gettingFilled + (tileWidth*random1+random2)
    				if newShift>-1 and newShift<(tileWidth*tileHeight):
    					notFound = usedPixels[newShift]

#     			print gettingFilled
#     			print " and "
#     			print newShift
#     			print myRandom
#     			print random1
#     			print random2
    			usedPixels[newShift]=1
    			fillPixels(originalImage,image,tile,newShift,gettingFilled)
    			if x==0:
    				print "----"
    				print y
    				print newShift%tileWidth
    image.show()


main()
