import ctypes
import OneXAPI.internal.util
from typing import Union

class futures_client:
    def __init__(self, request: Union[str, dict], lib: ctypes.cdll):
        # General
        lib.futures_getConfig.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.futures_getConfig.restype = ctypes.c_void_p

        lib.futures_setConfig.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.futures_setConfig.restype = ctypes.c_void_p

        lib.futures_getEndpointCandidates.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.futures_getEndpointCandidates.restype = ctypes.c_void_p

        lib.futures_has.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.futures_has.restype = ctypes.c_void_p

        # Wallet
        lib.futures_fetchBalance.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.futures_fetchBalance.restype = ctypes.c_void_p

        lib.futures_fetchPositions.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.futures_fetchPositions.restype = ctypes.c_void_p

        lib.futures_fetchFundingFeeIncomeHistory.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.futures_fetchFundingFeeIncomeHistory.restype = ctypes.c_void_p

        lib.futures_subscribeBalance.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.futures_subscribeBalance.restype = ctypes.c_void_p

        lib.futures_unsubscribeBalance.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.futures_unsubscribeBalance.restype = ctypes.c_void_p

        lib.futures_isSubscribingBalance.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.futures_isSubscribingBalance.restype = ctypes.c_void_p

        # Trade
        lib.futures_getOrderRoundingRule.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.futures_getOrderRoundingRule.restype = ctypes.c_void_p

        lib.futures_setOrderRoundingRule.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.futures_setOrderRoundingRule.restype = ctypes.c_void_p

        lib.futures_orderLimitBuy.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.futures_orderLimitBuy.restype = ctypes.c_void_p

        lib.futures_orderLimitSell.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.futures_orderLimitSell.restype = ctypes.c_void_p

        lib.futures_orderMarketBuy.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.futures_orderMarketBuy.restype = ctypes.c_void_p

        lib.futures_orderMarketSell.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.futures_orderMarketSell.restype = ctypes.c_void_p

        lib.futures_orderCancel.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.futures_orderCancel.restype = ctypes.c_void_p

        lib.futures_fetchOrderInfo.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.futures_fetchOrderInfo.restype = ctypes.c_void_p

        lib.futures_fetchOpenOrders.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.futures_fetchOpenOrders.restype = ctypes.c_void_p

        lib.futures_fetchTradingFee.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.futures_fetchTradingFee.restype = ctypes.c_void_p

        lib.futures_fetchLeverage.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.futures_fetchLeverage.restype = ctypes.c_void_p

        lib.futures_changeLeverage.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.futures_changeLeverage.restype = ctypes.c_void_p

        lib.futures_fetchMarginType.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.futures_fetchMarginType.restype = ctypes.c_void_p

        lib.futures_changeMarginType.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.futures_changeMarginType.restype = ctypes.c_void_p

        # Market
        lib.futures_getCandleIntervalCandidates.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.futures_getCandleIntervalCandidates.restype = ctypes.c_void_p

        lib.futures_fetchMarkets.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.futures_fetchMarkets.restype = ctypes.c_void_p

        lib.futures_fetchMarketInfo.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.futures_fetchMarketInfo.restype = ctypes.c_void_p

        lib.futures_fetchTicker.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.futures_fetchTicker.restype = ctypes.c_void_p

        lib.futures_fetchOrderbook.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.futures_fetchOrderbook.restype = ctypes.c_void_p

        lib.futures_fetchCandleHistory.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.futures_fetchCandleHistory.restype = ctypes.c_void_p

        lib.futures_getSubscribingMarketInfo.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.futures_getSubscribingMarketInfo.restype = ctypes.c_void_p

        lib.futures_getSubscribingTickers.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.futures_getSubscribingTickers.restype = ctypes.c_void_p

        lib.futures_getSubscribingOrderbooks.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.futures_getSubscribingOrderbooks.restype = ctypes.c_void_p

        lib.futures_subscribeMarketInfo.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.futures_subscribeMarketInfo.restype = ctypes.c_void_p

        lib.futures_unsubscribeMarketInfo.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.futures_unsubscribeMarketInfo.restype = ctypes.c_void_p

        lib.futures_subscribeTicker.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.futures_subscribeTicker.restype = ctypes.c_void_p

        lib.futures_unsubscribeTicker.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.futures_unsubscribeTicker.restype = ctypes.c_void_p

        lib.futures_subscribeOrderbook.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.futures_subscribeOrderbook.restype = ctypes.c_void_p

        lib.futures_unsubscribeOrderbook.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.futures_unsubscribeOrderbook.restype = ctypes.c_void_p

        self.lib = lib

    # General
    def getConfig(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.futures_getConfig, self.lib.char_free, self.client)

    def setConfig(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.futures_setConfig, self.lib.char_free, self.client)

    def getEndpointCandidates(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.futures_getEndpointCandidates, self.lib.char_free, self.client)

    def has(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.futures_has, self.lib.char_free, self.client)

    # Wallet    
    def fetchBalance(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.futures_fetchBalance, self.lib.char_free, self.client)

    def fetchPositions(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.futures_fetchPositions, self.lib.char_free, self.client)

    def fetchFundingFeeIncomeHistory(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.futures_fetchFundingFeeIncomeHistory, self.lib.char_free, self.client)

    def subscribeBalance(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.futures_subscribeBalance, self.lib.char_free, self.client)

    def unsubscribeBalance(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.futures_unsubscribeBalance, self.lib.char_free, self.client)

    def isSubscribingBalance(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.futures_isSubscribingBalance, self.lib.char_free, self.client)

    # Trade   
    def getOrderRoundingRule(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.futures_getOrderRoundingRule, self.lib.char_free, self.client)

    def setOrderRoundingRule(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.futures_setOrderRoundingRule, self.lib.char_free, self.client)

    def orderLimitBuy(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.futures_orderLimitBuy, self.lib.char_free, self.client)

    def orderLimitSell(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.futures_orderLimitSell, self.lib.char_free, self.client)

    def orderMarketBuy(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.futures_orderMarketBuy, self.lib.char_free, self.client)

    def orderMarketSell(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.futures_orderMarketSell, self.lib.char_free, self.client)

    def orderCancel(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.futures_orderCancel, self.lib.char_free, self.client)

    def fetchOrderInfo(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.futures_fetchOrderInfo, self.lib.char_free, self.client)

    def fetchOpenOrders(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.futures_fetchOpenOrders, self.lib.char_free, self.client)

    def fetchTradingFee(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.futures_fetchTradingFee, self.lib.char_free, self.client)

    def fetchLeverage(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.futures_fetchLeverage, self.lib.char_free, self.client)

    def changeLeverage(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.futures_changeLeverage, self.lib.char_free, self.client)

    def fetchMarginType(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.futures_fetchMarginType, self.lib.char_free, self.client)

    def changeMarginType(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.futures_changeMarginType, self.lib.char_free, self.client)

    # Market
    def getCandleIntervalCandidates(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.futures_getCandleIntervalCandidates, self.lib.char_free, self.client)

    def fetchMarkets(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.futures_fetchMarkets, self.lib.char_free, self.client)

    def fetchMarketInfo(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.futures_fetchMarketInfo, self.lib.char_free, self.client)
    
    def fetchTicker(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.futures_fetchTicker, self.lib.char_free, self.client)

    def fetchOrderbook(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.futures_fetchOrderbook, self.lib.char_free, self.client)

    def fetchCandleHistory(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.futures_fetchCandleHistory, self.lib.char_free, self.client)

    def getSubscribingMarketInfo(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.futures_getSubscribingMarketInfo, self.lib.char_free, self.client)

    def getSubscribingTickers(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.futures_getSubscribingTickers, self.lib.char_free, self.client)

    def getSubscribingOrderbooks(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.futures_getSubscribingOrderbooks, self.lib.char_free, self.client)

    def subscribeMarketInfo(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.futures_subscribeMarketInfo, self.lib.char_free, self.client)

    def unsubscribeMarketInfo(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.futures_unsubscribeMarketInfo, self.lib.char_free, self.client)

    def subscribeTicker(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.futures_subscribeTicker, self.lib.char_free, self.client)

    def unsubscribeTicker(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.futures_unsubscribeTicker, self.lib.char_free, self.client)

    def subscribeOrderbook(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.futures_subscribeOrderbook, self.lib.char_free, self.client)

    def unsubscribeOrderbook(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.futures_unsubscribeOrderbook, self.lib.char_free, self.client)