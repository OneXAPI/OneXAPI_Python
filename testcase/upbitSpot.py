import unittest
import sys, os, time
import json

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import OneXAPI

UPBIT_ACCESS_KEY = ""
UPBIT_SECRET_KEY = ""

hasMap = """
{
    "getConfig": true,
    "setConfig": true,
    "getEndpointCandidates": true,
    "has": true,
    "getWithdrawRoundingRule": true,
    "setWithdrawRoundingRule": true,
    "withdraw": true,
    "fetchAllCurrencies": true,
    "fetchBalance": true,
    "fetchWalletStatus": true,
    "fetchWithdrawHistory": true,
    "fetchDepositHistory": true,
    "fetchDepositAddress": true,
    "isDepositCompleted": true,
    "subscribeBalance": false,
    "unsubscribeBalance": false,
    "isSubscribingBalance": true,
    "getOrderRoundingRule": true,
    "setOrderRoundingRule": true,
    "orderLimitBuy": true,
    "orderLimitSell": true,
    "orderMarketBuy": true,
    "orderMarketSell": true,
    "orderCancel": true,
    "fetchTradingFee": true,
    "fetchOrderInfo": true,
    "fetchOpenOrders": true,
    "getCandleIntervalCandidates": true,
    "fetchMarkets": true,
    "fetchTicker": true,
    "fetchOrderbook": true,
    "fetchCandleHistory": true,
    "getSubscribingTickers": true,
    "getSubscribingOrderbooks": true,
    "subscribeTicker": true,
    "unsubscribeTicker": true,
    "subscribeOrderbook": true,
    "unsubscribeOrderbook": true,
    "unsubscribeTicker": true
}
"""

class Testing(unittest.TestCase):
    def test_UpbitSpot_Object_1(self):
        for i in range(0,5):
            client = OneXAPI.Upbit.Spot()
        self.assertEqual("", "")

    def test_UpbitSpot_Object_2(self):
        for i in range(0,5):
            client = OneXAPI.Upbit.Spot('')
        self.assertEqual("", "")

    def test_UpbitSpot_Object_3(self):
        for i in range(0,5):
            client = OneXAPI.Upbit.Spot("{}")
        self.assertEqual("", "")

    def test_UpbitSpot_Object_4(self):
        for i in range(0,5):
            client = OneXAPI.Upbit.Spot('fnq543wb')
        self.assertEqual("", "")

    def test_UpbitSpot_Object_5(self):
        client = OneXAPI.Upbit.Spot('{"accessKey":"Test Access Key"}')
        res = json.loads(client.getConfig())
        self.assertEqual(res['data']['accessKey'], 'Test Access Key')
        self.assertEqual(res['data']['secretKey'], '')

    def test_UpbitSpot_Object_6(self):
        client = OneXAPI.Upbit.Spot('{"secretKey":"Test Secret Key"}')
        res = json.loads(client.getConfig())
        self.assertEqual(res['data']['secretKey'], 'Test Secret Key')
        self.assertEqual(res['data']['accessKey'], '')    

    def test_UpbitSpot_Object_7(self):
        client = OneXAPI.Upbit.Spot('{"accessKey":"Test Access Key", "secretKey":"Test Secret Key"}')
        res = json.loads(client.getConfig())
        self.assertEqual(res['data']['accessKey'], 'Test Access Key')
        self.assertEqual(res['data']['secretKey'], 'Test Secret Key')

    def test_getConfig_1(self):
        client = OneXAPI.Upbit.Spot()
        res = client.getConfig()
        self.assertEqual(res, '{"success":true,"data":{"requestedApiCount":0,"exchange":"Upbit","instrument":"Spot","accessKey":"","secretKey":"","restEndpoint":"https://api.upbit.com/v1","publicWebsocketEndpoint":"wss://api.upbit.com/websocket/v1","privateWebsocketEndpoint":"","restRequestTimeout":5000,"websocketConnectTimeout":5000,"websocketIdleTimeout":5000}}')
    
    def test_getConfig_2(self):
        client = OneXAPI.Upbit.Spot()
        res = client.getConfig("")
        self.assertEqual(res, '{"success":true,"data":{"requestedApiCount":0,"exchange":"Upbit","instrument":"Spot","accessKey":"","secretKey":"","restEndpoint":"https://api.upbit.com/v1","publicWebsocketEndpoint":"wss://api.upbit.com/websocket/v1","privateWebsocketEndpoint":"","restRequestTimeout":5000,"websocketConnectTimeout":5000,"websocketIdleTimeout":5000}}')

    def test_getConfig_3(self):
        client = OneXAPI.Upbit.Spot()
        res = client.getConfig("{}")
        self.assertEqual(res, '{"success":true,"data":{"requestedApiCount":0,"exchange":"Upbit","instrument":"Spot","accessKey":"","secretKey":"","restEndpoint":"https://api.upbit.com/v1","publicWebsocketEndpoint":"wss://api.upbit.com/websocket/v1","privateWebsocketEndpoint":"","restRequestTimeout":5000,"websocketConnectTimeout":5000,"websocketIdleTimeout":5000}}')

    def test_getConfig_4(self):
        client = OneXAPI.Upbit.Spot()
        res = client.getConfig("trashData123@@!%")
        self.assertEqual(res, '{"success":true,"data":{"requestedApiCount":0,"exchange":"Upbit","instrument":"Spot","accessKey":"","secretKey":"","restEndpoint":"https://api.upbit.com/v1","publicWebsocketEndpoint":"wss://api.upbit.com/websocket/v1","privateWebsocketEndpoint":"","restRequestTimeout":5000,"websocketConnectTimeout":5000,"websocketIdleTimeout":5000}}')

    def test_setConfig_1(self):
        client = OneXAPI.Upbit.Spot()
        res = client.setConfig()
        self.assertEqual(res, '{"success":true,"data":{"requestedApiCount":0}}')

    def test_setConfig_2(self):
        client = OneXAPI.Upbit.Spot()
        res = client.setConfig("")
        self.assertEqual(res, '{"success":false,"data":{"errorType":"JSON_PARSING_ERROR","errorMsg":""}}')

    def test_setConfig_3(self):
        client = OneXAPI.Upbit.Spot()
        res = json.loads(client.setConfig('{"accessKey":1.1354}'))
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'WRONG_VALUE_TYPE')

        res = json.loads(client.setConfig('{"secretKey":11354}'))
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'WRONG_VALUE_TYPE')

        res = json.loads(client.setConfig('{"restEndpoint":null}'))
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'WRONG_VALUE_TYPE')

        res = json.loads(client.setConfig('{"publicWebsocketEndpoint":true}'))
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'WRONG_VALUE_TYPE')

        res = json.loads(client.setConfig('{"privateWebsocketEndpoint":{}}'))
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'WRONG_VALUE_TYPE')

        res = json.loads(client.setConfig('{"restRequestTimeout":1.1354}'))
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'WRONG_VALUE_TYPE')

        res = json.loads(client.setConfig('{"websocketConnectTimeout":"ffaew"}'))
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'WRONG_VALUE_TYPE')

        res = json.loads(client.setConfig('{"websocketIdleTimeout":false}'))
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'WRONG_VALUE_TYPE')

    def test_setConfig_4(self):
        client = OneXAPI.Upbit.Spot()
        res = json.loads(client.setConfig('{"restEndpoint":"wrongEndpoint"}'))
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'WRONG_VALUE')

        res = json.loads(client.setConfig('{"publicWebsocketEndpoint":"wrongEndpoint"}'))
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'WRONG_VALUE')

        res = json.loads(client.setConfig('{"privateWebsocketEndpoint":"wrongEndpoint"}'))
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'WRONG_VALUE')

    def test_setConfig_5(self):
        client = OneXAPI.Upbit.Spot()
        testList = [
            ('accessKey','"test access key"'),
            ('secretKey','"test secret key"'),
            ('restEndpoint','"https://api.upbit.com/v1"'),
            ('publicWebsocketEndpoint','"wss://api.upbit.com/websocket/v1"'),
            ('restRequestTimeout','1378331'),
            ('websocketConnectTimeout','3787123'),
            ('websocketIdleTimeout','8941313531215')
        ]

        for item in testList:
            input = '{"' + item[0] + '":' + item[1] + '}'
            res = json.loads(client.setConfig(input))

            self.assertEqual(res['success'], True)
            answer = None
            if type(res['data'][item[0]]) == str:
                answer = item[1].replace('"', "")
            elif type(res['data'][item[0]]) == int:
                answer = int(item[1])

            self.assertEqual(res['data'][item[0]], answer)

        res = json.loads(client.getConfig())

        for item in testList:
            self.assertEqual(res['success'], True)
            answer = None
            if type(res['data'][item[0]]) == str:
                answer = item[1].replace('"', "")
            elif type(res['data'][item[0]]) == int:
                answer = int(item[1])
                
            self.assertEqual(res['data'][item[0]], answer)

    def test_getEndpointCandidates_1(self):
        client = OneXAPI.Upbit.Spot()

        res = client.getEndpointCandidates()

        self.assertEqual(res, '{"success":true,"data":{"requestedApiCount":0,"restEndpoints":["https://api.upbit.com/v1"],"publicWebsocketEndpoints":["wss://api.upbit.com/websocket/v1"],"privateWebsocketEndpoints":[]}}')

    def test_getEndpointCandidates_2(self):
        client = OneXAPI.Upbit.Spot()

        res = client.getEndpointCandidates("")

        self.assertEqual(res, '{"success":true,"data":{"requestedApiCount":0,"restEndpoints":["https://api.upbit.com/v1"],"publicWebsocketEndpoints":["wss://api.upbit.com/websocket/v1"],"privateWebsocketEndpoints":[]}}')

    def test_getEndpointCandidates_3(self):
        client = OneXAPI.Upbit.Spot()

        res = client.getEndpointCandidates("{}")

        self.assertEqual(res, '{"success":true,"data":{"requestedApiCount":0,"restEndpoints":["https://api.upbit.com/v1"],"publicWebsocketEndpoints":["wss://api.upbit.com/websocket/v1"],"privateWebsocketEndpoints":[]}}')

    def test_getEndpointCandidates_4(self):
        client = OneXAPI.Upbit.Spot()

        res = client.getEndpointCandidates("uNPaRsib1eM5g")

        self.assertEqual(res, '{"success":true,"data":{"requestedApiCount":0,"restEndpoints":["https://api.upbit.com/v1"],"publicWebsocketEndpoints":["wss://api.upbit.com/websocket/v1"],"privateWebsocketEndpoints":[]}}')

    def test_has_1(self):
        client = OneXAPI.Upbit.Spot()

        res = json.loads(client.has(''))
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'JSON_PARSING_ERROR')

    def test_has_2(self):
        client = OneXAPI.Upbit.Spot()

        res = json.loads(client.has('{}'))
        answer = json.loads(hasMap)

        for key, value in answer.items():
            self.assertEqual(res['data'][key], value)

    def test_has_3(self):
        client = OneXAPI.Upbit.Spot()

        res = json.loads(client.has('el12nlgv@!'))
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'JSON_PARSING_ERROR')

    def test_has_4(self):
        client = OneXAPI.Upbit.Spot()

        answer = json.loads(hasMap)

        for key, value in answer.items():
            res = json.loads(client.has('{"api":"' + key + '"}'))
            self.assertEqual(res['success'], True)
            self.assertEqual(res['data'][key], value)
            self.assertEqual(res['data']['requestedApiCount'], 0)

    def test_has_5(self):
        client = OneXAPI.Upbit.Spot()

        res = json.loads(client.has('{"api":"notExistApi"}'))
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'WRONG_VALUE')

    def test_getWithdrawRoundingRule_1(self):
        client = OneXAPI.Upbit.Spot()

        res = client.getWithdrawRoundingRule()
        self.assertEqual(res, '{"success":true,"data":{"requestedApiCount":0,"roundingRule":"round"}}')

    def test_getWithdrawRoundingRule_2(self):
        client = OneXAPI.Upbit.Spot()

        res = client.getWithdrawRoundingRule('qwerion')
        self.assertEqual(res, '{"success":true,"data":{"requestedApiCount":0,"roundingRule":"round"}}')

    def test_setWithdrawRoundingRule_1(self):
        client = OneXAPI.Upbit.Spot()

        res = json.loads(client.setWithdrawRoundingRule('{"roundingRule":"wrongData"}'))
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'WRONG_VALUE')

    def test_setWithdrawRoundingRule_1(self):
        client = OneXAPI.Upbit.Spot()

        for value in ['ceil', 'floor', 'round']:
            res = json.loads(client.setWithdrawRoundingRule('{"roundingRule":"' + value +'"}'))
            self.assertEqual(res['success'], True)
            self.assertEqual(res['data']['roundingRule'], value)
            self.assertEqual(res['data']['requestedApiCount'], 0)

    def test_withdraw_1(self):
        client = OneXAPI.Upbit.Spot()
        
        testdict = ['{"currency":"bTc","address":"0x1345"}','{"currency":"bTc","amount":1.535478}','{"address":"fwlnvlwnlkfsd","amount":13384.13541345}']
        
        for payload in testdict:
            res = json.loads(client.withdraw(payload))
            self.assertEqual(res['success'], False)
            self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_fetchAllCurrencies_1(self):
        time.sleep(1)
        client = OneXAPI.Upbit.Spot('{"accessKey":"' + UPBIT_ACCESS_KEY + '", "secretKey":"' + UPBIT_SECRET_KEY + '"}')

        res = json.loads(client.fetchAllCurrencies())
        self.assertEqual(res['success'], True)
        self.assertEqual(res['data']['requestedApiCount'], 1)
        self.assertNotEqual(len(res['data']['currencies']), 0)

        for currency, chainsDict in res['data']['currencies'].items():
            self.assertTrue(type(currency), type(""))
            self.assertTrue(json.dumps(chainsDict), '{"chains": []}')

    def test_fetchAllCurrencies_2(self):
        time.sleep(1)
        client = OneXAPI.Upbit.Spot('{"accessKey":"' + UPBIT_ACCESS_KEY + '", "secretKey":"' + UPBIT_SECRET_KEY + '"}')

        res = json.loads(client.fetchAllCurrencies(""))
        self.assertEqual(res['success'], True)
        self.assertEqual(res['data']['requestedApiCount'], 1)
        self.assertNotEqual(len(res['data']['currencies']), 0)

        for currency, chainsDict in res['data']['currencies'].items():
            self.assertTrue(type(currency), type(""))
            self.assertTrue(json.dumps(chainsDict), '{"chains": []}')

    def test_fetchBalance_1(self):
        time.sleep(1)
        client = OneXAPI.Upbit.Spot('{"accessKey":"' + UPBIT_ACCESS_KEY + '", "secretKey":"' + UPBIT_SECRET_KEY + '"}')
        
        res = json.loads(client.fetchBalance('{"currencies":[]}'))
        self.assertEqual(res['success'], True)
        self.assertEqual(res['data']['requestedApiCount'], 1)
        self.assertEqual(res['data']['fetchType'], "rest")
        
        for currency, balance in res['data']['balance'].items():
            self.assertTrue(type(currency), type(""))
            self.assertTrue(type(balance["free"]), type(""))
            self.assertTrue(type(balance["locked"]), type(""))

    def test_fetchBalance_2(self):
        time.sleep(1)
        client = OneXAPI.Upbit.Spot('{"accessKey":"' + UPBIT_ACCESS_KEY + '", "secretKey":"' + UPBIT_SECRET_KEY + '"}')
        
        res = json.loads(client.fetchBalance('{"currencies":["bTc","xRP","Eth"], "zeroBalance": true}'))
        self.assertEqual(res['success'], True)
        self.assertEqual(res['data']['requestedApiCount'], 2)
        self.assertEqual(res['data']['fetchType'], "rest")
        self.assertEqual(len(res['data']['balance']), 3)
        
        for currency, balance in res['data']['balance'].items():
            self.assertTrue(type(currency), type(""))
            self.assertTrue(type(balance["free"]), type(""))
            self.assertTrue(type(balance["locked"]), type(""))

    def test_fetchWalletStatus_1(self):
        time.sleep(1)
        client = OneXAPI.Upbit.Spot('{"accessKey":"' + UPBIT_ACCESS_KEY + '", "secretKey":"' + UPBIT_SECRET_KEY + '"}')
        
        res = json.loads(client.fetchWalletStatus('{}'))
        self.assertEqual(res['success'], True)
        self.assertEqual(res['data']['requestedApiCount'], 1)
        self.assertNotEqual(len(res['data']['currencies']), 0)

        for currency, wallet in res['data']['currencies'].items():
            self.assertTrue(type(currency), type(""))
            self.assertTrue(type(wallet["chains"]), type([]))
            self.assertTrue(len(wallet["chains"]), 1)
            self.assertEqual(wallet["chains"][0]["chain"], "")
            self.assertTrue(type(wallet["chains"][0]["withdrawEnable"]), type(True))
            self.assertTrue(type(wallet["chains"][0]["depositEnable"]), type(True))

    def test_fetchWalletStatus_2(self):
        time.sleep(1)
        client = OneXAPI.Upbit.Spot('{"accessKey":"' + UPBIT_ACCESS_KEY + '", "secretKey":"' + UPBIT_SECRET_KEY + '"}')
        
        res = json.loads(client.fetchWalletStatus('{"currency":"bTc"}'))
        self.assertEqual(res['success'], True)
        self.assertEqual(res['data']['requestedApiCount'], 1)
        self.assertEqual(len(res['data']['currencies']), 1)

        for currency, wallet in res['data']['currencies'].items():
            self.assertTrue(type(currency), type(""))
            self.assertTrue(type(wallet["chains"]), type([]))
            self.assertTrue(len(wallet["chains"]), 1)
            self.assertEqual(wallet["chains"][0]["chain"], "")
            self.assertTrue(type(wallet["chains"][0]["withdrawEnable"]), type(True))
            self.assertTrue(type(wallet["chains"][0]["depositEnable"]), type(True))

    def test_fetchWithdrawHistory_1(self):
        time.sleep(1)
        client = OneXAPI.Upbit.Spot('{"accessKey":"' + UPBIT_ACCESS_KEY + '", "secretKey":"' + UPBIT_SECRET_KEY + '"}')
        
        res = json.loads(client.fetchWithdrawHistory('{}'))
        self.assertEqual(res['success'], True)
        self.assertEqual(res['data']['requestedApiCount'], 1)
        self.assertNotEqual(len(res['data']['withdrawals']), 0)

        for withdrawHistory in res['data']['withdrawals']:
            self.assertTrue(type(withdrawHistory["currency"]), type(""))
            self.assertTrue(type(withdrawHistory["amount"]), type(""))
            self.assertTrue(type(withdrawHistory["fee"]), type(""))
            self.assertTrue(type(withdrawHistory["orderId"]), type(""))
            self.assertTrue(type(withdrawHistory["txid"]), type(""))
            self.assertTrue(type(withdrawHistory["status"]), type(""))
            self.assertTrue(type(withdrawHistory["created"]), type(""))

    def test_fetchDepositHistory_1(self):
        time.sleep(1)
        client = OneXAPI.Upbit.Spot('{"accessKey":"' + UPBIT_ACCESS_KEY + '", "secretKey":"' + UPBIT_SECRET_KEY + '"}')
        
        res = json.loads(client.fetchDepositHistory('{}'))
        self.assertEqual(res['success'], True)
        self.assertEqual(res['data']['requestedApiCount'], 1)
        self.assertNotEqual(len(res['data']['deposits']), 0)

        for deposit in res['data']['deposits']:
            self.assertTrue(type(deposit["currency"]), type(""))
            self.assertTrue(type(deposit["amount"]), type(""))
            self.assertTrue(type(deposit["fee"]), type(""))
            self.assertTrue(type(deposit["orderId"]), type(""))
            self.assertTrue(type(deposit["txid"]), type(""))
            self.assertTrue(type(deposit["status"]), type(""))
            self.assertTrue(type(deposit["created"]), type(""))

    def test_fetchDepositAddress_1(self):
        time.sleep(1)
        client = OneXAPI.Upbit.Spot('{"accessKey":"' + UPBIT_ACCESS_KEY + '", "secretKey":"' + UPBIT_SECRET_KEY + '"}')
        
        res = json.loads(client.fetchDepositAddress('{}'))
        self.assertEqual(res['success'], True)
        self.assertEqual(res['data']['requestedApiCount'], 1)
        self.assertNotEqual(len(res['data']['addresses']), 0)

        for currency, depositDict in res['data']['addresses'].items():
            self.assertTrue(type(currency), type(""))
            self.assertTrue(type(depositDict), type([]))
            self.assertEqual(len(depositDict), 1)
            self.assertEqual(depositDict[0]["chain"], "")
            self.assertTrue(type(depositDict[0]["address"]), type(""))
            self.assertTrue(type(depositDict[0]["tag"]), type(""))
    
    def test_fetchDepositAddress_2(self):
        time.sleep(1)
        client = OneXAPI.Upbit.Spot('{"accessKey":"' + UPBIT_ACCESS_KEY + '", "secretKey":"' + UPBIT_SECRET_KEY + '"}')
        
        res = json.loads(client.fetchDepositAddress('{"currency":"Btc"}'))
        self.assertEqual(res['success'], True)
        self.assertEqual(res['data']['requestedApiCount'], 1)
        self.assertEqual(len(res['data']['addresses']), 1)

        for currency, depositDict in res['data']['addresses'].items():
            self.assertTrue(type(currency), type(""))
            self.assertTrue(type(depositDict), type([]))
            self.assertEqual(len(depositDict), 1)
            self.assertEqual(depositDict[0]["chain"], "")
            self.assertTrue(type(depositDict[0]["address"]), type(""))
            self.assertTrue(type(depositDict[0]["tag"]), type(""))

    def test_isDepositCompleted_1(self):
        client = OneXAPI.Upbit.Spot()

        res = json.loads(client.isDepositCompleted('{}'))
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_getOrderRoundingRule_1(self):
        client = OneXAPI.Upbit.Spot()
        res = client.getOrderRoundingRule()

        self.assertEqual(res, '{"success":true,"data":{"requestedApiCount":0,"limitBuyPrice":"round","limitBuyBaseAmount":"round","limitSellPrice":"round","limitSellBaseAmount":"round","marketBuyQuoteAmount":"round","marketSellBaseAmount":"round"}}')

    def test_getOrderRoundingRule_2(self):
        client = OneXAPI.Upbit.Spot()
        res = client.getOrderRoundingRule("")

        self.assertEqual(res, '{"success":true,"data":{"requestedApiCount":0,"limitBuyPrice":"round","limitBuyBaseAmount":"round","limitSellPrice":"round","limitSellBaseAmount":"round","marketBuyQuoteAmount":"round","marketSellBaseAmount":"round"}}')

    def test_setOrderRoundingRule_1(self):
        client = OneXAPI.Upbit.Spot()

        res = json.loads(client.setOrderRoundingRule('{"limitBuyBaseAmount":"wrongData"}'))
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'WRONG_VALUE')

    def test_orderLimitBuy_1(self):
        client = OneXAPI.Upbit.Spot()
        
        res = json.loads(client.orderLimitBuy('{}'))
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_orderLimitSell_1(self):
        client = OneXAPI.Upbit.Spot()
        
        res = json.loads(client.orderLimitSell('{}'))
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_orderMarketBuy_1(self):
        client = OneXAPI.Upbit.Spot()
        
        res = json.loads(client.orderMarketBuy('{}'))
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_orderMarketSell_1(self):
        client = OneXAPI.Upbit.Spot()
        
        res = json.loads(client.orderMarketSell('{}'))
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_orderCancel_1(self):
        client = OneXAPI.Upbit.Spot()
        
        res = json.loads(client.orderCancel('{}'))
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_fetchTradingFee_1(self):
        client = OneXAPI.Upbit.Spot()
        
        res = json.loads(client.fetchTradingFee('{"baseCurrency":"bTC"}'))
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_fetchTradingFee_2(self):
        time.sleep(1)
        client = OneXAPI.Upbit.Spot('{"accessKey":"' + UPBIT_ACCESS_KEY + '", "secretKey":"' + UPBIT_SECRET_KEY + '"}')
        
        res = client.fetchTradingFee('{"baseCurrency":"bTC","quoteCurrency":"KRw"}')
        self.assertEqual(res, '{"success":true,"data":{"requestedApiCount":1,"fees":[{"baseCurrency":"BTC","quoteCurrency":"KRW","symbol":"KRW-BTC","makerFee":"0.0005","takerFee":"0.0005"}]}}')

    def test_fetchOrderInfo_1(self):
        client = OneXAPI.Upbit.Spot()
        
        res = json.loads(client.fetchOrderInfo(''))
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

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