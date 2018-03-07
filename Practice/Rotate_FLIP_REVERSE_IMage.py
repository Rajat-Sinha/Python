#Basic Transformtion
from PIL import Image

img = Image.open('Cashless_Payment.jpg')
square_image = img.resize(250, 250) #for resizing the image
flip_image = img.transpose(Image.FLIP_LEFT_RIGHT) #for flipping the image\
rotate_image = img.transpose(Image.ROTATE_90)  #for Rotating the image

rotate_image.show()

