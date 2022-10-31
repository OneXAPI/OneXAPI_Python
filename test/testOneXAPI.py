import OneXAPI
import unittest
import sys, os, time
import json

class oneXAPITest(unittest.TestCase):
    def test_OneXAPI_getInfo_1(self):

        res = OneXAPI.getInfo()
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"supportedExchanges":[{"exchange":"Binance","instrument":"Spot"},{"exchange":"Binance","instrument":"Futures"},{"exchange":"Upbit","instrument":"Spot"}],"onexapiVersion":"0.0.2"}}')

        self.assertEqual(res, answer)
    
    def test_OneXAPI_getInfo_2(self):

        res = OneXAPI.getInfo('')
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"supportedExchanges":[{"exchange":"Binance","instrument":"Spot"},{"exchange":"Binance","instrument":"Futures"},{"exchange":"Upbit","instrument":"Spot"}],"onexapiVersion":"0.0.2"}}')

        self.assertEqual(res, answer)

    def test_OneXAPI_getInfo_3(self):

        res = OneXAPI.getInfo('{}')
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"supportedExchanges":[{"exchange":"Binance","instrument":"Spot"},{"exchange":"Binance","instrument":"Futures"},{"exchange":"Upbit","instrument":"Spot"}],"onexapiVersion":"0.0.2"}}')

        self.assertEqual(res, answer)

    def test_OneXAPI_getInfo_4(self):

        res = OneXAPI.getInfo('2gasdv@')

        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], False)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['errorType'], "JSON_PARSING_ERROR")

    def test_OneXAPI_getLoggerConfig_1(self):

        res = OneXAPI.getLoggerConfig()
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"main":{"outputMethod":"terminal","logLevel":"off"},"websocket":{"outputMethod":"terminal","logLevel":"off"}}}')

        self.assertEqual(res, answer)
    
    def test_OneXAPI_getLoggerConfig_2(self):

        res = OneXAPI.getLoggerConfig('')
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"main":{"outputMethod":"terminal","logLevel":"off"},"websocket":{"outputMethod":"terminal","logLevel":"off"}}}')

        self.assertEqual(res, answer)

    def test_OneXAPI_getLoggerConfig_3(self):

        res = OneXAPI.getLoggerConfig('{}')
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"main":{"outputMethod":"terminal","logLevel":"off"},"websocket":{"outputMethod":"terminal","logLevel":"off"}}}')

        self.assertEqual(res, answer)

    def test_OneXAPI_getLoggerConfig_4(self):

        res = OneXAPI.getLoggerConfig('2gasdv@')

        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], False)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['errorType'], "JSON_PARSING_ERROR")

    def test_OneXAPI_setLoggerConfig_1(self):

        res = OneXAPI.setLoggerConfig('')
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{}}')

    def test_OneXAPI_setLoggerConfig_2(self):

        res = OneXAPI.setLoggerConfig('{}')
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{}}')

    def test_OneXAPI_setLoggerConfig_3(self):

        res = OneXAPI.setLoggerConfig('2gasdv@')
        
        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], False)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['errorType'], "JSON_PARSING_ERROR")

    def test_OneXAPI_setLoggerConfig_4(self):

        res = OneXAPI.setLoggerConfig('{"main":["1","2"],"websocket":{"logLevel": "test","outputMethod": 22}}')

        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], False)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['errorType'], "WRONG_VALUE_TYPE")

    def test_OneXAPI_setLoggerConfig_5(self):

        res = OneXAPI.setLoggerConfig('{"main":{"outputMethod": "file", "logLevel": "test"},"websocket":{"outputMethod": "terminal", "logLevel": "test"}}')

        self.assertEqual(len(res), 3)
        self.assertEqual(res['success'], False)
        self.assertEqual(res['requestedApiCount'], 0)
        self.assertEqual(res['data']['errorType'], "WRONG_VALUE")

    def test_OneXAPI_setLoggerConfig_6(self):

        res = OneXAPI.setLoggerConfig('{"main":{"outputMethod": "file", "logLevel": "info"},"websocket":{"outputMethod": "terminal", "logLevel": "error"}}')
        answer = json.loads('{"success":true,"requestedApiCount":0,"data":{"main":{"outputMethod":"file","logLevel":"info"},"websocket":{"outputMethod":"terminal","logLevel":"error"}}}')
        OneXAPI.setLoggerConfig('{"main":{"outputMethod": "terminal", "logLevel": "off"},"websocket":{"outputMethod": "terminal", "logLevel": "off"}}')
        self.assertEqual(res, answer)


if __name__ == "__main__":
    unittest.main()