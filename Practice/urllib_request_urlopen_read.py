#Download Files From Web

from urllib import request

goog_url = 'http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv'

def download_data(url):
    response = request.urlopen(url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split('\n')
    dest_url = r'goog.csv'
    fx = open(dest_url,'w')
    for line in lines:
        fx.write(line+'\n')
    fx.close()

download_data(goog_url)