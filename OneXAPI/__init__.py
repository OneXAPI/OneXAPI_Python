import ctypes
from typing import Union
import OneXAPI.util
import OneXAPI.exchanges.upbitSpot
import OneXAPI.exchanges.binanceSpot

lib = ctypes.cdll.LoadLibrary('./libOneXAPI.so')

lib.char_free.argtypes = [ctypes.c_void_p]
lib.char_free.restype = None

lib.OneXAPI_getInfo.argtypes = [ctypes.c_char_p]
lib.OneXAPI_getInfo.restype = ctypes.c_void_p

lib.OneXAPI_getLoggerConfig.argtypes = [ctypes.c_char_p]
lib.OneXAPI_getLoggerConfig.restype = ctypes.c_void_p

lib.OneXAPI_setLoggerConfig.argtypes = [ctypes.c_char_p]
lib.OneXAPI_setLoggerConfig.restype = ctypes.c_void_p

def getInfo(request: Union[str, dict] = "{}") -> dict:
    return OneXAPI.util.sendAPI(request, lib.OneXAPI_getInfo, lib.char_free)

def getLoggerConfig(request: Union[str, dict] = "{}") -> dict:
    return OneXAPI.util.sendAPI(request, lib.OneXAPI_getLoggerConfig, lib.char_free)

def setLoggerConfig(request: Union[str, dict]) -> dict:
    return OneXAPI.util.sendAPI(request, lib.OneXAPI_setLoggerConfig, lib.char_free)

class Upbit():
    def Spot(request: Union[str, dict] = "{}"):
        return OneXAPI.exchanges.upbitSpot.client(request, lib)

class Binance():
    def Spot(request: Union[str, dict] = "{}"):
        return OneXAPI.exchanges.binanceSpot.client(request, lib)