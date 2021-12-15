import gzip ,shutil
import os, json
import pandas as pd
import numpy as np
import glob

with open('/Users/mohammed.hkhalil/PycharmProjects/github-archive-analytics/Data/uncompress/2015-01-01-15.json') as f:
    data = json.load(f)

print(data)