#Download an Image from Web

import random
import urllib.request # package.filename

def download_image(url):
    name = random.randrange(1,1000)
    full_name = str(name) + '.jpg' #str is used to convert into string
    urllib.request.urlretrieve(url, full_name)

download_image('http://achiredo.com/Images/achiredo.png')
