import urllib2
import ctypes

img = urllib2.urlopen('http://unsplash.it/1920/1080/?random')
localFile = open('Unsplash_random.jpg', 'wb')
localFile.write(img.read())
localFile.close()

SPI_SETDESKWALLPAPER = 20 
ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, "Unsplash_random.jpg" , 0)
