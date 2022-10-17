import ctypes
from typing import Union
from OneXAPI.internal.instruments.spot import spot_client
from OneXAPI.internal.instruments.futures import futures_client
from OneXAPI.internal.util import lib, createObject

class Spot(spot_client):
    def __init__(self, request: Union[str, dict] = "{}") -> None:
        spot_client.__init__(self, request, lib)
        self.lib.char_free.argtypes = [ctypes.c_void_p]
        self.lib.char_free.restype = None

        self.lib.binanceSpot_create.argtypes = [ctypes.c_void_p]
        self.lib.binanceSpot_create.restype = ctypes.c_void_p

        self.lib.binanceSpot_delete.argtypes = [ctypes.c_void_p]
        self.lib.binanceSpot_delete.restype = None

        self.client = createObject(request, self.lib.binanceSpot_create)
    
    def __del__(self):
        lib.binanceSpot_delete(self.client)

class Futures(futures_client):
    def __init__(self, request: Union[str, dict] = "{}") -> None:
        futures_client.__init__(self, request, lib)
        self.lib.char_free.argtypes = [ctypes.c_void_p]
        self.lib.char_free.restype = None

        self.lib.binanceFutures_create.argtypes = [ctypes.c_void_p]
        self.lib.binanceFutures_create.restype = ctypes.c_void_p

        self.lib.binanceFutures_delete.argtypes = [ctypes.c_void_p]
        self.lib.binanceFutures_delete.restype = None

        self.client = createObject(request, self.lib.binanceFutures_create)
    
    def __del__(self):
        lib.binanceFutures_delete(self.client)