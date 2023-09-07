"""
Cubic Python Packages - pyutils
Version 20220429
"""

__version__ = "V20220429"

import time

def str2ts(time_str,formats="%Y-%m-%d %H:%M:%S"):
    return int(time.mktime(time.strptime(time_str,formats)))

def ts2str(time_ts,formats="%Y-%m-%d %H:%M:%S"):
    return time.strftime(formats,time.localtime(int(str(time_ts)[:10])))

import pickle

def save_object(obj,filename):
    f = open(filename,"wb+")
    pickle.dump(obj,f)
    f.close()
    return

def load_object(filename):
    f = open(filename,"rb")
    obj = pickle.load(f)
    f.close()
    return obj

import csv

def read_csv(filename,encoding=None):
    f = open(filename,"r",encoding=encoding)
    data = list(csv.reader(f))
    f.close()
    return data

def write_csv(data,filename,encoding=None):
    f = open(filename,"w+",encoding=encoding,newline='')
    csv.writer(f).writerows(data)
    f.close()
    return 

def build_path(foldername):
	if not os.path.exists(foldername):
		os.mkdir(foldername)

def file_exists(filename):
    return os.path.exists(filename)

import json
def read_json(filename,encoding=None):
	f = open(filename,"r",encoding=encoding)
	data = json.load(f)
	f.close()
	return data

def write_json(data,filename,encoding=None):
	f = open(filename,"w+",encoding=encoding)
	json.dump(data,f)
	f.close()

