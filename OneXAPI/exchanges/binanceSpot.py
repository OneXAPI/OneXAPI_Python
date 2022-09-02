import ctypes
from typing import Union
import OneXAPI.instruments.spot
import OneXAPI.util

class client(OneXAPI.instruments.spot.client):
    def __init__(self, request: Union[str, dict], lib: ctypes.cdll) -> None:
        OneXAPI.instruments.spot.client.__init__(self, request, lib)
        self.lib.char_free.argtypes = [ctypes.c_void_p]
        self.lib.char_free.restype = None

        self.lib.binanceSpot_create.argtypes = [ctypes.c_void_p]
        self.lib.binanceSpot_create.restype = ctypes.c_void_p

        self.lib.binanceSpot_delete.argtypes = [ctypes.c_void_p]
        self.lib.binanceSpot_delete.restype = None

        self.client = OneXAPI.util.createObject(request, self.lib.binanceSpot_create)
    
    def __del__(self):
        self.lib.binanceSpot_delete(self.client)