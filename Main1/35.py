#getting indiviual channels
from PIL import Image

img = Image.open('Cashless_Payment.jpg')
print(img.mode)#This one is for printing the mode of the image

r,b,g = img.split()
r.show()
g.show()
b.show()
