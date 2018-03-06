#Download Image From Web

import random
import urllib.request #package.filename

def download_image(url):
    name = random.randrange(1,100)
    full_name = str(name) + '.jpg'
    urllib.request.urlretrieve(url, full_name)

download_image('http://achiredo.com/Images/achiredo.png')