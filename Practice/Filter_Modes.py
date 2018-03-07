#Modes and Filter

from PIL import Image
from PIL import ImageFilter #used for useing filter type function

img = Image.open('Easy_haults.jpg')
black_white = img.convert('L')
blur = img.filter(ImageFilter.BLUR) #for Blurred image
details = img.filter(ImageFilter.DETAIL)
edges = img.filter(ImageFilter.FIND_EDGES)


