import gzip ,shutil
import os, json
import pandas as pd
import numpy as np
import glob
pd.set_option('display.max_columns', None)


def unzip_downloaded_files (file_path,output_path) :
    files = os.listdir(file_path)
    for f in files:
        intput_file = f
        output_file = f[:-3]
        input_path = file_path+'/'+intput_file
        output_path = output_path+'/'+output_file
        with gzip.open(input_path, 'rb') as f_in:
            with open(output_path, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        #os.remove(input_path)  # delete zipped file

def flatten_json(path_to_json):
    temp = pd.DataFrame()
    json_pattern = os.path.join(path_to_json, '*.json')
    file_list = glob.glob(json_pattern)
    for file in file_list:
        data = pd.read_json(file, lines=True)
        df = temp.append(data, ignore_index=True)
        return df

in_path = '/Users/mohammed.hkhalil/PycharmProjects/github-archive-analytics/Data/raw'
out_path = '/Users/mohammed.hkhalil/PycharmProjects/github-archive-analytics/Data/uncompress'
path_to_json = '/Users/mohammed.hkhalil/PycharmProjects/github-archive-analytics/Data/uncompress/*'

#df = unzip_downloaded_files(in_path,out_path)
df = flatten_json(path_to_json)
print(df)