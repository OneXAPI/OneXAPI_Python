import ctypes, json
from typing import Callable, Union

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