#Pillow

from PIL import Image

img = Image.open('Cashless_Payment.jpg')# For assigning image to variable
print(img.size)#for getting the size of the image
print(img.format)#for getting the format of the image

img.show()# to open the image

#Cropping the image
area = (100,100,300,375) #left upper right lower
cropped_image = img.crop(area)
cropped_image.show()