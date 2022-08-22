import unittest
import sys, os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import OneXAPI

class Testing(unittest.TestCase):
    def test_withdraw(self):
        client = OneXAPI.Upbit.Spot()
        res = client.withdraw()
        self.assertEqual("1s", "")

    def test_fetchAllCurrencies(self):
        client = OneXAPI.Upbit.Spot()
        self.assertEqual("","")

    def test_fetchBalance(self):
        client = OneXAPI.Upbit.Spot()
        self.assertEqual("","")

    def test_fetchWalletStatus(self):
        client = OneXAPI.Upbit.Spot()
        self.assertEqual("","")

    def test_fetchWithdrawHistory(self):
        client = OneXAPI.Upbit.Spot()
        self.assertEqual("","")

    def test_fetchDepositHistory(self):
        client = OneXAPI.Upbit.Spot()
        self.assertEqual("","")

    def test_fetchDepositAddress(self):
        client = OneXAPI.Upbit.Spot()
        self.assertEqual("","")

    def test_isDepositCompleted(self):
        client = OneXAPI.Upbit.Spot()
        self.assertEqual("","")

    def test_orderLimitBuy(self):
        client = OneXAPI.Upbit.Spot()
        self.assertEqual("","")

    def test_orderLimitSell(self):
        client = OneXAPI.Upbit.Spot()
        self.assertEqual("","")

    def test_orderMarketBuy(self):
        client = OneXAPI.Upbit.Spot()
        self.assertEqual("","")

    def test_orderMarketSell(self):
        client = OneXAPI.Upbit.Spot()
        self.assertEqual("","")

    def test_orderCancel(self):
        client = OneXAPI.Upbit.Spot()
        self.assertEqual("","")

    def test_fetchTradingFee(self):
        client = OneXAPI.Upbit.Spot()
        self.assertEqual("","")

    def test_fetchOrderInfo(self):
        client = OneXAPI.Upbit.Spot()
        self.assertEqual("","")

    def test_fetchOpenOrders(self):
        client = OneXAPI.Upbit.Spot()
        self.assertEqual("","")

    def test_getCandleIntervalCandidates(self):
        client = OneXAPI.Upbit.Spot()
        self.assertEqual("","")

    def test_fetchMarkets(self):
        client = OneXAPI.Upbit.Spot()
        self.assertEqual("","")

    def test_fetchTicker(self):
        client = OneXAPI.Upbit.Spot()
        self.assertEqual("","")

    def test_fetchOrderbook(self):
        client = OneXAPI.Upbit.Spot()
        self.assertEqual("","")

    def test_fetchCandleHistory(self):
        client = OneXAPI.Upbit.Spot()
        self.assertEqual("","")

    def test_subscribeBalance(self):
        client = OneXAPI.Upbit.Spot()
        self.assertEqual("","")

    def test_unsubscribeBalance(self):
        client = OneXAPI.Upbit.Spot()
        self.assertEqual("","")

    def test_isSubscribingBalance(self):
        client = OneXAPI.Upbit.Spot()
        self.assertEqual("","")

    def test_getSubscribingTickers(self):
        client = OneXAPI.Upbit.Spot()
        self.assertEqual("","")

    def test_getSubscribingOrderbooks(self):
        client = OneXAPI.Upbit.Spot()
        self.assertEqual("","")

    def test_subscribeTicker(self):
        client = OneXAPI.Upbit.Spot()
        self.assertEqual("","")

    def test_unsubscribeTicker(self):
        client = OneXAPI.Upbit.Spot()
        self.assertEqual("","")

    def test_subscribeOrderbook(self):
        client = OneXAPI.Upbit.Spot()
        self.assertEqual("","")

    def test_unsubscribeOrderbook(self):
        client = OneXAPI.Upbit.Spot()
        self.assertEqual("","")



if __name__ == "__main__":
    unittest.main()