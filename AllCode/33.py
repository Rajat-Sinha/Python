#cropping of Image

from PIL import Image

image = Image.open('Cashless_payment.jpg')
area = (100,100,300,375)
cropped_image = image.crop(area)

image.show()
cropped_image.show()