#Aweesome merge Effect
from PIL import Image


'''
img = Image.open('Cashless_Payment.jpg')
r,b,g = img.split()

new_img = Image.merge('RGB',(r,g,b))
new_img.show()

'''
img1 = Image.open('Cashless_Payment.jpg')
img2 = Image.open('Easy_haults.jpg')
r1,b1,g1 = img1.split()
r2,b2,g2 = img2.split()

new_image = Image.merge('RGB',(r1,g2,b1))
new_image.show()
