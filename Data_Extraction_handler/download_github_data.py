from clint.textui import progress
import requests
import datetime


date = '2021-05-21 11:22:03'
datem = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
#print(datem.day)        # 25
#print(datem.month)      # 5
#print(datem.year)       # 2021
#print(datem.hour)       # 11

#wget https://data.gharchive.org/2015-01-01-15.json.gz
fname = '2015-10-31-20.json.gz'
url = 'https://data.gharchive.org/' + fname
r = requests.get(url, stream=True)
with open("/Users/mohammed.hkhalil/PycharmProjects/github-archive-analytics/Data/raw/"+fname, 'wb') as f:
    total_length = int(r.headers.get('content-length'))
    for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1):
        if chunk:
            f.write(chunk)
            f.flush()