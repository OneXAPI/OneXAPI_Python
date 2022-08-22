import ctypes

lib = ctypes.cdll.LoadLibrary('libOneXAPI.so')

class client:
    def __init__(self, request = "{}"):
        lib.char_free.argtypes = [ctypes.c_void_p]
        lib.char_free.restype = None

        lib.upbitSpot_create.argtypes = [ctypes.c_void_p]
        lib.upbitSpot_create.restype = ctypes.c_void_p

        lib.upbitSpot_delete.argtypes = [ctypes.c_void_p]
        lib.upbitSpot_delete.restype = None

        lib.upbitSpot_withdraw.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.upbitSpot_withdraw.restype = ctypes.c_void_p

        lib.upbitSpot_fetchAllCurrencies.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.upbitSpot_fetchAllCurrencies.restype = ctypes.c_void_p

        lib.upbitSpot_fetchBalance.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.upbitSpot_fetchBalance.restype = ctypes.c_void_p

        lib.upbitSpot_fetchWalletStatus.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.upbitSpot_fetchWalletStatus.restype = ctypes.c_void_p

        lib.upbitSpot_fetchWithdrawHistory.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.upbitSpot_fetchWithdrawHistory.restype = ctypes.c_void_p

        lib.upbitSpot_fetchDepositHistory.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.upbitSpot_fetchDepositHistory.restype = ctypes.c_void_p

        lib.upbitSpot_fetchDepositAddress.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.upbitSpot_fetchDepositAddress.restype = ctypes.c_void_p

        lib.upbitSpot_isDepositCompleted.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.upbitSpot_isDepositCompleted.restype = ctypes.c_void_p

        lib.upbitSpot_orderLimitBuy.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.upbitSpot_orderLimitBuy.restype = ctypes.c_void_p

        lib.upbitSpot_orderLimitSell.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.upbitSpot_orderLimitSell.restype = ctypes.c_void_p

        lib.upbitSpot_orderMarketBuy.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.upbitSpot_orderMarketBuy.restype = ctypes.c_void_p

        lib.upbitSpot_orderMarketSell.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.upbitSpot_orderMarketSell.restype = ctypes.c_void_p

        lib.upbitSpot_orderCancel.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.upbitSpot_orderCancel.restype = ctypes.c_void_p

        lib.upbitSpot_fetchTradingFee.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.upbitSpot_fetchTradingFee.restype = ctypes.c_void_p

        lib.upbitSpot_fetchOrderInfo.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.upbitSpot_fetchOrderInfo.restype = ctypes.c_void_p

        lib.upbitSpot_fetchOpenOrders.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.upbitSpot_fetchOpenOrders.restype = ctypes.c_void_p

        lib.upbitSpot_getCandleIntervalCandidates.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.upbitSpot_getCandleIntervalCandidates.restype = ctypes.c_void_p

        lib.upbitSpot_fetchMarkets.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.upbitSpot_fetchMarkets.restype = ctypes.c_void_p

        lib.upbitSpot_fetchTicker.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.upbitSpot_fetchTicker.restype = ctypes.c_void_p

        lib.upbitSpot_fetchOrderbook.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.upbitSpot_fetchOrderbook.restype = ctypes.c_void_p

        lib.upbitSpot_fetchCandleHistory.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.upbitSpot_fetchCandleHistory.restype = ctypes.c_void_p

        lib.upbitSpot_subscribeBalance.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.upbitSpot_subscribeBalance.restype = ctypes.c_void_p

        lib.upbitSpot_unsubscribeBalance.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.upbitSpot_unsubscribeBalance.restype = ctypes.c_void_p

        lib.upbitSpot_isSubscribingBalance.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.upbitSpot_isSubscribingBalance.restype = ctypes.c_void_p

        lib.upbitSpot_getSubscribingTickers.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.upbitSpot_getSubscribingTickers.restype = ctypes.c_void_p

        lib.upbitSpot_getSubscribingOrderbooks.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.upbitSpot_getSubscribingOrderbooks.restype = ctypes.c_void_p

        lib.upbitSpot_subscribeTicker.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.upbitSpot_subscribeTicker.restype = ctypes.c_void_p

        lib.upbitSpot_unsubscribeTicker.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.upbitSpot_unsubscribeTicker.restype = ctypes.c_void_p

        lib.upbitSpot_subscribeOrderbook.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.upbitSpot_subscribeOrderbook.restype = ctypes.c_void_p

        lib.upbitSpot_unsubscribeOrderbook.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.upbitSpot_unsubscribeOrderbook.restype = ctypes.c_void_p

        self.client = lib.upbitSpot_create(bytes(request, "utf-8"))
    
    def __del__(self):
        lib.upbitSpot_delete(self.client)

    def withdraw(self, request = "{}"):
        response = lib.upbitSpot_withdraw(self.client, bytes(request, "utf-8"))
        ret = str(ctypes.cast(response, ctypes.c_char_p).value, "utf-8")
        lib.char_free(response)
        return ret

    def fetchAllCurrencies(self, request = "{}"):
        response = lib.upbitSpot_fetchAllCurrencies(self.client, bytes(request, "utf-8"))
        ret = str(ctypes.cast(response, ctypes.c_char_p).value, "utf-8")
        lib.char_free(response)
        return ret

    def fetchBalance(self, request = "{}"):
        response = lib.upbitSpot_fetchBalance(self.client, bytes(request, "utf-8"))
        ret = str(ctypes.cast(response, ctypes.c_char_p).value, "utf-8")
        lib.char_free(response)
        return ret

    def fetchWalletStatus(self, request = "{}"):
        response = lib.upbitSpot_fetchWalletStatus(self.client, bytes(request, "utf-8"))
        ret = str(ctypes.cast(response, ctypes.c_char_p).value, "utf-8")
        lib.char_free(response)
        return ret

    def fetchWithdrawHistory(self, request = "{}"):
        response = lib.upbitSpot_fetchWithdrawHistory(self.client, bytes(request, "utf-8"))
        ret = str(ctypes.cast(response, ctypes.c_char_p).value, "utf-8")
        lib.char_free(response)
        return ret

    def fetchDepositHistory(self, request = "{}"):
        response = lib.upbitSpot_fetchDepositHistory(self.client, bytes(request, "utf-8"))
        ret = str(ctypes.cast(response, ctypes.c_char_p).value, "utf-8")
        lib.char_free(response)
        return ret

    def fetchDepositAddress(self, request = "{}"):
        response = lib.upbitSpot_fetchDepositAddress(self.client, bytes(request, "utf-8"))
        ret = str(ctypes.cast(response, ctypes.c_char_p).value, "utf-8")
        lib.char_free(response)
        return ret

    def isDepositCompleted(self, request = "{}"):
        response = lib.upbitSpot_isDepositCompleted(self.client, bytes(request, "utf-8"))
        ret = str(ctypes.cast(response, ctypes.c_char_p).value, "utf-8")
        lib.char_free(response)
        return ret

    def orderLimitBuy(self, request = "{}"):
        response = lib.upbitSpot_orderLimitBuy(self.client, bytes(request, "utf-8"))
        ret = str(ctypes.cast(response, ctypes.c_char_p).value, "utf-8")
        lib.char_free(response)
        return ret

    def orderLimitSell(self, request = "{}"):
        response = lib.upbitSpot_orderLimitSell(self.client, bytes(request, "utf-8"))
        ret = str(ctypes.cast(response, ctypes.c_char_p).value, "utf-8")
        lib.char_free(response)
        return ret

    def orderMarketBuy(self, request = "{}"):
        response = lib.upbitSpot_orderMarketBuy(self.client, bytes(request, "utf-8"))
        ret = str(ctypes.cast(response, ctypes.c_char_p).value, "utf-8")
        lib.char_free(response)
        return ret

    def orderMarketSell(self, request = "{}"):
        response = lib.upbitSpot_orderMarketSell(self.client, bytes(request, "utf-8"))
        ret = str(ctypes.cast(response, ctypes.c_char_p).value, "utf-8")
        lib.char_free(response)
        return ret

    def orderCancel(self, request = "{}"):
        response = lib.upbitSpot_orderCancel(self.client, bytes(request, "utf-8"))
        ret = str(ctypes.cast(response, ctypes.c_char_p).value, "utf-8")
        lib.char_free(response)
        return ret

    def fetchTradingFee(self, request = "{}"):
        response = lib.upbitSpot_fetchTradingFee(self.client, bytes(request, "utf-8"))
        ret = str(ctypes.cast(response, ctypes.c_char_p).value, "utf-8")
        lib.char_free(response)
        return ret

    def fetchOrderInfo(self, request = "{}"):
        response = lib.upbitSpot_fetchOrderInfo(self.client, bytes(request, "utf-8"))
        ret = str(ctypes.cast(response, ctypes.c_char_p).value, "utf-8")
        lib.char_free(response)
        return ret

    def fetchOpenOrders(self, request = "{}"):
        response = lib.upbitSpot_fetchOpenOrders(self.client, bytes(request, "utf-8"))
        ret = str(ctypes.cast(response, ctypes.c_char_p).value, "utf-8")
        lib.char_free(response)
        return ret

    def getCandleIntervalCandidates(self, request = "{}"):
        response = lib.upbitSpot_getCandleIntervalCandidates(self.client, bytes(request, "utf-8"))
        ret = str(ctypes.cast(response, ctypes.c_char_p).value, "utf-8")
        lib.char_free(response)
        return ret

    def fetchMarkets(self, request = "{}"):
        response = lib.upbitSpot_fetchMarkets(self.client, bytes(request, "utf-8"))
        ret = str(ctypes.cast(response, ctypes.c_char_p).value, "utf-8")
        lib.char_free(response)
        return ret

    def fetchTicker(self, request = "{}"):
        response = lib.upbitSpot_fetchTicker(self.client, bytes(request, "utf-8"))
        ret = str(ctypes.cast(response, ctypes.c_char_p).value, "utf-8")
        lib.char_free(response)
        return ret

    def fetchOrderbook(self, request = "{}"):
        response = lib.upbitSpot_fetchOrderbook(self.client, bytes(request, "utf-8"))
        ret = str(ctypes.cast(response, ctypes.c_char_p).value, "utf-8")
        lib.char_free(response)
        return ret

    def fetchCandleHistory(self, request = "{}"):
        response = lib.upbitSpot_fetchCandleHistory(self.client, bytes(request, "utf-8"))
        ret = str(ctypes.cast(response, ctypes.c_char_p).value, "utf-8")
        lib.char_free(response)
        return ret

    def subscribeBalance(self, request = "{}"):
        response = lib.upbitSpot_subscribeBalance(self.client, bytes(request, "utf-8"))
        ret = str(ctypes.cast(response, ctypes.c_char_p).value, "utf-8")
        lib.char_free(response)
        return ret

    def unsubscribeBalance(self, request = "{}"):
        response = lib.upbitSpot_unsubscribeBalance(self.client, bytes(request, "utf-8"))
        ret = str(ctypes.cast(response, ctypes.c_char_p).value, "utf-8")
        lib.char_free(response)
        return ret

    def isSubscribingBalance(self, request = "{}"):
        response = lib.upbitSpot_isSubscribingBalance(self.client, bytes(request, "utf-8"))
        ret = str(ctypes.cast(response, ctypes.c_char_p).value, "utf-8")
        lib.char_free(response)
        return ret

    def getSubscribingTickers(self, request = "{}"):
        response = lib.upbitSpot_getSubscribingTickers(self.client, bytes(request, "utf-8"))
        ret = str(ctypes.cast(response, ctypes.c_char_p).value, "utf-8")
        lib.char_free(response)
        return ret
    
    def getSubscribingOrderbooks(self, request = "{}"):
        response = lib.upbitSpot_getSubscribingOrderbooks(self.client, bytes(request, "utf-8"))
        ret = str(ctypes.cast(response, ctypes.c_char_p).value, "utf-8")
        lib.char_free(response)
        return ret

    def subscribeTicker(self, request = "{}"):
        response = lib.upbitSpot_subscribeTicker(self.client, bytes(request, "utf-8"))
        ret = str(ctypes.cast(response, ctypes.c_char_p).value, "utf-8")
        lib.char_free(response)
        return ret

    def unsubscribeTicker(self, request = "{}"):
        response = lib.upbitSpot_unsubscribeTicker(self.client, bytes(request, "utf-8"))
        ret = str(ctypes.cast(response, ctypes.c_char_p).value, "utf-8")
        lib.char_free(response)
        return ret

    def subscribeOrderbook(self, request = "{}"):
        response = lib.upbitSpot_subscribeOrderbook(self.client, bytes(request, "utf-8"))
        ret = str(ctypes.cast(response, ctypes.c_char_p).value, "utf-8")
        lib.char_free(response)
        return ret

    def unsubscribeOrderbook(self, request = "{}"):
        response = lib.upbitSpot_unsubscribeOrderbook(self.client, bytes(request, "utf-8"))
        ret = str(ctypes.cast(response, ctypes.c_char_p).value, "utf-8")
        lib.char_free(response)
        return ret



if __name__ == "__main__":
    lib = ctypes.cdll.LoadLibrary('../libOneXAPI.so')
    upbitClient = client()
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