import gzip ,shutil
import os, json
import pandas as pd
import numpy as np
import glob
pd.set_option('display.max_columns', None)


def unzip_downloaded_files (input_path,output_path) :
    files = os.listdir(input_path)
    for f in files:
        intput_file = f
        output_file = f[:-3]
        input_dir = input_path+'/'+intput_file
        output_dir = output_path+'/'+output_file
        with gzip.open(input_dir, 'rb') as f_in:
            with open(output_dir, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        os.remove(input_dir)  # delete zipped file



in_path = '/Users/mohammed.hkhalil/PycharmProjects/github-archive-analytics/Data/raw'
out_path = '/Users/mohammed.hkhalil/PycharmProjects/github-archive-analytics/Data/uncompress'
df = unzip_downloaded_files(in_path,out_path)