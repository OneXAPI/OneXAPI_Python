import unittest
import sys, os, time
from datetime import datetime, timedelta
import json
import util
from exchangeKeys import UPBIT_ACCESS_KEY, UPBIT_SECRET_KEY

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))))
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

    def test_setWithdrawRoundingRule_2(self):
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
            self.assertEqual(type(currency), type(""))
            self.assertEqual(json.dumps(chainsDict), '{"chains": []}')

    def test_fetchAllCurrencies_2(self):
        time.sleep(1)
        client = OneXAPI.Upbit.Spot('{"accessKey":"' + UPBIT_ACCESS_KEY + '", "secretKey":"' + UPBIT_SECRET_KEY + '"}')

        res = client.fetchAllCurrencies("")
        self.assertEqual(res['success'], True)
        self.assertEqual(res['data']['requestedApiCount'], 1)
        self.assertNotEqual(len(res['data']['currencies']), 0)

        for currency, chainsDict in res['data']['currencies'].items():
            self.assertEqual(type(currency), type(""))
            self.assertEqual(json.dumps(chainsDict), '{"chains": []}')

    def test_fetchBalance_1(self):
        time.sleep(1)
        client = OneXAPI.Upbit.Spot('{"accessKey":"' + UPBIT_ACCESS_KEY + '", "secretKey":"' + UPBIT_SECRET_KEY + '"}')
        
        res = client.fetchBalance('{"currencies":[]}')
        self.assertEqual(res['success'], True)
        self.assertEqual(res['data']['requestedApiCount'], 1)
        self.assertEqual(res['data']['fetchType'], "rest")
        
        for currency, balance in res['data']['balance'].items():
            self.assertEqual(type(currency), type(""))
            self.assertEqual(type(balance["free"]), type(""))
            self.assertEqual(type(balance["locked"]), type(""))

    def test_fetchBalance_2(self):
        time.sleep(1)
        client = OneXAPI.Upbit.Spot('{"accessKey":"' + UPBIT_ACCESS_KEY + '", "secretKey":"' + UPBIT_SECRET_KEY + '"}')
        
        res = client.fetchBalance('{"currencies":["bTc","xRP","Eth"], "zeroBalance": true}')
        self.assertEqual(res['success'], True)
        self.assertEqual(res['data']['requestedApiCount'], 2)
        self.assertEqual(res['data']['fetchType'], "rest")
        self.assertEqual(len(res['data']['balance']), 3)
        
        for currency, balance in res['data']['balance'].items():
            self.assertEqual(type(currency), type(""))
            self.assertEqual(type(balance["free"]), type(""))
            self.assertEqual(type(balance["locked"]), type(""))

    def test_fetchWalletStatus_1(self):
        time.sleep(1)
        client = OneXAPI.Upbit.Spot('{"accessKey":"' + UPBIT_ACCESS_KEY + '", "secretKey":"' + UPBIT_SECRET_KEY + '"}')
        
        res = client.fetchWalletStatus('{}')
        self.assertEqual(res['success'], True)
        self.assertEqual(res['data']['requestedApiCount'], 1)
        self.assertNotEqual(len(res['data']['currencies']), 0)

        for currency, wallet in res['data']['currencies'].items():
            self.assertEqual(type(currency), type(""))
            self.assertEqual(type(wallet["chains"]), type([]))
            self.assertEqual(len(wallet["chains"]), 1)
            self.assertEqual(wallet["chains"][0]["chain"], "")
            self.assertEqual(type(wallet["chains"][0]["withdrawEnable"]), type(True))
            self.assertEqual(type(wallet["chains"][0]["depositEnable"]), type(True))

    def test_fetchWalletStatus_2(self):
        time.sleep(1)
        client = OneXAPI.Upbit.Spot('{"accessKey":"' + UPBIT_ACCESS_KEY + '", "secretKey":"' + UPBIT_SECRET_KEY + '"}')
        
        res = client.fetchWalletStatus('{"currency":"bTc"}')
        self.assertEqual(res['success'], True)
        self.assertEqual(res['data']['requestedApiCount'], 1)
        self.assertEqual(len(res['data']['currencies']), 1)

        for currency, wallet in res['data']['currencies'].items():
            self.assertEqual(type(currency), type(""))
            self.assertEqual(type(wallet["chains"]), type([]))
            self.assertEqual(len(wallet["chains"]), 1)
            self.assertEqual(wallet["chains"][0]["chain"], "")
            self.assertEqual(type(wallet["chains"][0]["withdrawEnable"]), type(True))
            self.assertEqual(type(wallet["chains"][0]["depositEnable"]), type(True))

    def test_fetchWithdrawHistory_1(self):
        time.sleep(1)
        client = OneXAPI.Upbit.Spot('{"accessKey":"' + UPBIT_ACCESS_KEY + '", "secretKey":"' + UPBIT_SECRET_KEY + '"}')
        
        res = client.fetchWithdrawHistory('{}')
        self.assertEqual(res['success'], True)
        self.assertEqual(res['data']['requestedApiCount'], 1)

        for withdrawHistory in res['data']['withdrawals']:
            self.assertEqual(type(withdrawHistory["currency"]), type(""))
            self.assertEqual(type(withdrawHistory["amount"]), type(""))
            self.assertEqual(type(withdrawHistory["fee"]), type(""))
            self.assertEqual(type(withdrawHistory["orderId"]), type(""))
            self.assertEqual(type(withdrawHistory["txid"]), type(""))
            self.assertEqual(type(withdrawHistory["status"]), type(""))
            self.assertEqual(type(withdrawHistory["created"]), type(1))

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
            self.assertEqual(type(deposit["currency"]), type(""))
            self.assertEqual(type(deposit["amount"]), type(""))
            self.assertEqual(type(deposit["fee"]), type(""))
            self.assertEqual(type(deposit["orderId"]), type(""))
            self.assertEqual(type(deposit["txid"]), type(""))
            self.assertEqual(type(deposit["status"]), type(""))
            self.assertEqual(type(deposit["created"]), type(1))

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
            self.assertEqual(type(currency), type(""))
            self.assertEqual(type(depositDict), type([]))
            self.assertEqual(len(depositDict), 1)
            self.assertEqual(depositDict[0]["chain"], "")
            self.assertEqual(type(depositDict[0]["address"]), type(""))
            self.assertEqual(type(depositDict[0]["tag"]), type(""))
    
    def test_fetchDepositAddress_2(self):
        time.sleep(1)
        client = OneXAPI.Upbit.Spot('{"accessKey":"' + UPBIT_ACCESS_KEY + '", "secretKey":"' + UPBIT_SECRET_KEY + '"}')
        
        res = client.fetchDepositAddress('{"currency":"Btc"}')
        self.assertEqual(res['success'], True)
        self.assertEqual(res['data']['requestedApiCount'], 1)
        self.assertEqual(len(res['data']['addresses']), 1)

        for currency, depositDict in res['data']['addresses'].items():
            self.assertEqual(type(currency), type(""))
            self.assertEqual(type(depositDict), type([]))
            self.assertEqual(len(depositDict), 1)
            self.assertEqual(depositDict[0]["chain"], "")
            self.assertEqual(type(depositDict[0]["address"]), type(""))
            self.assertEqual(type(depositDict[0]["tag"]), type(""))

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
        time.sleep(1)
        client = OneXAPI.Upbit.Spot('{"accessKey":"' + UPBIT_ACCESS_KEY + '", "secretKey":"' + UPBIT_SECRET_KEY + '"}')

        res = client.fetchOrderbook('{"baseCurrency": "XrP", "quoteCurrency": "KrW"}')
        bidPrice = float(res['data']['bids'][0]['price'])

        res = client.orderLimitBuy('{"baseCurrency": "xRp", "quoteCurrency": "kRw", "price": ' + str(bidPrice) + ', "baseAmount": 25, "amplifier": 0.96}')
        orderId = res['data']['orderId']

        res = client.fetchOrderInfo('{"baseCurrency": "xRp", "quoteCurrency": "KrW", "orderId": "' + orderId + '"}')
        client.orderCancel('{"baseCurrency": "xRp", "quoteCurrency": "KrW", "orderId": "' + orderId + '"}')

        self.assertEqual(res['success'], True)
        self.assertEqual(res['data']['requestedApiCount'], 1)
        self.assertEqual(type(res['data']['baseCurrency']), type(''))
        self.assertEqual(type(res['data']['quoteCurrency']), type(''))
        self.assertEqual(type(res['data']['symbol']), type(''))
        self.assertEqual(type(res['data']['orderId']), type(''))
        self.assertEqual(res['data']['orderId'], orderId)
        if res['data']['side'] not in ['buy', 'sell']:
            self.fail('side is wrong')
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
        client = OneXAPI.Upbit.Spot('{"accessKey":"' + UPBIT_ACCESS_KEY + '", "secretKey":"' + UPBIT_SECRET_KEY + '"}')

        res = client.fetchOrderbook('{"baseCurrency": "XrP", "quoteCurrency": "KrW"}')
        bidPrice = float(res['data']['bids'][0]['price'])

        res = client.orderLimitBuy('{"baseCurrency": "xRp", "quoteCurrency": "kRw", "price": ' + str(bidPrice) + ', "baseAmount": 25, "amplifier": 0.96}')
        orderId = res['data']['orderId']

        res = client.fetchOpenOrders('{}')
        client.orderCancel('{"baseCurrency": "xRp", "quoteCurrency": "KrW", "orderId": "' + orderId + '"}')

        self.assertEqual(res['success'], True)
        self.assertEqual(res['data']['requestedApiCount'], 1)
        for openOrder in res['data']['openOrders']:
            self.assertEqual(type(openOrder['baseCurrency']), type(''))
            self.assertEqual(type(openOrder['quoteCurrency']), type(''))
            self.assertEqual(type(openOrder['symbol']), type(''))
            self.assertEqual(type(openOrder['orderId']), type(''))
            self.assertEqual(type(openOrder['side']), type(''))
            self.assertEqual(type(openOrder['originalAmount']), type(''))
            self.assertEqual(type(openOrder['filledAmount']), type(''))
            self.assertEqual(type(openOrder['remainingAmount']), type(''))
            self.assertEqual(type(openOrder['originalPrice']), type(''))
            self.assertEqual(type(openOrder['created']), type(1))
            self.assertEqual(type(openOrder['lockedCurrency']), type(''))
            self.assertEqual(type(openOrder['lockedAmount']), type(''))

    def test_fetchOpenOrders_2(self):
        time.sleep(1)
        client = OneXAPI.Upbit.Spot('{"accessKey":"' + UPBIT_ACCESS_KEY + '", "secretKey":"' + UPBIT_SECRET_KEY + '"}')

        res = client.fetchOrderbook('{"baseCurrency": "XrP", "quoteCurrency": "KrW"}')
        bidPrice = float(res['data']['bids'][0]['price'])

        res = client.orderLimitBuy('{"baseCurrency": "xRp", "quoteCurrency": "kRw", "price": ' + str(bidPrice) + ', "baseAmount": 25, "amplifier": 0.96}')
        orderId = res['data']['orderId']

        res = client.fetchOpenOrders('{"baseCurrency": "xRp", "quoteCurrency": "KrW", "side": "buy"}')
        client.orderCancel('{"baseCurrency": "xRp", "quoteCurrency": "KrW", "orderId": "' + orderId + '"}')

        self.assertEqual(res['success'], True)
        self.assertEqual(res['data']['requestedApiCount'], 1)
        for openOrder in res['data']['openOrders']:
            self.assertEqual(type(openOrder['baseCurrency']), type(''))
            self.assertEqual(type(openOrder['quoteCurrency']), type(''))
            self.assertEqual(type(openOrder['symbol']), type(''))
            self.assertEqual(type(openOrder['orderId']), type(''))
            self.assertEqual(type(openOrder['side']), type(''))
            self.assertEqual(type(openOrder['originalAmount']), type(''))
            self.assertEqual(type(openOrder['filledAmount']), type(''))
            self.assertEqual(type(openOrder['remainingAmount']), type(''))
            self.assertEqual(type(openOrder['originalPrice']), type(''))
            self.assertEqual(type(openOrder['created']), type(1))
            self.assertEqual(type(openOrder['lockedCurrency']), type(''))
            self.assertEqual(type(openOrder['lockedAmount']), type(''))

    def test_getCandleIntervalCandidates_1(self):
        client = OneXAPI.Upbit.Spot()

        res = client.getCandleIntervalCandidates()
        answer = json.loads('{"success":true,"data":{"requestedApiCount":0,"intervals":["10min","15min","1day","1hour","1min","1month","1week","30min","3min","4hour","5min"]}}')

        self.assertEqual(res, answer)

    def test_getCandleIntervalCandidates_2(self):
        client = OneXAPI.Upbit.Spot()

        res = client.getCandleIntervalCandidates('')
        answer = json.loads('{"success":true,"data":{"requestedApiCount":0,"intervals":["10min","15min","1day","1hour","1min","1month","1week","30min","3min","4hour","5min"]}}')

        self.assertEqual(res, answer)

    def test_fetchMarkets_1(self):
        time.sleep(1)
        client = OneXAPI.Upbit.Spot('{"accessKey":"' + UPBIT_ACCESS_KEY + '", "secretKey":"' + UPBIT_SECRET_KEY + '"}')

        res = client.fetchMarkets('{}')
        
        self.assertEqual(res['success'], True)
        self.assertEqual(res['data']['requestedApiCount'], 1)
        for market in res['data']['markets']:
            self.assertEqual(type(market['baseCurrency']), type(''))
            self.assertEqual(type(market['quoteCurrency']), type(''))
            self.assertEqual(type(market['symbol']), type(''))

    def test_fetchMarkets_2(self):
        time.sleep(1)
        client = OneXAPI.Upbit.Spot('{"accessKey":"' + UPBIT_ACCESS_KEY + '", "secretKey":"' + UPBIT_SECRET_KEY + '"}')

        res = client.fetchMarkets('{"baseCurrency":"bTC","quoteCurrency":"KrW"}')
        
        self.assertEqual(res['success'], True)
        self.assertEqual(res['data']['requestedApiCount'], 1)
        self.assertEqual(len(res['data']['markets']), 1)
        for market in res['data']['markets']:
            self.assertEqual(type(market['baseCurrency']), type(''))
            self.assertEqual(type(market['quoteCurrency']), type(''))
            self.assertEqual(type(market['symbol']), type(''))

    def test_fetchTicker_1(self):
        time.sleep(1)
        client = OneXAPI.Upbit.Spot('{"accessKey":"' + UPBIT_ACCESS_KEY + '", "secretKey":"' + UPBIT_SECRET_KEY + '"}')

        res = client.fetchTicker('{}')

        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_fetchTicker_2(self):
        time.sleep(1)
        client = OneXAPI.Upbit.Spot('{"accessKey":"' + UPBIT_ACCESS_KEY + '", "secretKey":"' + UPBIT_SECRET_KEY + '"}')

        res = client.fetchTicker('{"baseCurrency":"bTc","quoteCurrency":"kRw"}')

        self.assertEqual(res['success'], True)
        self.assertEqual(res['data']['requestedApiCount'], 1)
        self.assertEqual(res['data']['baseCurrency'], 'BTC')
        self.assertEqual(res['data']['quoteCurrency'], 'KRW')
        self.assertEqual(res['data']['symbol'], 'KRW-BTC')
        self.assertEqual(res['data']['fetchType'], 'rest')
        self.assertEqual(type(res['data']['openTime']), type(1234))
        self.assertEqual(type(res['data']['openPrice']), type(''))
        self.assertEqual(type(res['data']['closePrice']), type(''))
        self.assertEqual(type(res['data']['lowPrice']), type(''))
        self.assertEqual(type(res['data']['highPrice']), type(''))
        self.assertEqual(type(res['data']['baseVolume']), type(''))
        self.assertEqual(type(res['data']['quoteVolume']), type(''))

    def test_fetchTicker_3(self):
        time.sleep(1)
        client = OneXAPI.Upbit.Spot('{"accessKey":"' + UPBIT_ACCESS_KEY + '", "secretKey":"' + UPBIT_SECRET_KEY + '"}')

        client.subscribeTicker('{"market":[{"baseCurrency":"BTC","quoteCurrency":"KRW"}]}')
        res = client.fetchTicker('{"baseCurrency":"bTc","quoteCurrency":"kRw"}')

        self.assertEqual(res['success'], True)
        self.assertEqual(res['data']['requestedApiCount'], 0)
        self.assertEqual(res['data']['baseCurrency'], 'BTC')
        self.assertEqual(res['data']['quoteCurrency'], 'KRW')
        self.assertEqual(res['data']['symbol'], 'KRW-BTC')
        self.assertEqual(res['data']['fetchType'], 'websocket')
        self.assertEqual(type(res['data']['openTime']), type(1234))
        self.assertEqual(type(res['data']['openPrice']), type(''))
        self.assertEqual(type(res['data']['closePrice']), type(''))
        self.assertEqual(type(res['data']['lowPrice']), type(''))
        self.assertEqual(type(res['data']['highPrice']), type(''))
        self.assertEqual(type(res['data']['baseVolume']), type(''))
        self.assertEqual(type(res['data']['quoteVolume']), type(''))

    def test_fetchTicker_4(self):
        time.sleep(1)
        client = OneXAPI.Upbit.Spot('{"accessKey":"' + UPBIT_ACCESS_KEY + '", "secretKey":"' + UPBIT_SECRET_KEY + '"}')

        client.subscribeTicker('{"market":[{"baseCurrency":"BTC","quoteCurrency":"KRW"}]}')
        res = client.fetchTicker('{"baseCurrency":"bTc","quoteCurrency":"kRw","forceRestApi":true}')

        self.assertEqual(res['success'], True)
        self.assertEqual(res['data']['requestedApiCount'], 1)
        self.assertEqual(res['data']['baseCurrency'], 'BTC')
        self.assertEqual(res['data']['quoteCurrency'], 'KRW')
        self.assertEqual(res['data']['symbol'], 'KRW-BTC')
        self.assertEqual(res['data']['fetchType'], 'rest')
        self.assertEqual(type(res['data']['openTime']), type(1234))
        self.assertEqual(type(res['data']['openPrice']), type(''))
        self.assertEqual(type(res['data']['closePrice']), type(''))
        self.assertEqual(type(res['data']['lowPrice']), type(''))
        self.assertEqual(type(res['data']['highPrice']), type(''))
        self.assertEqual(type(res['data']['baseVolume']), type(''))
        self.assertEqual(type(res['data']['quoteVolume']), type(''))

    def test_fetchOrderbook_1(self):
        time.sleep(1)
        client = OneXAPI.Upbit.Spot('{"accessKey":"' + UPBIT_ACCESS_KEY + '", "secretKey":"' + UPBIT_SECRET_KEY + '"}')

        res = client.fetchOrderbook('{}')

        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_fetchOrderbook_2(self):
        time.sleep(1)
        client = OneXAPI.Upbit.Spot('{"accessKey":"' + UPBIT_ACCESS_KEY + '", "secretKey":"' + UPBIT_SECRET_KEY + '"}')

        res = client.fetchOrderbook('{"baseCurrency":"bTc","quoteCurrency":"kRw"}')

        self.assertEqual(res['success'], True)
        self.assertEqual(res['data']['requestedApiCount'], 1)
        self.assertEqual(res['data']['baseCurrency'], 'BTC')
        self.assertEqual(res['data']['quoteCurrency'], 'KRW')
        self.assertEqual(res['data']['symbol'], 'KRW-BTC')
        self.assertEqual(res['data']['fetchType'], 'rest')
        self.assertEqual(type(res['data']['timestamp']), type(1234))
        
        for bid in res['data']['bids']:
            self.assertEqual(type(bid['price']), type(''))
            self.assertEqual(type(bid['size']), type(''))
        
        for ask in res['data']['asks']:
            self.assertEqual(type(ask['price']), type(''))
            self.assertEqual(type(ask['size']), type(''))

    def test_fetchOrderbook_3(self):
        time.sleep(1)
        client = OneXAPI.Upbit.Spot('{"accessKey":"' + UPBIT_ACCESS_KEY + '", "secretKey":"' + UPBIT_SECRET_KEY + '"}')

        client.subscribeOrderbook('{"market":[{"baseCurrency":"BTC","quoteCurrency":"KRW"}]}')
        res = client.fetchOrderbook('{"baseCurrency":"bTc","quoteCurrency":"kRw"}')

        self.assertEqual(res['success'], True)
        self.assertEqual(res['data']['requestedApiCount'], 0)
        self.assertEqual(res['data']['baseCurrency'], 'BTC')
        self.assertEqual(res['data']['quoteCurrency'], 'KRW')
        self.assertEqual(res['data']['symbol'], 'KRW-BTC')
        self.assertEqual(res['data']['fetchType'], 'websocket')
        self.assertEqual(type(res['data']['timestamp']), type(1234))
        
        for bid in res['data']['bids']:
            self.assertEqual(type(bid['price']), type(''))
            self.assertEqual(type(bid['size']), type(''))
        
        for ask in res['data']['asks']:
            self.assertEqual(type(ask['price']), type(''))
            self.assertEqual(type(ask['size']), type(''))

    def test_fetchOrderbook_4(self):
        time.sleep(1)
        client = OneXAPI.Upbit.Spot('{"accessKey":"' + UPBIT_ACCESS_KEY + '", "secretKey":"' + UPBIT_SECRET_KEY + '"}')

        client.subscribeOrderbook('{"market":[{"baseCurrency":"BTC","quoteCurrency":"KRW"}]}')
        res = client.fetchOrderbook('{"baseCurrency":"bTc","quoteCurrency":"kRw","forceRestApi":true}')

        self.assertEqual(res['success'], True)
        self.assertEqual(res['data']['requestedApiCount'], 1)
        self.assertEqual(res['data']['baseCurrency'], 'BTC')
        self.assertEqual(res['data']['quoteCurrency'], 'KRW')
        self.assertEqual(res['data']['symbol'], 'KRW-BTC')
        self.assertEqual(res['data']['fetchType'], 'rest')
        self.assertEqual(type(res['data']['timestamp']), type(1234))
        
        for bid in res['data']['bids']:
            self.assertEqual(type(bid['price']), type(''))
            self.assertEqual(type(bid['size']), type(''))
        
        for ask in res['data']['asks']:
            self.assertEqual(type(ask['price']), type(''))
            self.assertEqual(type(ask['size']), type(''))

    def test_fetchCandleHistory_1(self):
        time.sleep(1)
        client = OneXAPI.Upbit.Spot('{"accessKey":"' + UPBIT_ACCESS_KEY + '", "secretKey":"' + UPBIT_SECRET_KEY + '"}')

        res = client.fetchCandleHistory('{"baseCurrency":"bTc","quoteCurrency":"kRw"}')

        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_fetchCandleHistory_2(self):
        time.sleep(1)
        client = OneXAPI.Upbit.Spot('{"accessKey":"' + UPBIT_ACCESS_KEY + '", "secretKey":"' + UPBIT_SECRET_KEY + '"}')
        
        specificTime = int((datetime.today() - timedelta(hours=2)).timestamp())
        
        res = client.fetchCandleHistory('{"baseCurrency":"bTc","quoteCurrency":"kRw","interval":"1min","startTime":' + str(specificTime) + '}')
        
        self.assertEqual(res['success'], True)
        self.assertEqual(type(res['data']['requestedApiCount']), type(1))
        self.assertEqual(type(res['data']['baseCurrency']), type(''))
        self.assertEqual(type(res['data']['quoteCurrency']), type(''))
        self.assertEqual(type(res['data']['symbol']), type(''))

        for candle in res['data']['candles']:
            self.assertEqual(type(candle['timestamp']), type(1))
            self.assertEqual(type(candle['openPrice']), type(''))
            self.assertEqual(type(candle['closePrice']), type(''))
            self.assertEqual(type(candle['highPrice']), type(''))
            self.assertEqual(type(candle['lowPrice']), type(''))
            self.assertEqual(type(candle['baseVolume']), type(''))
            self.assertEqual(type(candle['quoteVolume']), type(''))
            

    def test_fetchCandleHistory_3(self):
        time.sleep(1)
        client = OneXAPI.Upbit.Spot('{"accessKey":"' + UPBIT_ACCESS_KEY + '", "secretKey":"' + UPBIT_SECRET_KEY + '"}')
        
        res = client.fetchCandleHistory('{"baseCurrency":"bTc","quoteCurrency":"kRw","interval":"1min","startTime":1656042045,"endTime":1656063182,"fetchInterval":900}')
        
        self.assertEqual(res['success'], True)
        self.assertEqual(type(res['data']['requestedApiCount']), type(1))
        self.assertEqual(type(res['data']['baseCurrency']), type(''))
        self.assertEqual(type(res['data']['quoteCurrency']), type(''))
        self.assertEqual(type(res['data']['symbol']), type(''))

        for candle in res['data']['candles']:
            self.assertEqual(type(candle['timestamp']), type(1))
            self.assertEqual(type(candle['openPrice']), type(''))
            self.assertEqual(type(candle['closePrice']), type(''))
            self.assertEqual(type(candle['highPrice']), type(''))
            self.assertEqual(type(candle['lowPrice']), type(''))
            self.assertEqual(type(candle['baseVolume']), type(''))
            self.assertEqual(type(candle['quoteVolume']), type(''))
        
    def test_getSubscribingTickers_1(self):
        client = OneXAPI.Upbit.Spot()

        res = client.getSubscribingTickers()
        answer = json.loads('{"success":true,"data":{"tickers":[]}}')
        self.assertEqual(res, answer)

    def test_getSubscribingTickers_2(self):
        client = OneXAPI.Upbit.Spot()

        res = client.getSubscribingTickers('')
        answer = json.loads('{"success":true,"data":{"tickers":[]}}')
        self.assertEqual(res, answer)

    def test_getSubscribingTickers_3(self):
        client = OneXAPI.Upbit.Spot()

        res = client.getSubscribingTickers('{}')
        answer = json.loads('{"success":true,"data":{"tickers":[]}}')
        self.assertEqual(res, answer)

    def test_getSubscribingTickers_4(self):
        client = OneXAPI.Upbit.Spot()

        res = client.getSubscribingTickers('Bqbqb@')
        answer = json.loads('{"success":true,"data":{"tickers":[]}}')
        self.assertEqual(res, answer)

    def test_getSubscribingTickers_5(self):
        client = OneXAPI.Upbit.Spot()

        client.subscribeTicker('{"market":[{"baseCurrency":"BTC","quoteCurrency":"KRW"},{"baseCurrency":"ETH","quoteCurrency":"BTC"}]}')
        res = client.getSubscribingTickers()
        answer = json.loads('{"success":true,"data":{"tickers":[{"baseCurrency":"BTC","quoteCurrency":"KRW","symbol":"KRW-BTC"},{"baseCurrency":"ETH","quoteCurrency":"BTC","symbol":"BTC-ETH"}]}}')
        self.assertEqual(res, answer)

    def test_getSubscribingOrderbooks_1(self):
        client = OneXAPI.Upbit.Spot()

        res = client.getSubscribingOrderbooks()
        answer = json.loads('{"success":true,"data":{"orderbooks":[]}}')
        self.assertEqual(res, answer)
    
    def test_getSubscribingOrderbooks_2(self):
        client = OneXAPI.Upbit.Spot()

        res = client.getSubscribingOrderbooks('')
        answer = json.loads('{"success":true,"data":{"orderbooks":[]}}')
        self.assertEqual(res, answer)

    def test_getSubscribingOrderbooks_3(self):
        client = OneXAPI.Upbit.Spot()

        res = client.getSubscribingOrderbooks('{}')
        answer = json.loads('{"success":true,"data":{"orderbooks":[]}}')
        self.assertEqual(res, answer)

    def test_getSubscribingOrderbooks_4(self):
        client = OneXAPI.Upbit.Spot()

        res = client.getSubscribingOrderbooks('Bqbqb@')
        answer = json.loads('{"success":true,"data":{"orderbooks":[]}}')
        self.assertEqual(res, answer)

    def test_getSubscribingOrderbooks_5(self):
        client = OneXAPI.Upbit.Spot()

        client.subscribeOrderbook('{"market":[{"baseCurrency":"BTC","quoteCurrency":"KRW"},{"baseCurrency":"ETH","quoteCurrency":"BTC"}]}')
        res = client.getSubscribingOrderbooks()
        answer = json.loads('{"success":true,"data":{"orderbooks":[{"baseCurrency":"BTC","quoteCurrency":"KRW","symbol":"KRW-BTC"},{"baseCurrency":"ETH","quoteCurrency":"BTC","symbol":"BTC-ETH"}]}}')
        self.assertEqual(res, answer)

    def test_subscribeTicker_1(self):
        client = OneXAPI.Upbit.Spot()

        res = client.subscribeTicker('')
        
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'JSON_PARSING_ERROR')

    def test_subscribeTicker_2(self):
        client = OneXAPI.Upbit.Spot()

        res = client.subscribeTicker('{}')
        
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_subscribeTicker_3(self):
        client = OneXAPI.Upbit.Spot()

        res = client.subscribeTicker('Bqbqb@')
        
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'JSON_PARSING_ERROR')

    def test_subscribeTicker_4(self):
        client = OneXAPI.Upbit.Spot()

        res = client.subscribeTicker('{"market":[{"baseCurrency":"BTC","quoteCurrency":"KRW"},{"baseCurrency":"ETH","quoteCurrency":"BTC"}]}')
        answer = json.loads('{"success":true,"data":{"subscribed":[{"baseCurrency":"BTC","quoteCurrency":"KRW","symbol":"KRW-BTC"},{"baseCurrency":"ETH","quoteCurrency":"BTC","symbol":"BTC-ETH"}],"subscribeFailed":[]}}')

        self.assertEqual(res, answer)

        res = client.getSubscribingTickers()
        answer = json.loads('{"success":true,"data":{"tickers":[{"baseCurrency":"BTC","quoteCurrency":"KRW","symbol":"KRW-BTC"},{"baseCurrency":"ETH","quoteCurrency":"BTC","symbol":"BTC-ETH"}]}}')

        self.assertEqual(res, answer)

        res = client.subscribeTicker('{"market":[{"baseCurrency":"ETH","quoteCurrency":"KRW"}], "reconnect": true}')
        answer = json.loads('{"success":true,"data":{"subscribed":[{"baseCurrency":"ETH","quoteCurrency":"KRW","symbol":"KRW-ETH"}],"subscribeFailed":[]}}')

        self.assertEqual(res, answer)

        res = client.getSubscribingTickers()
        answer = json.loads('{"success":true,"data":{"tickers":[{"baseCurrency":"BTC","quoteCurrency":"KRW","symbol":"KRW-BTC"},{"baseCurrency":"ETH","quoteCurrency":"BTC","symbol":"BTC-ETH"},{"baseCurrency":"ETH","quoteCurrency":"KRW","symbol":"KRW-ETH"}]}}')

        self.assertEqual(res, answer)

    def test_unsubscribeTicker_1(self):
        client = OneXAPI.Upbit.Spot()

        res = client.unsubscribeTicker('')
        
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'JSON_PARSING_ERROR')

    def test_unsubscribeTicker_2(self):
        client = OneXAPI.Upbit.Spot()

        res = client.unsubscribeTicker('{}')
        
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_unsubscribeTicker_3(self):
        client = OneXAPI.Upbit.Spot()

        res = client.unsubscribeTicker('Bqbqb@')
        
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'JSON_PARSING_ERROR')

    def test_unsubscribeTicker_4(self):
        client = OneXAPI.Upbit.Spot()

        client.subscribeTicker('{"market":[{"baseCurrency":"BTC","quoteCurrency":"KRW"},{"baseCurrency":"ETH","quoteCurrency":"BTC"}]}')
        res = client.unsubscribeTicker('{"market":[{"baseCurrency":"BTC","quoteCurrency":"KRW"},{"baseCurrency":"ETH","quoteCurrency":"BTC"}]}')
        answer = json.loads('{"success":true,"data":{"unsubscribed":[{"baseCurrency":"BTC","quoteCurrency":"KRW","symbol":"KRW-BTC"},{"baseCurrency":"ETH","quoteCurrency":"BTC","symbol":"BTC-ETH"}],"unsubscribeFailed":[]}}')

        self.assertEqual(res, answer)

    def test_unsubscribeTicker_5(self):
        client = OneXAPI.Upbit.Spot()

        client.subscribeTicker('{"market":[{"baseCurrency":"BTC","quoteCurrency":"KRW"},{"baseCurrency":"ETH","quoteCurrency":"BTC"}]}')
        res = client.unsubscribeTicker('{"market":[{"baseCurrency":"BTC","quoteCurrency":"KRW"},{"baseCurrency":"ETH","quoteCurrency":"BTC"}],"reconnect":true}')
        answer = json.loads('{"success":true,"data":{"unsubscribed":[{"baseCurrency":"BTC","quoteCurrency":"KRW","symbol":"KRW-BTC"},{"baseCurrency":"ETH","quoteCurrency":"BTC","symbol":"BTC-ETH"}],"unsubscribeFailed":[]}}')

        self.assertEqual(res, answer)

    def test_subscribeOrderbook_1(self):
        client = OneXAPI.Upbit.Spot()

        res = client.subscribeOrderbook('')
        
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'JSON_PARSING_ERROR')

    def test_subscribeOrderbook_2(self):
        client = OneXAPI.Upbit.Spot()

        res = client.subscribeOrderbook('{}')
        
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_subscribeOrderbook_3(self):
        client = OneXAPI.Upbit.Spot()

        res = client.subscribeOrderbook('Bqbqb@')
        
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'JSON_PARSING_ERROR')

    def test_subscribeOrderbook_4(self):
        client = OneXAPI.Upbit.Spot()

        res = client.subscribeOrderbook('{"market":[{"baseCurrency":"BTC","quoteCurrency":"KRW"},{"baseCurrency":"ETH","quoteCurrency":"BTC"}]}')
        answer = json.loads('{"success":true,"data":{"subscribed":[{"baseCurrency":"BTC","quoteCurrency":"KRW","symbol":"KRW-BTC"},{"baseCurrency":"ETH","quoteCurrency":"BTC","symbol":"BTC-ETH"}],"subscribeFailed":[]}}')

        self.assertDictEqual(res, answer)

        res = client.getSubscribingOrderbooks()
        answer = json.loads('{"success":true,"data":{"orderbooks":[{"baseCurrency":"BTC","quoteCurrency":"KRW","symbol":"KRW-BTC"},{"baseCurrency":"ETH","quoteCurrency":"BTC","symbol":"BTC-ETH"}]}}')

        res = client.subscribeOrderbook('{"market":[{"baseCurrency":"ETH","quoteCurrency":"KRW"}], "reconnect": true}')
        answer = json.loads('{"success":true,"data":{"subscribed":[{"baseCurrency":"ETH","quoteCurrency":"KRW","symbol":"KRW-ETH"}],"subscribeFailed":[]}}')

        res = client.getSubscribingOrderbooks()
        answer = json.loads('{"success":true,"data":{"orderbooks":[{"baseCurrency":"BTC","quoteCurrency":"KRW","symbol":"KRW-BTC"},{"baseCurrency":"ETH","quoteCurrency":"BTC","symbol":"BTC-ETH"},{"baseCurrency":"ETH","quoteCurrency":"KRW","symbol":"BTC-ETH"}]}}')

    def test_unsubscribeOrderbook_1(self):
        client = OneXAPI.Upbit.Spot()

        res = client.unsubscribeOrderbook('')

        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'JSON_PARSING_ERROR')

    def test_unsubscribeOrderbook_2(self):
        client = OneXAPI.Upbit.Spot()

        res = client.unsubscribeOrderbook('{}')

        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_unsubscribeOrderbook_3(self):
        client = OneXAPI.Upbit.Spot()

        res = client.unsubscribeOrderbook('Bqbqb@')

        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'JSON_PARSING_ERROR')

    def test_unsubscribeOrderbook_4(self):
        client = OneXAPI.Upbit.Spot()

        client.subscribeOrderbook('{"market":[{"baseCurrency":"BTC","quoteCurrency":"KRW"},{"baseCurrency":"ETH","quoteCurrency":"BTC"}]}')
        res = client.unsubscribeOrderbook('{"market":[{"baseCurrency":"BTC","quoteCurrency":"KRW"},{"baseCurrency":"ETH","quoteCurrency":"BTC"}]}')
        answer = json.loads('{"success":true,"data":{"unsubscribed":[{"baseCurrency":"BTC","quoteCurrency":"KRW","symbol":"KRW-BTC"},{"baseCurrency":"ETH","quoteCurrency":"BTC","symbol":"BTC-ETH"}],"unsubscribeFailed":[]}}')

        self.assertDictEqual(res, answer)

    def test_unsubscribeOrderbook_5(self):
        client = OneXAPI.Upbit.Spot()

        client.subscribeOrderbook('{"market":[{"baseCurrency":"BTC","quoteCurrency":"KRW"},{"baseCurrency":"ETH","quoteCurrency":"BTC"}]}')
        res = client.unsubscribeOrderbook('{"market":[{"baseCurrency":"BTC","quoteCurrency":"KRW"},{"baseCurrency":"ETH","quoteCurrency":"BTC"}],"reconnect":true}')
        answer = json.loads('{"success":true,"data":{"unsubscribed":[{"baseCurrency":"BTC","quoteCurrency":"KRW","symbol":"KRW-BTC"},{"baseCurrency":"ETH","quoteCurrency":"BTC","symbol":"BTC-ETH"}],"unsubscribeFailed":[]}}')

        self.assertDictEqual(res, answer)

    def test_websocketFullTest(self):
        client = OneXAPI.Upbit.Spot()

        res = client.subscribeTicker('{"market":[{"baseCurrency":"BTC","quoteCurrency":"KRW"},{"baseCurrency":"ETH","quoteCurrency":"KRW"}]}')
        answer = json.loads('{"success":true,"data":{"subscribed":[{"baseCurrency":"BTC","quoteCurrency":"KRW","symbol":"KRW-BTC"},{"baseCurrency":"ETH","quoteCurrency":"KRW","symbol":"KRW-ETH"}],"subscribeFailed":[]}}')

        self.assertDictEqual(res, answer)

        res = client.getSubscribingTickers()
        answer = json.loads('{"success":true,"data":{"tickers":[{"baseCurrency":"BTC","quoteCurrency":"KRW","symbol":"KRW-BTC"},{"baseCurrency":"ETH","quoteCurrency":"KRW","symbol":"KRW-ETH"}]}}')

        self.assertDictEqual(res, answer)

        res = client.subscribeOrderbook('{"market":[{"baseCurrency":"BTC","quoteCurrency":"KRW"},{"baseCurrency":"ETH","quoteCurrency":"KRW"}],"reconnect":true}')
        answer = json.loads('{"success":true,"data":{"subscribed":[{"baseCurrency":"BTC","quoteCurrency":"KRW","symbol":"KRW-BTC"},{"baseCurrency":"ETH","quoteCurrency":"KRW","symbol":"KRW-ETH"}],"subscribeFailed":[]}}')

        self.assertDictEqual(res, answer)

        res = client.getSubscribingTickers()
        answer = json.loads('{"success":true,"data":{"tickers":[{"baseCurrency":"BTC","quoteCurrency":"KRW","symbol":"KRW-BTC"},{"baseCurrency":"ETH","quoteCurrency":"KRW","symbol":"KRW-ETH"}]}}')

        self.assertDictEqual(res, answer)

        res = client.getSubscribingOrderbooks()
        answer = json.loads('{"success":true,"data":{"orderbooks":[{"baseCurrency":"BTC","quoteCurrency":"KRW","symbol":"KRW-BTC"},{"baseCurrency":"ETH","quoteCurrency":"KRW","symbol":"KRW-ETH"}]}}')

        self.assertDictEqual(res, answer)

        res = client.unsubscribeTicker('{"market":[{"baseCurrency":"BTC","quoteCurrency":"KRW"}],"reconnect":true}')
        answer = json.loads('{"success":true,"data":{"unsubscribed":[{"baseCurrency":"BTC","quoteCurrency":"KRW","symbol":"KRW-BTC"}],"unsubscribeFailed":[]}}')

        self.assertDictEqual(res, answer)

        res = client.getSubscribingTickers()
        answer = json.loads('{"success":true,"data":{"tickers":[{"baseCurrency":"ETH","quoteCurrency":"KRW","symbol":"KRW-ETH"}]}}')

        self.assertDictEqual(res, answer)

        res = client.getSubscribingOrderbooks()
        answer = json.loads('{"success":true,"data":{"orderbooks":[{"baseCurrency":"BTC","quoteCurrency":"KRW","symbol":"KRW-BTC"},{"baseCurrency":"ETH","quoteCurrency":"KRW","symbol":"KRW-ETH"}]}}')

        self.assertDictEqual(res, answer)

        res = client.unsubscribeOrderbook('{"market":[{"baseCurrency":"ETH","quoteCurrency":"KRW"}],"reconnect":true}')
        answer = json.loads('{"success":true,"data":{"unsubscribed":[{"baseCurrency":"ETH","quoteCurrency":"KRW","symbol":"KRW-ETH"}],"unsubscribeFailed":[]}}')

        self.assertDictEqual(res, answer)

        res = client.getSubscribingTickers()
        answer = json.loads('{"success":true,"data":{"tickers":[{"baseCurrency":"ETH","quoteCurrency":"KRW","symbol":"KRW-ETH"}]}}')

        self.assertDictEqual(res, answer)

        res = client.getSubscribingOrderbooks()
        answer = json.loads('{"success":true,"data":{"orderbooks":[{"baseCurrency":"BTC","quoteCurrency":"KRW","symbol":"KRW-BTC"}]}}')

        self.assertDictEqual(res, answer)

        res = client.subscribeOrderbook('{"market":[{"baseCurrency":"XRP","quoteCurrency":"KRW"},{"baseCurrency":"ETH","quoteCurrency":"KRW"}],"reconnect":true}')
        answer = json.loads('{"success":true,"data":{"subscribed":[{"baseCurrency":"XRP","quoteCurrency":"KRW","symbol":"KRW-XRP"},{"baseCurrency":"ETH","quoteCurrency":"KRW","symbol":"KRW-ETH"}],"subscribeFailed":[]}}')

        self.assertDictEqual(res, answer)

        res = client.getSubscribingTickers()
        answer = json.loads('{"success":true,"data":{"tickers":[{"baseCurrency":"ETH","quoteCurrency":"KRW","symbol":"KRW-ETH"}]}}')

        self.assertDictEqual(res, answer)

        res = client.getSubscribingOrderbooks()
        answer = json.loads('{"success":true,"data":{"orderbooks":[{"baseCurrency":"BTC","quoteCurrency":"KRW","symbol":"KRW-BTC"},{"baseCurrency":"XRP","quoteCurrency":"KRW","symbol":"KRW-XRP"},{"baseCurrency":"ETH","quoteCurrency":"KRW","symbol":"KRW-ETH"}]}}')



if __name__ == "__main__":
    import os
    filepath = './OneXAPI_Logs/OneXAPI_' + time.strftime('%Y-%m-%d', time.localtime(time.time())) + '.log'
    
    if os.path.exists(filepath):
        os.remove(filepath)

    unittest.main()