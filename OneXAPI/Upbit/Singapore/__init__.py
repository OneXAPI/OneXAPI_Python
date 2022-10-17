import ctypes
from typing import Union
from OneXAPI.internal.instruments.spot import spot_client
from OneXAPI.internal.util import lib, createObject

class Spot(spot_client):
    def __init__(self, request: Union[str, dict] = "{}") -> None:
        spot_client.__init__(self, request, lib)
        self.lib.char_free.argtypes = [ctypes.c_void_p]
        self.lib.char_free.restype = None

        self.lib.upbitSingaporeSpot_create.argtypes = [ctypes.c_void_p]
        self.lib.upbitSingaporeSpot_create.restype = ctypes.c_void_p

        self.lib.upbitSingaporeSpot_delete.argtypes = [ctypes.c_void_p]
        self.lib.upbitSingaporeSpot_delete.restype = None

        self.client = createObject(request, self.lib.upbitSingaporeSpot_create)
    
    def __del__(self):
        self.lib.upbitSingaporeSpot_delete(self.client)