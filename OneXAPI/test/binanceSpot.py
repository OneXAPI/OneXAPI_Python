import unittest
import sys, os, time
from datetime import datetime, timedelta
import json
import util
from exchangeKeys import BINANCE_ACCESS_KEY, BINANCE_SECRET_KEY

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
    def test_BinanceSpot_Object_1(self):
        for i in range(0,5):
            client = OneXAPI.Binance.Spot()

    def test_BinanceSpot_Object_2(self):
        for i in range(0,5):
            client = OneXAPI.Binance.Spot('')

    def test_BinanceSpot_Object_3(self):
        for i in range(0,5):
            client = OneXAPI.Binance.Spot("{}")

    def test_BinanceSpot_Object_4(self):
        for i in range(0,5):
            client = OneXAPI.Binance.Spot('fnq543wb')

    def test_BinanceSpot_Object_5(self):
        client = OneXAPI.Binance.Spot('{"accessKey":"Test Access Key"}')
        res = client.getConfig()
        self.assertEqual(res['data']['accessKey'], 'Test Access Key')
        self.assertEqual(res['data']['secretKey'], '')

    def test_BinanceSpot_Object_6(self):
        client = OneXAPI.Binance.Spot('{"secretKey":"Test Secret Key"}')
        res = client.getConfig()
        self.assertEqual(res['data']['secretKey'], 'Test Secret Key')
        self.assertEqual(res['data']['accessKey'], '')    

    def test_BinanceSpot_Object_7(self):
        client = OneXAPI.Binance.Spot('{"accessKey":"Test Access Key", "secretKey":"Test Secret Key"}')
        res = client.getConfig()
        self.assertEqual(res['data']['accessKey'], 'Test Access Key')
        self.assertEqual(res['data']['secretKey'], 'Test Secret Key')

    def test_getConfig_1(self):
        client = OneXAPI.Binance.Spot()
        res = client.getConfig()
        answer = json.loads('{"success":true,"data":{"requestedApiCount":0,"exchange":"Binance","instrument":"Spot","accessKey":"","secretKey":"","restEndpoint":"https://api.binance.com","publicWebsocketEndpoint":"wss://stream.binance.com:9443/stream","privateWebsocketEndpoint":"wss://stream.binance.com:9443/ws","restRequestTimeout":5000,"websocketConnectTimeout":5000,"websocketIdleTimeout":5000}}')
        self.assertEqual(res, answer)
    
    def test_getConfig_2(self):
        client = OneXAPI.Binance.Spot()
        res = client.getConfig("")
        answer = json.loads('{"success":true,"data":{"requestedApiCount":0,"exchange":"Binance","instrument":"Spot","accessKey":"","secretKey":"","restEndpoint":"https://api.binance.com","publicWebsocketEndpoint":"wss://stream.binance.com:9443/stream","privateWebsocketEndpoint":"wss://stream.binance.com:9443/ws","restRequestTimeout":5000,"websocketConnectTimeout":5000,"websocketIdleTimeout":5000}}')
        self.assertEqual(res, answer)

    def test_getConfig_3(self):
        client = OneXAPI.Binance.Spot()
        res = client.getConfig("{}")
        answer = json.loads('{"success":true,"data":{"requestedApiCount":0,"exchange":"Binance","instrument":"Spot","accessKey":"","secretKey":"","restEndpoint":"https://api.binance.com","publicWebsocketEndpoint":"wss://stream.binance.com:9443/stream","privateWebsocketEndpoint":"wss://stream.binance.com:9443/ws","restRequestTimeout":5000,"websocketConnectTimeout":5000,"websocketIdleTimeout":5000}}')
        self.assertEqual(res, answer)

    def test_getConfig_4(self):
        client = OneXAPI.Binance.Spot()
        res = client.getConfig("trashData123@@!%")
        answer = json.loads('{"success":true,"data":{"requestedApiCount":0,"exchange":"Binance","instrument":"Spot","accessKey":"","secretKey":"","restEndpoint":"https://api.binance.com","publicWebsocketEndpoint":"wss://stream.binance.com:9443/stream","privateWebsocketEndpoint":"wss://stream.binance.com:9443/ws","restRequestTimeout":5000,"websocketConnectTimeout":5000,"websocketIdleTimeout":5000}}')
        self.assertEqual(res, answer)

    def test_setConfig_1(self):
        client = OneXAPI.Binance.Spot()
        res = client.setConfig("")
        answer = json.loads('{"success":false,"data":{"errorType":"JSON_PARSING_ERROR","errorMsg":""}}')
        self.assertEqual(res, answer)

    def test_setConfig_2(self):
        client = OneXAPI.Binance.Spot()
        res = client.setConfig("{}")
        answer = json.loads('{"success":true,"data":{"requestedApiCount":0}}')
        self.assertEqual(res, answer)

    def test_setConfig_3(self):
        client = OneXAPI.Binance.Spot()
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
        client = OneXAPI.Binance.Spot()
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
        client = OneXAPI.Binance.Spot()
        testList = [
            ('accessKey','"test access key"'),
            ('secretKey','"test secret key"'),
            ('restEndpoint','"https://api3.binance.com"'),
            ('publicWebsocketEndpoint','"wss://testnet.binance.vision/stream"'),
            ('privateWebsocketEndpoint','"wss://testnet.binance.vision/ws"'),
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
        client = OneXAPI.Binance.Spot()

        res = client.getEndpointCandidates()
        answer = json.loads('{"success":true,"data":{"requestedApiCount":0,"restEndpoints":["https://api.binance.com","https://api1.binance.com","https://api2.binance.com","https://api3.binance.com","https://testnet.binance.vision/api"],"publicWebsocketEndpoints":["wss://stream.binance.com:9443/stream","wss://testnet.binance.vision/stream"],"privateWebsocketEndpoints":["wss://stream.binance.com:9443/ws","wss://testnet.binance.vision/ws"]}}')

        self.assertEqual(res, answer)

    def test_getEndpointCandidates_2(self):
        client = OneXAPI.Binance.Spot()

        res = client.getEndpointCandidates("")
        answer = json.loads('{"success":true,"data":{"requestedApiCount":0,"restEndpoints":["https://api.binance.com","https://api1.binance.com","https://api2.binance.com","https://api3.binance.com","https://testnet.binance.vision/api"],"publicWebsocketEndpoints":["wss://stream.binance.com:9443/stream","wss://testnet.binance.vision/stream"],"privateWebsocketEndpoints":["wss://stream.binance.com:9443/ws","wss://testnet.binance.vision/ws"]}}')

        self.assertEqual(res, answer)

    def test_getEndpointCandidates_3(self):
        client = OneXAPI.Binance.Spot()

        res = client.getEndpointCandidates("{}")
        answer = json.loads('{"success":true,"data":{"requestedApiCount":0,"restEndpoints":["https://api.binance.com","https://api1.binance.com","https://api2.binance.com","https://api3.binance.com","https://testnet.binance.vision/api"],"publicWebsocketEndpoints":["wss://stream.binance.com:9443/stream","wss://testnet.binance.vision/stream"],"privateWebsocketEndpoints":["wss://stream.binance.com:9443/ws","wss://testnet.binance.vision/ws"]}}')

        self.assertEqual(res, answer)

    def test_getEndpointCandidates_4(self):
        client = OneXAPI.Binance.Spot()

        res = client.getEndpointCandidates("uNPaRsib1eM5g")
        answer = json.loads('{"success":true,"data":{"requestedApiCount":0,"restEndpoints":["https://api.binance.com","https://api1.binance.com","https://api2.binance.com","https://api3.binance.com","https://testnet.binance.vision/api"],"publicWebsocketEndpoints":["wss://stream.binance.com:9443/stream","wss://testnet.binance.vision/stream"],"privateWebsocketEndpoints":["wss://stream.binance.com:9443/ws","wss://testnet.binance.vision/ws"]}}')

        self.assertEqual(res, answer)

    def test_has_1(self):
        client = OneXAPI.Binance.Spot()

        res = client.has('')
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'JSON_PARSING_ERROR')

    def test_has_2(self):
        client = OneXAPI.Binance.Spot()

        res = client.has('{}')
        answer = json.loads(hasMap)

        for key, value in answer.items():
            self.assertEqual(res['data'][key], value)

    def test_has_3(self):
        client = OneXAPI.Binance.Spot()

        res = client.has('el12nlgv@!')
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'JSON_PARSING_ERROR')

    def test_has_4(self):
        client = OneXAPI.Binance.Spot()

        answer = json.loads(hasMap)

        for key, value in answer.items():
            res = client.has('{"api":"' + key + '"}')
            self.assertEqual(res['success'], True)
            self.assertEqual(res['data'][key], value)
            self.assertEqual(res['data']['requestedApiCount'], 0)

    def test_has_5(self):
        client = OneXAPI.Binance.Spot()

        res = client.has('{"api":"notExistApi"}')
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'WRONG_VALUE')

    def test_getWithdrawRoundingRule_1(self):
        client = OneXAPI.Binance.Spot()

        res = client.getWithdrawRoundingRule()
        answer = json.loads('{"success":true,"data":{"requestedApiCount":0,"roundingRule":"round"}}')
        self.assertEqual(res, answer)

    def test_getWithdrawRoundingRule_2(self):
        client = OneXAPI.Binance.Spot()

        res = client.getWithdrawRoundingRule('{}')
        answer = json.loads('{"success":true,"data":{"requestedApiCount":0,"roundingRule":"round"}}')
        self.assertEqual(res, answer)

    def test_setWithdrawRoundingRule_1(self):
        client = OneXAPI.Binance.Spot()

        res = client.setWithdrawRoundingRule('{"roundingRule":"wrongData"}')
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'WRONG_VALUE')

    def test_setWithdrawRoundingRule_2(self):
        client = OneXAPI.Binance.Spot()

        for value in ['ceil', 'floor', 'round']:
            res = client.setWithdrawRoundingRule('{"roundingRule":"' + value +'"}')
            self.assertEqual(res['success'], True)
            self.assertEqual(res['data']['roundingRule'], value)
            self.assertEqual(res['data']['requestedApiCount'], 0)

    def test_withdraw_1(self):
        client = OneXAPI.Binance.Spot()
        
        testdict = ['{"currency":"bTc","address":"0x1345"}','{"currency":"bTc","amount":1.535478}','{"address":"fwlnvlwnlkfsd","amount":13384.13541345}']
        
        for payload in testdict:
            res = client.withdraw(payload)
            self.assertEqual(res['success'], False)
            self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_withdraw_2(self):
        time.sleep(1)
        client = OneXAPI.Binance.Spot('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')
        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"file","logLevel":"info"}}')

        nowTime = time.localtime(time.time())
        
        client.withdraw('{"currency":"aDA","address":"wrongAddress","amount":135.1234358}')
        time.sleep(1)
        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"terminal","logLevel":"off"}}')
        answer1 = 'https://api.binance.com/sapi/v1/capital/config/getall'
        answer2 = 'https://api.binance.com/sapi/v1/capital/withdraw/apply?coin=ADA&address=wrongAddress&amount=135.123436'

        if util.searchLog(nowTime, answer1) is False:
            self.fail(f'{answer1} not found')
        if util.searchLog(nowTime, answer2) is False:
            self.fail(f'{answer2} not found')

    def test_withdraw_3(self):
        time.sleep(1)
        client = OneXAPI.Binance.Spot('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')
        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"file","logLevel":"info"}}')

        nowTime = time.localtime(time.time())
        
        client.withdraw('{"currency":"aDA","chain":"AdA","address":"wrongAddress","tag":"wrongTag","amount":135.1234358,"feeInAmount":false}')
        time.sleep(1)
        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"terminal","logLevel":"off"}}')
        answer1 = 'https://api.binance.com/sapi/v1/capital/config/getall'
        answer2 = 'https://api.binance.com/sapi/v1/capital/withdraw/apply?coin=ADA&network=ADA&address=wrongAddress&addressTag=wrongTag&amount=136.123436'

        if util.searchLog(nowTime, answer1) is False:
            self.fail(f'{answer1} not found')
        if util.searchLog(nowTime, answer2) is False:
            self.fail(f'{answer2} not found')

    def test_fetchAllCurrencies_1(self):
        time.sleep(1)
        client = OneXAPI.Binance.Spot('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        res = client.fetchAllCurrencies()
        self.assertEqual(res['success'], True)
        self.assertEqual(res['data']['requestedApiCount'], 1)

        for currency, chainsDict in res['data']['currencies'].items():
            self.assertEqual(type(currency), type(""))
            self.assertEqual(type(chainsDict['chains']), type([]))
            
            self.assertNotEqual(len(chainsDict['chains']), 1)

            for chain in chainsDict['chains']:
                self.assertEqual(type(chain['chain']), type(""))
                self.assertEqual(type(chain['isDefault']), type(True))

    def test_fetchAllCurrencies_2(self):
        time.sleep(1)
        client = OneXAPI.Binance.Spot('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        res = client.fetchAllCurrencies("")
        self.assertEqual(res['success'], True)
        self.assertEqual(res['data']['requestedApiCount'], 1)
        
        for currency, chainsDict in res['data']['currencies'].items():
            self.assertEqual(type(currency), type(""))
            self.assertEqual(type(chainsDict['chains']), type([]))
            
            self.assertNotEqual(len(chainsDict['chains']), 1)

            for chain in chainsDict['chains']:
                self.assertEqual(type(chain['chain']), type(""))
                self.assertEqual(type(chain['isDefault']), type(True))

    def test_fetchBalance_1(self):
        time.sleep(1)
        client = OneXAPI.Binance.Spot('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')
        
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
        client = OneXAPI.Binance.Spot('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')
        
        res = client.fetchBalance('{"currencies":["bTc","xRP","Eth"], "zeroBalance": true}')
        self.assertEqual(res['success'], True)
        self.assertEqual(res['data']['requestedApiCount'], 1)
        self.assertEqual(res['data']['fetchType'], "rest")
        self.assertEqual(len(res['data']['balance']), 3)
        
        for currency, balance in res['data']['balance'].items():
            self.assertEqual(type(currency), type(""))
            self.assertEqual(type(balance["free"]), type(""))
            self.assertEqual(type(balance["locked"]), type(""))

    def test_fetchBalance_3(self):
        time.sleep(1)
        client = OneXAPI.Binance.Spot('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        client.subscribeBalance()
        res = client.fetchBalance('{"currencies":["bTc","xRP","Eth"], "zeroBalance": true}')
        self.assertEqual(res['success'], True)
        self.assertEqual(res['data']['requestedApiCount'], 0)
        self.assertEqual(res['data']['fetchType'], "websocket")
        self.assertEqual(len(res['data']['balance']), 3)
        
        for currency, balance in res['data']['balance'].items():
            self.assertEqual(type(currency), type(""))
            self.assertEqual(type(balance["free"]), type(""))
            self.assertEqual(type(balance["locked"]), type(""))

    def test_fetchBalance_4(self):
        time.sleep(1)
        client = OneXAPI.Binance.Spot('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        client.subscribeBalance()
        res = client.fetchBalance('{"currencies":["bTc","xRP","Eth"], "zeroBalance": true, "forceRestApi": true}')
        self.assertEqual(res['success'], True)
        self.assertEqual(res['data']['requestedApiCount'], 1)
        self.assertEqual(res['data']['fetchType'], "rest")
        self.assertEqual(len(res['data']['balance']), 3)
        
        for currency, balance in res['data']['balance'].items():
            self.assertEqual(type(currency), type(""))
            self.assertEqual(type(balance["free"]), type(""))
            self.assertEqual(type(balance["locked"]), type(""))

    def test_fetchWalletStatus_1(self):
        time.sleep(1)
        client = OneXAPI.Binance.Spot('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')
        
        res = client.fetchWalletStatus('{}')
        self.assertEqual(res['success'], True)
        self.assertEqual(res['data']['requestedApiCount'], 1)
        self.assertNotEqual(len(res['data']['currencies']), 0)

        for currency, chains in res['data']['currencies'].items():
            self.assertEqual(type(currency), type(""))
            self.assertEqual(type(chains["chains"]), type([]))
            
            if len(chains["chains"]) == 1:
                self.assertEqual(chains["chains"][0]["chain"], "")
            
            for chain in chains["chains"]:
                if len(chains["chains"]) != 1:
                    self.assertNotEqual(chain["chain"], "")
                self.assertEqual(type(chain["chain"]), type(""))
                self.assertEqual(type(chain["withdrawEnable"]), type(True))
                self.assertEqual(type(chain["depositEnable"]), type(True))
            

    def test_fetchWalletStatus_2(self):
        time.sleep(1)
        client = OneXAPI.Binance.Spot('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')
        
        res = client.fetchWalletStatus('{"currency":"bTc"}')
        self.assertEqual(res['success'], True)
        self.assertEqual(res['data']['requestedApiCount'], 1)
        self.assertEqual(len(res['data']['currencies']), 1)

        for currency, chains in res['data']['currencies'].items():
            self.assertEqual(type(currency), type(""))
            self.assertEqual(type(chains["chains"]), type([]))
            self.assertGreaterEqual(len(chains["chains"]), 1)

            for chain in chains['chains']:
                if len(chains['chains']) == 1:
                    self.assertEqual(chain["chain"], "")
                else:
                    self.assertNotEqual(chain["chain"], "")
                self.assertEqual(type(chain["withdrawEnable"]), type(True))
                self.assertEqual(type(chain["depositEnable"]), type(True))

    def test_fetchWithdrawHistory_1(self):
        time.sleep(1)
        client = OneXAPI.Binance.Spot('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')
        
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
        client = OneXAPI.Binance.Spot('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')
        
        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"file","logLevel":"info"}}')

        nowTime = time.localtime(time.time())
        
        client.fetchWithdrawHistory('{"currency":"mATic","orderId":"testOrderId","txid":"testTxId","startTime":132123534,"endTime":1125615123}')
        time.sleep(1)
        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"terminal","logLevel":"off"}}')

        answer1 = 'https://api.binance.com/sapi/v1/capital/withdraw/history?coin=MATIC&startTime=132123534&endTime=1125615123'

        if util.searchLog(nowTime, answer1) is False:
            self.fail(f'{answer1} not found')

    def test_fetchDepositHistory_1(self):
        time.sleep(1)
        client = OneXAPI.Binance.Spot('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')
        
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
        client = OneXAPI.Binance.Spot('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"file","logLevel":"info"}}')

        nowTime = time.localtime(time.time())
        
        client.fetchDepositHistory('{"currency":"mATic","orderId":"testOrderId","txid":"testTxId","startTime":132123534,"endTime":1125615123}')
        time.sleep(1)
        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"terminal","logLevel":"off"}}')

        answer1 = 'https://api.binance.com/sapi/v1/capital/deposit/hisrec?coin=MATIC&startTime=132123534&endTime=1125615123'

        if util.searchLog(nowTime, answer1) is False:
            self.fail(f'{answer1} not found')

    def test_fetchDepositAddress_1(self):
        time.sleep(1)
        client = OneXAPI.Binance.Spot('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')
        
        res = client.fetchDepositAddress('{}')
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')
    
    def test_fetchDepositAddress_2(self):
        time.sleep(1)
        client = OneXAPI.Binance.Spot('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')
        
        res = client.fetchDepositAddress('{"currency":"Btc","chain":"BsC"}')
        self.assertEqual(res['success'], True)
        self.assertEqual(res['data']['requestedApiCount'], 1)
        self.assertEqual(len(res['data']['addresses']), 1)

        self.assertEqual(type(res['data']['addresses']['BTC']), type([]))
        self.assertEqual(res['data']['addresses']['BTC'][0]['chain'], 'BSC')
        self.assertEqual(type(res['data']['addresses']['BTC'][0]['address']), type(''))
        self.assertEqual(type(res['data']['addresses']['BTC'][0]['tag']), type(''))

    def test_isDepositCompleted_1(self):
        client = OneXAPI.Binance.Spot()

        res = client.isDepositCompleted('{}')
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_isDepositCompleted_2(self):
        time.sleep(1)
        client = OneXAPI.Binance.Spot('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"file","logLevel":"info"}}')

        nowTime = time.localtime(time.time())
        
        res = client.isDepositCompleted('{"txid":"testTxid"}')
        time.sleep(1)
        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"terminal","logLevel":"off"}}')

        answer1 = 'https://api.binance.com/sapi/v1/capital/deposit/hisrec'

        if util.searchLog(nowTime, answer1) is False:
            self.fail(f'{answer1} not found')

        answer = json.loads('{"success":true,"data":{"requestedApiCount":1,"isDepositCompleted":false}}')
        self.assertEqual(res, answer)


    def test_isDepositCompleted_3(self):
        time.sleep(1)
        client = OneXAPI.Binance.Spot('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"file","logLevel":"info"}}')

        nowTime = time.localtime(time.time())
        
        res = client.isDepositCompleted('{"currency":"sOl","amount":35.213843,"since":1656044045154}')
        time.sleep(1)
        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"terminal","logLevel":"off"}}')

        answer1 = 'https://api.binance.com/sapi/v1/capital/deposit/hisrec?coin=SOL&startTime=1656044045154'

        if util.searchLog(nowTime, answer1) is False:
            self.fail(f'{answer1} not found')

        answer = json.loads('{"success":true,"data":{"requestedApiCount":1,"isDepositCompleted":false}}')
        self.assertEqual(res, answer)

    def test_subscribeBalance_1(self):
        time.sleep(1)
        client = OneXAPI.Binance.Spot('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        res = client.subscribeBalance()
        answer = json.loads('{"success":true,"data":{}}')
        self.assertEqual(res, answer)


    def test_subscribeBalance_2(self):
        time.sleep(1)
        client = OneXAPI.Binance.Spot('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        res = client.subscribeBalance('')
        answer = json.loads('{"success":true,"data":{}}')
        self.assertEqual(res, answer)

    def test_subscribeBalance_3(self):
        time.sleep(1)
        client = OneXAPI.Binance.Spot('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        res = client.subscribeBalance('{}')
        answer = json.loads('{"success":true,"data":{}}')
        self.assertEqual(res, answer)

    def test_subscribeBalance_4(self):
        time.sleep(1)
        client = OneXAPI.Binance.Spot('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        res = client.subscribeBalance('Bqbqb@')
        answer = json.loads('{"success":true,"data":{}}')
        self.assertEqual(res, answer)

    def test_unsubscribeBalance_1(self):
        time.sleep(1)
        client = OneXAPI.Binance.Spot('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        res = client.unsubscribeBalance()
        answer = json.loads('{"success":true,"data":{}}')
        self.assertEqual(res, answer)

    def test_unsubscribeBalance_2(self):
        time.sleep(1)
        client = OneXAPI.Binance.Spot('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        res = client.unsubscribeBalance('')
        answer = json.loads('{"success":true,"data":{}}')
        self.assertEqual(res, answer)

    def test_unsubscribeBalance_3(self):
        time.sleep(1)
        client = OneXAPI.Binance.Spot('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        client.subscribeBalance()
        res = client.unsubscribeBalance('{}')
        answer = json.loads('{"success":true,"data":{}}')
        self.assertEqual(res, answer)

    def test_unsubscribeBalance_4(self):
        time.sleep(1)
        client = OneXAPI.Binance.Spot('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        client.subscribeBalance()
        res = client.unsubscribeBalance('Bqbqb@')
        answer = json.loads('{"success":true,"data":{}}')
        self.assertEqual(res, answer)

    def test_isSubscribingBalance_1(self):
        time.sleep(1)
        client = OneXAPI.Binance.Spot('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        res = client.isSubscribingBalance()
        answer = json.loads('{"success":true,"data":{"isSubscribing":false}}')

        self.assertEqual(res, answer)

    def test_isSubscribingBalance_2(self):
        time.sleep(1)
        client = OneXAPI.Binance.Spot('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        res = client.isSubscribingBalance('')
        answer = json.loads('{"success":true,"data":{"isSubscribing":false}}')

        self.assertEqual(res, answer)

    def test_isSubscribingBalance_3(self):
        time.sleep(1)
        client = OneXAPI.Binance.Spot('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        client.subscribeBalance()
        res = client.isSubscribingBalance('{}')
        answer = json.loads('{"success":true,"data":{"isSubscribing":true}}')

        self.assertEqual(res, answer)

    def test_isSubscribingBalance_4(self):
        time.sleep(1)
        client = OneXAPI.Binance.Spot('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        client.subscribeBalance()
        client.unsubscribeBalance()
        res = client.isSubscribingBalance('Bqbqb@')
        answer = json.loads('{"success":true,"data":{"isSubscribing":false}}')

        self.assertEqual(res, answer)

    def test_getOrderRoundingRule_1(self):
        client = OneXAPI.Binance.Spot()
        res = client.getOrderRoundingRule()
        answer = json.loads('{"success":true,"data":{"requestedApiCount":0,"limitBuyPrice":"round","limitBuyBaseAmount":"round","limitSellPrice":"round","limitSellBaseAmount":"round","marketBuyQuoteAmount":"round","marketSellBaseAmount":"round"}}')

        self.assertEqual(res, answer)

    def test_getOrderRoundingRule_2(self):
        client = OneXAPI.Binance.Spot()
        res = client.getOrderRoundingRule("")
        answer = json.loads('{"success":true,"data":{"requestedApiCount":0,"limitBuyPrice":"round","limitBuyBaseAmount":"round","limitSellPrice":"round","limitSellBaseAmount":"round","marketBuyQuoteAmount":"round","marketSellBaseAmount":"round"}}')

        self.assertEqual(res, answer)

    def test_setOrderRoundingRule_1(self):
        client = OneXAPI.Binance.Spot()

        res = client.setOrderRoundingRule('{"limitBuyBaseAmount":"wrongData"}')
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'WRONG_VALUE')

    def test_setOrderRoundingRule_2(self):
        client = OneXAPI.Binance.Spot()

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
        client = OneXAPI.Binance.Spot()
        
        res = client.orderLimitBuy('{}')
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_orderLimitBuy_2(self):
        time.sleep(1)
        client = OneXAPI.Binance.Spot('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"file","logLevel":"info"}}')

        nowTime = time.localtime(time.time())
        
        client.orderLimitBuy('{"baseCurrency":"bTC","quoteCurrency":"uSDt","price":25312.1234358,"baseAmount":35.135689342158}')
        time.sleep(1)
        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"terminal","logLevel":"off"}}')

        answer1 = 'https://api.binance.com/api/v3/order?symbol=BTCUSDT&side=BUY&type=LIMIT&timeInForce=GTC&quantity=35.13569&price=25312.12'

        if util.searchLog(nowTime, answer1) is False:
            self.fail(f'{answer1} not found')

    def test_orderLimitBuy_3(self):
        time.sleep(1)
        client = OneXAPI.Binance.Spot('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"file","logLevel":"info"}}')

        nowTime = time.localtime(time.time())
        
        client.orderLimitBuy('{"baseCurrency":"bTC","quoteCurrency":"uSDt","price":25312.1234358,"baseAmount":35.135689342158,"clientOrderId":"testId","amplifier":1.0346,"type":"fok"}')
        time.sleep(1)
        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"terminal","logLevel":"off"}}')

        answer1 = 'https://api.binance.com/api/v3/order?symbol=BTCUSDT&side=BUY&type=LIMIT&timeInForce=FOK&quantity=35.13569&price=26187.92&newClientOrderId=testId'

        if util.searchLog(nowTime, answer1) is False:
            self.fail(f'{answer1} not found')

    def test_orderLimitSell_1(self):
        client = OneXAPI.Binance.Spot()
        
        res = client.orderLimitSell('{}')
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_orderLimitSell_2(self):
        time.sleep(1)
        client = OneXAPI.Binance.Spot('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"file","logLevel":"info"}}')

        nowTime = time.localtime(time.time())
        
        client.orderLimitSell('{"baseCurrency":"bTC","quoteCurrency":"uSDt","price":25312.1234358,"baseAmount":35.135689342158}')
        time.sleep(1)
        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"terminal","logLevel":"off"}}')

        answer1 = 'https://api.binance.com/api/v3/order?symbol=BTCUSDT&side=SELL&type=LIMIT&timeInForce=GTC&quantity=35.13569&price=25312.12'

        if util.searchLog(nowTime, answer1) is False:
            self.fail(f'{answer1} not found')

    def test_orderLimitSell_3(self):
        time.sleep(1)
        client = OneXAPI.Binance.Spot('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"file","logLevel":"info"}}')

        nowTime = time.localtime(time.time())
        
        client.orderLimitSell('{"baseCurrency":"bTC","quoteCurrency":"uSDt","price":25312.1234358,"baseAmount":35.135689342158,"clientOrderId":"testId","amplifier":0.96348,"type":"fok"}')
        time.sleep(1)
        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"terminal","logLevel":"off"}}')

        answer1 = 'https://api.binance.com/api/v3/order?symbol=BTCUSDT&side=SELL&type=LIMIT&timeInForce=IOC&quantity=35.13569&price=24387.72&newClientOrderId=testId'

        if util.searchLog(nowTime, answer1) is False:
            self.fail(f'{answer1} not found')

    def test_orderMarketBuy_1(self):
        client = OneXAPI.Binance.Spot()
        
        res = client.orderMarketBuy('{}')
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_orderMarketBuy_2(self):
        time.sleep(1)
        client = OneXAPI.Binance.Spot('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"file","logLevel":"info"}}')

        nowTime = time.localtime(time.time())
        
        client.orderMarketBuy('{"baseCurrency":"bTC","quoteCurrency":"usdT","quoteAmount":41381.391351334}')
        time.sleep(1)
        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"terminal","logLevel":"off"}}')

        answer1 = 'https://api.binance.com/api/v3/order?symbol=BTCUSDT&side=BUY&type=MARKET&quoteOrderQty=41381.39'

        if util.searchLog(nowTime, answer1) is False:
            self.fail(f'{answer1} not found')

    def test_orderMarketBuy_3(self):
        time.sleep(1)
        client = OneXAPI.Binance.Spot('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"file","logLevel":"info"}}')

        nowTime = time.localtime(time.time())
        
        client.orderMarketBuy('{"baseCurrency":"bTC","quoteCurrency":"usdT","quoteAmount":41381.391351334,"clientOrderId":"testId"}')
        time.sleep(1)
        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"terminal","logLevel":"off"}}')

        answer1 = 'https://api.binance.com/api/v3/order?symbol=BTCUSDT&side=BUY&type=MARKET&quoteOrderQty=41381.39&newClientOrderId=testId'

        if util.searchLog(nowTime, answer1) is False:
            self.fail(f'{answer1} not found')

    def test_orderMarketSell_1(self):
        client = OneXAPI.Binance.Spot()
        
        res = client.orderMarketSell('{}')
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_orderMarketSell_2(self):
        time.sleep(1)
        client = OneXAPI.Binance.Spot('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"file","logLevel":"info"}}')

        nowTime = time.localtime(time.time())
        
        client.orderMarketSell('{"baseCurrency":"bTC","quoteCurrency":"usdT","baseAmount":83.1338494835}')
        time.sleep(1)
        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"terminal","logLevel":"off"}}')

        answer1 = 'https://api.binance.com/api/v3/order?symbol=BTCUSDT&side=SELL&type=MARKET&quantity=83.13385'

        if util.searchLog(nowTime, answer1) is False:
            self.fail(f'{answer1} not found')

    def test_orderMarketSell_3(self):
        time.sleep(1)
        client = OneXAPI.Binance.Spot('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"file","logLevel":"info"}}')

        nowTime = time.localtime(time.time())
        
        client.orderMarketSell('{"baseCurrency":"bTC","quoteCurrency":"usdT","baseAmount":83.1338494835,"clientOrderId":"testId"}')
        time.sleep(1)
        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"terminal","logLevel":"off"}}')

        answer1 = 'https://api.binance.com/api/v3/order?symbol=BTCUSDT&side=SELL&type=MARKET&quantity=83.13385&newClientOrderId=testId'

        if util.searchLog(nowTime, answer1) is False:
            self.fail(f'{answer1} not found')

    def test_orderCancel_1(self):
        client = OneXAPI.Binance.Spot()
        
        res = client.orderCancel('{}')
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_orderCancel_2(self):
        time.sleep(1)
        client = OneXAPI.Binance.Spot('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        res = client.orderCancel('{"orderId":"testOrderId"}')
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_orderCancel_3(self):
        time.sleep(1)
        client = OneXAPI.Binance.Spot('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"file","logLevel":"info"}}')

        nowTime = time.localtime(time.time())
        
        client.orderCancel('{"baseCurrency":"bTC","quoteCurrency":"usdT","orderId":"testOrderId"}')
        time.sleep(1)
        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"terminal","logLevel":"off"}}')

        answer1 = 'https://api.binance.com/api/v3/order?symbol=BTCUSDT&orderId=testOrderId'

        if util.searchLog(nowTime, answer1) is False:
            self.fail(f'{answer1} not found')

    def test_orderCancel_4(self):
        time.sleep(1)
        client = OneXAPI.Binance.Spot('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"file","logLevel":"info"}}')

        nowTime = time.localtime(time.time())
        
        client.orderCancel('{"baseCurrency":"bTC","quoteCurrency":"usdT","clientOrderId":"testClientOrderId"}')
        time.sleep(1)
        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"terminal","logLevel":"off"}}')

        answer1 = 'https://api.binance.com/api/v3/order?symbol=BTCUSDT&origClientOrderId=testClientOrderId'

        if util.searchLog(nowTime, answer1) is False:
            self.fail(f'{answer1} not found')

    def test_fetchTradingFee_1(self):
        time.sleep(1)
        client = OneXAPI.Binance.Spot('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')
        
        res = client.fetchTradingFee('{}')
        self.assertEqual(res['success'], True)
        self.assertEqual(res['data']['requestedApiCount'], 1)
        self.assertEqual(type(res['data']['fees']), type([]))
        self.assertNotEqual(len(res['data']['fees']), 0)
        
        for fee in res['data']['fees']:
            self.assertEqual(type(fee['baseCurrency']), type(""))
            self.assertEqual(type(fee['quoteCurrency']), type(""))
            self.assertEqual(type(fee['symbol']), type(""))
            self.assertEqual(type(fee['makerFee']), type(""))
            self.assertEqual(type(fee['takerFee']), type(""))

    def test_fetchTradingFee_2(self):
        time.sleep(1)
        client = OneXAPI.Binance.Spot('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')
        
        res = client.fetchTradingFee('{"baseCurrency":"bTC","quoteCurrency":"UsdT"}')
        self.assertEqual(res['success'], True)
        self.assertEqual(res['data']['requestedApiCount'], 1)
        self.assertEqual(type(res['data']['fees']), type([]))
        self.assertEqual(len(res['data']['fees']), 1)
        
        for fee in res['data']['fees']:
            self.assertEqual(type(fee['baseCurrency']), type(""))
            self.assertEqual(type(fee['quoteCurrency']), type(""))
            self.assertEqual(type(fee['symbol']), type(""))
            self.assertEqual(type(fee['makerFee']), type(""))
            self.assertEqual(type(fee['takerFee']), type(""))

    def test_fetchOrderInfo_1(self):
        client = OneXAPI.Binance.Spot()
        
        res = client.fetchOrderInfo('{}')
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_fetchOrderInfo_2(self):
        time.sleep(1)
        client = OneXAPI.Binance.Spot('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        res = client.fetchOrderInfo('{"orderId":"testOrderId"}')
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_fetchOrderInfo_3(self):
        time.sleep(1)
        client = OneXAPI.Binance.Spot('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"file","logLevel":"info"}}')

        nowTime = time.localtime(time.time())
        
        client.fetchOrderInfo('{"baseCurrency":"bTC","quoteCurrency":"UsdT","orderId":"testOrderId"}')
        time.sleep(1)
        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"terminal","logLevel":"off"}}')

        answer1 = 'https://api.binance.com/api/v3/order?symbol=BTCUSDT&orderId=testOrderId'

        if util.searchLog(nowTime, answer1) is False:
            self.fail(f'{answer1} not found')

    def test_fetchOrderInfo_4(self):
        time.sleep(1)
        client = OneXAPI.Binance.Spot('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"file","logLevel":"info"}}')

        nowTime = time.localtime(time.time())
        
        client.fetchOrderInfo('{"baseCurrency":"bTC","quoteCurrency":"UsdT","clientOrderId":"testClientOrderId"}')
        time.sleep(1)
        OneXAPI.setLoggerConfig('{"main":{"outputMethod":"terminal","logLevel":"off"}}')

        answer1 = 'https://api.binance.com/api/v3/order?symbol=BTCUSDT&origClientOrderId=testClientOrderId'

        if util.searchLog(nowTime, answer1) is False:
            self.fail(f'{answer1} not found')

    def test_fetchOrderInfo_5(self):
        time.sleep(1)
        client = OneXAPI.Binance.Spot('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        res = client.fetchOrderbook('{"baseCurrency": "XrP", "quoteCurrency": "UsdT"}')
        bidPrice = int(res['bids'][0]['price'])

        res = client.orderLimitBuy('{"baseCurrency": "xRp", "quoteCurrency": "UsdT", "price": ' + bidPrice + ', "baseAmount": 25, "amplifier": 0.96}')
        orderId = res['orderId']

        res = client.fetchOrderInfo('{"baseCurrency": "xRp", "quoteCurrency": "UsdT", "orderId": ' + orderId + '}')
        client.orderCancel('{"baseCurrency": "xRp", "quoteCurrency": "UsdT", "orderId": ' + orderId + '}')

        self.assertEqual(res['success'], True)
        self.assertEqual(res['data']['requestedApiCount'], 2)
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
        client = OneXAPI.Binance.Spot('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        res = client.fetchOrderbook('{"baseCurrency": "XrP", "quoteCurrency": "UsdT"}')
        bidPrice = int(res['bids'][0]['price'])

        res = client.orderLimitBuy('{"baseCurrency": "xRp", "quoteCurrency": "UsdT", "price": ' + bidPrice + ', "baseAmount": 25, "amplifier": 0.96}')
        orderId = res['orderId']

        res = client.fetchOpenOrders('{}')
        client.orderCancel('{"baseCurrency": "xRp", "quoteCurrency": "UsdT", "orderId": ' + orderId + '}')

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
        client = OneXAPI.Binance.Spot('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        res = client.fetchOrderbook('{"baseCurrency": "XrP", "quoteCurrency": "UsdT"}')
        bidPrice = int(res['bids'][0]['price'])

        res = client.orderLimitBuy('{"baseCurrency": "xRp", "quoteCurrency": "UsdT", "price": ' + bidPrice + ', "baseAmount": 25, "amplifier": 0.96}')
        orderId = res['orderId']

        res = client.fetchOpenOrders('{"baseCurrency": "XRP", "quoteCurrency": "uSDt", "side": "buy"}')
        client.orderCancel('{"baseCurrency": "xRp", "quoteCurrency": "UsdT", "orderId": ' + orderId + '}')

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
        client = OneXAPI.Binance.Spot()

        res = client.getCandleIntervalCandidates()
        answer = json.loads('{"success":true,"data":{"requestedApiCount":0,"intervals":["12hour","15min","1day","1hour","1min","1month","1week","2hour","30min","3day","3min","4hour","5min","6hour","8hour"]}}')

        self.assertEqual(res, answer)

    def test_getCandleIntervalCandidates_2(self):
        client = OneXAPI.Binance.Spot()

        res = client.getCandleIntervalCandidates('')
        answer = json.loads('{"success":true,"data":{"requestedApiCount":0,"intervals":["12hour","15min","1day","1hour","1min","1month","1week","2hour","30min","3day","3min","4hour","5min","6hour","8hour"]}}')

        self.assertEqual(res, answer)

    def test_fetchMarkets_1(self):
        time.sleep(1)
        client = OneXAPI.Binance.Spot('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        res = client.fetchMarkets('{}')
        
        self.assertEqual(res['success'], True)
        self.assertEqual(res['data']['requestedApiCount'], 1)
        for market in res['data']['markets']:
            self.assertEqual(type(market['baseCurrency']), type(''))
            self.assertEqual(type(market['quoteCurrency']), type(''))
            self.assertEqual(type(market['symbol']), type(''))

    def test_fetchMarkets_2(self):
        time.sleep(1)
        client = OneXAPI.Binance.Spot('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        res = client.fetchMarkets('{"baseCurrency":"bTC","quoteCurrency":"usDT"}')
        
        self.assertEqual(res['success'], True)
        self.assertEqual(res['data']['requestedApiCount'], 1)
        self.assertEqual(len(res['data']['markets']), 1)
        for market in res['data']['markets']:
            self.assertEqual(type(market['baseCurrency']), type(''))
            self.assertEqual(type(market['quoteCurrency']), type(''))
            self.assertEqual(type(market['symbol']), type(''))

    def test_fetchTicker_1(self):
        time.sleep(1)
        client = OneXAPI.Binance.Spot('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        res = client.fetchTicker('{}')

        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_fetchTicker_2(self):
        time.sleep(1)
        client = OneXAPI.Binance.Spot('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        res = client.fetchTicker('{"baseCurrency":"bTc","quoteCurrency":"USdt"}')

        self.assertEqual(res['success'], True)
        self.assertEqual(res['data']['requestedApiCount'], 1)
        self.assertEqual(res['data']['baseCurrency'], 'BTC')
        self.assertEqual(res['data']['quoteCurrency'], 'USDT')
        self.assertEqual(res['data']['symbol'], 'BTCUSDT')
        self.assertEqual(res['data']['fetchType'], 'rest')
        self.assertEqual(type(res['data']['openTime']), type(1))
        self.assertEqual(type(res['data']['openPrice']), type(''))
        self.assertEqual(type(res['data']['closePrice']), type(''))
        self.assertEqual(type(res['data']['lowPrice']), type(''))
        self.assertEqual(type(res['data']['highPrice']), type(''))
        self.assertEqual(type(res['data']['baseVolume']), type(''))
        self.assertEqual(type(res['data']['quoteVolume']), type(''))

    def test_fetchTicker_3(self):
        time.sleep(1)
        client = OneXAPI.Binance.Spot('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        client.subscribeTicker('{"market":[{"baseCurrency":"bTc","quoteCurrency":"USdt"}]}')
        res = client.fetchTicker('{"baseCurrency":"bTc","quoteCurrency":"USdt"}')

        self.assertEqual(res['success'], True)
        self.assertEqual(res['data']['requestedApiCount'], 0)
        self.assertEqual(res['data']['baseCurrency'], 'BTC')
        self.assertEqual(res['data']['quoteCurrency'], 'USDT')
        self.assertEqual(res['data']['symbol'], 'BTCUSDT')
        self.assertEqual(res['data']['fetchType'], 'websocket')
        self.assertEqual(type(res['data']['openTime']), type(1))
        self.assertEqual(type(res['data']['openPrice']), type(''))
        self.assertEqual(type(res['data']['closePrice']), type(''))
        self.assertEqual(type(res['data']['lowPrice']), type(''))
        self.assertEqual(type(res['data']['highPrice']), type(''))
        self.assertEqual(type(res['data']['baseVolume']), type(''))
        self.assertEqual(type(res['data']['quoteVolume']), type(''))

    def test_fetchTicker_4(self):
        time.sleep(1)
        client = OneXAPI.Binance.Spot('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        client.subscribeTicker('{"market":[{"baseCurrency":"bTc","quoteCurrency":"USdt"}]}')
        res = client.fetchTicker('{"baseCurrency":"bTc","quoteCurrency":"USdt","forceRestApi":true}')

        self.assertEqual(res['success'], True)
        self.assertEqual(res['data']['requestedApiCount'], 1)
        self.assertEqual(res['data']['baseCurrency'], 'BTC')
        self.assertEqual(res['data']['quoteCurrency'], 'USDT')
        self.assertEqual(res['data']['symbol'], 'BTCUSDT')
        self.assertEqual(res['data']['fetchType'], 'rest')
        self.assertEqual(type(res['data']['openTime']), type(1))
        self.assertEqual(type(res['data']['openPrice']), type(''))
        self.assertEqual(type(res['data']['closePrice']), type(''))
        self.assertEqual(type(res['data']['lowPrice']), type(''))
        self.assertEqual(type(res['data']['highPrice']), type(''))
        self.assertEqual(type(res['data']['baseVolume']), type(''))
        self.assertEqual(type(res['data']['quoteVolume']), type(''))

    def test_fetchOrderbook_1(self):
        time.sleep(1)
        client = OneXAPI.Binance.Spot('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        res = client.fetchOrderbook('{}')

        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_fetchOrderbook_2(self):
        time.sleep(1)
        client = OneXAPI.Binance.Spot('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        res = client.fetchOrderbook('{"baseCurrency":"bTc","quoteCurrency":"USdt"}')

        self.assertEqual(res['success'], True)
        self.assertEqual(res['data']['requestedApiCount'], 1)
        self.assertEqual(res['data']['baseCurrency'], 'BTC')
        self.assertEqual(res['data']['quoteCurrency'], 'USDT')
        self.assertEqual(res['data']['symbol'], 'BTCUSDT')
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
        client = OneXAPI.Binance.Spot('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        client.subscribeOrderbook('{"market":[{"baseCurrency":"bTc","quoteCurrency":"USdt"}]}')
        res = client.fetchOrderbook('{"baseCurrency":"bTc","quoteCurrency":"USdt"}')

        self.assertEqual(res['success'], True)
        self.assertEqual(res['data']['requestedApiCount'], 0)
        self.assertEqual(res['data']['baseCurrency'], 'BTC')
        self.assertEqual(res['data']['quoteCurrency'], 'USDT')
        self.assertEqual(res['data']['symbol'], 'BTCUSDT')
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
        client = OneXAPI.Binance.Spot('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        client.subscribeOrderbook('{"market":[{"baseCurrency":"bTc","quoteCurrency":"USdt"}]}')
        res = client.fetchOrderbook('{"baseCurrency":"bTc","quoteCurrency":"USdt","forceRestApi":true}')

        self.assertEqual(res['success'], True)
        self.assertEqual(res['data']['requestedApiCount'], 1)
        self.assertEqual(res['data']['baseCurrency'], 'BTC')
        self.assertEqual(res['data']['quoteCurrency'], 'USDT')
        self.assertEqual(res['data']['symbol'], 'BTCUSDT')
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
        client = OneXAPI.Binance.Spot('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')

        res = client.fetchCandleHistory('{"baseCurrency":"bTc","quoteCurrency":"uSdT"}')

        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_fetchCandleHistory_2(self):
        time.sleep(1)
        client = OneXAPI.Binance.Spot('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')
        
        specificTime = int((datetime.today() - timedelta(hours=2)).timestamp())
        res = client.fetchCandleHistory('{"baseCurrency":"bTc","quoteCurrency":"uSdT","interval":"1min","startTime":' + str(specificTime) + '}')
        
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
        client = OneXAPI.Binance.Spot('{"accessKey":"' + BINANCE_ACCESS_KEY + '", "secretKey":"' + BINANCE_SECRET_KEY + '"}')
        
        res = client.fetchCandleHistory('{"baseCurrency":"bTc","quoteCurrency":"uSdT","interval":"1min","startTime":1656042045,"endTime":1656063182,"fetchInterval":900}')
        
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
        client = OneXAPI.Binance.Spot()

        res = client.getSubscribingTickers()
        answer = json.loads('{"success":true,"data":{"tickers":[]}}')
        self.assertEqual(res, answer)

    def test_getSubscribingTickers_2(self):
        client = OneXAPI.Binance.Spot()

        res = client.getSubscribingTickers('')
        answer = json.loads('{"success":true,"data":{"tickers":[]}}')
        self.assertEqual(res, answer)

    def test_getSubscribingTickers_3(self):
        client = OneXAPI.Binance.Spot()

        res = client.getSubscribingTickers('{}')
        answer = json.loads('{"success":true,"data":{"tickers":[]}}')
        self.assertEqual(res, answer)

    def test_getSubscribingTickers_4(self):
        client = OneXAPI.Binance.Spot()

        res = client.getSubscribingTickers('Bqbqb@')
        answer = json.loads('{"success":true,"data":{"tickers":[]}}')
        self.assertEqual(res, answer)

    def test_getSubscribingTickers_5(self):
        client = OneXAPI.Binance.Spot()

        client.subscribeTicker('{"market":[{"baseCurrency":"BTC","quoteCurrency":"USDT"},{"baseCurrency":"ETH","quoteCurrency":"BTC"}]}')
        res = client.getSubscribingTickers()
        answer = json.loads('{"success":true,"data":{"tickers":[{"baseCurrency":"BTC","quoteCurrency":"USDT","symbol":"BTCUSDT"},{"baseCurrency":"ETH","quoteCurrency":"BTC","symbol":"ETHBTC"}]}}')
        self.assertEqual(res, answer)

    def test_getSubscribingOrderbooks_1(self):
        client = OneXAPI.Binance.Spot()

        res = client.getSubscribingOrderbooks()
        answer = json.loads('{"success":true,"data":{"orderbooks":[]}}')
        self.assertEqual(res, answer)
    
    def test_getSubscribingOrderbooks_2(self):
        client = OneXAPI.Binance.Spot()

        res = client.getSubscribingOrderbooks('')
        answer = json.loads('{"success":true,"data":{"orderbooks":[]}}')
        self.assertEqual(res, answer)

    def test_getSubscribingOrderbooks_3(self):
        client = OneXAPI.Binance.Spot()

        res = client.getSubscribingOrderbooks('{}')
        answer = json.loads('{"success":true,"data":{"orderbooks":[]}}')
        self.assertEqual(res, answer)

    def test_getSubscribingOrderbooks_4(self):
        client = OneXAPI.Binance.Spot()

        res = client.getSubscribingOrderbooks('Bqbqb@')
        answer = json.loads('{"success":true,"data":{"orderbooks":[]}}')
        self.assertEqual(res, answer)

    def test_getSubscribingOrderbooks_5(self):
        client = OneXAPI.Binance.Spot()

        client.subscribeOrderbook('{"market":[{"baseCurrency":"BTC","quoteCurrency":"USDT"},{"baseCurrency":"ETH","quoteCurrency":"BTC"}]}')
        res = client.getSubscribingOrderbooks()
        answer = json.loads('{"success":true,"data":{"orderbooks":[{"baseCurrency":"BTC","quoteCurrency":"USDT","symbol":"BTCUSDT"},{"baseCurrency":"ETH","quoteCurrency":"BTC","symbol":"ETHBTC"}]}}')
        self.assertEqual(res, answer)

    def test_subscribeTicker_1(self):
        client = OneXAPI.Binance.Spot()

        res = client.subscribeTicker('')
        
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'JSON_PARSING_ERROR')

    def test_subscribeTicker_2(self):
        client = OneXAPI.Binance.Spot()

        res = client.subscribeTicker('{}')
        
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_subscribeTicker_3(self):
        client = OneXAPI.Binance.Spot()

        res = client.subscribeTicker('Bqbqb@')
        
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'JSON_PARSING_ERROR')

    def test_subscribeTicker_4(self):
        client = OneXAPI.Binance.Spot()

        res = client.subscribeTicker('{"market":[{"baseCurrency":"BTC","quoteCurrency":"USDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT"}]}')
        answer = json.loads('{"success":true,"data":{"subscribed":[{"baseCurrency":"BTC","quoteCurrency":"USDT","symbol":"BTCUSDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT","symbol":"ETHUSDT"}],"subscribeFailed":[]}}')

        self.assertEqual(res, answer)

        res = client.getSubscribingTickers()
        answer = json.loads('{"success":true,"data":{"tickers":[{"baseCurrency":"BTC","quoteCurrency":"USDT","symbol":"BTCUSDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT","symbol":"ETHUSDT"}]}}')

        self.assertEqual(res, answer)

        res = client.subscribeTicker('{"market":[{"baseCurrency":"XRP","quoteCurrency":"USDT"}], "reconnect": true}')
        answer = json.loads('{"success":true,"data":{"subscribed":[{"baseCurrency":"XRP","quoteCurrency":"USDT","symbol":"XRPUSDT"}],"subscribeFailed":[]}}')

        self.assertEqual(res, answer)

        res = client.getSubscribingTickers()
        answer = json.loads('{"success":true,"data":{"tickers":[{"baseCurrency":"BTC","quoteCurrency":"USDT","symbol":"BTCUSDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT","symbol":"ETHUSDT"},{"baseCurrency":"XRP","quoteCurrency":"USDT","symbol":"XRPUSDT"}]}}')

        self.assertEqual(res, answer)

    def test_unsubscribeTicker_1(self):
        client = OneXAPI.Binance.Spot()

        res = client.unsubscribeTicker('')
        
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'JSON_PARSING_ERROR')

    def test_unsubscribeTicker_2(self):
        client = OneXAPI.Binance.Spot()

        res = client.unsubscribeTicker('{}')
        
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_unsubscribeTicker_3(self):
        client = OneXAPI.Binance.Spot()

        res = client.unsubscribeTicker('Bqbqb@')
        
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'JSON_PARSING_ERROR')

    def test_unsubscribeTicker_4(self):
        client = OneXAPI.Binance.Spot()

        client.subscribeTicker('{"market":[{"baseCurrency":"BTC","quoteCurrency":"USDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT"}]}')
        res = client.unsubscribeTicker('{"market":[{"baseCurrency":"BTC","quoteCurrency":"USDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT"}]}')
        answer = json.loads('{"success":true,"data":{"unsubscribed":[{"baseCurrency":"BTC","quoteCurrency":"USDT","symbol":"BTCUSDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT","symbol":"ETHUSDT"}],"unsubscribeFailed":[]}}')

        self.assertEqual(res, answer)

    def test_unsubscribeTicker_5(self):
        client = OneXAPI.Binance.Spot()

        client.subscribeTicker('{"market":[{"baseCurrency":"BTC","quoteCurrency":"USDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT"}]}')
        res = client.unsubscribeTicker('{"market":[{"baseCurrency":"BTC","quoteCurrency":"USDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT"}],"reconnect":true}')
        answer = json.loads('{"success":true,"data":{"unsubscribed":[{"baseCurrency":"BTC","quoteCurrency":"USDT","symbol":"BTCUSDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT","symbol":"ETHUSDT"}],"unsubscribeFailed":[]}}')

        self.assertEqual(res, answer)

    def test_subscribeOrderbook_1(self):
        client = OneXAPI.Binance.Spot()

        res = client.subscribeOrderbook('')
        
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'JSON_PARSING_ERROR')

    def test_subscribeOrderbook_2(self):
        client = OneXAPI.Binance.Spot()

        res = client.subscribeOrderbook('{}')
        
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_subscribeOrderbook_3(self):
        client = OneXAPI.Binance.Spot()

        res = client.subscribeOrderbook('Bqbqb@')
        
        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'JSON_PARSING_ERROR')

    def test_subscribeOrderbook_4(self):
        client = OneXAPI.Binance.Spot()

        res = client.subscribeOrderbook('{"market":[{"baseCurrency":"BTC","quoteCurrency":"USDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT"}]}')
        answer = json.loads('{"success":true,"data":{"subscribed":[{"baseCurrency":"BTC","quoteCurrency":"USDT","symbol":"BTCUSDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT","symbol":"ETHUSDT"}],"subscribeFailed":[]}}')

        self.assertDictEqual(res, answer)

        res = client.getSubscribingOrderbooks()
        answer = json.loads('{"success":true,"data":{"orderbooks":[{"baseCurrency":"BTC","quoteCurrency":"USDT","symbol":"BTCUSDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT","symbol":"ETHUSDT"}]}}')

        res = client.subscribeOrderbook('{"market":[{"baseCurrency":"XRP","quoteCurrency":"USDT"}], "reconnect": true}')
        answer = json.loads('{"success":true,"data":{"subscribed":[{"baseCurrency":"XRP","quoteCurrency":"USDT","symbol":"XRPUSDT"}],"subscribeFailed":[]}}')

        res = client.getSubscribingOrderbooks()
        answer = json.loads('{"success":true,"data":{"orderbooks":[{"baseCurrency":"BTC","quoteCurrency":"USDT","symbol":"BTCUSDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT","symbol":"ETHUSDT"},{"baseCurrency":"XRP","quoteCurrency":"USDT","symbol":"XRPUSDT"}]}}')

    def test_unsubscribeOrderbook_1(self):
        client = OneXAPI.Binance.Spot()

        res = client.unsubscribeOrderbook('')

        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'JSON_PARSING_ERROR')

    def test_unsubscribeOrderbook_2(self):
        client = OneXAPI.Binance.Spot()

        res = client.unsubscribeOrderbook('{}')

        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'NOT_ENOUGH_PARAM')

    def test_unsubscribeOrderbook_3(self):
        client = OneXAPI.Binance.Spot()

        res = client.unsubscribeOrderbook('Bqbqb@')

        self.assertEqual(res['success'], False)
        self.assertEqual(res['data']['errorType'], 'JSON_PARSING_ERROR')

    def test_unsubscribeOrderbook_4(self):
        client = OneXAPI.Binance.Spot()

        client.subscribeOrderbook('{"market":[{"baseCurrency":"BTC","quoteCurrency":"USDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT"}]}')
        res = client.unsubscribeOrderbook('{"market":[{"baseCurrency":"BTC","quoteCurrency":"USDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT"}]}')
        answer = json.loads('{"success":true,"data":{"unsubscribed":[{"baseCurrency":"BTC","quoteCurrency":"USDT","symbol":"BTCUSDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT","symbol":"ETHUSDT"}],"unsubscribeFailed":[]}}')

        self.assertDictEqual(res, answer)

    def test_unsubscribeOrderbook_5(self):
        client = OneXAPI.Binance.Spot()

        client.subscribeOrderbook('{"market":[{"baseCurrency":"BTC","quoteCurrency":"USDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT"}]}')
        res = client.unsubscribeOrderbook('{"market":[{"baseCurrency":"BTC","quoteCurrency":"USDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT"}],"reconnect":true}')
        answer = json.loads('{"success":true,"data":{"unsubscribed":[{"baseCurrency":"BTC","quoteCurrency":"USDT","symbol":"BTCUSDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT","symbol":"ETHUSDT"}],"unsubscribeFailed":[]}}')

        self.assertDictEqual(res, answer)

    def test_websocketFullTest(self):
        client = OneXAPI.Binance.Spot()

        res = client.subscribeTicker('{"market":[{"baseCurrency":"BTC","quoteCurrency":"USDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT"}]}')
        answer = json.loads('{"success":true,"data":{"subscribed":[{"baseCurrency":"BTC","quoteCurrency":"USDT","symbol":"BTCUSDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT","symbol":"ETHUSDT"}],"subscribeFailed":[]}}')

        self.assertDictEqual(res, answer)

        res = client.getSubscribingTickers()
        answer = json.loads('{"success":true,"data":{"tickers":[{"baseCurrency":"BTC","quoteCurrency":"USDT","symbol":"BTCUSDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT","symbol":"ETHUSDT"}]}}')

        self.assertDictEqual(res, answer)

        res = client.subscribeOrderbook('{"market":[{"baseCurrency":"BTC","quoteCurrency":"USDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT"}],"reconnect":true}')
        answer = json.loads('{"success":true,"data":{"subscribed":[{"baseCurrency":"BTC","quoteCurrency":"USDT","symbol":"BTCUSDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT","symbol":"ETHUSDT"}],"subscribeFailed":[]}}')

        self.assertDictEqual(res, answer)

        res = client.getSubscribingTickers()
        answer = json.loads('{"success":true,"data":{"tickers":[{"baseCurrency":"BTC","quoteCurrency":"USDT","symbol":"BTCUSDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT","symbol":"ETHUSDT"}]}}')

        self.assertDictEqual(res, answer)

        res = client.getSubscribingOrderbooks()
        answer = json.loads('{"success":true,"data":{"orderbooks":[{"baseCurrency":"BTC","quoteCurrency":"USDT","symbol":"BTCUSDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT","symbol":"ETHUSDT"}]}}')

        self.assertDictEqual(res, answer)

        res = client.unsubscribeTicker('{"market":[{"baseCurrency":"BTC","quoteCurrency":"USDT"}],"reconnect":true}')
        answer = json.loads('{"success":true,"data":{"unsubscribed":[{"baseCurrency":"BTC","quoteCurrency":"USDT","symbol":"BTCUSDT"}],"unsubscribeFailed":[]}}')

        self.assertDictEqual(res, answer)

        res = client.getSubscribingTickers()
        answer = json.loads('{"success":true,"data":{"tickers":[{"baseCurrency":"ETH","quoteCurrency":"USDT","symbol":"ETHUSDT"}]}}')

        self.assertDictEqual(res, answer)

        res = client.getSubscribingOrderbooks()
        answer = json.loads('{"success":true,"data":{"orderbooks":[{"baseCurrency":"BTC","quoteCurrency":"USDT","symbol":"BTCUSDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT","symbol":"ETHUSDT"}]}}')

        self.assertDictEqual(res, answer)

        res = client.unsubscribeOrderbook('{"market":[{"baseCurrency":"ETH","quoteCurrency":"USDT"}],"reconnect":true}')
        answer = json.loads('{"success":true,"data":{"unsubscribed":[{"baseCurrency":"ETH","quoteCurrency":"USDT","symbol":"ETHUSDT"}],"unsubscribeFailed":[]}}')

        self.assertDictEqual(res, answer)

        res = client.getSubscribingTickers()
        answer = json.loads('{"success":true,"data":{"tickers":[{"baseCurrency":"ETH","quoteCurrency":"USDT","symbol":"ETHUSDT"}]}}')

        self.assertDictEqual(res, answer)

        res = client.getSubscribingOrderbooks()
        answer = json.loads('{"success":true,"data":{"orderbooks":[{"baseCurrency":"BTC","quoteCurrency":"USDT","symbol":"BTCUSDT"}]}}')

        self.assertDictEqual(res, answer)

        res = client.subscribeOrderbook('{"market":[{"baseCurrency":"XRP","quoteCurrency":"USDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT"}],"reconnect":true}')
        answer = json.loads('{"success":true,"data":{"subscribed":[{"baseCurrency":"XRP","quoteCurrency":"USDT","symbol":"XRPUSDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT","symbol":"ETHUSDT"}],"subscribeFailed":[]}}')

        self.assertDictEqual(res, answer)

        res = client.getSubscribingTickers()
        answer = json.loads('{"success":true,"data":{"tickers":[{"baseCurrency":"ETH","quoteCurrency":"USDT","symbol":"ETHUSDT"}]}}')

        self.assertDictEqual(res, answer)

        res = client.getSubscribingOrderbooks()
        answer = json.loads('{"success":true,"data":{"orderbooks":[{"baseCurrency":"BTC","quoteCurrency":"USDT","symbol":"BTCUSDT"},{"baseCurrency":"XRP","quoteCurrency":"USDT","symbol":"XRPUSDT"},{"baseCurrency":"ETH","quoteCurrency":"USDT","symbol":"ETHUSDT"}]}}')



if __name__ == "__main__":
    import os
    filepath = './OneXAPI_Logs/OneXAPI_' + time.strftime('%Y-%m-%d', time.localtime(time.time())) + '.log'
    
    if os.path.exists(filepath):
        os.remove(filepath)

    unittest.main()