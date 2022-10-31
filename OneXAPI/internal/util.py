import ctypes, json
import ftplib
import os
import site
import platform
import pkg_resources
from typing import Callable, Union
from tqdm import tqdm

file_name = 'libOneXAPI.' + pkg_resources.get_distribution('OneXAPI').version

def file_write(file, data):
   file.write(data) 
   global pbar
   pbar += len(data)
   
def ftp_download(down_path, loc_file_name) :
    print('Cannot found ' + loc_file_name + ' in local. Begin to download.')
    
    try:
        ftp=ftplib.FTP(host='27.96.134.108')
        ftp.login()

        data = []
        ftp.dir(data.append)
        
        size = ftp.size(loc_file_name)
        pbar=tqdm(total=size)
        
        bufsize=1024
        with open(os.path.join(down_path, loc_file_name),'wb') as fd:
            def bar(data):
                fd.write(data)
                pbar.update(len(data))

            ftp.retrbinary("RETR " + loc_file_name, bar, bufsize)

            pbar.close()
        
    except Exception as e:
        if os.path.exists(os.path.join(down_path, loc_file_name)):
            os.remove(os.path.join(down_path, loc_file_name))
        print("Failed to download dynamic library from OneX FTP Server. Please contact OneX Team.")
        print("Error : " + str(e))
        exit()

if platform.system() == 'Linux' :               # Linux        
    base_path = os.path.join(os.path.expanduser('~'), '.OneXAPI_libs')
    if not os.path.exists(base_path):
        os.mkdir(base_path)
    if not os.path.exists(os.path.join(base_path, file_name + '.so')):
        ftp_download(base_path, file_name + '.so')
        
    if platform.architecture()[0] == '64bit' :
        lib = ctypes.cdll.LoadLibrary(os.path.join(base_path, file_name + '.so'))
    else :
        print("OneXAPI currently supports 64bit linux only. Please contact development team.")
        exit()
elif platform.system() == 'Windows' :           # Windows
    base_path = os.path.join(os.getenv('LOCALAPPDATA'), 'OneXAPI_libs')
    if not os.path.exists(base_path):
        os.mkdir(base_path)
    if not os.path.exists(os.path.join(base_path, file_name + '.dll')):
        ftp_download(base_path, file_name + '.dll')
        
    if platform.architecture()[0] == '64bit' :
        lib = ctypes.cdll.LoadLibrary(os.path.join(base_path, file_name + '.dll'))
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