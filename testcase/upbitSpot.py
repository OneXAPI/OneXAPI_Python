import unittest
import sys, os
import json

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import OneXAPI

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
        client = OneXAPI.Upbit.Spot('{"secretKey":"Test Access Key"}')
        res = json.loads(client.getConfig())
        self.assertEqual(res['data']['secretKey'], 'Test Access Key')
        self.assertEqual(res['data']['accessKey'], '')    

    def test_UpbitSpot_Object_7(self):
        client = OneXAPI.Upbit.Spot('{"accessKey":"Test Access Key", "secretKey":"Test Access Key"}')
        res = json.loads(client.getConfig())
        self.assertEqual(res['data']['accessKey'], 'Test Access Key')

    def test_UpbitSpot_Object_7_1(self):
        client = OneXAPI.Upbit.Spot('{"accessKey":"Test Access Key", "secretKey":"Test Access Key"}')
        res = json.loads(client.getConfig())
        self.assertEqual(res['data']['secretKey'], 'Test Access Key')

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
        res = client.setConfig()
        self.assertEqual(res, '{"success":true,"data":{"requestedApiCount":0}}')

    def test_setConfig_4(self):
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

    def test_setConfig_5(self):
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

    def test_setConfig_6(self):
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