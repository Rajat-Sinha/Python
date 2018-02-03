# Modes and Filter

from PIL import Image
from PIL import ImageFilter

img = Image.open('Cashless_Payment.jpg')
black_white = img.convert('L') # L stands for luminant
blur = img.filter(ImageFilter.BLUR)
details = img.filter(ImageFilter.DETAIL)
edges = img.filter(ImageFilter.FIND_EDGES)


img.show()
black_white.show()
blur.show()
details.show()
edges.show()