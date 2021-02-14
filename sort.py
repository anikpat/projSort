import os
import json
import shutil
from pprint import pprint
from configparser import ConfigParser
from glob import glob

dirPath = input("add full path to sort directory - ")
confFile = 'file.conf.json'
#Get the configparser object
config_object = ConfigParser()
config_object.read("config.ini")
with open(confFile, 'rb') as f:
        config = json.loads(f.read())


os.chdir(dirPath)

def sortTextFiles():
    textFormats = config['text']
    if not os.path.exists('Text'):
        os.mkdir('Text')
    exts = set(f.split('.')[-1] for dir,dirs,files in os.walk('.') for f in files if '.' in f)
    for filename in os.listdir():
        if (filename.endswith('.txt')):
            shutil.move(filename, 'Text')

sortTextFiles()
exit


