import unittest
import sys, os, time
import json
import util

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))))
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

    def test_UpbitSpot_Object_2(self):
        for i in range(0,5):
            client = OneXAPI.Upbit.Spot('')

    def test_UpbitSpot_Object_3(self):
        for i in range(0,5):
            client = OneXAPI.Upbit.Spot("{}")

    def test_UpbitSpot_Object_4(self):
        for i in range(0,5):
            client = OneXAPI.Upbit.Spot('fnq543wb')

    def test_UpbitSpot_Object_5(self):
        client = OneXAPI.Upbit.Spot('{"accessKey":"Test Access Key"}')
        res = client.getConfig()
        self.assertEqual(res['data']['accessKey'], 'Test Access Key')
        self.assertEqual(res['data']['secretKey'], '')

    def test_UpbitSpot_Object_6(self):
        client = OneXAPI.Upbit.Spot('{"secretKey":"Test Secret Key"}')
        res = client.getConfig()
        self.assertEqual(res['data']['secretKey'], 'Test Secret Key')
        self.assertEqual(res['data']['accessKey'], '')    

    def test_UpbitSpot_Object_7(self):
        client = OneXAPI.Upbit.Spot('{"accessKey":"Test Access Key", "secretKey":"Test Secret Key"}')
        res = client.getConfig()
        self.assertEqual(res['data']['accessKey'], 'Test Access Key')
        self.assertEqual(res['data']['secretKey'], 'Test Secret Key')

    def test_getConfig_1(self):
        client = OneXAPI.Upbit.Spot()
        res = client.getConfig()
        answer = json.loads('{"success":true,"data":{"requestedApiCount":0,"exchange":"Upbit","instrument":"Spot","accessKey":"","secretKey":"","restEndpoint":"https://api.upbit.com/v1","publicWebsocketEndpoint":"wss://api.upbit.com/websocket/v1","privateWebsocketEndpoint":"","restRequestTimeout":5000,"websocketConnectTimeout":5000,"websocketIdleTimeout":5000}}')
        self.assertEqual(res, answer)
    
    def test_getConfig_2(self):
        client = OneXAPI.Upbit.Spot()
        res = client.getConfig("")
        answer = json.loads('{"success":true,"data":{"requestedApiCount":0,"exchange":"Upbit","instrument":"Spot","accessKey":"","secretKey":"","restEndpoint":"https://api.upbit.com/v1","publicWebsocketEndpoint":"wss://api.upbit.com/websocket/v1","privateWebsocketEndpoint":"","restRequestTimeout":5000,"websocketConnectTimeout":5000,"websocketIdleTimeout":5000}}')
        self.assertEqual(res, answer)

    def test_getConfig_3(self):
        client = OneXAPI.Upbit.Spot()
        res = client.getConfig("{}")
        answer = json.loads('{"success":true,"data":{"requestedApiCount":0,"exchange":"Upbit","instrument":"Spot","accessKey":"","secretKey":"","restEndpoint":"https://api.upbit.com/v1","publicWebsocketEndpoint":"wss://api.upbit.com/websocket/v1","privateWebsocketEndpoint":"","restRequestTimeout":5000,"websocketConnectTimeout":5000,"websocketIdleTimeout":5000}}')
        self.assertEqual(res, answer)

    def test_getConfig_4(self):
        client = OneXAPI.Upbit.Spot()
        res = client.getConfig("trashData123@@!%")
        answer = json.loads('{"success":true,"data":{"requestedApiCount":0,"exchange":"Upbit","instrument":"Spot","accessKey":"","secretKey":"","restEndpoint":"https://api.upbit.com/v1","publicWebsocketEndpoint":"wss://api.upbit.com/websocket/v1","privateWebsocketEndpoint":"","restRequestTimeout":5000,"websocketConnectTimeout":5000,"websocketIdleTimeout":5000}}')
        self.assertEqual(res, answer)

    def test_setConfig_1(self):
        client = OneXAPI.Upbit.Spot()
        res = client.setConfig("")
        answer = json.loads('{"success":false,"data":{"errorType":"JSON_PARSING_ERROR","errorMsg":""}}')
        self.assertEqual(res, answer)

    def test_setConfig_2(self):
        client = OneXAPI.Upbit.Spot()
        res = client.setConfig("{}")
        answer = json.loads('{"success":true,"data":{"requestedApiCount":0}}')
        self.assertEqual(res, answer)

    def test_setConfig_3(self):
        client = OneXAPI.Upbit.Spot()
        res = client.setConfig('{"accessKey":1.1354}')
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'WRONG_VALUE_TYPE')

        res = client.setConfig('{"secretKey":11354}')
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'WRONG_VALUE_TYPE')

        res = client.setConfig('{"restEndpoint":null}')
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'WRONG_VALUE_TYPE')

        res = client.setConfig('{"publicWebsocketEndpoint":true}')
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'WRONG_VALUE_TYPE')

        res = client.setConfig('{"privateWebsocketEndpoint":{}}')
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'WRONG_VALUE_TYPE')

        res = client.setConfig('{"restRequestTimeout":1.1354}')
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'WRONG_VALUE_TYPE')

        res = client.setConfig('{"websocketConnectTimeout":"ffaew"}')
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'WRONG_VALUE_TYPE')

        res = client.setConfig('{"websocketIdleTimeout":false}')
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'WRONG_VALUE_TYPE')

    def test_setConfig_4(self):
        client = OneXAPI.Upbit.Spot()
        res = client.setConfig('{"restEndpoint":"wrongEndpoint"}')
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'WRONG_VALUE')

        res = client.setConfig('{"publicWebsocketEndpoint":"wrongEndpoint"}')
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'WRONG_VALUE')

        res = client.setConfig('{"privateWebsocketEndpoint":"wrongEndpoint"}')
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
            res = client.setConfig(input)

            self.assertEqual(res['success'], True)
            answer = None
            if type(res['data'][item[0]]) == str:
                answer = item[1].replace('"', "")
            elif type(res['data'][item[0]]) == int:
                answer = int(item[1])

            self.assertEqual(res['data'][item[0]], answer)

        res = client.getConfig()

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
        answer = json.loads('{"success":true,"data":{"requestedApiCount":0,"restEndpoints":["https://api.upbit.com/v1"],"publicWebsocketEndpoints":["wss://api.upbit.com/websocket/v1"],"privateWebsocketEndpoints":[]}}')

        self.assertEqual(res, answer)

    def test_getEndpointCandidates_2(self):
        client = OneXAPI.Upbit.Spot()

        res = client.getEndpointCandidates("")
        answer = json.loads('{"success":true,"data":{"requestedApiCount":0,"restEndpoints":["https://api.upbit.com/v1"],"publicWebsocketEndpoints":["wss://api.upbit.com/websocket/v1"],"privateWebsocketEndpoints":[]}}')

        self.assertEqual(res, answer)

    def test_getEndpointCandidates_3(self):
        client = OneXAPI.Upbit.Spot()

        res = client.getEndpointCandidates("{}")
        answer = json.loads('{"success":true,"data":{"requestedApiCount":0,"restEndpoints":["https://api.upbit.com/v1"],"publicWebsocketEndpoints":["wss://api.upbit.com/websocket/v1"],"privateWebsocketEndpoints":[]}}')

        self.assertEqual(res, answer)

    def test_getEndpointCandidates_4(self):
        client = OneXAPI.Upbit.Spot()

        res = client.getEndpointCandidates("uNPaRsib1eM5g")
        answer = json.loads('{"success":true,"data":{"requestedApiCount":0,"restEndpoints":["https://api.upbit.com/v1"],"publicWebsocketEndpoints":["wss://api.upbit.com/websocket/v1"],"privateWebsocketEndpoints":[]}}')

        self.assertEqual(res, answer)

    def test_has_1(self):
        client = OneXAPI.Upbit.Spot()

        res = client.has('')
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'JSON_PARSING_ERROR')

    def test_has_2(self):
        client = OneXAPI.Upbit.Spot()

        res = client.has('{}')
        answer = json.loads(hasMap)

        for key, value in answer.items():
            self.assertEqual(res['data'][key], value)

    def test_has_3(self):
        client = OneXAPI.Upbit.Spot()

        res = client.has('el12nlgv@!')
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'JSON_PARSING_ERROR')

    def test_has_4(self):
        client = OneXAPI.Upbit.Spot()

        answer = json.loads(hasMap)

        for key, value in answer.items():
            res = client.has('{"api":"' + key + '"}')
            self.assertEqual(res['success'], True)
            self.assertEqual(res['data'][key], value)
            self.assertEqual(res['data']['requestedApiCount'], 0)

    def test_has_5(self):
        client = OneXAPI.Upbit.Spot()

        res = client.has('{"api":"notExistApi"}')
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'WRONG_VALUE')

    def test_getWithdrawRoundingRule_1(self):
        client = OneXAPI.Upbit.Spot()

        res = client.getWithdrawRoundingRule()
        answer = json.loads('{"success":true,"data":{"requestedApiCount":0,"roundingRule":"round"}}')
        self.assertEqual(res, answer)

    def test_getWithdrawRoundingRule_2(self):
        client = OneXAPI.Upbit.Spot()

        res = client.getWithdrawRoundingRule('qwerion')
        answer = json.loads('{"success":true,"data":{"requestedApiCount":0,"roundingRule":"round"}}')
        self.assertEqual(res, answer)

    def test_setWithdrawRoundingRule_1(self):
        client = OneXAPI.Upbit.Spot()

        res = client.setWithdrawRoundingRule('{"roundingRule":"wrongData"}')
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'WRONG_VALUE')

    def test_setWithdrawRoundingRule_1(self):
        client = OneXAPI.Upbit.Spot()

        for value in ['ceil', 'floor', 'round']:
            res = client.setWithdrawRoundingRule('{"roundingRule":"' + value +'"}')
            self.assertEqual(res['success'], True)
            self.assertEqual(res['data']['roundingRule'], value)
            self.assertEqual(res['data']['requestedApiCount'], 0)

    def test_withdraw_1(self):
        client = OneXAPI.Upbit.Spot()
        
        testdict = ['{"currency":"bTc","address":"0x1345"}','{"currency":"bTc","amount":1.535478}','{"address":"fwlnvlwnlkfsd","amount":13384.13541345}']
        
        for payload in testdict:
            res = client.withdraw(payload)
            self.assertEqual(res['success'], False)
            self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_withdraw_2(self):
        time.sleep(1)
        client = OneXAPI.Upbit.Spot('{"accessKey":"' + UPBIT_ACCESS_KEY + '", "secretKey":"' + UPBIT_SECRET_KEY + '"}')
        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"file","logLevel":"info"}}')

        nowTime = time.localtime(time.time())
        
        res = client.withdraw('{"currency":"aDA","address":"wrongAddress","amount":135.1234358}')
        time.sleep(1)
        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"terminal","logLevel":"off"}}')
        answer1 = 'https://api.upbit.com/v1/withdraws/chance?currency=ADA'
        answer2 = 'https://api.upbit.com/v1/withdraws/coin?currency=ADA&amount=134.623436&address=wrongAddress&transaction_type=default'

        if util.searchLog(nowTime, answer1) is False:
            self.fail(f'{answer1} not found')
        if util.searchLog(nowTime, answer2) is False:
            self.fail(f'{answer2} not found')

    def test_withdraw_3(self):
        time.sleep(1)
        client = OneXAPI.Upbit.Spot('{"accessKey":"' + UPBIT_ACCESS_KEY + '", "secretKey":"' + UPBIT_SECRET_KEY + '"}')
        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"file","logLevel":"info"}}')

        nowTime = time.localtime(time.time())
        
        res = client.withdraw('{"currency":"aDA","address":"wrongAddress","tag":"wrongTag","amount":135.1234358,"feeInAmount":false,"internal":true}')
        time.sleep(1)
        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"terminal","logLevel":"off"}}')
        answer1 = 'https://api.upbit.com/v1/withdraws/chance?currency=ADA'
        answer2 = 'https://api.upbit.com/v1/withdraws/coin?currency=ADA&amount=135.123436&address=wrongAddress&secondary_address=wrongTag&transaction_type=internal'

        if util.searchLog(nowTime, answer1) is False:
            self.fail(f'{answer1} not found')
        if util.searchLog(nowTime, answer2) is False:
            self.fail(f'{answer2} not found')

    def test_fetchAllCurrencies_1(self):
        time.sleep(1)
        client = OneXAPI.Upbit.Spot('{"accessKey":"' + UPBIT_ACCESS_KEY + '", "secretKey":"' + UPBIT_SECRET_KEY + '"}')

        res = client.fetchAllCurrencies()
        self.assertEqual(res['success'], True)
        self.assertEqual(res['data']['requestedApiCount'], 1)
        self.assertNotEqual(len(res['data']['currencies']), 0)

        for currency, chainsDict in res['data']['currencies'].items():
            self.assertTrue(type(currency), type(""))
            self.assertTrue(json.dumps(chainsDict), '{"chains": []}')

    def test_fetchAllCurrencies_2(self):
        time.sleep(1)
        client = OneXAPI.Upbit.Spot('{"accessKey":"' + UPBIT_ACCESS_KEY + '", "secretKey":"' + UPBIT_SECRET_KEY + '"}')

        res = client.fetchAllCurrencies("")
        self.assertEqual(res['success'], True)
        self.assertEqual(res['data']['requestedApiCount'], 1)
        self.assertNotEqual(len(res['data']['currencies']), 0)

        for currency, chainsDict in res['data']['currencies'].items():
            self.assertTrue(type(currency), type(""))
            self.assertTrue(json.dumps(chainsDict), '{"chains": []}')

    def test_fetchBalance_1(self):
        time.sleep(1)
        client = OneXAPI.Upbit.Spot('{"accessKey":"' + UPBIT_ACCESS_KEY + '", "secretKey":"' + UPBIT_SECRET_KEY + '"}')
        
        res = client.fetchBalance('{"currencies":[]}')
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
        
        res = client.fetchBalance('{"currencies":["bTc","xRP","Eth"], "zeroBalance": true}')
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
        
        res = client.fetchWalletStatus('{}')
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
        
        res = client.fetchWalletStatus('{"currency":"bTc"}')
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
        
        res = client.fetchWithdrawHistory('{}')
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

    def test_fetchWithdrawHistory_2(self):
        time.sleep(1)
        client = OneXAPI.Upbit.Spot('{"accessKey":"' + UPBIT_ACCESS_KEY + '", "secretKey":"' + UPBIT_SECRET_KEY + '"}')
        
        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"file","logLevel":"info"}}')

        nowTime = time.localtime(time.time())
        
        client.fetchWithdrawHistory('{"currency":"mATic","orderId":"testOrderId","txid":"testTxId","startTime":132123534,"endTime":1125615123}')
        time.sleep(1)
        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"terminal","logLevel":"off"}}')

        answer1 = 'https://api.upbit.com/v1/withdraws?currency=MATIC&uuids=testOrderId&txids=testTxId'

        if util.searchLog(nowTime, answer1) is False:
            self.fail(f'{answer1} not found')

    def test_fetchDepositHistory_1(self):
        time.sleep(1)
        client = OneXAPI.Upbit.Spot('{"accessKey":"' + UPBIT_ACCESS_KEY + '", "secretKey":"' + UPBIT_SECRET_KEY + '"}')
        
        res = client.fetchDepositHistory('{}')
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

    def test_fetchDepositHistory_2(self):
        time.sleep(1)
        client = OneXAPI.Upbit.Spot('{"accessKey":"' + UPBIT_ACCESS_KEY + '", "secretKey":"' + UPBIT_SECRET_KEY + '"}')

        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"file","logLevel":"info"}}')

        nowTime = time.localtime(time.time())
        
        client.fetchDepositHistory('{"currency":"mATic","orderId":"testOrderId","txid":"testTxId","startTime":132123534,"endTime":1125615123}')
        time.sleep(1)
        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"terminal","logLevel":"off"}}')

        answer1 = 'https://api.upbit.com/v1/deposits?currency=MATIC&uuids=testOrderId&txids=testTxId'

        if util.searchLog(nowTime, answer1) is False:
            self.fail(f'{answer1} not found')

    def test_fetchDepositAddress_1(self):
        time.sleep(1)
        client = OneXAPI.Upbit.Spot('{"accessKey":"' + UPBIT_ACCESS_KEY + '", "secretKey":"' + UPBIT_SECRET_KEY + '"}')
        
        res = client.fetchDepositAddress('{}')
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
        
        res = client.fetchDepositAddress('{"currency":"Btc"}')
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

        res = client.isDepositCompleted('{}')
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_isDepositCompleted_2(self):
        time.sleep(1)
        client = OneXAPI.Upbit.Spot('{"accessKey":"' + UPBIT_ACCESS_KEY + '", "secretKey":"' + UPBIT_SECRET_KEY + '"}')

        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"file","logLevel":"info"}}')

        nowTime = time.localtime(time.time())
        
        res = client.isDepositCompleted('{"txid":"testTxid"}')
        time.sleep(1)
        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"terminal","logLevel":"off"}}')

        answer1 = 'https://api.upbit.com/v1/deposits?txids=testTxid'

        if util.searchLog(nowTime, answer1) is False:
            self.fail(f'{answer1} not found')

        answer = json.loads('{"success":true,"data":{"requestedApiCount":1,"isDepositCompleted":false}}')
        self.assertEqual(res, answer)


    def test_isDepositCompleted_3(self):
        time.sleep(1)
        client = OneXAPI.Upbit.Spot('{"accessKey":"' + UPBIT_ACCESS_KEY + '", "secretKey":"' + UPBIT_SECRET_KEY + '"}')

        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"file","logLevel":"info"}}')

        nowTime = time.localtime(time.time())
        
        res = client.isDepositCompleted('{"currency":"sOl","amount":35.213843,"since":1656044045154}')
        time.sleep(1)
        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"terminal","logLevel":"off"}}')

        answer1 = 'https://api.upbit.com/v1/deposits?currency=SOL'

        if util.searchLog(nowTime, answer1) is False:
            self.fail(f'{answer1} not found')

        answer = json.loads('{"success":true,"data":{"requestedApiCount":1,"isDepositCompleted":false}}')
        self.assertEqual(res, answer)

    def test_subscribeBalance_1(self):
        client = OneXAPI.Upbit.Spot()

        res = client.subscribeBalance()
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'NOT_SUPPORTED_API')


    def test_subscribeBalance_2(self):
        client = OneXAPI.Upbit.Spot()

        res = client.subscribeBalance('')
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'NOT_SUPPORTED_API')

    def test_subscribeBalance_3(self):
        client = OneXAPI.Upbit.Spot()

        res = client.subscribeBalance('{}')
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'NOT_SUPPORTED_API')

    def test_subscribeBalance_4(self):
        client = OneXAPI.Upbit.Spot()

        res = client.subscribeBalance('Bqbqb@')
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'NOT_SUPPORTED_API')

    def test_unsubscribeBalance_1(self):
        client = OneXAPI.Upbit.Spot()

        res = client.unsubscribeBalance()
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'NOT_SUPPORTED_API')

    def test_unsubscribeBalance_2(self):
        client = OneXAPI.Upbit.Spot()

        res = client.unsubscribeBalance('')
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'NOT_SUPPORTED_API')

    def test_unsubscribeBalance_3(self):
        client = OneXAPI.Upbit.Spot()

        res = client.unsubscribeBalance('{}')
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'NOT_SUPPORTED_API')

    def test_unsubscribeBalance_4(self):
        client = OneXAPI.Upbit.Spot()

        res = client.unsubscribeBalance('Bqbqb@')
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'NOT_SUPPORTED_API')

    def test_isSubscribingBalance_1(self):
        client = OneXAPI.Upbit.Spot()

        res = client.isSubscribingBalance()
        answer = json.loads('{"success":true,"data":{"isSubscribing":false}}')

        self.assertEqual(res, answer)

    def test_isSubscribingBalance_2(self):
        client = OneXAPI.Upbit.Spot()

        res = client.isSubscribingBalance('')
        answer = json.loads('{"success":true,"data":{"isSubscribing":false}}')

        self.assertEqual(res, answer)

    def test_isSubscribingBalance_3(self):
        client = OneXAPI.Upbit.Spot()

        res = client.isSubscribingBalance('{}')
        answer = json.loads('{"success":true,"data":{"isSubscribing":false}}')

        self.assertEqual(res, answer)

    def test_isSubscribingBalance_4(self):
        client = OneXAPI.Upbit.Spot()

        res = client.isSubscribingBalance('Bqbqb@')
        answer = json.loads('{"success":true,"data":{"isSubscribing":false}}')

        self.assertEqual(res, answer)

    def test_getOrderRoundingRule_1(self):
        client = OneXAPI.Upbit.Spot()
        res = client.getOrderRoundingRule()
        answer = json.loads('{"success":true,"data":{"requestedApiCount":0,"limitBuyPrice":"round","limitBuyBaseAmount":"round","limitSellPrice":"round","limitSellBaseAmount":"round","marketBuyQuoteAmount":"round","marketSellBaseAmount":"round"}}')

        self.assertEqual(res, answer)

    def test_getOrderRoundingRule_2(self):
        client = OneXAPI.Upbit.Spot()
        res = client.getOrderRoundingRule("")
        answer = json.loads('{"success":true,"data":{"requestedApiCount":0,"limitBuyPrice":"round","limitBuyBaseAmount":"round","limitSellPrice":"round","limitSellBaseAmount":"round","marketBuyQuoteAmount":"round","marketSellBaseAmount":"round"}}')

        self.assertEqual(res, answer)

    def test_setOrderRoundingRule_1(self):
        client = OneXAPI.Upbit.Spot()

        res = client.setOrderRoundingRule('{"limitBuyBaseAmount":"wrongData"}')
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'WRONG_VALUE')

    def test_setOrderRoundingRule_2(self):
        client = OneXAPI.Upbit.Spot()

        answer_ceil = json.loads('{"success":true,"data":{"requestedApiCount":0,"limitBuyPrice":"ceil","limitBuyBaseAmount":"ceil","limitSellPrice":"ceil","limitSellBaseAmount":"ceil","marketBuyQuoteAmount":"ceil","marketSellBaseAmount":"ceil"}}')
        answer_floor = json.loads('{"success":true,"data":{"requestedApiCount":0,"limitBuyPrice":"floor","limitBuyBaseAmount":"floor","limitSellPrice":"floor","limitSellBaseAmount":"floor","marketBuyQuoteAmount":"floor","marketSellBaseAmount":"floor"}}')
        answer_round = json.loads('{"success":true,"data":{"requestedApiCount":0,"limitBuyPrice":"round","limitBuyBaseAmount":"round","limitSellPrice":"round","limitSellBaseAmount":"round","marketBuyQuoteAmount":"round","marketSellBaseAmount":"round"}}')

        keyList = ['limitBuyPrice', 'limitBuyBaseAmount', 'limitSellPrice', 'limitSellBaseAmount', 'marketBuyQuoteAmount', 'marketSellBaseAmount']
        valueList = ['ceil', 'floor', 'round']
        
        self.maxDiff = None

        for value in valueList:
            for key in keyList:
                input = '{"' + key + '":"' + value + '"}'
                client.setOrderRoundingRule(input)
            res = client.getOrderRoundingRule()
            if(value == 'ceil'):
                self.assertEqual(res, answer_ceil)
            elif(value == 'floor'):
                self.assertEqual(res, answer_floor)
            elif(value == 'round'):
                self.assertEqual(res, answer_round)

    def test_orderLimitBuy_1(self):
        client = OneXAPI.Upbit.Spot()
        
        res = client.orderLimitBuy('{}')
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_orderLimitBuy_2(self):
        time.sleep(1)
        client = OneXAPI.Upbit.Spot('{"accessKey":"' + UPBIT_ACCESS_KEY + '", "secretKey":"' + UPBIT_SECRET_KEY + '"}')

        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"file","logLevel":"info"}}')

        nowTime = time.localtime(time.time())
        
        client.orderLimitBuy('{"baseCurrency":"bTC","quoteCurrency":"KRw","price":13501545.1234358,"baseAmount":35.135689342158}')
        time.sleep(1)
        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"terminal","logLevel":"off"}}')

        answer1 = 'https://api.upbit.com/v1/orders?market=KRW-BTC&side=bid&volume=35.13568934&price=13502000&ord_type=limit'

        if util.searchLog(nowTime, answer1) is False:
            self.fail(f'{answer1} not found')

    def test_orderLimitBuy_3(self):
        time.sleep(1)
        client = OneXAPI.Upbit.Spot('{"accessKey":"' + UPBIT_ACCESS_KEY + '", "secretKey":"' + UPBIT_SECRET_KEY + '"}')

        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"file","logLevel":"info"}}')

        nowTime = time.localtime(time.time())
        
        client.orderLimitBuy('{"baseCurrency":"bTC","quoteCurrency":"KRw","price":13501545.1234358,"baseAmount":35.135689342158,"clientOrderId":"testId","amplifier":1.0346}')
        time.sleep(1)
        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"terminal","logLevel":"off"}}')

        answer1 = 'https://api.upbit.com/v1/orders?market=KRW-BTC&side=bid&volume=35.13568934&price=13969000&ord_type=limit&identifier=testId'

        if util.searchLog(nowTime, answer1) is False:
            self.fail(f'{answer1} not found')

    def test_orderLimitSell_1(self):
        client = OneXAPI.Upbit.Spot()
        
        res = client.orderLimitSell('{}')
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_orderLimitSell_2(self):
        time.sleep(1)
        client = OneXAPI.Upbit.Spot('{"accessKey":"' + UPBIT_ACCESS_KEY + '", "secretKey":"' + UPBIT_SECRET_KEY + '"}')

        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"file","logLevel":"info"}}')

        nowTime = time.localtime(time.time())
        
        client.orderLimitSell('{"baseCurrency":"bTC","quoteCurrency":"KRw","price":13501545.1234358,"baseAmount":35.135689342158}')
        time.sleep(1)
        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"terminal","logLevel":"off"}}')

        answer1 = 'https://api.upbit.com/v1/orders?market=KRW-BTC&side=ask&volume=35.13568934&price=13502000&ord_type=limit'

        if util.searchLog(nowTime, answer1) is False:
            self.fail(f'{answer1} not found')

    def test_orderLimitSell_3(self):
        time.sleep(1)
        client = OneXAPI.Upbit.Spot('{"accessKey":"' + UPBIT_ACCESS_KEY + '", "secretKey":"' + UPBIT_SECRET_KEY + '"}')

        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"file","logLevel":"info"}}')

        nowTime = time.localtime(time.time())
        
        client.orderLimitSell('{"baseCurrency":"bTC","quoteCurrency":"KRw","price":13501545.1234358,"baseAmount":35.135689342158,"clientOrderId":"testId","amplifier":0.96348}')
        time.sleep(1)
        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"terminal","logLevel":"off"}}')

        answer1 = 'https://api.upbit.com/v1/orders?market=KRW-BTC&side=ask&volume=35.13568934&price=13008000&ord_type=limit&identifier=testId'

        if util.searchLog(nowTime, answer1) is False:
            self.fail(f'{answer1} not found')

    def test_orderMarketBuy_1(self):
        client = OneXAPI.Upbit.Spot()
        
        res = client.orderMarketBuy('{}')
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_orderMarketBuy_2(self):
        time.sleep(1)
        client = OneXAPI.Upbit.Spot('{"accessKey":"' + UPBIT_ACCESS_KEY + '", "secretKey":"' + UPBIT_SECRET_KEY + '"}')

        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"file","logLevel":"info"}}')

        nowTime = time.localtime(time.time())
        
        client.orderMarketBuy('{"baseCurrency":"bTC","quoteCurrency":"KRw","quoteAmount":38951381.391351334}')
        time.sleep(1)
        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"terminal","logLevel":"off"}}')

        answer1 = 'https://api.upbit.com/v1/orders?market=KRW-BTC&side=bid&price=38951381&ord_type=price'

        if util.searchLog(nowTime, answer1) is False:
            self.fail(f'{answer1} not found')

    def test_orderMarketBuy_3(self):
        time.sleep(1)
        client = OneXAPI.Upbit.Spot('{"accessKey":"' + UPBIT_ACCESS_KEY + '", "secretKey":"' + UPBIT_SECRET_KEY + '"}')

        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"file","logLevel":"info"}}')

        nowTime = time.localtime(time.time())
        
        client.orderMarketBuy('{"baseCurrency":"bTC","quoteCurrency":"KRw","quoteAmount":38951381.391351334,"clientOrderId":"testId"}')
        time.sleep(1)
        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"terminal","logLevel":"off"}}')

        answer1 = 'https://api.upbit.com/v1/orders?market=KRW-BTC&side=bid&price=38951381&ord_type=price&identifier=testId'

        if util.searchLog(nowTime, answer1) is False:
            self.fail(f'{answer1} not found')

    def test_orderMarketSell_1(self):
        client = OneXAPI.Upbit.Spot()
        
        res = client.orderMarketSell('{}')
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_orderMarketSell_2(self):
        time.sleep(1)
        client = OneXAPI.Upbit.Spot('{"accessKey":"' + UPBIT_ACCESS_KEY + '", "secretKey":"' + UPBIT_SECRET_KEY + '"}')

        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"file","logLevel":"info"}}')

        nowTime = time.localtime(time.time())
        
        client.orderMarketSell('{"baseCurrency":"bTC","quoteCurrency":"KRw","baseAmount":83.1338494835}')
        time.sleep(1)
        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"terminal","logLevel":"off"}}')

        answer1 = 'https://api.upbit.com/v1/orders?market=KRW-BTC&side=ask&volume=83.13384948&ord_type=market'

        if util.searchLog(nowTime, answer1) is False:
            self.fail(f'{answer1} not found')

    def test_orderMarketSell_3(self):
        time.sleep(1)
        client = OneXAPI.Upbit.Spot('{"accessKey":"' + UPBIT_ACCESS_KEY + '", "secretKey":"' + UPBIT_SECRET_KEY + '"}')

        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"file","logLevel":"info"}}')

        nowTime = time.localtime(time.time())
        
        client.orderMarketSell('{"baseCurrency":"bTC","quoteCurrency":"KRw","baseAmount":83.1338494835,"clientOrderId":"testId"}')
        time.sleep(1)
        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"terminal","logLevel":"off"}}')

        answer1 = 'https://api.upbit.com/v1/orders?market=KRW-BTC&side=ask&volume=83.13384948&ord_type=market&identifier=testId'

        if util.searchLog(nowTime, answer1) is False:
            self.fail(f'{answer1} not found')

    def test_orderCancel_1(self):
        client = OneXAPI.Upbit.Spot()
        
        res = client.orderCancel('{}')
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_orderCancel_2(self):
        time.sleep(1)
        client = OneXAPI.Upbit.Spot('{"accessKey":"' + UPBIT_ACCESS_KEY + '", "secretKey":"' + UPBIT_SECRET_KEY + '"}')

        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"file","logLevel":"info"}}')

        nowTime = time.localtime(time.time())
        
        client.orderCancel('{"orderId":"testOrderId"}')
        time.sleep(1)
        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"terminal","logLevel":"off"}}')

        answer1 = 'https://api.upbit.com/v1/order?uuid=testOrderId'

        if util.searchLog(nowTime, answer1) is False:
            self.fail(f'{answer1} not found')

    def test_orderCancel_3(self):
        time.sleep(1)
        client = OneXAPI.Upbit.Spot('{"accessKey":"' + UPBIT_ACCESS_KEY + '", "secretKey":"' + UPBIT_SECRET_KEY + '"}')

        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"file","logLevel":"info"}}')

        nowTime = time.localtime(time.time())
        
        client.orderCancel('{"clientOrderId":"testClientOrderId"}')
        time.sleep(1)
        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"terminal","logLevel":"off"}}')

        answer1 = 'https://api.upbit.com/v1/order?identifier=testClientOrderId'

        if util.searchLog(nowTime, answer1) is False:
            self.fail(f'{answer1} not found')

    def test_fetchTradingFee_1(self):
        client = OneXAPI.Upbit.Spot()
        
        res = client.fetchTradingFee('{"baseCurrency":"bTC"}')
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_fetchTradingFee_2(self):
        time.sleep(1)
        client = OneXAPI.Upbit.Spot('{"accessKey":"' + UPBIT_ACCESS_KEY + '", "secretKey":"' + UPBIT_SECRET_KEY + '"}')
        
        res = client.fetchTradingFee('{"baseCurrency":"bTC","quoteCurrency":"KRw"}')
        answer = json.loads('{"success":true,"data":{"requestedApiCount":1,"fees":[{"baseCurrency":"BTC","quoteCurrency":"KRW","symbol":"KRW-BTC","makerFee":"0.0005","takerFee":"0.0005"}]}}')
        self.assertEqual(res, answer)

    def test_fetchOrderInfo_1(self):
        client = OneXAPI.Upbit.Spot()
        
        res = client.fetchOrderInfo('{}')
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_fetchOrderInfo_2(self):
        time.sleep(1)
        client = OneXAPI.Upbit.Spot('{"accessKey":"' + UPBIT_ACCESS_KEY + '", "secretKey":"' + UPBIT_SECRET_KEY + '"}')

        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"file","logLevel":"info"}}')

        nowTime = time.localtime(time.time())
        
        client.fetchOrderInfo('{"orderId":"testOrderId"}')
        time.sleep(1)
        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"terminal","logLevel":"off"}}')

        answer1 = 'https://api.upbit.com/v1/order?uuid=testOrderId'

        if util.searchLog(nowTime, answer1) is False:
            self.fail(f'{answer1} not found')

    def test_fetchOrderInfo_3(self):
        time.sleep(1)
        client = OneXAPI.Upbit.Spot('{"accessKey":"' + UPBIT_ACCESS_KEY + '", "secretKey":"' + UPBIT_SECRET_KEY + '"}')

        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"file","logLevel":"info"}}')

        nowTime = time.localtime(time.time())
        
        client.fetchOrderInfo('{"clientOrderId":"testClientOrderId"}')
        time.sleep(1)
        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"terminal","logLevel":"off"}}')

        answer1 = 'https://api.upbit.com/v1/order?identifier=testClientOrderId'

        if util.searchLog(nowTime, answer1) is False:
            self.fail(f'{answer1} not found')

    def test_fetchOrderInfo_4(self):
        self.skipTest("Not Defined")

    def test_fetchOpenOrders_1(self):
        self.skipTest("Not Defined")

    def test_fetchOpenOrders_2(self):
        self.skipTest("Not Defined")

    def test_getCandleIntervalCandidates(self):
        self.skipTest("Not Defined")

    def test_fetchMarkets(self):
        self.skipTest("Not Defined")

    def test_fetchTicker(self):
        self.skipTest("Not Defined")

    def test_fetchOrderbook(self):
        self.skipTest("Not Defined")

    def test_fetchCandleHistory(self):
        self.skipTest("Not Defined")

    def test_subscribeBalance(self):
        self.skipTest("Not Defined")

    def test_unsubscribeBalance(self):
        self.skipTest("Not Defined")

    def test_isSubscribingBalance(self):
        self.skipTest("Not Defined")

    def test_getSubscribingTickers(self):
        self.skipTest("Not Defined")

    def test_getSubscribingOrderbooks(self):
        self.skipTest("Not Defined")

    def test_subscribeTicker(self):
        self.skipTest("Not Defined")

    def test_unsubscribeTicker(self):
        self.skipTest("Not Defined")

    def test_subscribeOrderbook(self):
        self.skipTest("Not Defined")

    def test_unsubscribeOrderbook(self):
        self.skipTest("Not Defined")


if __name__ == "__main__":
    import os
    filepath = './OneXAPI_Logs/OneXAPI_' + time.strftime('%Y-%m-%d', time.localtime(time.time())) + '.log'
    
    if os.path.exists(filepath):
        os.remove(filepath)

    unittest.main()