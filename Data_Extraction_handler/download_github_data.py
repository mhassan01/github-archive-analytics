from clint.textui import progress
import requests
from datetime import datetime, timedelta

def hourly_it(start, finish):
    while finish > start:
        start = start + timedelta(hours=1)
        yield start


start = datetime(2015, 10,3, 0)
finish = datetime(2015, 10,5, 23)
for hour in hourly_it(start, finish):
    fname=hour.strftime("%Y-%m-%d-%-H")
    url = 'https://data.gharchive.org/' + fname+'.json.gz'
    r = requests.get(url, stream=True)
    with open("/Users/mohammed.hkhalil/PycharmProjects/github-archive-analytics/Data/raw/"+ fname+'.json.gz', 'wb') as f:
        total_length = int(r.headers.get('content-length'))
        for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length / 1024) + 1):
            if chunk:
                f.write(chunk)
                f.flush()


