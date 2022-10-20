import ctypes, json
import ftplib
import os
import site
import platform
from typing import Callable, Union
from tqdm import tqdm

base_path = site.getsitepackages()[0]
file_name = 'libOneXAPI'

def file_write(file, data):
   file.write(data) 
   global pbar
   pbar += len(data)
   
def ftp_download(down_path, loc_file_name) :
    print('Cannot found ' + loc_file_name + ' in local. Begin to download.')
    
    ftp=ftplib.FTP(host='27.96.134.108')
    ftp.login()

    data = []
    #ftp.cwd("./")
    ftp.dir(data.append)
    
    fd = open(down_path + loc_file_name,'wb')
    size = ftp.size(loc_file_name)
    pbar=tqdm(total=size)
    
    bufsize=1024
    def bar(data):
        fd.write(data)
        pbar.update(len(data))

    ftp.retrbinary("RETR " + loc_file_name, bar, bufsize)

    pbar.close()
    fd.close()

if platform.system() == 'Linux' :               # Linux
    base_path = base_path + '/OneXAPI_libs'
    if not os.path.exists(base_path):
        os.mkdir(base_path)
    if not os.path.exists(base_path + '/' + file_name + '.so'):
        ftp_download(base_path + '/', file_name + '.so')
        
    if platform.architecture()[0] == '64bit' :
        lib = ctypes.cdll.LoadLibrary(base_path + '/' + file_name + '.so')
    else :
        print("OneXAPI currently supports 64bit linux only. Please contact development team.")
        exit()
elif platform.system() == 'Windows' :           # Windows
    base_path = base_path + '\OneXAPI_libs'
    if not os.path.exists(base_path):
        os.mkdir(base_path)
    if not os.path.exists(base_path + '\\' + file_name + '.dll'):
        ftp_download(base_path + '\\', file_name + '.dll')
        
    if platform.architecture()[0] == '64bit' :
        lib = ctypes.cdll.LoadLibrary(base_path + '\\' + file_name + '.dll')
    else :
        print("OneXAPI currently supports 64bit windows only. Please contact development team.")
        exit()
elif platform.system() == 'Darwin' :            # Mac
    print("OneXAPI currently supports linux and windows only. Please contact development team.")
    exit()
else :
    print("We support Linux Only")
    exit()

def createObject(request: Union[str, dict], create_func: Callable):
    if type(request) is dict:
        request = json.dumps(request)
    
    if type(request) is not str:
        print("\033[91m[Error] Create object request is not 'str' or 'dict'. Create an object without any parameter.\033[0m")
        request = "{}"
        
    return create_func(bytes(request, "utf-8"))

def sendAPI(request: Union[str, dict], req_func: Callable, free_func: Callable, client = None) -> dict:
    ret = dict()
    if type(request) is dict:
        request = json.dumps(request)
    
    if type(request) is str:
        if client is None:
            response = req_func(bytes(request, "utf-8"))
        else:
            response = req_func(client, bytes(request, "utf-8"))
        ret = json.loads(str(ctypes.cast(response, ctypes.c_char_p).value, "utf-8"))
        free_func(response)
    else:   # data type error
        ret['success'] = False
        ret['data'] = dict()
        ret['data']['errorType'] = "JSON_PARSING_ERROR"
        ret['data']['errorMsg'] = "Python request type must be 'str' or 'dict'"
    return ret