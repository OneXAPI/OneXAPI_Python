import ctypes, sys, os
from typing import Union
from .internal.util import lib, sendAPI
from .Binance import Spot
from .Binance import Futures
from .Upbit import Spot

lib.char_free.argtypes = [ctypes.c_void_p]
lib.char_free.restype = None

lib.OneXAPI_getInfo.argtypes = [ctypes.c_char_p]
lib.OneXAPI_getInfo.restype = ctypes.c_void_p

lib.OneXAPI_getLoggerConfig.argtypes = [ctypes.c_char_p]
lib.OneXAPI_getLoggerConfig.restype = ctypes.c_void_p

lib.OneXAPI_setLoggerConfig.argtypes = [ctypes.c_char_p]
lib.OneXAPI_setLoggerConfig.restype = ctypes.c_void_p

path = os.path.dirname(os.path.abspath(sys.argv[0]))
restPath = os.path.join(path, 'OneXAPI_Logs', 'OneXAPI.log')
websocketPath = os.path.join(path, 'OneXAPI_Logs', 'OneXAPI_Websocket.log')

request = ('{"main":{"customPath":"' + restPath + '"},"websocket":{"customPath":"' + websocketPath + '"}}').replace('\\', '/')

sendAPI(request, lib.OneXAPI_setLoggerConfig, lib.char_free)

def getInfo(request: Union[str, dict] = "{}") -> dict:
    return sendAPI(request, lib.OneXAPI_getInfo, lib.char_free)

def getLoggerConfig(request: Union[str, dict] = "{}") -> dict:
    return sendAPI(request, lib.OneXAPI_getLoggerConfig, lib.char_free)

def setLoggerConfig(request: Union[str, dict]) -> dict:
    return sendAPI(request, lib.OneXAPI_setLoggerConfig, lib.char_free)
