import urllib2
import os, ctypes, sys

img = urllib2.urlopen('http://unsplash.it/1920/1080/?random')

filename = 'Unsplash_random.jpg'

localFile = open(filename, 'wb')
localFile.write(img.read())
localFile.close()

pathname = os.path.dirname(sys.argv[0])        
fullPath = (os.path.abspath(pathname))
path = os.path.join(fullPath, filename)

ctypes.windll.user32.SystemParametersInfoA(20, 0, path , 3)

