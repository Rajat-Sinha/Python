#Basic Transformation

from PIL import Image

img = Image.open('Cashless_Payment.jpg')
square_image = img.resize(250, 250)#for resize the image

flip_image = img.transpose(Image.FLIP_LEFT_RIGHT) #  for flipping the image
spin_image = img.transpose(Image.ROTATE_90) # for rotating the image 90 degree


img.show()
square_image.show()
flip_image.show()
spin_image.show()




