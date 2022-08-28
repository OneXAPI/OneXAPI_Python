import ctypes
import exchanges.upbitSpot

lib = ctypes.cdll.LoadLibrary('libOneXAPI.so')

lib.char_free.argtypes = [ctypes.c_void_p]
lib.char_free.restype = None

lib.OneXAPI_getInfo.argtypes = [ctypes.c_char_p]
lib.OneXAPI_getInfo.restype = ctypes.c_void_p

lib.OneXAPI_getLoggerConfig.argtypes = [ctypes.c_char_p]
lib.OneXAPI_getLoggerConfig.restype = ctypes.c_void_p

lib.OneXAPI_setLoggerConfig.argtypes = [ctypes.c_char_p]
lib.OneXAPI_setLoggerConfig.restype = ctypes.c_void_p

def getInfo(request = "{}"):
    response = lib.OneXAPI_getInfo(bytes(request, "utf-8"))
    ret = str(ctypes.cast(response, ctypes.c_char_p).value, "utf-8")
    lib.char_free(response)
    return ret

def getLoggerConfig(request = "{}"):
    response = lib.OneXAPI_getLoggerConfig(bytes(request, "utf-8"))
    ret = str(ctypes.cast(response, ctypes.c_char_p).value, "utf-8")
    lib.char_free(response)
    return ret

def setLoggerConfig(request = "{}"):
    response = lib.OneXAPI_setLoggerConfig(bytes(request, "utf-8"))
    ret = str(ctypes.cast(response, ctypes.c_char_p).value, "utf-8")
    lib.char_free(response)
    return ret

class Upbit():
    def Spot(request = "{}"):
        return exchanges.upbitSpot.client(request)
