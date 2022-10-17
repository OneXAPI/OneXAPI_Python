import ctypes
import OneXAPI.internal.util
from typing import Union

class spot_client:
    def __init__(self, request: Union[str, dict], lib: ctypes.cdll):
        # General
        lib.spot_getConfig.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.spot_getConfig.restype = ctypes.c_void_p

        lib.spot_setConfig.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.spot_setConfig.restype = ctypes.c_void_p

        lib.spot_getEndpointCandidates.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.spot_getEndpointCandidates.restype = ctypes.c_void_p

        lib.spot_has.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.spot_has.restype = ctypes.c_void_p

        # Wallet
        lib.spot_getWithdrawRoundingRule.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.spot_getWithdrawRoundingRule.restype = ctypes.c_void_p

        lib.spot_setWithdrawRoundingRule.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.spot_setWithdrawRoundingRule.restype = ctypes.c_void_p

        lib.spot_withdraw.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.spot_withdraw.restype = ctypes.c_void_p

        lib.spot_fetchAllCurrencies.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.spot_fetchAllCurrencies.restype = ctypes.c_void_p

        lib.spot_fetchBalance.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.spot_fetchBalance.restype = ctypes.c_void_p

        lib.spot_fetchWalletStatus.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.spot_fetchWalletStatus.restype = ctypes.c_void_p

        lib.spot_fetchWithdrawHistory.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.spot_fetchWithdrawHistory.restype = ctypes.c_void_p

        lib.spot_fetchDepositHistory.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.spot_fetchDepositHistory.restype = ctypes.c_void_p

        lib.spot_fetchDepositAddress.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.spot_fetchDepositAddress.restype = ctypes.c_void_p

        lib.spot_isDepositCompleted.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.spot_isDepositCompleted.restype = ctypes.c_void_p

        lib.spot_subscribeBalance.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.spot_subscribeBalance.restype = ctypes.c_void_p

        lib.spot_unsubscribeBalance.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.spot_unsubscribeBalance.restype = ctypes.c_void_p

        lib.spot_isSubscribingBalance.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.spot_isSubscribingBalance.restype = ctypes.c_void_p

        # Trade
        lib.spot_getOrderRoundingRule.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.spot_getOrderRoundingRule.restype = ctypes.c_void_p

        lib.spot_setOrderRoundingRule.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.spot_setOrderRoundingRule.restype = ctypes.c_void_p

        lib.spot_orderLimitBuy.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.spot_orderLimitBuy.restype = ctypes.c_void_p

        lib.spot_orderLimitSell.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.spot_orderLimitSell.restype = ctypes.c_void_p

        lib.spot_orderMarketBuy.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.spot_orderMarketBuy.restype = ctypes.c_void_p

        lib.spot_orderMarketSell.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.spot_orderMarketSell.restype = ctypes.c_void_p

        lib.spot_orderCancel.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.spot_orderCancel.restype = ctypes.c_void_p

        lib.spot_fetchOrderInfo.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.spot_fetchOrderInfo.restype = ctypes.c_void_p

        lib.spot_fetchOpenOrders.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.spot_fetchOpenOrders.restype = ctypes.c_void_p

        lib.spot_fetchTradingFee.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.spot_fetchTradingFee.restype = ctypes.c_void_p

        # Market
        lib.spot_getCandleIntervalCandidates.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.spot_getCandleIntervalCandidates.restype = ctypes.c_void_p

        lib.spot_fetchMarkets.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.spot_fetchMarkets.restype = ctypes.c_void_p

        lib.spot_fetchTicker.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.spot_fetchTicker.restype = ctypes.c_void_p

        lib.spot_fetchOrderbook.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.spot_fetchOrderbook.restype = ctypes.c_void_p

        lib.spot_fetchCandleHistory.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.spot_fetchCandleHistory.restype = ctypes.c_void_p

        lib.spot_getSubscribingTickers.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.spot_getSubscribingTickers.restype = ctypes.c_void_p

        lib.spot_getSubscribingOrderbooks.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.spot_getSubscribingOrderbooks.restype = ctypes.c_void_p

        lib.spot_subscribeTicker.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.spot_subscribeTicker.restype = ctypes.c_void_p

        lib.spot_unsubscribeTicker.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.spot_unsubscribeTicker.restype = ctypes.c_void_p

        lib.spot_subscribeOrderbook.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.spot_subscribeOrderbook.restype = ctypes.c_void_p

        lib.spot_unsubscribeOrderbook.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.spot_unsubscribeOrderbook.restype = ctypes.c_void_p

        self.lib = lib

    # General
    def getConfig(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.spot_getConfig, self.lib.char_free, self.client)

    def setConfig(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.spot_setConfig, self.lib.char_free, self.client)

    def getEndpointCandidates(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.spot_getEndpointCandidates, self.lib.char_free, self.client)

    def has(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.spot_has, self.lib.char_free, self.client)

    # Wallet
    def getWithdrawRoundingRule(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.spot_getWithdrawRoundingRule, self.lib.char_free, self.client)

    def setWithdrawRoundingRule(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.spot_setWithdrawRoundingRule, self.lib.char_free, self.client)

    def withdraw(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.spot_withdraw, self.lib.char_free, self.client)

    def fetchAllCurrencies(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.spot_fetchAllCurrencies, self.lib.char_free, self.client)

    def fetchBalance(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.spot_fetchBalance, self.lib.char_free, self.client)

    def fetchWalletStatus(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.spot_fetchWalletStatus, self.lib.char_free, self.client)

    def fetchWithdrawHistory(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.spot_fetchWithdrawHistory, self.lib.char_free, self.client)

    def fetchDepositHistory(self, request ) -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.spot_fetchDepositHistory, self.lib.char_free, self.client)

    def fetchDepositAddress(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.spot_fetchDepositAddress, self.lib.char_free, self.client)

    def isDepositCompleted(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.spot_isDepositCompleted, self.lib.char_free, self.client)

    def subscribeBalance(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.spot_subscribeBalance, self.lib.char_free, self.client)

    def unsubscribeBalance(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.spot_unsubscribeBalance, self.lib.char_free, self.client)

    def isSubscribingBalance(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.spot_isSubscribingBalance, self.lib.char_free, self.client)

    # Trade
    def getOrderRoundingRule(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.spot_getOrderRoundingRule, self.lib.char_free, self.client)

    def setOrderRoundingRule(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.spot_setOrderRoundingRule, self.lib.char_free, self.client)

    def orderLimitBuy(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.spot_orderLimitBuy, self.lib.char_free, self.client)

    def orderLimitSell(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.spot_orderLimitSell, self.lib.char_free, self.client)

    def orderMarketBuy(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.spot_orderMarketBuy, self.lib.char_free, self.client)

    def orderMarketSell(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.spot_orderMarketSell, self.lib.char_free, self.client)

    def orderCancel(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.spot_orderCancel, self.lib.char_free, self.client)

    def fetchOrderInfo(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.spot_fetchOrderInfo, self.lib.char_free, self.client)

    def fetchOpenOrders(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.spot_fetchOpenOrders, self.lib.char_free, self.client)

    def fetchTradingFee(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.spot_fetchTradingFee, self.lib.char_free, self.client)

    # Market
    def getCandleIntervalCandidates(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.spot_getCandleIntervalCandidates, self.lib.char_free, self.client)

    def fetchMarkets(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.spot_fetchMarkets, self.lib.char_free, self.client)

    def fetchTicker(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.spot_fetchTicker, self.lib.char_free, self.client)

    def fetchOrderbook(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.spot_fetchOrderbook, self.lib.char_free, self.client)

    def fetchCandleHistory(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.spot_fetchCandleHistory, self.lib.char_free, self.client)

    def getSubscribingTickers(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.spot_getSubscribingTickers, self.lib.char_free, self.client)

    def getSubscribingOrderbooks(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.spot_getSubscribingOrderbooks, self.lib.char_free, self.client)

    def subscribeTicker(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.spot_subscribeTicker, self.lib.char_free, self.client)

    def unsubscribeTicker(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.spot_unsubscribeTicker, self.lib.char_free, self.client)

    def subscribeOrderbook(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.spot_subscribeOrderbook, self.lib.char_free, self.client)

    def unsubscribeOrderbook(self, request: Union[str, dict] = "{}") -> dict:
        return OneXAPI.internal.util.sendAPI(request, self.lib.spot_unsubscribeOrderbook, self.lib.char_free, self.client)