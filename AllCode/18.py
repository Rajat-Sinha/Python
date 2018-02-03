#Dowload Files From Web

from urllib import request#differet way to import module

goog_url = 'http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv'

def download_data(csv_url):
    response = request.urlopen(csv_url) # For connecting to the url
    csv = response.read() # same as connect to url
    csv_str = str(csv)
    lines = csv_str.split("\n")
    dest_url = r'goog.csv'
    fx = open(dest_url,'w')
    for line in lines:
        fx.write(line+'\n')
    fx.close()

download_data(goog_url)
