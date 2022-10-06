from turtle import fd
import OneXAPI
from config import *

import time, logging

spot_clients = []
spot_clients_info = []
futures_clients = []
futures_clients_info = []

spot_asset = dict()
futures_asset = dict()


# Logger setting
logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('[%(asctime)s][%(levelname)s|%(filename)s:%(lineno)s] %(message)s')
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

def init_variables():
    spot_asset["header"]=[]
    spot_asset["amount"]={}
    spot_asset["value"]=[]
    
    futures_asset["header"]=[]
    futures_asset["positions"]={}
    futures_asset["amount"]={}
    futures_asset["value"]=[]
    
    for account in accounts:    
        if account["exchange"].upper() == "UPBIT":
            if account["instrument"].upper() != "SPOT":
                logger.error("Upbit instrument must be spot")
                exit()
            spot_clients.append(OneXAPI.Upbit.Spot(account))
            spot_clients_info.append(account)
            if "nickname" not in account.keys() or account["nickname"] == "":
                spot_asset["header"].append(account["exchange"] + " " + account["instrument"])
            else:
                spot_asset["header"].append(account["nickname"])
        elif account["exchange"].upper() == "BINANCE":
            if account["instrument"].upper() == "SPOT":
                spot_clients.append(OneXAPI.Binance.Spot(account))
                spot_clients_info.append(account)
                if "nickname" not in account.keys() or account["nickname"] == "":
                    spot_asset["header"].append(account["exchange"] + " " + account["instrument"])
                else:
                    spot_asset["header"].append(account["nickname"])
            elif account["instrument"].upper() == "FUTURES":
                futures_clients.append(OneXAPI.Binance.Futures(account))
                futures_clients_info.append(account)
                if "nickname" not in account.keys() or account["nickname"] == "":
                    futures_asset["header"].append(account["exchange"] + " " + account["instrument"])
                else:
                    futures_asset["header"].append(account["nickname"])
            else:
                logger.error("Binance instrument must be spot or futures")
                exit()
        else:
            logger.error("Exchange must be upbit or binance")
            exit()

def subscribe_balance():
    try:
        for client in spot_clients + futures_clients:
            has_check = client.has({"api":"subscribeBalance"})
            if has_check["success"]:
                if has_check["data"]["subscribeBalance"]:
                    client.subscribeBalance()
        time.sleep(3)                   # Waiting for receiving balance data
    except Exception as e:
        logger.error("Exception in " + subscribe_balance.__name__ + "(), error : " + str(e))

def fetch_asset_data():
    fetch_try = 0
    while True:
        try:
            spot_asset["amount"].clear()
            futures_asset["positions"].clear()
            futures_asset["amount"].clear()
            
            # Spot
            for client_idx, client in enumerate(spot_clients):
                balance_resp = client.fetchBalance({})
                if balance_resp["success"]:
                    for currency in balance_resp["data"]["balance"]:
                        if currency not in spot_asset["amount"]:
                            spot_asset["amount"][currency] = []
                            for i in range(client_idx):
                                spot_asset["amount"][currency].append(0.0)
                        amount = float(balance_resp["data"]["balance"][currency]["free"]) + float(balance_resp["data"]["balance"][currency]["locked"])
                        spot_asset["amount"][currency].append(amount)
                    for currency in spot_asset["amount"]:
                        if len(spot_asset["amount"][currency]) < client_idx + 1:
                            spot_asset["amount"][currency].append(0.0)
                    if balance_resp["data"]["requestedApiCount"] > 0:
                        time.sleep(0.5)     # Wait for avoiding rate limit
                else:
                    raise Exception("Spot fetchBalance() failed, message is '" + balance_resp + "'")
                
            # Futures
            for client_idx, client in enumerate(futures_clients):
                positions_resp = client.fetchPositions({})
                if positions_resp["success"]:
                    for position in positions_resp["data"]["positions"]:
                        if position["symbol"] not in futures_asset["positions"]:
                            futures_asset["positions"][position["symbol"]] = []
                            for i in range(client_idx):
                                futures_asset["positions"][position["symbol"]].append(0.0)
                        futures_asset["positions"][position["symbol"]].append(float(position["positionAmt"]))
                    for symbol in futures_asset["positions"]:
                        if len(futures_asset["positions"][symbol]) < client_idx + 1:
                            futures_asset["positions"][symbol].append(0.0)
                    if positions_resp["data"]["requestedApiCount"] > 0:
                        time.sleep(0.5)     # Wait for avoiding rate limit
                else:
                    raise Exception("Futures fetchPositions() failed, message is '" + positions_resp + "'")
                
                
                balance_resp = client.fetchBalance({})
                if balance_resp["success"]:
                    for currency in balance_resp["data"]["balance"]:
                        if currency not in futures_asset["amount"]:
                            futures_asset["amount"][currency] = []
                            for i in range(client_idx):
                                futures_asset["amount"][currency].append(0.0)
                        amount = float(balance_resp["data"]["balance"][currency]["balance"])
                        futures_asset["amount"][currency].append(amount)
                    for currency in futures_asset["amount"]:
                        if len(futures_asset["amount"][currency]) < client_idx + 1:
                            futures_asset["amount"][currency].append(0.0)
                    if balance_resp["data"]["requestedApiCount"] > 0:
                        time.sleep(0.5)     # Wait for avoiding rate limit
                else:
                    raise Exception("Futures fetchBalance() failed, message is '" + balance_resp + "'")
                
            break
                
        except Exception as e:
            logger.error("Exception in " + fetch_asset_data.__name__ + "(), error : " + str(e))
            fetch_try += 1
            if fetch_try >= 5:
                logger.error("Program exit")
                exit()

def subscribe_orderbook():
    subscribe_try = 0
    while True:
        try:
            for client_idx, client in enumerate(spot_clients):
                query = dict()
                query["market"] = []
                for currency in spot_asset["amount"]:
                    query["market"].append({"baseCurrency":currency,"quoteCurrency":spot_clients_info[client_idx]["value_currency"]})
                subscribeOrderbook_resp = client.subscribeOrderbook(query)
                if not subscribeOrderbook_resp["success"]:
                    logger.info(subscribeOrderbook_resp)
            time.sleep(3)                   # Waiting for receiving orderbook data
            break
        except Exception as e:
            logger.error("Exception in " + subscribe_orderbook.__name__ + "(), error : " + str(e))
            subscribe_try += 1
            if subscribe_try >= 5:
                break

def calc_asset_value():
    fetch_try = 0
    while True:
        try:
            # Spot
            for client_idx, client in enumerate(spot_clients):
                markets_resp = client.fetchMarkets({})
                logger.info(markets_resp)
                
                '''
                balance_resp = client.fetchBalance({})
                if balance_resp["success"]:
                    for currency in balance_resp["data"]["balance"]:
                        if currency not in spot_asset["amount"]:
                            spot_asset["amount"][currency] = []
                            for i in range(client_idx):
                                spot_asset["amount"][currency].append(0.0)
                        amount = float(balance_resp["data"]["balance"][currency]["free"]) + float(balance_resp["data"]["balance"][currency]["locked"])
                        spot_asset["amount"][currency].append(amount)
                    for currency in spot_asset["amount"]:
                        if len(spot_asset["amount"][currency]) < client_idx + 1:
                            spot_asset["amount"][currency].append(0.0)
                    if balance_resp["data"]["requestedApiCount"] > 0:
                        time.sleep(0.5)     # Wait for avoiding rate limit
                else:
                    raise Exception("Spot fetchBalance() failed, message is '" + balance_resp + "'")
                '''
                
            # # Futures
            # for client_idx, client in enumerate(futures_clients):
            #     positions_resp = client.fetchPositions({})
            #     if positions_resp["success"]:
            #         for position in positions_resp["data"]["positions"]:
            #             if position["symbol"] not in futures_asset["positions"]:
            #                 futures_asset["positions"][position["symbol"]] = []
            #                 for i in range(client_idx):
            #                     futures_asset["positions"][position["symbol"]].append(0.0)
            #             futures_asset["positions"][position["symbol"]].append(float(position["positionAmt"]))
            #         for symbol in futures_asset["positions"]:
            #             if len(futures_asset["positions"][symbol]) < client_idx + 1:
            #                 futures_asset["positions"][symbol].append(0.0)
            #         if positions_resp["data"]["requestedApiCount"] > 0:
            #             time.sleep(0.5)     # Wait for avoiding rate limit
            #     else:
            #         raise Exception("Futures fetchPositions() failed, message is '" + positions_resp + "'")
                
                
            #     balance_resp = client.fetchBalance({})
            #     if balance_resp["success"]:
            #         for currency in balance_resp["data"]["balance"]:
            #             if currency not in futures_asset["amount"]:
            #                 futures_asset["amount"][currency] = []
            #                 for i in range(client_idx):
            #                     futures_asset["amount"][currency].append(0.0)
            #             amount = float(balance_resp["data"]["balance"][currency]["balance"])
            #             futures_asset["amount"][currency].append(amount)
            #         for currency in futures_asset["amount"]:
            #             if len(futures_asset["amount"][currency]) < client_idx + 1:
            #                 futures_asset["amount"][currency].append(0.0)
            #         if balance_resp["data"]["requestedApiCount"] > 0:
            #             time.sleep(0.5)     # Wait for avoiding rate limit
            #     else:
            #         raise Exception("Futures fetchBalance() failed, message is '" + balance_resp + "'")
                
            break
                
        except Exception as e:
            logger.error("Exception in " + calc_asset_value.__name__ + "(), error : " + str(e))
            fetch_try += 1
            if fetch_try >= 5:
                logger.error("Program exit")
                exit()


if __name__ == "__main__":
    logger.info("Reporter is started")
    init_variables()
    
    subscribe_balance()
    fetch_asset_data()
    subscribe_orderbook()
    calc_asset_value()
    print(spot_asset)
    print(futures_asset)
