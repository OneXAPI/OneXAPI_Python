import OneXAPI
import unittest
import sys, os, time
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import json
import util
from exchangeKeys import BINANCE_ACCESS_KEY, BINANCE_SECRET_KEY

hasMap = """
{
    "getConfig": true,
    "setConfig": true,
    "getEndpointCandidates": true,
    "has": true,
    "fetchBalance": true,
    "fetchPositions": true,
    "fetchFundingFeeIncomeHistory": true,
    "subscribeBalance": true,
    "unsubscribeBalance": true,
    "isSubscribingBalance": true,
    "getOrderRoundingRule": true,
    "setOrderRoundingRule": true,
    "orderLimitBuy": true,
    "orderLimitSell": true,
    "orderMarketBuy": true,
    "orderMarketSell": true,
    "orderCancel": true,
    "fetchOrderInfo": true,
    "fetchOpenOrders": true,
    "fetchTradingFee": true,
    "fetchLeverage": true,
    "changeLeverage": true,
    "fetchMarginType": true,
    "changeMarginType": true,
    "getCandleIntervalCandidates": true,
    "fetchMarkets": true,
    "fetchMarketInfo": true,
    "fetchTicker": true,
    "fetchOrderbook": true,
    "fetchCandleHistory": true,
    "getSubscribingMarketInfo": true,
    "getSubscribingTickers": true,
    "getSubscribingOrderbooks": true,
    "subscribeMarketInfo": true,
    "unsubscribeMarketInfo": true,
    "subscribeTicker": true,
    "unsubscribeTicker": true,
    "subscribeOrderbook": true,
    "unsubscribeOrderbook": true
}
"""

class binanceFuturesTest(unittest.TestCase):
    def test_BinanceFutures_Object_1(self):
        for i in range(0,5):
            client = OneXAPI.Binance.Futures()

    def test_BinanceFutures_Object_2(self):
        for i in range(0,5):
            client = OneXAPI.Binance.Futures('')

    def test_BinanceFutures_Object_3(self):
        for i in range(0,5):
            client = OneXAPI.Binance.Futures("{}")

    def test_BinanceFutures_Object_4(self):
        for i in range(0,5):
            client = OneXAPI.Binance.Futures('fnq543wb')

    def test_BinanceFutures_Object_5(self):
        client = OneXAPI.Binance.Futures('{"accessKey":"Test Access Key"}')
        res = client.getConfig()
        self.assertEqual(res['data']['accessKey'], 'Test Access Key')
        self.assertEqual(res['data']['secretKey'], '')

    def test_BinanceFutures_Object_6(self):
        client = OneXAPI.Binance.Futures('{"secretKey":"Test Secret Key"}')
        res = client.getConfig()
        self.assertEqual(res['data']['secretKey'], 'Test Secret Key')
        self.assertEqual(res['data']['accessKey'], '')    

    def test_BinanceFutures_Object_7(self):
        client = OneXAPI.Binance.Futures('{"accessKey":"Test Access Key", "secretKey":"Test Secret Key"}')
        res = client.getConfig()
        self.assertEqual(res['data']['accessKey'], 'Test Access Key')
        self.assertEqual(res['data']['secretKey'], 'Test Secret Key')

    def test_getConfig_1(self):
        client = OneXAPI.Binance.Futures()
        res = client.getConfig()
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"exchange":"Binance","instrument":"Futures","accessKey":"","secretKey":"","restEndpoint":"https://fapi.binance.com","publicWebsocketEndpoint":"wss://fstream.binance.com/ws","privateWebsocketEndpoint":"wss://fstream.binance.com/ws","restRequestTimeout":5000,"websocketConnectTimeout":5000,"websocketIdleTimeout":5000}}')
        self.assertEqual(res, answer)
    
    def test_getConfig_2(self):
        client = OneXAPI.Binance.Futures()
        res = client.getConfig("")
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"exchange":"Binance","instrument":"Futures","accessKey":"","secretKey":"","restEndpoint":"https://fapi.binance.com","publicWebsocketEndpoint":"wss://fstream.binance.com/ws","privateWebsocketEndpoint":"wss://fstream.binance.com/ws","restRequestTimeout":5000,"websocketConnectTimeout":5000,"websocketIdleTimeout":5000}}')
        self.assertEqual(res, answer)

    def test_getConfig_3(self):
        client = OneXAPI.Binance.Futures()
        res = client.getConfig("{}")
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"exchange":"Binance","instrument":"Futures","accessKey":"","secretKey":"","restEndpoint":"https://fapi.binance.com","publicWebsocketEndpoint":"wss://fstream.binance.com/ws","privateWebsocketEndpoint":"wss://fstream.binance.com/ws","restRequestTimeout":5000,"websocketConnectTimeout":5000,"websocketIdleTimeout":5000}}')
        self.assertEqual(res, answer)

    def test_getConfig_4(self):
        client = OneXAPI.Binance.Futures()
        res = client.getConfig("trashData123@@!%")

        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], False)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['errorType'], 'JSON_PARSING_ERROR')

    def test_setConfig_1(self):
        client = OneXAPI.Binance.Futures()
        res = client.setConfig("")
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{}}')
        self.assertEqual(res, answer)

    def test_setConfig_2(self):
        client = OneXAPI.Binance.Futures()
        res = client.setConfig("{}")
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{}}')
        self.assertEqual(res, answer)

    def test_setConfig_3(self):
        client = OneXAPI.Binance.Futures()
        res = client.setConfig('{"accessKey":1.1354}')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], False)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['errorType'], 'WRONG_VALUE_TYPE')

        res = client.setConfig('{"secretKey":11354}')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], False)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['errorType'], 'WRONG_VALUE_TYPE')

        res = client.setConfig('{"restEndpoint":null}')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], False)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['errorType'], 'WRONG_VALUE_TYPE')

        res = client.setConfig('{"publicWebsocketEndpoint":true}')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], False)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['errorType'], 'WRONG_VALUE_TYPE')

        res = client.setConfig('{"privateWebsocketEndpoint":{}}')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], False)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['errorType'], 'WRONG_VALUE_TYPE')

        res = client.setConfig('{"restRequestTimeout":1.1354}')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], False)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['errorType'], 'WRONG_VALUE_TYPE')

        res = client.setConfig('{"websocketConnectTimeout":"ffaew"}')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], False)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['errorType'], 'WRONG_VALUE_TYPE')

        res = client.setConfig('{"websocketIdleTimeout":false}')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], False)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['errorType'], 'WRONG_VALUE_TYPE')

    def test_setConfig_4(self):
        client = OneXAPI.Binance.Futures()
        res = client.setConfig('{"restEndpoint":"wrongEndpoint"}')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], False)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['errorType'], 'WRONG_VALUE')

        res = client.setConfig('{"publicWebsocketEndpoint":"wrongEndpoint"}')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], False)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['errorType'], 'WRONG_VALUE')

        res = client.setConfig('{"privateWebsocketEndpoint":"wrongEndpoint"}')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], False)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['errorType'], 'WRONG_VALUE')

    def test_setConfig_5(self):
        client = OneXAPI.Binance.Futures()
        testList = [
            ('accessKey','"test access key"'),
            ('secretKey','"test secret key"'),
            ('restEndpoint','"https://testnet.binancefuture.com"'),
            ('publicWebsocketEndpoint','"wss://fstream-auth.binance.com/ws"'),
            ('privateWebsocketEndpoint','"wss://fstream-auth.binance.com/ws"'),
            ('restRequestTimeout','1378331'),
            ('websocketConnectTimeout','3787123'),
            ('websocketIdleTimeout','8941313531215')
        ]

        for item in testList:
            input = '{"' + item[0] + '":' + item[1] + '}'
            res = client.setConfig(input)

            self.assertEqual(len(res), 3)
            self.assertEqual(res['success'], True)
            self.assertEqual(res['requestedApiCount'], 0)
            answer = None
            if type(res['data'][item[0]]) == str:
                answer = item[1].replace('"', "")
            elif type(res['data'][item[0]]) == int:
                answer = int(item[1])

            self.assertEqual(res['data'][item[0]], answer)

        res = client.getConfig()

        for item in testList:
            self.assertEqual(len(res), 3)
            self.assertEqual(res['success'], True)
            self.assertEqual(res['requestedApiCount'], 0)
            answer = None
            if type(res['data'][item[0]]) == str:
                answer = item[1].replace('"', "")
            elif type(res['data'][item[0]]) == int:
                answer = int(item[1])
                
            self.assertEqual(res['data'][item[0]], answer)

    def test_getEndpointCandidates_1(self):
        client = OneXAPI.Binance.Futures()

        res = client.getEndpointCandidates()
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"restEndpoints":["https://fapi.binance.com","https://testnet.binancefuture.com"],"publicWebsocketEndpoints":["wss://fstream.binance.com/ws","wss://fstream-auth.binance.com/ws","wss://stream.binancefuture.com/ws"],"privateWebsocketEndpoints":["wss://fstream.binance.com/ws","wss://fstream-auth.binance.com/ws","wss://stream.binancefuture.com/ws"]}}')

        self.assertEqual(res, answer)

    def test_getEndpointCandidates_2(self):
        client = OneXAPI.Binance.Futures()

        res = client.getEndpointCandidates("")
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"restEndpoints":["https://fapi.binance.com","https://testnet.binancefuture.com"],"publicWebsocketEndpoints":["wss://fstream.binance.com/ws","wss://fstream-auth.binance.com/ws","wss://stream.binancefuture.com/ws"],"privateWebsocketEndpoints":["wss://fstream.binance.com/ws","wss://fstream-auth.binance.com/ws","wss://stream.binancefuture.com/ws"]}}')

        self.assertEqual(res, answer)

    def test_getEndpointCandidates_3(self):
        client = OneXAPI.Binance.Futures()

        res = client.getEndpointCandidates("{}")
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"restEndpoints":["https://fapi.binance.com","https://testnet.binancefuture.com"],"publicWebsocketEndpoints":["wss://fstream.binance.com/ws","wss://fstream-auth.binance.com/ws","wss://stream.binancefuture.com/ws"],"privateWebsocketEndpoints":["wss://fstream.binance.com/ws","wss://fstream-auth.binance.com/ws","wss://stream.binancefuture.com/ws"]}}')

        self.assertEqual(res, answer)

    def test_getEndpointCandidates_4(self):
        client = OneXAPI.Binance.Futures()

        res = client.getEndpointCandidates("uNPaRsib1eM5g")
        
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], False)
        self.assertEqual(res['requestedApiCount'], 0)

        self.assertEqual(res['data']['errorType'], "JSON_PARSING_ERROR")

    def test_has_1(self):
        client = OneXAPI.Binance.Futures()

        res = client.has('')

        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], True)
        self.assertEqual(res['requestedApiCount'], 0)
        answer = json.loads(hasMap)

        for key, value in answer.items():
            self.assertEqual(res['data'][key], value)

        self.assertEqual(len(res['data']), 39)

    def test_has_2(self):
        client = OneXAPI.Binance.Futures()

        res = client.has('{}')
        
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], True)
        self.assertEqual(res['requestedApiCount'], 0)
        answer = json.loads(hasMap)

        for key, value in answer.items():
            self.assertEqual(res['data'][key], value)

        self.assertEqual(len(res['data']), 39)

    def test_has_3(self):
        client = OneXAPI.Binance.Futures()

        res = client.has('el12nlgv@!')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], False)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['errorType'], 'JSON_PARSING_ERROR')

    def test_has_4(self):
        client = OneXAPI.Binance.Futures()

        answer = json.loads(hasMap)

        for key, value in answer.items():
            res = client.has('{"api":"' + key + '"}')
            self.assertEqual(len(res), 3)
            self.assertEqual(res['success'], True)
            self.assertEqual(res['requestedApiCount'], 0)
            self.assertEqual(res['data'][key], value)
            self.assertEqual(len(res['data']), 1)

    def test_has_5(self):
        client = OneXAPI.Binance.Futures()

        res = client.has('{"api":"notExistApi"}')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], False)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['errorType'], 'WRONG_VALUE')

    def test_fetchBalance_1(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')
        
        res = client.fetchBalance('{"currencies":[]}')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], True)
        self.assertEqual(res['requestedApiCount'], 1)
        self.assertEqual(res['data']['fetchType'], "rest")
        self.assertEqual(len(res['data']), 2)
        
        for currency, balance in res['data']['balance'].items():
            self.assertEqual(type(balance["balance"]), type(""))
            self.assertEqual(type(balance["crossWalletBalance"]), type(""))
            self.assertEqual(type(balance["availableBalance"]), type(""))
            self.assertEqual(len(balance), 3)

    def test_fetchBalance_2(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')
        
        res = client.fetchBalance('{"currencies":["bTc","xRP","Eth"], "zeroBalance": true}')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], True)
        self.assertEqual(res['requestedApiCount'], 1)
        self.assertEqual(res['data']['fetchType'], "rest")
        self.assertEqual(len(res['data']), 2)
        self.assertEqual(len(res['data']['balance']), 3)
        
        for currency, balance in res['data']['balance'].items():
            self.assertEqual(type(balance["balance"]), type(""))
            self.assertEqual(type(balance["crossWalletBalance"]), type(""))
            self.assertEqual(type(balance["availableBalance"]), type(""))
            self.assertEqual(len(balance), 3)

    def test_fetchBalance_3(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        client.subscribeBalance()
        res = client.fetchBalance('{"currencies":["bTc","xRP","Eth"], "zeroBalance": true}')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], True)
        self.assertEqual(res['requestedApiCount'], 1)
        self.assertEqual(res['data']['fetchType'], "rest")
        self.assertEqual(len(res['data']), 2)
        self.assertEqual(len(res['data']['balance']), 3)
        
        for currency, balance in res['data']['balance'].items():
            self.assertEqual(type(balance["balance"]), type(""))
            self.assertEqual(type(balance["crossWalletBalance"]), type(""))
            self.assertEqual(type(balance["availableBalance"]), type(""))
            self.assertEqual(len(balance), 3)

    def test_fetchBalance_4(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        client.subscribeBalance()
        res = client.fetchBalance('{"currencies":["bTc","xRP","Eth"], "zeroBalance": true, "forceRestApi": true}')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], True)
        self.assertEqual(res['requestedApiCount'], 1)
        self.assertEqual(res['data']['fetchType'], "rest")
        self.assertEqual(len(res['data']), 2)
        
        for currency, balance in res['data']['balance'].items():
            self.assertEqual(type(balance["balance"]), type(""))
            self.assertEqual(type(balance["crossWalletBalance"]), type(""))
            self.assertEqual(type(balance["availableBalance"]), type(""))
            self.assertEqual(len(balance), 3)

    def test_fetchPositions_1(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')
        res = client.fetchPositions('{}')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], True)
        self.assertEqual(res['requestedApiCount'], 1)
        self.assertEqual(res['data']['fetchType'], "rest")
        self.assertEqual(type(res['data']['positions']), type([]))
        self.assertEqual(len(res['data']), 2)
        
        for position in res['data']['positions']:
            self.assertEqual(type(position["baseCurrency"]), type(""))
            self.assertEqual(type(position["quoteCurrency"]), type(""))
            self.assertEqual(type(position["expiration"]), type(""))
            self.assertEqual(type(position["symbol"]), type(""))
            self.assertEqual(type(position["unrealizedProfit"]), type(""))
            self.assertEqual(type(position["entryPrice"]), type(""))
            self.assertEqual(type(position["positionAmt"]), type(""))
            positionAmt = float(position["positionAmt"])
            self.assertNotEqual(0.0, positionAmt)
            self.assertEqual(type(position["leverage"]), type(1))
            marginType = position["marginType"]
            if marginType not in ['cross', 'isolated']:
                self.fail('marginType is not cross or isolated')
            self.assertEqual(len(position), 9)
    
    def test_fetchPositions_2(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')
        res = client.fetchPositions('{"baseCurrency":"bTC","zeroAmount":true}')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], True)
        self.assertEqual(res['requestedApiCount'], 1)
        self.assertEqual(res['data']['fetchType'], "rest")
        self.assertEqual(type(res['data']['positions']), type([]))
        self.assertGreater(len(res['data']['positions']), 0)
        self.assertEqual(len(res['data']), 2)
        
        for position in res['data']['positions']:
            self.assertEqual(position["baseCurrency"], "BTC")
            self.assertEqual(type(position["quoteCurrency"]), type(""))
            self.assertEqual(type(position["expiration"]), type(""))
            self.assertEqual(type(position["symbol"]), type(""))
            self.assertEqual(type(position["unrealizedProfit"]), type(""))
            self.assertEqual(type(position["entryPrice"]), type(""))
            self.assertEqual(type(position["positionAmt"]), type(""))
            self.assertEqual(type(position["leverage"]), type(1))
            marginType = position["marginType"]
            if marginType not in ['cross', 'isolated']:
                self.fail('marginType is not cross or isolated')
            self.assertEqual(len(position), 9)

    def test_fetchPositions_3(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')
        res = client.fetchPositions('{"baseCurrency":"etH","quoteCurrency":"usdT","expiration":"PerP","zeroAmount":true}')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], True)
        self.assertEqual(res['requestedApiCount'], 1)
        self.assertEqual(res['data']['fetchType'], "rest")
        self.assertEqual(type(res['data']['positions']), type([]))
        self.assertEqual(len(res['data']['positions']), 1)
        self.assertEqual(len(res['data']), 2)
        
        for position in res['data']['positions']:
            self.assertEqual(position["baseCurrency"], "ETH")
            self.assertEqual(position["quoteCurrency"], "USDT")
            self.assertEqual(position["expiration"], "PERP")
            self.assertEqual(position["symbol"], "ETHUSDT")
            self.assertEqual(type(position["unrealizedProfit"]), type(""))
            self.assertEqual(type(position["entryPrice"]), type(""))
            self.assertEqual(type(position["positionAmt"]), type(""))
            self.assertEqual(type(position["leverage"]), type(1))
            marginType = position["marginType"]
            if marginType not in ['cross', 'isolated']:
                self.fail('marginType is not cross or isolated')
            self.assertEqual(len(position), 9)

    def test_fetchPositions_4(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')
        client.subscribeBalance()
        res = client.fetchPositions('{"baseCurrency":"Eth"}')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], True)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['fetchType'], "websocket")
        self.assertEqual(type(res['data']['positions']), type([]))
        self.assertEqual(len(res['data']), 2)
        
        for position in res['data']['positions']:
            self.assertEqual(position["baseCurrency"], "ETH")
            self.assertEqual(type(position["quoteCurrency"]), type(""))
            self.assertEqual(type(position["expiration"]), type(""))
            self.assertEqual(type(position["symbol"]), type(""))
            self.assertEqual(type(position["unrealizedProfit"]), type(""))
            self.assertEqual(type(position["entryPrice"]), type(""))
            self.assertEqual(type(position["positionAmt"]), type(""))
            positionAmt = float(position["positionAmt"])
            self.assertNotEqual(0.0, positionAmt)
            self.assertEqual(type(position["leverage"]), type(1))
            marginType = position["marginType"]
            if marginType not in ['cross', 'isolated']:
                self.fail('marginType is not cross or isolated')
            self.assertEqual(len(position), 9)

    def test_fetchPositions_5(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')
        client.subscribeBalance()
        res = client.fetchPositions('{"baseCurrency":"Eth","zeroAmount":true}')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], True)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['fetchType'], "websocket")
        self.assertEqual(type(res['data']['positions']), type([]))
        self.assertGreater(len(res['data']['positions']), 0)
        self.assertEqual(len(res['data']), 2)
        
        for position in res['data']['positions']:
            self.assertEqual(position["baseCurrency"], "ETH")
            self.assertEqual(type(position["quoteCurrency"]), type(""))
            self.assertEqual(type(position["expiration"]), type(""))
            self.assertEqual(type(position["symbol"]), type(""))
            self.assertEqual(type(position["unrealizedProfit"]), type(""))
            self.assertEqual(type(position["entryPrice"]), type(""))
            self.assertEqual(type(position["positionAmt"]), type(""))
            self.assertEqual(type(position["leverage"]), type(1))
            marginType = position["marginType"]
            if marginType not in ['cross', 'isolated']:
                self.fail('marginType is not cross or isolated')
            self.assertEqual(len(position), 9)

    def test_fetchPositions_6(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')
        client.subscribeBalance()
        res = client.fetchPositions('{"baseCurrency":"Eth","zeroAmount":true, "forceRestApi": true}')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], True)
        self.assertEqual(res['requestedApiCount'], 1)
        self.assertEqual(res['data']['fetchType'], "rest")
        self.assertEqual(type(res['data']['positions']), type([]))
        self.assertGreater(len(res['data']['positions']), 0)
        self.assertEqual(len(res['data']), 2)
        
        for position in res['data']['positions']:
            self.assertEqual(position["baseCurrency"], "ETH")
            self.assertEqual(type(position["quoteCurrency"]), type(""))
            self.assertEqual(type(position["expiration"]), type(""))
            self.assertEqual(type(position["symbol"]), type(""))
            self.assertEqual(type(position["unrealizedProfit"]), type(""))
            self.assertEqual(type(position["entryPrice"]), type(""))
            self.assertEqual(type(position["positionAmt"]), type(""))
            self.assertEqual(type(position["leverage"]), type(1))
            marginType = position["marginType"]
            if marginType not in ['cross', 'isolated']:
                self.fail('marginType is not cross or isolated')
            self.assertEqual(len(position), 9)

    def test_fetchFundingFeeIncomeHistory_1(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        res = client.fetchFundingFeeIncomeHistory('{}')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], False)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['errorType'], "NOT_ENOUGH_PARAM")

    def test_fetchFundingFeeIncomeHistory_2(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        specificTime = int((datetime.today() - relativedelta(years=1)).timestamp())

        res = client.fetchFundingFeeIncomeHistory('{"startTime":' + str(specificTime) +'}')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], True)
        self.assertEqual(res['requestedApiCount'], 1)
        self.assertEqual(type(res['data']['incomes']), type([]))
        self.assertEqual(len(res['data']), 1)

        for income in res['data']['incomes']:
            self.assertEqual(type(income['baseCurrency']), type(""))
            self.assertEqual(type(income['quoteCurrency']), type(""))
            self.assertEqual(type(income['expiration']), type(""))
            self.assertEqual(type(income['symbol']), type(""))
            self.assertEqual(type(income['income']), type(""))
            self.assertEqual(type(income['incomeCurrency']), type(""))
            self.assertGreater(income['timestamp'], 10000000000)
            self.assertEqual(len(income), 7)

    def test_fetchFundingFeeIncomeHistory_3(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        specificTime = int((datetime.today() - relativedelta(years=1)).timestamp())
        nowTime = int(datetime.now().timestamp())

        requestTime = time.localtime(time.time())

        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"file","logLevel":"info"}}')

        res = client.fetchFundingFeeIncomeHistory('{"baseCurrency":"dOGe","quoteCurrency":"uSdT","expiration":"PerP","startTime":' +
            str(specificTime) + ',"endTime":' + str(nowTime) + '}')
        
        time.sleep(1)
        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"terminal","logLevel":"off"}}')

        answer1 = 'https://fapi.binance.com/fapi/v1/income?incomeType=FUNDING_FEE&startTime=' + str(specificTime) + '&endTime=' + str(nowTime)

        if util.searchLog(requestTime, answer1) is False:
            self.fail(f'{answer1} not found')

        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], True)
        self.assertEqual(res['requestedApiCount'], 1)
        self.assertEqual(type(res['data']['incomes']), type([]))
        self.assertEqual(len(res['data']), 1)

        for income in res['data']['incomes']:
            self.assertEqual(income['baseCurrency'], "DOGE")
            self.assertEqual(income['quoteCurrency'], "USDT")
            self.assertEqual(income['expiration'], "PERP")
            self.assertEqual(income['symbol'], "DOGEUSDT")
            self.assertEqual(type(income['income']), type(""))
            self.assertEqual(type(income['incomeCurrency']), type(""))
            self.assertGreater(income['timestamp'], 10000000000)
            self.assertEqual(len(income), 7)

    def test_subscribeBalance_1(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        res = client.subscribeBalance()
        answer = json.loads('{"success":true,"requestedApiCount":2,"data":{}}')
        self.assertEqual(res, answer)

    def test_subscribeBalance_2(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        res = client.subscribeBalance('')
        answer = json.loads('{"success":true,"requestedApiCount":2,"data":{}}')
        self.assertEqual(res, answer)

    def test_subscribeBalance_3(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        res = client.subscribeBalance('{}')
        answer = json.loads('{"success":true,"requestedApiCount":2,"data":{}}')
        self.assertEqual(res, answer)

    def test_subscribeBalance_4(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        res = client.subscribeBalance('Bqbqb@')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], False)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['errorType'], 'JSON_PARSING_ERROR')

    def test_unsubscribeBalance_1(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        res = client.unsubscribeBalance()
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{}}')
        self.assertEqual(res, answer)

    def test_unsubscribeBalance_2(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        res = client.unsubscribeBalance('')
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{}}')
        self.assertEqual(res, answer)

    def test_unsubscribeBalance_3(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        client.subscribeBalance()
        res = client.unsubscribeBalance('{}')
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{}}')
        self.assertEqual(res, answer)

    def test_unsubscribeBalance_4(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        res = client.unsubscribeBalance('Bqbqb@')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], False)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['errorType'], 'JSON_PARSING_ERROR')

    def test_isSubscribingBalance_1(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        res = client.isSubscribingBalance()
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"isSubscribing":false}}')

        self.assertEqual(res, answer)

    def test_isSubscribingBalance_2(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        res = client.isSubscribingBalance('')
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"isSubscribing":false}}')

        self.assertEqual(res, answer)

    def test_isSubscribingBalance_3(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        client.subscribeBalance()
        res = client.isSubscribingBalance('{}')
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"isSubscribing":true}}')

        self.assertEqual(res, answer)

    def test_isSubscribingBalance_4(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        client.subscribeBalance()
        client.unsubscribeBalance()
        res = client.isSubscribingBalance('Bqbqb@')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], False)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['errorType'], 'JSON_PARSING_ERROR')

    def test_getOrderRoundingRule_1(self):
        client = OneXAPI.Binance.Futures()
        res = client.getOrderRoundingRule()
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"limitBuyPrice":"round","limitBuyBaseAmount":"round","limitSellPrice":"round","limitSellBaseAmount":"round","marketBuyBaseAmount":"round","marketSellBaseAmount":"round"}}')

        self.assertEqual(res, answer)

    def test_getOrderRoundingRule_2(self):
        client = OneXAPI.Binance.Futures()
        res = client.getOrderRoundingRule("")
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"limitBuyPrice":"round","limitBuyBaseAmount":"round","limitSellPrice":"round","limitSellBaseAmount":"round","marketBuyBaseAmount":"round","marketSellBaseAmount":"round"}}')

        self.assertEqual(res, answer)

    def test_setOrderRoundingRule_1(self):
        client = OneXAPI.Binance.Futures()

        res = client.setOrderRoundingRule('{"limitBuyBaseAmount":"wrongData"}')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], False)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['errorType'], 'WRONG_VALUE')

    def test_setOrderRoundingRule_2(self):
        client = OneXAPI.Binance.Futures()

        answer_ceil = json.loads('{"success":true,"requestedApiCount":0,"data":{"limitBuyPrice":"ceil","limitBuyBaseAmount":"ceil","limitSellPrice":"ceil","limitSellBaseAmount":"ceil","marketBuyBaseAmount":"ceil","marketSellBaseAmount":"ceil"}}')
        answer_floor = json.loads('{"success":true,"requestedApiCount":0,"data":{"limitBuyPrice":"floor","limitBuyBaseAmount":"floor","limitSellPrice":"floor","limitSellBaseAmount":"floor","marketBuyBaseAmount":"floor","marketSellBaseAmount":"floor"}}')
        answer_round = json.loads('{"success":true,"requestedApiCount":0,"data":{"limitBuyPrice":"round","limitBuyBaseAmount":"round","limitSellPrice":"round","limitSellBaseAmount":"round","marketBuyBaseAmount":"round","marketSellBaseAmount":"round"}}')

        keyList = ['limitBuyPrice', 'limitBuyBaseAmount', 'limitSellPrice', 'limitSellBaseAmount', 'marketBuyBaseAmount', 'marketSellBaseAmount']
        valueList = ['ceil', 'floor', 'round']

        for value in valueList:
            for key in keyList:
                input = '{"' + key + '":"' + value + '"}'
                answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"' + key + '":"' + value + '"}}')
                res = client.setOrderRoundingRule(input)
                self.assertEqual(len(res), 3)
                self.assertEqual(res['success'], True)
                self.assertEqual(res['requestedApiCount'], 0)
                self.assertEqual(len(res['data']), 1)
                self.assertEqual(res, answer)

            res = client.getOrderRoundingRule()
            self.assertEqual(len(res), 3)
            self.assertEqual(res['success'], True)
            self.assertEqual(res['requestedApiCount'], 0)
            if(value == 'ceil'):
                self.assertEqual(res, answer_ceil)
            elif(value == 'floor'):
                self.assertEqual(res, answer_floor)
            elif(value == 'round'):
                self.assertEqual(res, answer_round)

    def test_orderLimitBuy_1(self):
        client = OneXAPI.Binance.Futures()
        
        res = client.orderLimitBuy('{}')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], False)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_orderLimitBuy_2(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures()

        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"file","logLevel":"info"}}')

        nowTime = time.localtime(time.time())
        
        client.orderLimitBuy('{"baseCurrency":"bTC","quoteCurrency":"uSDt","price":25312.1234358,"baseAmount":35.135689342158}')
        time.sleep(1)
        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"terminal","logLevel":"off"}}')

        answer1 = 'https://fapi.binance.com/fapi/v1/order?symbol=BTCUSDT&side=BUY&type=LIMIT&timeInForce=GTC&quantity=35.136&reduceOnly=false&price=25312.1'

        if util.searchLog(nowTime, answer1) is False:
            self.fail(f'{answer1} not found')

    def test_orderLimitBuy_3(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures()

        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"file","logLevel":"info"}}')

        nowTime = time.localtime(time.time())
        
        client.orderLimitBuy('{"baseCurrency":"bTC","quoteCurrency":"uSDt","expiration":"peRP","price":25312.1234358,"baseAmount":35.135689342158,"reduceOnly":true,"clientOrderId":"testId","amplifier":1.0346,"type":"fok"}')
        time.sleep(1)
        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"terminal","logLevel":"off"}}')

        answer1 = 'https://fapi.binance.com/fapi/v1/order?symbol=BTCUSDT&side=BUY&type=LIMIT&timeInForce=FOK&quantity=35.136&reduceOnly=true&price=26187.9&newClientOrderId=testId'

        if util.searchLog(nowTime, answer1) is False:
            self.fail(f'{answer1} not found')

    def test_orderLimitSell_1(self):
        client = OneXAPI.Binance.Futures()
        
        res = client.orderLimitSell('{}')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], False)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_orderLimitSell_2(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures()

        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"file","logLevel":"info"}}')

        nowTime = time.localtime(time.time())
        
        client.orderLimitSell('{"baseCurrency":"bTC","quoteCurrency":"uSDt","price":25312.1234358,"baseAmount":35.135689342158}')
        time.sleep(1)
        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"terminal","logLevel":"off"}}')

        answer1 = 'https://fapi.binance.com/fapi/v1/order?symbol=BTCUSDT&side=SELL&type=LIMIT&timeInForce=GTC&quantity=35.136&reduceOnly=false&price=25312.1'

        if util.searchLog(nowTime, answer1) is False:
            self.fail(f'{answer1} not found')

    def test_orderLimitSell_3(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures()

        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"file","logLevel":"info"}}')

        nowTime = time.localtime(time.time())
        
        client.orderLimitSell('{"baseCurrency":"bTC","quoteCurrency":"uSDt","expiration":"peRP","price":25312.1234358,"baseAmount":35.135689342158,"reduceOnly":true,"clientOrderId":"testId","amplifier":0.96348,"type":"ioc"}')
        time.sleep(1)
        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"terminal","logLevel":"off"}}')

        answer1 = 'https://fapi.binance.com/fapi/v1/order?symbol=BTCUSDT&side=SELL&type=LIMIT&timeInForce=IOC&quantity=35.136&reduceOnly=true&price=24387.7&newClientOrderId=testId'

        if util.searchLog(nowTime, answer1) is False:
            self.fail(f'{answer1} not found')

    def test_orderMarketBuy_1(self):
        client = OneXAPI.Binance.Futures()
        
        res = client.orderMarketBuy('{}')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], False)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_orderMarketBuy_2(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures()

        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"file","logLevel":"info"}}')

        nowTime = time.localtime(time.time())
        
        client.orderMarketBuy('{"baseCurrency":"bTC","quoteCurrency":"usdT","baseAmount":35.135689342158}')
        time.sleep(1)
        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"terminal","logLevel":"off"}}')

        answer1 = 'https://fapi.binance.com/fapi/v1/order?symbol=BTCUSDT&side=BUY&type=MARKET&quantity=35.136&reduceOnly=false'

        if util.searchLog(nowTime, answer1) is False:
            self.fail(f'{answer1} not found')

    def test_orderMarketBuy_3(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures()

        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"file","logLevel":"info"}}')

        nowTime = time.localtime(time.time())
        
        client.orderMarketBuy('{"baseCurrency":"bTC","quoteCurrency":"usdT","expiration":"peRP","baseAmount":35.135689342158,"reduceOnly":true,"clientOrderId":"testId"}')
        time.sleep(1)
        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"terminal","logLevel":"off"}}')

        answer1 = 'https://fapi.binance.com/fapi/v1/order?symbol=BTCUSDT&side=BUY&type=MARKET&quantity=35.136&reduceOnly=true&newClientOrderId=testId'

        if util.searchLog(nowTime, answer1) is False:
            self.fail(f'{answer1} not found')

    def test_orderMarketSell_1(self):
        client = OneXAPI.Binance.Futures()
        
        res = client.orderMarketSell('{}')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], False)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_orderMarketSell_2(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures()

        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"file","logLevel":"info"}}')

        nowTime = time.localtime(time.time())
        
        client.orderMarketSell('{"baseCurrency":"bTC","quoteCurrency":"usdT","baseAmount":83.1338494835}')
        time.sleep(1)
        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"terminal","logLevel":"off"}}')

        answer1 = 'https://fapi.binance.com/fapi/v1/order?symbol=BTCUSDT&side=SELL&type=MARKET&quantity=83.134&reduceOnly=false'

        if util.searchLog(nowTime, answer1) is False:
            self.fail(f'{answer1} not found')

    def test_orderMarketSell_3(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures()

        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"file","logLevel":"info"}}')

        nowTime = time.localtime(time.time())
        
        client.orderMarketSell('{"baseCurrency":"bTC","quoteCurrency":"usdT","expiration":"peRP","baseAmount":83.1338494835,"reduceOnly":true,"clientOrderId":"testId"}')
        time.sleep(1)
        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"terminal","logLevel":"off"}}')

        answer1 = 'https://fapi.binance.com/fapi/v1/order?symbol=BTCUSDT&side=SELL&type=MARKET&quantity=83.134&reduceOnly=true&newClientOrderId=testId'

        if util.searchLog(nowTime, answer1) is False:
            self.fail(f'{answer1} not found')

    def test_orderCancel_1(self):
        client = OneXAPI.Binance.Futures()
        
        res = client.orderCancel('{}')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], False)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_orderCancel_2(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures()

        res = client.orderCancel('{"orderId":"testOrderId"}')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], False)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_orderCancel_3(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures()

        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"file","logLevel":"info"}}')

        nowTime = time.localtime(time.time())
        
        client.orderCancel('{"baseCurrency":"bTC","quoteCurrency":"usdT","expiration":"123456","orderId":"testOrderId"}')
        time.sleep(1)
        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"terminal","logLevel":"off"}}')

        answer1 = 'https://fapi.binance.com/fapi/v1/order?symbol=BTCUSDT_123456&orderId=testOrderId'

        if util.searchLog(nowTime, answer1) is False:
            self.fail(f'{answer1} not found')

    def test_orderCancel_4(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures()

        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"file","logLevel":"info"}}')

        nowTime = time.localtime(time.time())
        
        client.orderCancel('{"baseCurrency":"bTC","quoteCurrency":"usdT","clientOrderId":"testClientOrderId"}')
        time.sleep(1)
        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"terminal","logLevel":"off"}}')

        answer1 = 'https://fapi.binance.com/fapi/v1/order?symbol=BTCUSDT&origClientOrderId=testClientOrderId'

        if util.searchLog(nowTime, answer1) is False:
            self.fail(f'{answer1} not found')

    def test_fetchOrderInfo_1(self):
        client = OneXAPI.Binance.Futures()
        
        res = client.fetchOrderInfo('{}')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], False)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_fetchOrderInfo_2(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        res = client.fetchOrderInfo('{"orderId":"testOrderId"}')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], False)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_fetchOrderInfo_3(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures()

        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"file","logLevel":"info"}}')

        nowTime = time.localtime(time.time())
        
        client.fetchOrderInfo('{"baseCurrency":"bTC","quoteCurrency":"UsdT","orderId":"testOrderId"}')
        time.sleep(1)
        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"terminal","logLevel":"off"}}')

        answer1 = 'https://fapi.binance.com/fapi/v1/order?symbol=BTCUSDT&orderId=testOrderId'

        if util.searchLog(nowTime, answer1) is False:
            self.fail(f'{answer1} not found')

    def test_fetchOrderInfo_4(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures()

        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"file","logLevel":"info"}}')

        nowTime = time.localtime(time.time())
        
        client.fetchOrderInfo('{"baseCurrency":"bTC","quoteCurrency":"UsdT","expiration":"953215","clientOrderId":"testClientOrderId"}')
        time.sleep(1)
        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"terminal","logLevel":"off"}}')

        answer1 = 'https://fapi.binance.com/fapi/v1/order?symbol=BTCUSDT_953215&origClientOrderId=testClientOrderId'

        if util.searchLog(nowTime, answer1) is False:
            self.fail(f'{answer1} not found')

    def test_fetchOrderInfo_5(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        res = client.fetchOrderbook('{"baseCurrency": "XrP", "quoteCurrency": "UsdT"}')
        bidPrice = float(res['data']['bids'][0]['price'])

        res = client.orderLimitBuy('{"baseCurrency": "xRp", "quoteCurrency": "UsdT", "price": ' + str(bidPrice) + ', "baseAmount": 25, "amplifier": 0.96}')
        orderId = res['data']['orderId']

        res = client.fetchOrderInfo('{"baseCurrency": "xRp", "quoteCurrency": "UsdT", "orderId": "' + orderId + '"}')
        client.orderCancel('{"baseCurrency": "xRp", "quoteCurrency": "UsdT", "orderId": "' + orderId + '"}')

        self.assertEqual(res['success'], True)
        self.assertEqual(res['requestedApiCount'], 2)
        self.assertEqual(len(res['data']), 19)
        self.assertEqual(type(res['data']['baseCurrency']), type(''))
        self.assertEqual(type(res['data']['quoteCurrency']), type(''))
        self.assertEqual(type(res['data']['expiration']), type(''))
        self.assertEqual(type(res['data']['symbol']), type(''))
        self.assertEqual(res['data']['orderId'], orderId)
        self.assertEqual(type(res['data']['clientOrderId']), type(''))
        self.assertEqual(res['data']['side'], 'buy')
        self.assertEqual(res['data']['positionSide'], 'long')
        self.assertEqual(type(res['data']['reduceOnly']), type(True))
        self.assertEqual(type(res['data']['originalAmount']), type(''))
        self.assertEqual(type(res['data']['filledAmount']), type(''))
        self.assertEqual(type(res['data']['remainingAmount']), type(''))
        self.assertEqual(type(res['data']['originalPrice']), type(''))
        self.assertEqual(type(res['data']['avgFillPrice']), type(''))
        self.assertEqual(type(res['data']['created']), type(1))
        self.assertEqual(type(res['data']['feeCurrency']), type(''))
        self.assertEqual(type(res['data']['feeAmount']), type(''))
        self.assertEqual(type(res['data']['status']), type(''))
        self.assertEqual(res['data']['fills'], [])

    def test_fetchOpenOrders_1(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        res = client.fetchOrderbook('{"baseCurrency": "XrP", "quoteCurrency": "UsdT"}')
        bidPrice = float(res['data']['bids'][0]['price'])

        res = client.orderLimitBuy('{"baseCurrency": "xRp", "quoteCurrency": "UsdT", "price": ' + str(bidPrice) + ', "baseAmount": 25, "amplifier": 0.96}')
        orderId = res['data']['orderId']

        res = client.fetchOpenOrders('{}')
        client.orderCancel('{"baseCurrency": "xRp", "quoteCurrency": "UsdT", "orderId": "' + orderId + '"}')

        self.assertEqual(res['success'], True)
        self.assertEqual(res['requestedApiCount'], 1)
        self.assertEqual(len(res['data']), 1)
        self.assertGreater(len(res['data']['openOrders']), 0)

        for openOrder in res['data']['openOrders']:
            self.assertEqual(type(openOrder['baseCurrency']), type(''))
            self.assertEqual(type(openOrder['quoteCurrency']), type(''))
            self.assertEqual(type(openOrder['expiration']), type(''))
            self.assertEqual(type(openOrder['symbol']), type(''))
            self.assertEqual(type(openOrder['orderId']), type(''))
            self.assertEqual(type(openOrder['side']), type(''))
            self.assertEqual(type(openOrder['positionSide']), type(''))
            self.assertEqual(type(openOrder['reduceOnly']), type(True))
            self.assertEqual(type(openOrder['originalAmount']), type(''))
            self.assertEqual(type(openOrder['filledAmount']), type(''))
            self.assertEqual(type(openOrder['remainingAmount']), type(''))
            self.assertEqual(type(openOrder['originalPrice']), type(''))
            self.assertEqual(type(openOrder['created']), type(1))
            self.assertEqual(len(openOrder), 13)

    def test_fetchOpenOrders_2(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        res = client.fetchOrderbook('{"baseCurrency": "XrP", "quoteCurrency": "UsdT"}')
        bidPrice = float(res['data']['bids'][0]['price'])

        res = client.orderLimitBuy('{"baseCurrency": "xRp", "quoteCurrency": "UsdT", "price": ' + str(bidPrice) + ', "baseAmount": 25, "amplifier": 0.96}')
        orderId = res['data']['orderId']

        res = client.fetchOpenOrders('{"baseCurrency":"xRP","quoteCurrency":"uSDt","expiration":"PerP","side":"buy"}')
        client.orderCancel('{"baseCurrency": "xRp","quoteCurrency": "UsdT","expiration":"PerP","orderId":"' + orderId + '"}')

        self.assertEqual(res['success'], True)
        self.assertEqual(res['requestedApiCount'], 1)
        self.assertEqual(len(res['data']), 1)
        self.assertEqual(len(res['data']['openOrders']), 1)

        for openOrder in res['data']['openOrders']:
            self.assertEqual(type(openOrder['baseCurrency']), type(''))
            self.assertEqual(type(openOrder['quoteCurrency']), type(''))
            self.assertEqual(type(openOrder['expiration']), type(''))
            self.assertEqual(type(openOrder['symbol']), type(''))
            self.assertEqual(type(openOrder['orderId']), type(''))
            self.assertEqual(type(openOrder['side']), type(''))
            self.assertEqual(type(openOrder['positionSide']), type(''))
            self.assertEqual(type(openOrder['reduceOnly']), type(True))
            self.assertEqual(type(openOrder['originalAmount']), type(''))
            self.assertEqual(type(openOrder['filledAmount']), type(''))
            self.assertEqual(type(openOrder['remainingAmount']), type(''))
            self.assertEqual(type(openOrder['originalPrice']), type(''))
            self.assertEqual(type(openOrder['created']), type(1))
            self.assertEqual(len(openOrder), 13)

    def test_fetchTradingFee_1(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')
        
        res = client.fetchTradingFee('{"baseCurrency":"bTC"}')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], False)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['errorType'], "NOT_ENOUGH_PARAM")

    def test_fetchTradingFee_2(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')
        
        res = client.fetchTradingFee('{"baseCurrency":"bTC","quoteCurrency":"UsdT","expiration":"PerP"}')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], True)
        self.assertEqual(res['requestedApiCount'], 1)
        self.assertEqual(type(res['data']['fees']), type([]))
        self.assertEqual(len(res['data']), 1)
        self.assertEqual(len(res['data']['fees']), 1)
        
        for fee in res['data']['fees']:
            self.assertEqual(type(fee['baseCurrency']), type(""))
            self.assertEqual(type(fee['quoteCurrency']), type(""))
            self.assertEqual(type(fee['expiration']), type(""))
            self.assertEqual(type(fee['symbol']), type(""))
            self.assertEqual(type(fee['makerFee']), type(""))
            self.assertEqual(type(fee['takerFee']), type(""))
            self.assertEqual(len(fee), 6)

    def test_fetchLeverage_1(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')
        
        res = client.fetchLeverage('{}')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], True)
        self.assertEqual(res['requestedApiCount'], 1)
        self.assertEqual(res['data']['fetchType'], 'rest')
        self.assertEqual(type(res['data']['leverages']), type([]))
        self.assertEqual(len(res['data']), 2)
        self.assertGreater(len(res['data']['leverages']), 10)

        for leverage in res['data']['leverages']:
            self.assertEqual(type(leverage['baseCurrency']), type(""))
            self.assertEqual(type(leverage['quoteCurrency']), type(""))
            self.assertEqual(type(leverage['expiration']), type(""))
            self.assertEqual(type(leverage['symbol']), type(""))
            self.assertEqual(type(leverage['leverage']), type(1))
            self.assertEqual(len(leverage), 5)

    def test_fetchLeverage_2(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')
        
        res = client.fetchLeverage('{"baseCurrency":"bTc","quoteCurrency":"USdt","expiration":"peRp"}')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], True)
        self.assertEqual(res['requestedApiCount'], 1)
        self.assertEqual(res['data']['fetchType'], 'rest')
        self.assertEqual(type(res['data']['leverages']), type([]))
        self.assertEqual(len(res['data']), 2)
        self.assertEqual(len(res['data']['leverages']), 1)

        for leverage in res['data']['leverages']:
            self.assertEqual(leverage['baseCurrency'], "BTC")
            self.assertEqual(leverage['quoteCurrency'], "USDT")
            self.assertEqual(leverage['expiration'], "PERP")
            self.assertEqual(leverage['symbol'], "BTCUSDT")
            self.assertEqual(type(leverage['leverage']), type(1))
            self.assertEqual(len(leverage), 5)

    def test_fetchLeverage_3(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')
        
        client.subscribeBalance()
        res = client.fetchLeverage('{"baseCurrency": "eTh"}')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], True)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['fetchType'], 'websocket')
        self.assertEqual(type(res['data']['leverages']), type([]))
        self.assertEqual(len(res['data']), 2)

        for leverage in res['data']['leverages']:
            self.assertEqual(leverage['baseCurrency'], "ETH")
            self.assertEqual(type(leverage['quoteCurrency']), type(""))
            self.assertEqual(type(leverage['expiration']), type(""))
            self.assertEqual(type(leverage['symbol']), type(""))
            self.assertEqual(type(leverage['leverage']), type(1))
            self.assertEqual(len(leverage), 5)

    def test_fetchLeverage_4(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')
        
        client.subscribeBalance()
        res = client.fetchLeverage('{"baseCurrency": "eTh", "forceRestApi": true}')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], True)
        self.assertEqual(res['requestedApiCount'], 1)
        self.assertEqual(res['data']['fetchType'], 'rest')
        self.assertEqual(type(res['data']['leverages']), type([]))
        self.assertEqual(len(res['data']), 2)

        for leverage in res['data']['leverages']:
            self.assertEqual(leverage['baseCurrency'], "ETH")
            self.assertEqual(type(leverage['quoteCurrency']), type(""))
            self.assertEqual(type(leverage['expiration']), type(""))
            self.assertEqual(type(leverage['symbol']), type(""))
            self.assertEqual(type(leverage['leverage']), type(1))
            self.assertEqual(len(leverage), 5)

    def test_changeLeverage_1(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')
        
        res = client.changeLeverage('{}')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], False)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_changeLeverage_2(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')
        
        res = client.fetchLeverage('{"baseCurrency":"bTC","quoteCurrency":"usDT","expiration":"perP"}')
        oldLeverage = res['data']['leverages'][0]['leverage']

        res = client.changeLeverage('{"baseCurrency":"bTC","quoteCurrency":"usDT","expiration":"perP","leverage":5}')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], True)
        self.assertEqual(res['requestedApiCount'], 1)
        
        self.assertEqual(res['data']['baseCurrency'], "BTC")
        self.assertEqual(res['data']['quoteCurrency'], "USDT")
        self.assertEqual(res['data']['expiration'], "PERP")
        self.assertEqual(res['data']['symbol'], "BTCUSDT")
        self.assertEqual(res['data']['leverage'], 5)
        self.assertEqual(len(res['data']), 5)

        res = client.changeLeverage('{"baseCurrency":"bTC","quoteCurrency":"usDT","expiration":"perP","leverage":' + str(oldLeverage) + '}')
        self.assertEqual(res['success'], True, "Can't restore Leverage")

    def test_fetchMarginType_1(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')
        
        res = client.fetchMarginType('{}')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], True)
        self.assertEqual(res['requestedApiCount'], 1)

        self.assertEqual(res['data']['fetchType'], "rest")
        self.assertEqual(type(res['data']['marginTypes']), type([]))
        self.assertEqual(len(res['data']), 2)
        self.assertGreater(len(res['data']['marginTypes']), 10)

        for marginType in res['data']['marginTypes']:
            self.assertEqual(type(marginType['baseCurrency']), type(''))
            self.assertEqual(type(marginType['quoteCurrency']), type(''))
            self.assertEqual(type(marginType['expiration']), type(''))
            self.assertEqual(type(marginType['symbol']), type(''))
            marginTypeName = marginType['marginType']
            if marginTypeName not in ['cross', 'isolated']:
                self.fail('marginType is not cross or isolated')
            self.assertEqual(len(marginType), 5)

    def test_fetchMarginType_2(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')
        
        res = client.fetchMarginType('{"baseCurrency":"bTc","quoteCurrency":"USdt","expiration":"peRp"}')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], True)
        self.assertEqual(res['requestedApiCount'], 1)

        self.assertEqual(res['data']['fetchType'], "rest")
        self.assertEqual(type(res['data']['marginTypes']), type([]))
        self.assertEqual(len(res['data']), 2)
        self.assertEqual(len(res['data']['marginTypes']), 1)

        for marginType in res['data']['marginTypes']:
            self.assertEqual(marginType['baseCurrency'], 'BTC')
            self.assertEqual(marginType['quoteCurrency'], 'USDT')
            self.assertEqual(marginType['expiration'], 'PERP')
            self.assertEqual(marginType['symbol'], 'BTCUSDT')
            marginTypeName = marginType['marginType']
            if marginTypeName not in ['cross', 'isolated']:
                self.fail('marginType is not cross or isolated')
            self.assertEqual(len(marginType), 5)

    def test_fetchMarginType_3(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')
        
        client.subscribeBalance()
        res = client.fetchMarginType('{"baseCurrency": "eTh"}')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], True)
        self.assertEqual(res['requestedApiCount'], 0)

        self.assertEqual(res['data']['fetchType'], "websocket")
        self.assertEqual(type(res['data']['marginTypes']), type([]))
        self.assertEqual(len(res['data']), 2)

        for marginType in res['data']['marginTypes']:
            self.assertEqual(marginType['baseCurrency'], 'ETH')
            self.assertEqual(type(marginType['quoteCurrency']), type(''))
            self.assertEqual(type(marginType['expiration']), type(''))
            self.assertEqual(type(marginType['symbol']), type(''))
            marginTypeName = marginType['marginType']
            if marginTypeName not in ['cross', 'isolated']:
                self.fail('marginType is not cross or isolated')
            self.assertEqual(len(marginType), 5)

    def test_fetchMarginType_4(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')
        
        client.subscribeBalance()
        res = client.fetchMarginType('{"baseCurrency": "eTh", "forceRestApi": true}')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], True)
        self.assertEqual(res['requestedApiCount'], 1)

        self.assertEqual(res['data']['fetchType'], "rest")
        self.assertEqual(type(res['data']['marginTypes']), type([]))
        self.assertEqual(len(res['data']), 2)

        for marginType in res['data']['marginTypes']:
            self.assertEqual(marginType['baseCurrency'], 'ETH')
            self.assertEqual(type(marginType['quoteCurrency']), type(''))
            self.assertEqual(type(marginType['expiration']), type(''))
            self.assertEqual(type(marginType['symbol']), type(''))
            marginTypeName = marginType['marginType']
            if marginTypeName not in ['cross', 'isolated']:
                self.fail('marginType is not cross or isolated')
            self.assertEqual(len(marginType), 5)

    def test_changeMarginType_1(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')
        
        res = client.changeMarginType('{"baseCurrency": "eTh", "forceRestApi": true}')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], False)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['errorType'], "NOT_ENOUGH_PARAM")

    def test_changeMarginType_2(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')
        
        res = client.fetchMarginType('{"baseCurrency":"bTC","quoteCurrency":"usDT","expiration":"perP"}')
        oldMarginType = res['data']['marginTypes'][0]['marginType']

        if oldMarginType == 'isolated':
            res = client.changeMarginType('{"baseCurrency":"bTC","quoteCurrency":"usDT","expiration":"perP","marginType":"cross"}')
        elif oldMarginType == 'cross':
            res = client.changeMarginType('{"baseCurrency":"bTC","quoteCurrency":"usDT","expiration":"perP","marginType":"isolated"}')
        else:
            self.fail('fetchMarginType result is something wrong')

        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], True)
        self.assertEqual(res['requestedApiCount'], 1)

        self.assertEqual(res['data']['baseCurrency'], 'BTC')
        self.assertEqual(res['data']['quoteCurrency'], 'USDT')
        self.assertEqual(res['data']['expiration'], 'PERP')
        self.assertEqual(res['data']['symbol'], 'BTCUSDT')
        if oldMarginType == 'isolated':
            self.assertEqual(res['data']['marginType'], 'cross')
        elif oldMarginType == 'cross':
            self.assertEqual(res['data']['marginType'], 'isolated')
        self.assertEqual(len(res['data']), 5)

        if oldMarginType == 'isolated':
            res = client.changeMarginType('{"baseCurrency":"bTC","quoteCurrency":"usDT","expiration":"perP","marginType":"isolated"}')
        elif oldMarginType == 'cross':
            res = client.changeMarginType('{"baseCurrency":"bTC","quoteCurrency":"usDT","expiration":"perP","marginType":"cross"}')

        self.assertEqual(res['success'], True, 'MarginType restore fail')

    def test_getCandleIntervalCandidates_1(self):
        client = OneXAPI.Binance.Futures()

        res = client.getCandleIntervalCandidates()
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"intervals":["12hour","15min","1day","1hour","1min","1month","1week","2hour","30min","3day","3min","4hour","5min","6hour","8hour"]}}')

        self.assertEqual(res, answer)

    def test_getCandleIntervalCandidates_2(self):
        client = OneXAPI.Binance.Futures()

        res = client.getCandleIntervalCandidates('')
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"intervals":["12hour","15min","1day","1hour","1min","1month","1week","2hour","30min","3day","3min","4hour","5min","6hour","8hour"]}}')

        self.assertEqual(res, answer)

    def test_fetchMarkets_1(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        res = client.fetchMarkets('{}')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], True)
        self.assertEqual(res['requestedApiCount'], 1)
        self.assertEqual(len(res['data']), 1)
        self.assertGreater(len(res['data']['markets']), 0)

        for market in res['data']['markets']:
            self.assertEqual(type(market['baseCurrency']), type(''))
            self.assertEqual(type(market['quoteCurrency']), type(''))
            self.assertEqual(type(market['expiration']), type(''))
            self.assertEqual(type(market['symbol']), type(''))
            self.assertEqual(len(market), 4)

    def test_fetchMarkets_2(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        res = client.fetchMarkets('{"baseCurrency":"bTC","quoteCurrency":"usDT","expiration":"perP"}')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], True)
        self.assertEqual(res['requestedApiCount'], 1)
        self.assertEqual(len(res['data']), 1)
        self.assertEqual(len(res['data']['markets']), 1)

        for market in res['data']['markets']:
            self.assertEqual(market['baseCurrency'], 'BTC')
            self.assertEqual(market['quoteCurrency'], 'USDT')
            self.assertEqual(market['expiration'], 'PERP')
            self.assertEqual(market['symbol'], 'BTCUSDT')
            self.assertEqual(len(market), 4)

    def test_fetchMarketInfo_1(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        res = client.fetchMarketInfo('{}')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], False)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_fetchMarketInfo_2(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        res = client.fetchMarketInfo('{"baseCurrency":"bTc","quoteCurrency":"USdt","expiration":"peRp"}')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], True)
        self.assertEqual(res['requestedApiCount'], 1)
        self.assertEqual(res['data']['fetchType'], 'rest')
        self.assertEqual(res['data']['baseCurrency'], 'BTC')
        self.assertEqual(res['data']['quoteCurrency'], 'USDT')
        self.assertEqual(res['data']['expiration'], 'PERP')
        self.assertEqual(res['data']['symbol'], 'BTCUSDT')
        self.assertEqual(type(res['data']['markPrice']), type(''))
        self.assertEqual(type(res['data']['fundingRate']), type(''))
        self.assertEqual(type(res['data']['nextFundingTime']), type(1))
        self.assertEqual(len(res['data']), 8)

    def test_fetchMarketInfo_3(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        client.subscribeMarketInfo('{"market":[{"baseCurrency":"eTh","quoteCurrency":"USdt"}]}')
        res = client.fetchMarketInfo('{"baseCurrency": "eTh", "quoteCurrency": "uSdT"}')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], True)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['fetchType'], 'websocket')
        self.assertEqual(res['data']['baseCurrency'], 'ETH')
        self.assertEqual(res['data']['quoteCurrency'], 'USDT')
        self.assertEqual(type(res['data']['expiration']), type(''))
        self.assertEqual(type(res['data']['symbol']), type(''))
        self.assertEqual(type(res['data']['markPrice']), type(''))
        self.assertEqual(type(res['data']['fundingRate']), type(''))
        self.assertEqual(type(res['data']['nextFundingTime']), type(1))
        self.assertEqual(len(res['data']), 8)

    def test_fetchMarketInfo_4(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        client.subscribeMarketInfo('{"market":[{"baseCurrency":"eTh","quoteCurrency":"USdt"}]}')
        res = client.fetchMarketInfo('{"baseCurrency": "eTh", "quoteCurrency": "uSdT", "forceRestApi": true}')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], True)
        self.assertEqual(res['requestedApiCount'], 1)
        self.assertEqual(res['data']['fetchType'], 'rest')
        self.assertEqual(res['data']['baseCurrency'], 'ETH')
        self.assertEqual(type(res['data']['quoteCurrency']), type(''))
        self.assertEqual(type(res['data']['expiration']), type(''))
        self.assertEqual(type(res['data']['symbol']), type(''))
        self.assertEqual(type(res['data']['markPrice']), type(''))
        self.assertEqual(type(res['data']['fundingRate']), type(''))
        self.assertEqual(type(res['data']['nextFundingTime']), type(1))
        self.assertEqual(len(res['data']), 8)

    def test_fetchTicker_1(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        res = client.fetchTicker('{}')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], False)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_fetchTicker_2(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        res = client.fetchTicker('{"baseCurrency":"bTc","quoteCurrency":"USdt","expiration":"peRp"}')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], True)
        self.assertEqual(res['requestedApiCount'], 1)
        self.assertEqual(res['data']['baseCurrency'], 'BTC')
        self.assertEqual(res['data']['quoteCurrency'], 'USDT')
        self.assertEqual(res['data']['expiration'], 'PERP')
        self.assertEqual(res['data']['symbol'], 'BTCUSDT')
        self.assertEqual(res['data']['fetchType'], 'rest')
        self.assertEqual(type(res['data']['openTime']), type(1))
        self.assertEqual(type(res['data']['openPrice']), type(''))
        self.assertEqual(type(res['data']['closePrice']), type(''))
        self.assertEqual(type(res['data']['lowPrice']), type(''))
        self.assertEqual(type(res['data']['highPrice']), type(''))
        self.assertEqual(type(res['data']['baseVolume']), type(''))
        self.assertEqual(type(res['data']['quoteVolume']), type(''))
        self.assertEqual(len(res['data']), 12)

    def test_fetchTicker_3(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        client.subscribeTicker('{"market":[{"baseCurrency":"bTc","quoteCurrency":"USdt"}]}')
        res = client.fetchTicker('{"baseCurrency":"bTc","quoteCurrency":"USdt"}')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], True)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['baseCurrency'], 'BTC')
        self.assertEqual(res['data']['quoteCurrency'], 'USDT')
        self.assertEqual(res['data']['expiration'], 'PERP')
        self.assertEqual(res['data']['symbol'], 'BTCUSDT')
        self.assertEqual(res['data']['fetchType'], 'websocket')
        self.assertEqual(type(res['data']['openTime']), type(1))
        self.assertEqual(type(res['data']['openPrice']), type(''))
        self.assertEqual(type(res['data']['closePrice']), type(''))
        self.assertEqual(type(res['data']['lowPrice']), type(''))
        self.assertEqual(type(res['data']['highPrice']), type(''))
        self.assertEqual(type(res['data']['baseVolume']), type(''))
        self.assertEqual(type(res['data']['quoteVolume']), type(''))
        self.assertEqual(len(res['data']), 12)

    def test_fetchTicker_4(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        client.subscribeTicker('{"market":[{"baseCurrency":"bTc","quoteCurrency":"USdt"}]}')
        res = client.fetchTicker('{"baseCurrency":"bTc","quoteCurrency":"USdt","forceRestApi":true}')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], True)
        self.assertEqual(res['requestedApiCount'], 1)
        self.assertEqual(res['data']['baseCurrency'], 'BTC')
        self.assertEqual(res['data']['quoteCurrency'], 'USDT')
        self.assertEqual(res['data']['expiration'], 'PERP')
        self.assertEqual(res['data']['symbol'], 'BTCUSDT')
        self.assertEqual(res['data']['fetchType'], 'rest')
        self.assertEqual(type(res['data']['openTime']), type(1))
        self.assertEqual(type(res['data']['openPrice']), type(''))
        self.assertEqual(type(res['data']['closePrice']), type(''))
        self.assertEqual(type(res['data']['lowPrice']), type(''))
        self.assertEqual(type(res['data']['highPrice']), type(''))
        self.assertEqual(type(res['data']['baseVolume']), type(''))
        self.assertEqual(type(res['data']['quoteVolume']), type(''))
        self.assertEqual(len(res['data']), 12)

    def test_fetchOrderbook_1(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        res = client.fetchOrderbook('{}')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], False)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_fetchOrderbook_2(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        res = client.fetchOrderbook('{"baseCurrency":"bTc","quoteCurrency":"USdt"}')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], True)
        self.assertEqual(res['requestedApiCount'], 1)
        self.assertEqual(res['data']['baseCurrency'], 'BTC')
        self.assertEqual(res['data']['quoteCurrency'], 'USDT')
        self.assertEqual(res['data']['expiration'], 'PERP')
        self.assertEqual(res['data']['symbol'], 'BTCUSDT')
        self.assertEqual(res['data']['fetchType'], 'rest')
        self.assertEqual(type(res['data']['timestamp']), type(1234))
        self.assertEqual(len(res['data']), 8)
        
        for bid in res['data']['bids']:
            self.assertEqual(type(bid['price']), type(''))
            self.assertEqual(type(bid['size']), type(''))
            self.assertEqual(len(bid), 2)
        
        for ask in res['data']['asks']:
            self.assertEqual(type(ask['price']), type(''))
            self.assertEqual(type(ask['size']), type(''))
            self.assertEqual(len(ask), 2)

    def test_fetchOrderbook_3(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        client.subscribeOrderbook('{"market":[{"baseCurrency":"bTc","quoteCurrency":"USdt"}]}')
        res = client.fetchOrderbook('{"baseCurrency":"bTc","quoteCurrency":"USdt"}')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], True)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['baseCurrency'], 'BTC')
        self.assertEqual(res['data']['quoteCurrency'], 'USDT')
        self.assertEqual(res['data']['expiration'], 'PERP')
        self.assertEqual(res['data']['symbol'], 'BTCUSDT')
        self.assertEqual(res['data']['fetchType'], 'websocket')
        self.assertEqual(type(res['data']['timestamp']), type(1234))
        self.assertEqual(len(res['data']), 8)
        
        for bid in res['data']['bids']:
            self.assertEqual(type(bid['price']), type(''))
            self.assertEqual(type(bid['size']), type(''))
            self.assertEqual(len(bid), 2)
        
        for ask in res['data']['asks']:
            self.assertEqual(type(ask['price']), type(''))
            self.assertEqual(type(ask['size']), type(''))
            self.assertEqual(len(ask), 2)

    def test_fetchOrderbook_4(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        client.subscribeOrderbook('{"market":[{"baseCurrency":"bTc","quoteCurrency":"USdt"}]}')
        res = client.fetchOrderbook('{"baseCurrency":"bTc","quoteCurrency":"USdt","forceRestApi":true}')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], True)
        self.assertEqual(res['requestedApiCount'], 1)
        self.assertEqual(res['data']['baseCurrency'], 'BTC')
        self.assertEqual(res['data']['quoteCurrency'], 'USDT')
        self.assertEqual(res['data']['expiration'], 'PERP')
        self.assertEqual(res['data']['symbol'], 'BTCUSDT')
        self.assertEqual(res['data']['fetchType'], 'rest')
        self.assertEqual(type(res['data']['timestamp']), type(1234))
        self.assertEqual(len(res['data']), 8)
        
        for bid in res['data']['bids']:
            self.assertEqual(type(bid['price']), type(''))
            self.assertEqual(type(bid['size']), type(''))
            self.assertEqual(len(bid), 2)
        
        for ask in res['data']['asks']:
            self.assertEqual(type(ask['price']), type(''))
            self.assertEqual(type(ask['size']), type(''))
            self.assertEqual(len(ask), 2)

    def test_fetchCandleHistory_1(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        res = client.fetchCandleHistory('{"baseCurrency":"bTc","quoteCurrency":"uSdT"}')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], False)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_fetchCandleHistory_2(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')
        
        specificTime = int((datetime.today() - timedelta(hours=2)).timestamp())
        res = client.fetchCandleHistory('{"baseCurrency":"bTc","quoteCurrency":"uSdT","interval":"1min","startTime":' + str(specificTime) + '}')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], True)
        self.assertEqual(type(res['requestedApiCount']), type(1))
        self.assertEqual(res['data']['baseCurrency'], 'BTC')
        self.assertEqual(res['data']['quoteCurrency'], 'USDT')
        self.assertEqual(res['data']['expiration'], 'PERP')
        self.assertEqual(res['data']['symbol'], 'BTCUSDT')
        self.assertEqual(len(res['data']), 5)
        self.assertGreater(len(res['data']['candles']), 100)

        for candle in res['data']['candles']:
            self.assertEqual(type(candle['timestamp']), type(1))
            self.assertEqual(type(candle['openPrice']), type(''))
            self.assertEqual(type(candle['closePrice']), type(''))
            self.assertEqual(type(candle['highPrice']), type(''))
            self.assertEqual(type(candle['lowPrice']), type(''))
            self.assertEqual(type(candle['baseVolume']), type(''))
            self.assertEqual(type(candle['quoteVolume']), type(''))
            self.assertEqual(len(candle), 7)
            
    def test_fetchCandleHistory_3(self):
        time.sleep(1)
        client = OneXAPI.Binance.Futures('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')
        
        res = client.fetchCandleHistory('{"baseCurrency":"bTc","quoteCurrency":"uSdT","expiration":"peRp","interval":"1min","startTime":1656042045,"endTime":1656063182,"fetchInterval":900}')
        
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], True)
        self.assertEqual(type(res['requestedApiCount']), type(1))
        self.assertEqual(res['data']['baseCurrency'], 'BTC')
        self.assertEqual(res['data']['quoteCurrency'], 'USDT')
        self.assertEqual(res['data']['expiration'], 'PERP')
        self.assertEqual(res['data']['symbol'], 'BTCUSDT')
        self.assertEqual(len(res['data']), 5)
        self.assertGreater(len(res['data']['candles']), 300)

        for candle in res['data']['candles']:
            self.assertEqual(type(candle['timestamp']), type(1))
            self.assertEqual(type(candle['openPrice']), type(''))
            self.assertEqual(type(candle['closePrice']), type(''))
            self.assertEqual(type(candle['highPrice']), type(''))
            self.assertEqual(type(candle['lowPrice']), type(''))
            self.assertEqual(type(candle['baseVolume']), type(''))
            self.assertEqual(type(candle['quoteVolume']), type(''))
            self.assertEqual(len(candle), 7)

    def test_getSubscribingMarketInfo_1(self):
        client = OneXAPI.Binance.Futures()

        res = client.getSubscribingMarketInfo()
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"marketInfo":[]}}')
        self.assertEqual(res, answer)

    def test_getSubscribingMarketInfo_2(self):
        client = OneXAPI.Binance.Futures()

        res = client.getSubscribingMarketInfo('')
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"marketInfo":[]}}')
        self.assertEqual(res, answer)

    def test_getSubscribingMarketInfo_3(self):
        client = OneXAPI.Binance.Futures()

        res = client.getSubscribingMarketInfo('{}')
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"marketInfo":[]}}')
        self.assertEqual(res, answer)

    def test_getSubscribingMarketInfo_4(self):
        client = OneXAPI.Binance.Futures()

        res = client.getSubscribingMarketInfo('Bqbqb@')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], False)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['errorType'], 'JSON_PARSING_ERROR')

    def test_getSubscribingMarketInfo_5(self):
        client = OneXAPI.Binance.Futures()

        client.subscribeMarketInfo('{"market":[{"baseCurrency":"BTC","quoteCurrency":"USDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT"}]}')
        res = client.getSubscribingMarketInfo()
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"marketInfo":[{"baseCurrency":"BTC","quoteCurrency":"USDT","expiration":"PERP","symbol":"BTCUSDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT","expiration":"PERP","symbol":"ETHUSDT"}]}}')
        self.assertEqual(res, answer)
        
    def test_getSubscribingTickers_1(self):
        client = OneXAPI.Binance.Futures()

        res = client.getSubscribingTickers()
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"tickers":[]}}')
        self.assertEqual(res, answer)

    def test_getSubscribingTickers_2(self):
        client = OneXAPI.Binance.Futures()

        res = client.getSubscribingTickers('')
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"tickers":[]}}')
        self.assertEqual(res, answer)

    def test_getSubscribingTickers_3(self):
        client = OneXAPI.Binance.Futures()

        res = client.getSubscribingTickers('{}')
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"tickers":[]}}')
        self.assertEqual(res, answer)

    def test_getSubscribingTickers_4(self):
        client = OneXAPI.Binance.Futures()

        res = client.getSubscribingTickers('Bqbqb@')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], False)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['errorType'], 'JSON_PARSING_ERROR')

    def test_getSubscribingTickers_5(self):
        client = OneXAPI.Binance.Futures()

        client.subscribeTicker('{"market":[{"baseCurrency":"BTC","quoteCurrency":"USDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT"}]}')
        res = client.getSubscribingTickers()
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"tickers":[{"baseCurrency":"BTC","quoteCurrency":"USDT","expiration":"PERP","symbol":"BTCUSDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT","expiration":"PERP","symbol":"ETHUSDT"}]}}')
        self.assertEqual(res, answer)

    def test_getSubscribingOrderbooks_1(self):
        client = OneXAPI.Binance.Futures()

        res = client.getSubscribingOrderbooks()
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"orderbooks":[]}}')
        self.assertEqual(res, answer)
    
    def test_getSubscribingOrderbooks_2(self):
        client = OneXAPI.Binance.Futures()

        res = client.getSubscribingOrderbooks('')
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"orderbooks":[]}}')
        self.assertEqual(res, answer)

    def test_getSubscribingOrderbooks_3(self):
        client = OneXAPI.Binance.Futures()

        res = client.getSubscribingOrderbooks('{}')
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"orderbooks":[]}}')
        self.assertEqual(res, answer)

    def test_getSubscribingOrderbooks_4(self):
        client = OneXAPI.Binance.Futures()

        res = client.getSubscribingOrderbooks('Bqbqb@')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], False)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['errorType'], 'JSON_PARSING_ERROR')

    def test_getSubscribingOrderbooks_5(self):
        self.maxDiff = None

        client = OneXAPI.Binance.Futures()

        client.subscribeOrderbook('{"market":[{"baseCurrency":"BTC","quoteCurrency":"USDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT"}]}')
        res = client.getSubscribingOrderbooks()
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"orderbooks":[{"baseCurrency":"BTC","quoteCurrency":"USDT","expiration":"PERP","symbol":"BTCUSDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT","expiration":"PERP","symbol":"ETHUSDT"}]}}')
        self.assertEqual(res, answer)

    def test_subscribeMarketInfo_1(self):
        client = OneXAPI.Binance.Futures()

        res = client.subscribeMarketInfo()
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], False)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_subscribeMarketInfo_2(self):
        client = OneXAPI.Binance.Futures()

        res = client.subscribeMarketInfo('')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], False)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_subscribeMarketInfo_3(self):
        client = OneXAPI.Binance.Futures()

        res = client.subscribeMarketInfo('{}')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], False)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_subscribeMarketInfo_4(self):
        client = OneXAPI.Binance.Futures()

        res = client.subscribeMarketInfo('Bqbqb@')
        
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], False)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['errorType'], 'JSON_PARSING_ERROR')

    def test_subscribeMarketInfo_5(self):

        for i in range(0, 10):
            client = OneXAPI.Binance.Futures()

            res = client.subscribeMarketInfo('{"market":[{"baseCurrency":"BTC","quoteCurrency":"USDT"}]}')
            answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"subscribed":[{"baseCurrency":"BTC","quoteCurrency":"USDT","expiration":"PERP","symbol":"BTCUSDT"}],"subscribeFailed":[]}}')

            self.assertEqual(res, answer)

            res = client.getSubscribingMarketInfo()
            answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"marketInfo":[{"baseCurrency":"BTC","quoteCurrency":"USDT","expiration":"PERP","symbol":"BTCUSDT"}]}}')

    def test_subscribeMarketInfo_6(self):

        client = OneXAPI.Binance.Futures()
        res = client.subscribeMarketInfo('{"market":[{"baseCurrency":"BTC","quoteCurrency":"USDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT"}]}')
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"subscribed":[{"baseCurrency":"BTC","quoteCurrency":"USDT","expiration":"PERP","symbol":"BTCUSDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT","expiration":"PERP","symbol":"ETHUSDT"}],"subscribeFailed":[]}}')

        self.assertEqual(res, answer)

        res = client.getSubscribingMarketInfo()
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"marketInfo":[{"baseCurrency":"BTC","quoteCurrency":"USDT","expiration":"PERP","symbol":"BTCUSDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT","expiration":"PERP","symbol":"ETHUSDT"}]}}')

        res = client.subscribeMarketInfo('{"market":[{"baseCurrency":"XRP","quoteCurrency":"USDT"}], "reconnect": true}')
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"subscribed":[{"baseCurrency":"XRP","quoteCurrency":"USDT","expiration":"PERP","symbol":"XRPUSDT"}],"subscribeFailed":[]}}')

        self.assertEqual(res, answer)

        res = client.getSubscribingMarketInfo()
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"marketInfo":[{"baseCurrency":"BTC","quoteCurrency":"USDT","expiration":"PERP","symbol":"BTCUSDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT","expiration":"PERP","symbol":"ETHUSDT"},{"baseCurrency":"XRP","quoteCurrency":"USDT","expiration":"PERP","symbol":"XRPUSDT"}]}}')

    def test_subscribeMarketInfo_7(self):

        client = OneXAPI.Binance.Futures()
        baseCurrencys = [
            "BTC", "ETH", "BCH", "XRP", "EOS", "LTC", "TRX", "ETC", "LINK", "XLM",
            "ADA", "XMR", "DASH", "ZEC", "XTZ", "BNB", "ATOM", "ONT", "IOTA", "BAT",
            "VET", "NEO", "QTUM", "IOST", "THETA", "ALGO", "ZIL", "KNC", "ZRX", "COMP",
            "OMG", "DOGE", "SXP", "KAVA", "BAND", "RLC", "WAVES", "MKR", "SNX", "DOT",
            "DEFI", "YFI", "BAL", "CRV", "TRB", "RUNE", "SUSHI", "SRM", "EGLD", "SOL",
            "ICX", "STORJ", "BLZ", "UNI", "AVAX", "FTM", "HNT", "ENJ", "FLM", "TOMO"
        ]

        markets = []

        for baseCurrency in baseCurrencys:
            pair = dict()
            pair['baseCurrency'] = baseCurrency
            pair['quoteCurrency'] = 'USDT'
            markets.append(pair)

        payload = dict()
        payload['market'] = markets

        res = client.subscribeMarketInfo(payload)
        
        self.assertEqual(len(res), 3)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(len(res['data']), 2 )

        self.assertGreater(len(res['data']['subscribed']), 25)
        self.assertEqual(type(res['data']['subscribed']), type([]))
        self.assertEqual(type(res['data']['subscribeFailed']), type([]))

        subscribed = res['data']['subscribed']
        subscribeFailed = res['data']['subscribeFailed']

        for data in subscribed:
            self.assertEqual(len(data), 4)

        for data in subscribeFailed:
            self.assertEqual(len(data), 4)

        res = client.getSubscribingMarketInfo()

        self.assertEqual(len(res), 3)
        self.assertEqual(res['requestedApiCount'], 0)

        self.assertEqual(len(res['data']), 1)
        self.assertEqual(len(res['data']['marketInfo']), len(subscribed))

        for MarketInfo in res['data']['marketInfo']:
            self.assertEqual(len(MarketInfo), 4)
            symbol = MarketInfo['symbol']
            isFound = False

            for subscribedMarketInfo in subscribed:
                if symbol == subscribedMarketInfo['symbol']:
                    isFound = True
                    break
            
            if isFound is False:
                self.assertFalse("Can't find subscribed symbol : " + symbol)

            isFound = True
            for failedMarketInfo in subscribeFailed:
                if symbol == failedMarketInfo['symbol']:
                    isFound = False
                    break

            if isFound is False:
                self.assertFalse("find subscribeFailed symbol : " + symbol)

    def test_subscribeMarketInfo_8(self):

        client = OneXAPI.Binance.Futures()
        res = client.subscribeMarketInfo('{"market":[{"baseCurrency":"HYUNKYU","quoteCurrency":"USDT"}]}')
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"subscribed":[],"subscribeFailed":[{"baseCurrency":"HYUNKYU","quoteCurrency":"USDT","expiration":"PERP","symbol":"HYUNKYUUSDT"}]}}')

        self.assertEqual(res, answer)

        res = client.getSubscribingMarketInfo()
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"marketInfo":[]}}')

        self.assertEqual(res, answer)

    def test_subscribeMarketInfo_9(self):

        client = OneXAPI.Binance.Futures()
        res = client.subscribeMarketInfo('{"market":[{"baseCurrency":"BTC","quoteCurrency":"USDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT"}]}')
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"subscribed":[{"baseCurrency":"BTC","quoteCurrency":"USDT","expiration":"PERP","symbol":"BTCUSDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT","expiration":"PERP","symbol":"ETHUSDT"}],"subscribeFailed":[]}}')

        self.assertEqual(res, answer)

        res = client.getSubscribingMarketInfo()
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"marketInfo":[{"baseCurrency":"BTC","quoteCurrency":"USDT","expiration":"PERP","symbol":"BTCUSDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT","expiration":"PERP","symbol":"ETHUSDT"}]}}')

        self.assertEqual(res, answer)

        res = client.subscribeMarketInfo('{"market":[],"reconnect":true}')
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"subscribed":[],"subscribeFailed":[]}}')

        self.assertEqual(res, answer)

    def test_unsubscribeMarketInfo_1(self):
        client = OneXAPI.Binance.Futures()

        res = client.unsubscribeMarketInfo()
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], False)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_unsubscribeMarketInfo_2(self):
        client = OneXAPI.Binance.Futures()

        res = client.unsubscribeMarketInfo('')
        
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], False)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_unsubscribeMarketInfo_3(self):
        client = OneXAPI.Binance.Futures()

        res = client.unsubscribeMarketInfo('{}')
        
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], False)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_unsubscribeMarketInfo_4(self):
        client = OneXAPI.Binance.Futures()

        res = client.unsubscribeMarketInfo('Bqbqb@')
        
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], False)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['errorType'], 'JSON_PARSING_ERROR')
        
    def test_unsubscribeMarketInfo_5(self):
        client = OneXAPI.Binance.Futures()

        client.subscribeMarketInfo('{"market":[{"baseCurrency":"BTC","quoteCurrency":"USDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT"}]}')
        res = client.unsubscribeMarketInfo('{"market":[{"baseCurrency":"BTC","quoteCurrency":"USDT"}]}')
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"unsubscribed":[{"baseCurrency":"BTC","quoteCurrency":"USDT","expiration":"PERP","symbol":"BTCUSDT"}],"unsubscribeFailed":[]}}')

        self.assertEqual(res, answer)

        res = client.getSubscribingMarketInfo()
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"marketInfo":[{"baseCurrency":"ETH","quoteCurrency":"USDT","expiration":"PERP","symbol":"ETHUSDT"}]}}')

        self.assertEqual(res, answer)

    def test_unsubscribeMarketInfo_6(self):
        client = OneXAPI.Binance.Futures()

        client.subscribeMarketInfo('{"market":[{"baseCurrency":"BTC","quoteCurrency":"USDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT"}]}')
        res = client.unsubscribeMarketInfo('{"market":[{"baseCurrency":"BTC","quoteCurrency":"USDT"}],"reconnect":true}')
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"unsubscribed":[{"baseCurrency":"BTC","quoteCurrency":"USDT","expiration":"PERP","symbol":"BTCUSDT"}],"unsubscribeFailed":[]}}')
        
        self.assertEqual(res, answer)

        res = client.getSubscribingMarketInfo()
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"marketInfo":[{"baseCurrency":"ETH","quoteCurrency":"USDT","expiration":"PERP","symbol":"ETHUSDT"}]}}')

        self.assertEqual(res, answer)

    def test_unsubscribeMarketInfo_7(self):
        client = OneXAPI.Binance.Futures()
        baseCurrencys = [
            "BTC", "ETH", "BCH", "XRP", "EOS", "LTC", "TRX", "ETC", "LINK", "XLM",
            "ADA", "XMR", "DASH", "ZEC", "XTZ", "BNB", "ATOM", "ONT", "IOTA", "BAT",
            "VET", "NEO", "QTUM", "IOST", "THETA", "ALGO", "ZIL", "KNC", "ZRX", "COMP",
            "OMG", "DOGE", "SXP", "KAVA", "BAND", "RLC", "WAVES", "MKR", "SNX", "DOT",
            "DEFI", "YFI", "BAL", "CRV", "TRB", "RUNE", "SUSHI", "SRM", "EGLD", "SOL",
            "ICX", "STORJ", "BLZ", "UNI", "AVAX", "FTM", "HNT", "ENJ", "FLM", "TOMO"
        ]
        markets = []

        for baseCurrency in baseCurrencys:
            pair = dict()
            pair['baseCurrency'] = baseCurrency
            pair['quoteCurrency'] = 'USDT'
            markets.append(pair)

        payload = dict()
        payload['market'] = markets

        res = client.subscribeMarketInfo(payload)

        self.assertGreater(len(res['data']['subscribed']), 25)

        res = client.unsubscribeMarketInfo(payload)

        self.assertEqual(len(res['data']), 2)
        self.assertEqual(type(res['data']['unsubscribed']), type([]))
        self.assertEqual(type(res['data']['unsubscribeFailed']), type([]))

        for unsubscribed in res['data']['unsubscribed']:
            self.assertEqual(len(unsubscribed), 4)

        for unsubscribeFailed in res['data']['unsubscribeFailed']:
            self.assertEqual(len(unsubscribeFailed), 4)

        res = client.getSubscribingMarketInfo()
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"marketInfo":[]}}')

        self.assertEqual(res, answer)

    def test_unsubscribeMarketInfo_8(self):
        client = OneXAPI.Binance.Futures()
        res = client.unsubscribeMarketInfo('{"market":[{"baseCurrency":"HYUNKYU","quoteCurrency":"USDT"}]}')
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"unsubscribed":[],"unsubscribeFailed":[{"baseCurrency":"HYUNKYU","quoteCurrency":"USDT","expiration":"PERP","symbol":"HYUNKYUUSDT"}]}}')

        self.assertEqual(res, answer)

    def test_unsubscribeMarketInfo_9(self):
        client = OneXAPI.Binance.Futures()
        res = client.subscribeMarketInfo('{"market":[{"baseCurrency":"BTC","quoteCurrency":"USDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT"}]}')
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"subscribed":[{"baseCurrency":"BTC","quoteCurrency":"USDT","expiration":"PERP","symbol":"BTCUSDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT","expiration":"PERP","symbol":"ETHUSDT"}],"subscribeFailed":[]}}')

        self.assertEqual(res, answer)

        res = client.getSubscribingMarketInfo()
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"marketInfo":[{"baseCurrency":"BTC","quoteCurrency":"USDT","expiration":"PERP","symbol":"BTCUSDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT","expiration":"PERP","symbol":"ETHUSDT"}]}}')

        self.assertEqual(res, answer)

        res = client.unsubscribeMarketInfo('{"market":[],"reconnect":true}')
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"unsubscribed":[],"unsubscribeFailed":[]}}')

        self.assertEqual(res, answer)

    def test_subscribeTicker_1(self):
        client = OneXAPI.Binance.Futures()

        res = client.subscribeTicker()
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], False)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_subscribeTicker_2(self):
        client = OneXAPI.Binance.Futures()

        res = client.subscribeTicker('')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], False)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_subscribeTicker_3(self):
        client = OneXAPI.Binance.Futures()

        res = client.subscribeTicker('{}')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], False)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_subscribeTicker_4(self):
        client = OneXAPI.Binance.Futures()

        res = client.subscribeTicker('Bqbqb@')
        
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], False)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['errorType'], 'JSON_PARSING_ERROR')

    def test_subscribeTicker_5(self):

        for i in range(0, 10):
            client = OneXAPI.Binance.Futures()

            res = client.subscribeTicker('{"market":[{"baseCurrency":"BTC","quoteCurrency":"USDT"}]}')
            answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"subscribed":[{"baseCurrency":"BTC","quoteCurrency":"USDT","expiration":"PERP","symbol":"BTCUSDT"}],"subscribeFailed":[]}}')

            self.assertEqual(res, answer)

            res = client.getSubscribingTickers()
            answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"tickers":[{"baseCurrency":"BTC","quoteCurrency":"USDT","expiration":"PERP","symbol":"BTCUSDT"}]}}')

    def test_subscribeTicker_6(self):

        client = OneXAPI.Binance.Futures()
        res = client.subscribeTicker('{"market":[{"baseCurrency":"BTC","quoteCurrency":"USDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT"}]}')
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"subscribed":[{"baseCurrency":"BTC","quoteCurrency":"USDT","expiration":"PERP","symbol":"BTCUSDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT","expiration":"PERP","symbol":"ETHUSDT"}],"subscribeFailed":[]}}')

        self.assertEqual(res, answer)

        res = client.getSubscribingTickers()
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"tickers":[{"baseCurrency":"BTC","quoteCurrency":"USDT","expiration":"PERP","symbol":"BTCUSDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT","expiration":"PERP","symbol":"ETHUSDT"}]}}')

        self.assertEqual(res, answer)

        res = client.subscribeTicker('{"market":[{"baseCurrency":"XRP","quoteCurrency":"USDT"}], "reconnect": true}')
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"subscribed":[{"baseCurrency":"XRP","quoteCurrency":"USDT","expiration":"PERP","symbol":"XRPUSDT"}],"subscribeFailed":[]}}')

        self.assertEqual(res, answer)

        res = client.getSubscribingTickers()
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"tickers":[{"baseCurrency":"BTC","quoteCurrency":"USDT","expiration":"PERP","symbol":"BTCUSDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT","expiration":"PERP","symbol":"ETHUSDT"},{"baseCurrency":"XRP","quoteCurrency":"USDT","expiration":"PERP","symbol":"XRPUSDT"}]}}')

        self.assertEqual(res, answer)

    def test_subscribeTicker_7(self):

        client = OneXAPI.Binance.Futures()
        baseCurrencys = [
            "BTC", "ETH", "BCH", "XRP", "EOS", "LTC", "TRX", "ETC", "LINK", "XLM",
            "ADA", "XMR", "DASH", "ZEC", "XTZ", "BNB", "ATOM", "ONT", "IOTA", "BAT",
            "VET", "NEO", "QTUM", "IOST", "THETA", "ALGO", "ZIL", "KNC", "ZRX", "COMP",
            "OMG", "DOGE", "SXP", "KAVA", "BAND", "RLC", "WAVES", "MKR", "SNX", "DOT",
            "DEFI", "YFI", "BAL", "CRV", "TRB", "RUNE", "SUSHI", "SRM", "EGLD", "SOL",
            "ICX", "STORJ", "BLZ", "UNI", "AVAX", "FTM", "HNT", "ENJ", "FLM", "TOMO"
        ]

        markets = []

        for baseCurrency in baseCurrencys:
            pair = dict()
            pair['baseCurrency'] = baseCurrency
            pair['quoteCurrency'] = 'USDT'
            markets.append(pair)

        payload = dict()
        payload['market'] = markets

        res = client.subscribeTicker(payload)
        
        self.assertEqual(len(res), 3)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(len(res['data']), 2 )

        self.assertGreater(len(res['data']['subscribed']), 25)
        self.assertEqual(type(res['data']['subscribed']), type([]))
        self.assertEqual(type(res['data']['subscribeFailed']), type([]))

        subscribed = res['data']['subscribed']
        subscribeFailed = res['data']['subscribeFailed']

        for data in subscribed:
            self.assertEqual(len(data), 4)

        for data in subscribeFailed:
            self.assertEqual(len(data), 4)

        res = client.getSubscribingTickers()

        self.assertEqual(len(res), 3)
        self.assertEqual(res['requestedApiCount'], 0)

        self.assertEqual(len(res['data']), 1)
        self.assertEqual(len(res['data']['tickers']), len(subscribed))

        for Ticker in res['data']['tickers']:
            self.assertEqual(len(Ticker), 4)
            symbol = Ticker['symbol']
            isFound = False

            for subscribedTicker in subscribed:
                if symbol == subscribedTicker['symbol']:
                    isFound = True
                    break
            
            if isFound is False:
                self.assertFalse("Can't find subscribed symbol : " + symbol)

            isFound = True
            for failedTicker in subscribeFailed:
                if symbol == failedTicker['symbol']:
                    isFound = False
                    break

            if isFound is False:
                self.assertFalse("find subscribeFailed symbol : " + symbol)

    def test_subscribeTicker_8(self):

        client = OneXAPI.Binance.Futures()
        res = client.subscribeTicker('{"market":[{"baseCurrency":"HYUNKYU","quoteCurrency":"USDT"}]}')
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"subscribed":[],"subscribeFailed":[{"baseCurrency":"HYUNKYU","quoteCurrency":"USDT","expiration":"PERP","symbol":"HYUNKYUUSDT"}]}}')

        self.assertEqual(res, answer)

        res = client.getSubscribingTickers()
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"tickers":[]}}')

        self.assertEqual(res, answer)

    def test_subscribeTicker_9(self):

        client = OneXAPI.Binance.Futures()
        res = client.subscribeTicker('{"market":[{"baseCurrency":"BTC","quoteCurrency":"USDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT"}]}')
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"subscribed":[{"baseCurrency":"BTC","quoteCurrency":"USDT","expiration":"PERP","symbol":"BTCUSDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT","expiration":"PERP","symbol":"ETHUSDT"}],"subscribeFailed":[]}}')

        self.assertEqual(res, answer)

        res = client.getSubscribingTickers()
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"tickers":[{"baseCurrency":"BTC","quoteCurrency":"USDT","expiration":"PERP","symbol":"BTCUSDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT","expiration":"PERP","symbol":"ETHUSDT"}]}}')

        self.assertEqual(res, answer)

        res = client.subscribeTicker('{"market":[],"reconnect":true}')
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"subscribed":[],"subscribeFailed":[]}}')

        self.assertEqual(res, answer)

    def test_unsubscribeTicker_1(self):
        client = OneXAPI.Binance.Futures()

        res = client.unsubscribeTicker()
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], False)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_unsubscribeTicker_2(self):
        client = OneXAPI.Binance.Futures()

        res = client.unsubscribeTicker('')
        
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], False)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_unsubscribeTicker_3(self):
        client = OneXAPI.Binance.Futures()

        res = client.unsubscribeTicker('{}')
        
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], False)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_unsubscribeTicker_4(self):
        client = OneXAPI.Binance.Futures()

        res = client.unsubscribeTicker('Bqbqb@')
        
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], False)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['errorType'], 'JSON_PARSING_ERROR')
        
    def test_unsubscribeTicker_5(self):
        client = OneXAPI.Binance.Futures()

        client.subscribeTicker('{"market":[{"baseCurrency":"BTC","quoteCurrency":"USDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT"}]}')
        res = client.unsubscribeTicker('{"market":[{"baseCurrency":"BTC","quoteCurrency":"USDT"}]}')
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"unsubscribed":[{"baseCurrency":"BTC","quoteCurrency":"USDT","expiration":"PERP","symbol":"BTCUSDT"}],"unsubscribeFailed":[]}}')

        self.assertEqual(res, answer)

        res = client.getSubscribingTickers()
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"tickers":[{"baseCurrency":"ETH","quoteCurrency":"USDT","expiration":"PERP","symbol":"ETHUSDT"}]}}')

        self.assertEqual(res, answer)

    def test_unsubscribeTicker_6(self):
        client = OneXAPI.Binance.Futures()

        client.subscribeTicker('{"market":[{"baseCurrency":"BTC","quoteCurrency":"USDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT"}]}')
        res = client.unsubscribeTicker('{"market":[{"baseCurrency":"BTC","quoteCurrency":"USDT"}],"reconnect":true}')
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"unsubscribed":[{"baseCurrency":"BTC","quoteCurrency":"USDT","expiration":"PERP","symbol":"BTCUSDT"}],"unsubscribeFailed":[]}}')
        
        self.assertEqual(res, answer)

        res = client.getSubscribingTickers()
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"tickers":[{"baseCurrency":"ETH","quoteCurrency":"USDT","expiration":"PERP","symbol":"ETHUSDT"}]}}')

        self.assertEqual(res, answer)

    def test_unsubscribeTicker_7(self):
        client = OneXAPI.Binance.Futures()
        baseCurrencys = [
            "BTC", "ETH", "BCH", "XRP", "EOS", "LTC", "TRX", "ETC", "LINK", "XLM",
            "ADA", "XMR", "DASH", "ZEC", "XTZ", "BNB", "ATOM", "ONT", "IOTA", "BAT",
            "VET", "NEO", "QTUM", "IOST", "THETA", "ALGO", "ZIL", "KNC", "ZRX", "COMP",
            "OMG", "DOGE", "SXP", "KAVA", "BAND", "RLC", "WAVES", "MKR", "SNX", "DOT",
            "DEFI", "YFI", "BAL", "CRV", "TRB", "RUNE", "SUSHI", "SRM", "EGLD", "SOL",
            "ICX", "STORJ", "BLZ", "UNI", "AVAX", "FTM", "HNT", "ENJ", "FLM", "TOMO"
        ]
        markets = []

        for baseCurrency in baseCurrencys:
            pair = dict()
            pair['baseCurrency'] = baseCurrency
            pair['quoteCurrency'] = 'USDT'
            markets.append(pair)

        payload = dict()
        payload['market'] = markets

        res = client.subscribeTicker(payload)

        self.assertGreater(len(res['data']['subscribed']), 25)

        res = client.unsubscribeTicker(payload)

        self.assertEqual(len(res['data']), 2)
        self.assertEqual(type(res['data']['unsubscribed']), type([]))
        self.assertEqual(type(res['data']['unsubscribeFailed']), type([]))

        for unsubscribed in res['data']['unsubscribed']:
            self.assertEqual(len(unsubscribed), 4)

        for unsubscribeFailed in res['data']['unsubscribeFailed']:
            self.assertEqual(len(unsubscribeFailed), 4)

        res = client.getSubscribingTickers()
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"tickers":[]}}')

        self.assertEqual(res, answer)

    def test_unsubscribeTicker_8(self):
        client = OneXAPI.Binance.Futures()
        res = client.unsubscribeTicker('{"market":[{"baseCurrency":"HYUNKYU","quoteCurrency":"USDT"}]}')
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"unsubscribed":[],"unsubscribeFailed":[{"baseCurrency":"HYUNKYU","quoteCurrency":"USDT","expiration":"PERP","symbol":"HYUNKYUUSDT"}]}}')

        self.assertEqual(res, answer)

    def test_unsubscribeTicker_9(self):
        client = OneXAPI.Binance.Futures()
        res = client.subscribeTicker('{"market":[{"baseCurrency":"BTC","quoteCurrency":"USDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT"}]}')
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"subscribed":[{"baseCurrency":"BTC","quoteCurrency":"USDT","expiration":"PERP","symbol":"BTCUSDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT","expiration":"PERP","symbol":"ETHUSDT"}],"subscribeFailed":[]}}')

        self.assertEqual(res, answer)

        res = client.getSubscribingTickers()
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"tickers":[{"baseCurrency":"BTC","quoteCurrency":"USDT","expiration":"PERP","symbol":"BTCUSDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT","expiration":"PERP","symbol":"ETHUSDT"}]}}')

        self.assertEqual(res, answer)

        res = client.unsubscribeTicker('{"market":[],"reconnect":true}')
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"unsubscribed":[],"unsubscribeFailed":[]}}')

        self.assertEqual(res, answer)

    def test_subscribeOrderbook_1(self):
        client = OneXAPI.Binance.Futures()

        res = client.subscribeOrderbook()
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], False)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_subscribeOrderbook_2(self):
        client = OneXAPI.Binance.Futures()

        res = client.subscribeOrderbook('')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], False)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_subscribeOrderbook_3(self):
        client = OneXAPI.Binance.Futures()

        res = client.subscribeOrderbook('{}')
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], False)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_subscribeOrderbook_4(self):
        client = OneXAPI.Binance.Futures()

        res = client.subscribeOrderbook('Bqbqb@')
        
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], False)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['errorType'], 'JSON_PARSING_ERROR')

    def test_subscribeOrderbook_5(self):

        for i in range(0, 10):
            client = OneXAPI.Binance.Futures()

            res = client.subscribeOrderbook('{"market":[{"baseCurrency":"BTC","quoteCurrency":"USDT"}]}')
            answer = json.loads('{"success":true,"requestedApiCount":1,"data":{"subscribed":[{"baseCurrency":"BTC","quoteCurrency":"USDT","expiration":"PERP","symbol":"BTCUSDT"}],"subscribeFailed":[]}}')

            self.assertEqual(res, answer)

            res = client.getSubscribingOrderbooks()
            answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"orderbooks":[{"baseCurrency":"BTC","quoteCurrency":"USDT","expiration":"PERP","symbol":"BTCUSDT"}]}}')

    def test_subscribeOrderbook_6(self):

        client = OneXAPI.Binance.Futures()
        res = client.subscribeOrderbook('{"market":[{"baseCurrency":"BTC","quoteCurrency":"USDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT"}]}')
        answer = json.loads('{"success":true,"requestedApiCount":2,"data":{"subscribed":[{"baseCurrency":"BTC","quoteCurrency":"USDT","expiration":"PERP","symbol":"BTCUSDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT","expiration":"PERP","symbol":"ETHUSDT"}],"subscribeFailed":[]}}')

        self.assertEqual(res, answer)

        res = client.getSubscribingOrderbooks()
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"orderbooks":[{"baseCurrency":"BTC","quoteCurrency":"USDT","expiration":"PERP","symbol":"BTCUSDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT","expiration":"PERP","symbol":"ETHUSDT"}]}}')

        self.assertEqual(res, answer)

        res = client.subscribeOrderbook('{"market":[{"baseCurrency":"XRP","quoteCurrency":"USDT"}], "reconnect": true}')
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"subscribed":[{"baseCurrency":"XRP","quoteCurrency":"USDT","expiration":"PERP","symbol":"XRPUSDT"}],"subscribeFailed":[]}}')

        self.assertEqual(res, answer)

        res = client.getSubscribingOrderbooks()
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"orderbooks":[{"baseCurrency":"BTC","quoteCurrency":"USDT","expiration":"PERP","symbol":"BTCUSDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT","expiration":"PERP","symbol":"ETHUSDT"},{"baseCurrency":"XRP","quoteCurrency":"USDT","expiration":"PERP","symbol":"XRPUSDT"}]}}')

        self.assertEqual(res, answer)

    def test_subscribeOrderbook_7(self):

        client = OneXAPI.Binance.Futures()
        baseCurrencys = [
            "BTC", "ETH", "BCH", "XRP", "EOS", "LTC", "TRX", "ETC", "LINK", "XLM",
            "ADA", "XMR", "DASH", "ZEC", "XTZ", "BNB", "ATOM", "ONT", "IOTA", "BAT",
            "VET", "NEO", "QTUM", "IOST", "THETA", "ALGO", "ZIL", "KNC", "ZRX", "COMP",
            "OMG", "DOGE", "SXP", "KAVA", "BAND", "RLC", "WAVES", "MKR", "SNX", "DOT",
            "DEFI", "YFI", "BAL", "CRV", "TRB", "RUNE", "SUSHI", "SRM", "EGLD", "SOL",
            "ICX", "STORJ", "BLZ", "UNI", "AVAX", "FTM", "HNT", "ENJ", "FLM", "TOMO"
        ]

        markets = []

        for baseCurrency in baseCurrencys:
            pair = dict()
            pair['baseCurrency'] = baseCurrency
            pair['quoteCurrency'] = 'USDT'
            markets.append(pair)

        payload = dict()
        payload['market'] = markets

        res = client.subscribeOrderbook(payload)
        
        self.assertEqual(len(res), 3)
        self.assertEqual(res['requestedApiCount'], len(baseCurrencys))
        self.assertEqual(len(res['data']), 2 )

        self.assertGreater(len(res['data']['subscribed']), 25)
        self.assertEqual(type(res['data']['subscribed']), type([]))
        self.assertEqual(type(res['data']['subscribeFailed']), type([]))

        subscribed = res['data']['subscribed']
        subscribeFailed = res['data']['subscribeFailed']

        for data in subscribed:
            self.assertEqual(len(data), 4)

        for data in subscribeFailed:
            self.assertEqual(len(data), 4)

        res = client.getSubscribingOrderbooks()

        self.assertEqual(len(res), 3)
        self.assertEqual(res['requestedApiCount'], 0)

        self.assertEqual(len(res['data']), 1)
        self.assertEqual(len(res['data']['orderbooks']), len(subscribed))

        for Orderbook in res['data']['orderbooks']:
            self.assertEqual(len(Orderbook), 4)
            symbol = Orderbook['symbol']
            isFound = False

            for subscribedOrderbook in subscribed:
                if symbol == subscribedOrderbook['symbol']:
                    isFound = True
                    break
            
            if isFound is False:
                self.assertFalse("Can't find subscribed symbol : " + symbol)

            isFound = True
            for failedOrderbook in subscribeFailed:
                if symbol == failedOrderbook['symbol']:
                    isFound = False
                    break

            if isFound is False:
                self.assertFalse("find subscribeFailed symbol : " + symbol)

    def test_subscribeOrderbook_8(self):

        client = OneXAPI.Binance.Futures()
        res = client.subscribeOrderbook('{"market":[{"baseCurrency":"HYUNKYU","quoteCurrency":"USDT"}]}')
        answer = json.loads('{"success":true,"requestedApiCount":1,"data":{"subscribed":[],"subscribeFailed":[{"baseCurrency":"HYUNKYU","quoteCurrency":"USDT","expiration":"PERP","symbol":"HYUNKYUUSDT"}]}}')

        self.assertEqual(res, answer)

        res = client.getSubscribingOrderbooks()
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"orderbooks":[]}}')

        self.assertEqual(res, answer)

    def test_subscribeOrderbook_9(self):

        client = OneXAPI.Binance.Futures()
        res = client.subscribeOrderbook('{"market":[{"baseCurrency":"BTC","quoteCurrency":"USDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT"}]}')
        answer = json.loads('{"success":true,"requestedApiCount":2,"data":{"subscribed":[{"baseCurrency":"BTC","quoteCurrency":"USDT","expiration":"PERP","symbol":"BTCUSDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT","expiration":"PERP","symbol":"ETHUSDT"}],"subscribeFailed":[]}}')

        self.assertEqual(res, answer)

        res = client.getSubscribingOrderbooks()
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"orderbooks":[{"baseCurrency":"BTC","quoteCurrency":"USDT","expiration":"PERP","symbol":"BTCUSDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT","expiration":"PERP","symbol":"ETHUSDT"}]}}')

        self.assertEqual(res, answer)

        res = client.subscribeOrderbook('{"market":[],"reconnect":true}')
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"subscribed":[],"subscribeFailed":[]}}')

        self.assertEqual(res, answer)

    def test_unsubscribeOrderbook_1(self):
        client = OneXAPI.Binance.Futures()

        res = client.unsubscribeOrderbook()
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], False)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_unsubscribeOrderbook_2(self):
        client = OneXAPI.Binance.Futures()

        res = client.unsubscribeOrderbook('')
        
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], False)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_unsubscribeOrderbook_3(self):
        client = OneXAPI.Binance.Futures()

        res = client.unsubscribeOrderbook('{}')
        
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], False)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_unsubscribeOrderbook_4(self):
        client = OneXAPI.Binance.Futures()

        res = client.unsubscribeOrderbook('Bqbqb@')
        
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], False)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['errorType'], 'JSON_PARSING_ERROR')
        
    def test_unsubscribeOrderbook_5(self):
        client = OneXAPI.Binance.Futures()

        client.subscribeOrderbook('{"market":[{"baseCurrency":"BTC","quoteCurrency":"USDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT"}]}')
        res = client.unsubscribeOrderbook('{"market":[{"baseCurrency":"BTC","quoteCurrency":"USDT"}]}')
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"unsubscribed":[{"baseCurrency":"BTC","quoteCurrency":"USDT","expiration":"PERP","symbol":"BTCUSDT"}],"unsubscribeFailed":[]}}')

        self.assertEqual(res, answer)

        res = client.getSubscribingOrderbooks()
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"orderbooks":[{"baseCurrency":"ETH","quoteCurrency":"USDT","expiration":"PERP","symbol":"ETHUSDT"}]}}')

        self.assertEqual(res, answer)

    def test_unsubscribeOrderbook_6(self):
        client = OneXAPI.Binance.Futures()

        client.subscribeOrderbook('{"market":[{"baseCurrency":"BTC","quoteCurrency":"USDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT"}]}')
        res = client.unsubscribeOrderbook('{"market":[{"baseCurrency":"BTC","quoteCurrency":"USDT"}],"reconnect":true}')
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"unsubscribed":[{"baseCurrency":"BTC","quoteCurrency":"USDT","expiration":"PERP","symbol":"BTCUSDT"}],"unsubscribeFailed":[]}}')
        
        self.assertEqual(res, answer)

        res = client.getSubscribingOrderbooks()
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"orderbooks":[{"baseCurrency":"ETH","quoteCurrency":"USDT","expiration":"PERP","symbol":"ETHUSDT"}]}}')

        self.assertEqual(res, answer)

    def test_unsubscribeOrderbook_7(self):
        client = OneXAPI.Binance.Futures()
        baseCurrencys = [
            "BTC", "ETH", "BCH", "XRP", "EOS", "LTC", "TRX", "ETC", "LINK", "XLM",
            "ADA", "XMR", "DASH", "ZEC", "XTZ", "BNB", "ATOM", "ONT", "IOTA", "BAT",
            "VET", "NEO", "QTUM", "IOST", "THETA", "ALGO", "ZIL", "KNC", "ZRX", "COMP",
            "OMG", "DOGE", "SXP", "KAVA", "BAND", "RLC", "WAVES", "MKR", "SNX", "DOT",
            "DEFI", "YFI", "BAL", "CRV", "TRB", "RUNE", "SUSHI", "SRM", "EGLD", "SOL",
            "ICX", "STORJ", "BLZ", "UNI", "AVAX", "FTM", "HNT", "ENJ", "FLM", "TOMO"
        ]
        markets = []

        for baseCurrency in baseCurrencys:
            pair = dict()
            pair['baseCurrency'] = baseCurrency
            pair['quoteCurrency'] = 'USDT'
            markets.append(pair)

        payload = dict()
        payload['market'] = markets

        res = client.subscribeOrderbook(payload)

        self.assertGreater(len(res['data']['subscribed']), 25)

        res = client.unsubscribeOrderbook(payload)

        self.assertEqual(len(res['data']), 2)
        self.assertEqual(type(res['data']['unsubscribed']), type([]))
        self.assertEqual(type(res['data']['unsubscribeFailed']), type([]))

        for unsubscribed in res['data']['unsubscribed']:
            self.assertEqual(len(unsubscribed), 4)

        for unsubscribeFailed in res['data']['unsubscribeFailed']:
            self.assertEqual(len(unsubscribeFailed), 4)

        res = client.getSubscribingOrderbooks()
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"orderbooks":[]}}')

        self.assertEqual(res, answer)

    def test_unsubscribeOrderbook_8(self):
        client = OneXAPI.Binance.Futures()
        res = client.unsubscribeOrderbook('{"market":[{"baseCurrency":"HYUNKYU","quoteCurrency":"USDT"}]}')
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"unsubscribed":[],"unsubscribeFailed":[{"baseCurrency":"HYUNKYU","quoteCurrency":"USDT","expiration":"PERP","symbol":"HYUNKYUUSDT"}]}}')

        self.assertEqual(res, answer)

    def test_unsubscribeOrderbook_9(self):
        client = OneXAPI.Binance.Futures()
        res = client.subscribeOrderbook('{"market":[{"baseCurrency":"BTC","quoteCurrency":"USDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT"}]}')
        answer = json.loads('{"success":true,"requestedApiCount":2,"data":{"subscribed":[{"baseCurrency":"BTC","quoteCurrency":"USDT","expiration":"PERP","symbol":"BTCUSDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT","expiration":"PERP","symbol":"ETHUSDT"}],"subscribeFailed":[]}}')

        self.assertEqual(res, answer)

        res = client.getSubscribingOrderbooks()
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"orderbooks":[{"baseCurrency":"BTC","quoteCurrency":"USDT","expiration":"PERP","symbol":"BTCUSDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT","expiration":"PERP","symbol":"ETHUSDT"}]}}')

        self.assertEqual(res, answer)

        res = client.unsubscribeOrderbook('{"market":[],"reconnect":true}')
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"unsubscribed":[],"unsubscribeFailed":[]}}')

        self.assertEqual(res, answer)

if __name__ == "__main__":
    import os
    filepath = './OneXAPI_Logs/OneXAPI_' + time.strftime('%Y-%m-%d', time.localtime(time.time())) + '.log'
    
    if os.path.exists(filepath):
        os.remove(filepath)

    unittest.main()