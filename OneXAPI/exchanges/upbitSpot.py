import ctypes
from typing import Union
import OneXAPI.instruments.spot
import OneXAPI.util

class client(OneXAPI.instruments.spot.client):
    def __init__(self, request: Union[str, dict], lib: ctypes.cdll) -> None:
        OneXAPI.instruments.spot.client.__init__(self, request, lib)
        self.lib.char_free.argtypes = [ctypes.c_void_p]
        self.lib.char_free.restype = None

        self.lib.upbitSpot_create.argtypes = [ctypes.c_void_p]
        self.lib.upbitSpot_create.restype = ctypes.c_void_p

        self.lib.upbitSpot_delete.argtypes = [ctypes.c_void_p]
        self.lib.upbitSpot_delete.restype = None

        self.client = OneXAPI.util.createObject(request, self.lib.upbitSpot_create)
    
    def __del__(self):
        self.lib.upbitSpot_delete(self.client)


if __name__ == "__main__":
    lib = ctypes.cdll.LoadLibrary('../libOneXAPI.so')
    upbitClient = client('{"accessKey":"user accessKey","secretKey":"user secretKey"}')
    print(upbitClient.withdraw())
    print(upbitClient.fetchAllCurrencies())
    print(upbitClient.fetchBalance())
    print(upbitClient.fetchWalletStatus())
    print(upbitClient.fetchWithdrawHistory())
    print(upbitClient.fetchDepositHistory())
    print(upbitClient.fetchDepositAddress())
    print(upbitClient.isDepositCompleted())
    print(upbitClient.orderLimitBuy())
    print(upbitClient.orderLimitSell())
    print(upbitClient.orderMarketBuy())
    print(upbitClient.orderMarketSell())
    print(upbitClient.orderCancel())
    print(upbitClient.fetchTradingFee())
    print(upbitClient.fetchOrderInfo())
    print(upbitClient.fetchOpenOrders())
    print(upbitClient.getCandleIntervalCandidates())
    print(upbitClient.fetchMarkets())
    print(upbitClient.fetchTicker())
    print(upbitClient.fetchOrderbook())
    print(upbitClient.fetchCandleHistory())
    print(upbitClient.subscribeBalance())
    print(upbitClient.unsubscribeBalance())
    print(upbitClient.isSubscribingBalance())
    print(upbitClient.getSubscribingTickers())
    print(upbitClient.getSubscribingOrderbooks())
    print(upbitClient.subscribeTicker())
    print(upbitClient.unsubscribeTicker())
    print(upbitClient.subscribeOrderbook())
    print(upbitClient.unsubscribeOrderbook())