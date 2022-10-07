import ctypes
import site
import platform
from typing import Union
import OneXAPI.util
import OneXAPI.exchanges.upbitSpot
import OneXAPI.exchanges.binanceSpot
import OneXAPI.exchanges.binanceFutures

if platform.system() == 'Linux' :               # Linux
    if platform.architecture()[0] == '64bit' :
        lib = ctypes.cdll.LoadLibrary(site.getsitepackages()[0] + '/OneXAPI_libs/libOneXAPI.so')
    else :
        print("OneXAPI currently supports 64bit linux only. Please contact development team.")
        exit()
elif platform.system() == 'Windows' :           # Windows
    if platform.architecture()[0] == '64bit' :
        lib = ctypes.cdll.LoadLibrary(site.getsitepackages()[0] + '/OneXAPI_libs/libOneXAPI.dll')
    else :
        print("OneXAPI currently supports 64bit windows only. Please contact development team.")
        exit()
elif platform.system() == 'Darwin' :            # Mac
    print("OneXAPI currently supports linux and windows only. Please contact development team.")
else :
    print("We support Linux Only")

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
    
    def Futures(request: Union[str, dict] = "{}"):
        return OneXAPI.exchanges.binanceFutures.client(request, lib)