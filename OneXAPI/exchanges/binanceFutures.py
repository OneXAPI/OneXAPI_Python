import ctypes
from typing import Union
import OneXAPI.instruments.futures
import OneXAPI.util

class client(OneXAPI.instruments.futures.client):
    def __init__(self, request: Union[str, dict], lib: ctypes.cdll) -> None:
        OneXAPI.instruments.futures.client.__init__(self, request, lib)
        self.lib.char_free.argtypes = [ctypes.c_void_p]
        self.lib.char_free.restype = None

        self.lib.binanceFutures_create.argtypes = [ctypes.c_void_p]
        self.lib.binanceFutures_create.restype = ctypes.c_void_p

        self.lib.binanceFutures_delete.argtypes = [ctypes.c_void_p]
        self.lib.binanceFutures_delete.restype = None

        self.client = OneXAPI.util.createObject(request, self.lib.binanceFutures_create)
    
    def __del__(self):
        self.lib.binanceFutures_delete(self.client)