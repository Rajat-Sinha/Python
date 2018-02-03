#Combinning image together
from PIL import Image

first_image = Image.open('Cashless_Payment.jpg')
sec_image = Image.open('Icon4.jpg')

area = (100,100,356,356) # 356-100 must be equal to the size of the sec_image
first_image.paste(sec_image,area)
first_image.show()
