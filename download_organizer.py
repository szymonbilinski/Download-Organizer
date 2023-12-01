import os
import collections
from pprint import pprint

EXT_AUDIO = ['mp3','wav','raw','wma','mid','midi']
EXT_VIDEO = ['mp4','mpg','mpeg','avi','mov','flv','mkv','mwv','m4v','h264']
EXT_IMGS = ['png','jpg','jpeg','gif','svg','bmp','psd','tiff','tif','ico']
EXT_DOCS = ['txt','pdf','csv','xls','xlsx','ods','doc','docx','html','odt','tex','ppt','pptx','log']
EXT_COMPR = ['zip','z','7z','rar','tar','gz','rpm','pkg','zip','deb']
EXT_INSTL = ['dmg','exe','iso']


BASE_PATH = os.path.expanduser('~')
DEST_DIRS = ['Music','Movies','Pictures','Documents','Applications','Other']


DOWNLOADS_PATH = os.path.join(BASE_PATH,'Downloads')
files_mapping = collections.defaultdict(list)
files_list = os.listdir(DOWNLOADS_PATH)

for d in DEST_DIRS:
    dir_path = os.path.join(DOWNLOADS_PATH,d)
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)

for file_name in files_list:
    if file_name not in DEST_DIRS:
        file_ext = file_name.split('.')[-1]
        files_mapping[file_ext].append(file_name)


for f_ext, f_list in files_mapping.items():


    if f_ext in EXT_INSTL:
        for file in f_list:
            os.rename(os.path.join(DOWNLOADS_PATH,file), os.path.join(DOWNLOADS_PATH,'Applications',file))
    elif f_ext in EXT_COMPR:
        for file in f_list:
            os.rename(os.path.join(DOWNLOADS_PATH,file), os.path.join(DOWNLOADS_PATH,'Other',file))
    elif f_ext in EXT_DOCS:
        for file in f_list:
            os.rename(os.path.join(DOWNLOADS_PATH,file), os.path.join(DOWNLOADS_PATH,'Documents',file))
    elif f_ext in EXT_IMGS:
        for file in f_list:
            os.rename(os.path.join(DOWNLOADS_PATH,file), os.path.join(DOWNLOADS_PATH,'Pictures',file))
    elif f_ext in EXT_VIDEO:
        for file in f_list:
            os.rename(os.path.join(DOWNLOADS_PATH,file), os.path.join(DOWNLOADS_PATH,'Movies',file))
    elif f_ext in EXT_AUDIO:
        for file in f_list:
            os.rename(os.path.join(DOWNLOADS_PATH,file), os.path.join(DOWNLOADS_PATH,'Music',file))
    else:
        for file in f_list:
            for file in f_list:
                os.rename(os.path.join(DOWNLOADS_PATH,file), os.path.join(DOWNLOADS_PATH,'Other',file))


print("Done")
os.system('pause')