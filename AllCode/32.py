#Pillow

from PIL import Image

img = Image.open('Cashless_Payment.jpg')# For assigning image to variable
print(img.size)#for getting the size of the image
print(img.format)#for getting the format of the image

img.show()# to open the image
