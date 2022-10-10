from turtle import fd
import OneXAPI
from config import *

import time, logging
import prettytable as pt

clients = dict()
clients["Spot"] = []
clients["Futures"] = []
clients_info = dict()
clients_info["Spot"] = []
clients_info["Futures"] = []

asset_data = dict()
asset_data["Spot"] = dict()
asset_data["Futures"] = dict()


# Logger setting
logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('[%(asctime)s][%(levelname)s|%(filename)s:%(lineno)s] %(message)s')
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

def init_variables():
    asset_data["Spot"]["header"]=[]
    asset_data["Spot"]["amount"]={}
    asset_data["Spot"]["value"]=[]
    
    asset_data["Futures"]["header"]=[]
    asset_data["Futures"]["positions"]={}
    asset_data["Futures"]["unrealizedPnl"]={}
    asset_data["Futures"]["amount"]={}
    asset_data["Futures"]["value"]=[]
    
    OneXAPI_info = OneXAPI.getInfo()
    
    if not OneXAPI_info["success"]:
        logger.error("OneXAPI.getInfo() failed   response : " + str(OneXAPI_info))
        exit()
    
    for account in accounts:
        exchange = account["exchange"].capitalize()
        instrument = account["instrument"].capitalize()
        
        if {"exchange":exchange,"instrument":instrument} not in OneXAPI_info["data"]["supportedExchanges"]:
            logger.error("Not supported exchange or instrument! Pair : " + exchange + " & " + instrument)
            exit()
        
        clients[instrument].append(getattr(getattr(OneXAPI, exchange),instrument)(account))
        clients_info[instrument].append(account)
        if "nickname" not in account.keys() or account["nickname"] == "":
            asset_data[instrument]["header"].append(account["exchange"] + " " + account["instrument"])
        else:
            asset_data[instrument]["header"].append(account["nickname"])

def subscribe_balance():
    try:
        for client in clients["Spot"] + clients["Futures"]:
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
            asset_data["Spot"]["amount"].clear()
            asset_data["Futures"]["positions"].clear()
            asset_data["Futures"]["unrealizedPnl"].clear()
            asset_data["Futures"]["amount"].clear()
            
            # Spot
            for client_idx, client in enumerate(clients["Spot"]):
                balance_resp = client.fetchBalance({})
                if balance_resp["success"]:
                    for currency in balance_resp["data"]["balance"]:
                        if currency not in asset_data["Spot"]["amount"]:
                            asset_data["Spot"]["amount"][currency] = []
                            for i in range(client_idx):
                                asset_data["Spot"]["amount"][currency].append(0.0)
                        amount = float(balance_resp["data"]["balance"][currency]["free"]) + float(balance_resp["data"]["balance"][currency]["locked"])
                        asset_data["Spot"]["amount"][currency].append(amount)
                    for currency in asset_data["Spot"]["amount"]:
                        if len(asset_data["Spot"]["amount"][currency]) < client_idx + 1:
                            asset_data["Spot"]["amount"][currency].append(0.0)
                    if balance_resp["data"]["requestedApiCount"] > 0:
                        time.sleep(0.5)     # Wait for avoiding rate limit
                else:
                    raise Exception("Spot fetchBalance() failed, message is '" + str(balance_resp) + "'")
                
            # Futures
            for client_idx, client in enumerate(clients["Futures"]):
                positions_resp = client.fetchPositions({})
                if positions_resp["success"]:
                    for position in positions_resp["data"]["positions"]:
                        # positionAmt
                        if position["symbol"] not in asset_data["Futures"]["positions"]:
                            asset_data["Futures"]["positions"][position["symbol"]] = []
                            for i in range(client_idx):
                                asset_data["Futures"]["positions"][position["symbol"]].append(0.0)
                        asset_data["Futures"]["positions"][position["symbol"]].append(float(position["positionAmt"]))
                        # unrealizedPnl
                        if position["quoteCurrency"] not in asset_data["Futures"]["unrealizedPnl"]:
                            asset_data["Futures"]["unrealizedPnl"][position["quoteCurrency"]] = []
                        for i in range(client_idx + 1):
                            asset_data["Futures"]["unrealizedPnl"][position["quoteCurrency"]].append(0.0)
                        asset_data["Futures"]["unrealizedPnl"][position["quoteCurrency"]][-1] += float(position["unrealizedProfit"])
                    for symbol in asset_data["Futures"]["positions"]:
                        if len(asset_data["Futures"]["positions"][symbol]) < client_idx + 1:
                            asset_data["Futures"]["positions"][symbol].append(0.0)
                    if positions_resp["data"]["requestedApiCount"] > 0:
                        time.sleep(0.5)     # Wait for avoiding rate limit
                else:
                    raise Exception("Futures fetchPositions() failed, message is '" + str(positions_resp) + "'")
                
                
                balance_resp = client.fetchBalance({})
                if balance_resp["success"]:
                    for currency in balance_resp["data"]["balance"]:
                        if currency not in asset_data["Futures"]["amount"]:
                            asset_data["Futures"]["amount"][currency] = []
                            for i in range(client_idx):
                                asset_data["Futures"]["amount"][currency].append(0.0)
                        amount = float(balance_resp["data"]["balance"][currency]["balance"])
                        asset_data["Futures"]["amount"][currency].append(amount)
                    for currency in asset_data["Futures"]["amount"]:
                        if len(asset_data["Futures"]["amount"][currency]) < client_idx + 1:
                            asset_data["Futures"]["amount"][currency].append(0.0)
                    if balance_resp["data"]["requestedApiCount"] > 0:
                        time.sleep(0.5)     # Wait for avoiding rate limit
                else:
                    raise Exception("Futures fetchBalance() failed, message is '" + str(balance_resp) + "'")
                
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
            for client_idx, client in enumerate(clients["Spot"]):
                query = dict()
                query["market"] = []
                for currency in asset_data["Spot"]["amount"]:
                    query["market"].append({"baseCurrency":currency,"quoteCurrency":clients_info["Spot"][client_idx]["value_currency"]})
                subscribeOrderbook_resp = client.subscribeOrderbook(query)
                if not subscribeOrderbook_resp["success"]:
                    raise Exception("Spot subscribeOrderbook() failed, message is '" + str(subscribeOrderbook_resp) + "'")
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
            asset_data["Spot"]["value"].clear()
            asset_data["Futures"]["value"].clear()
            
            # Spot
            for client_idx, client in enumerate(clients["Spot"]):
                markets_resp = client.fetchMarkets({})
                markets = []
                if markets_resp["success"]:
                    for market in markets_resp["data"]["markets"]:
                        markets.append([market["baseCurrency"], market["quoteCurrency"]])
                else:
                    raise Exception("Spot fetchMarkets() failed, message is '" + str(markets_resp) + "'")
                
                value = 0.0
                clients_info["Spot"][client_idx]["cannot_find_market"] = []
                
                for currency in asset_data["Spot"]["amount"]:
                    if asset_data["Spot"]["amount"][currency][client_idx] == 0:
                        continue
                    elif [currency, clients_info["Spot"][client_idx]["value_currency"].upper()] in markets:
                        query = {
                            "baseCurrency" : currency,
                            "quoteCurrency" : clients_info["Spot"][client_idx]["value_currency"]
                        }
                        fetchOrderbook_resp = client.fetchOrderbook(query)
                        
                        if not fetchOrderbook_resp["success"]:
                            raise Exception("Spot fetchOrderbook() failed, message is '" + str(fetchOrderbook_resp) + "'")
                        
                        bid = float(fetchOrderbook_resp["data"]["bids"][0]["price"])
                        
                        value += asset_data["Spot"]["amount"][currency][client_idx] * bid
                        
                        if fetchOrderbook_resp["data"]["requestedApiCount"] > 0:
                            time.sleep(0.5)     # Wait for avoiding rate limit
                    elif currency == clients_info["Spot"][client_idx]["value_currency"].upper():
                        value += asset_data["Spot"]["amount"][currency][client_idx]
                    else:
                        clients_info["Spot"][client_idx]["cannot_find_market"].append(currency)
                            
                asset_data["Spot"]["value"].append(value)
                
            # Futures
            for client_idx, client in enumerate(clients["Futures"]):
                markets_resp = client.fetchMarkets({})
                markets = []
                if markets_resp["success"]:
                    for market in markets_resp["data"]["markets"]:
                        markets.append([market["baseCurrency"], market["quoteCurrency"], market["expiration"]])
                else:
                    raise Exception("Futures fetchMarkets() failed, message is '" + str(markets_resp) + "'")
                
                value = 0.0
                for currency in asset_data["Futures"]["unrealizedPnl"]:
                    asset_data["Futures"]["amount"][currency][client_idx] += asset_data["Futures"]["unrealizedPnl"][currency][client_idx]
                
                clients_info["Futures"][client_idx]["cannot_find_market"] = []
                
                for currency in asset_data["Futures"]["amount"]:
                    if asset_data["Futures"]["amount"][currency][client_idx] == 0:
                        continue
                    elif [currency, clients_info["Futures"][client_idx]["value_currency"].upper(), "PERP"] in markets:
                        query = {
                            "baseCurrency" : currency,
                            "quoteCurrency" : clients_info["Futures"][client_idx]["value_currency"]
                        }
                        fetchOrderbook_resp = client.fetchOrderbook(query)
                        
                        if not fetchOrderbook_resp["success"]:
                            raise Exception("Futures fetchOrderbook() failed, message is '" + str(fetchOrderbook_resp) + "'")
                        
                        bid = float(fetchOrderbook_resp["data"]["bids"][0]["price"])
                        
                        value += asset_data["Futures"]["amount"][currency][client_idx] * bid
                        
                        if fetchOrderbook_resp["data"]["requestedApiCount"] > 0:
                            time.sleep(0.5)     # Wait for avoiding rate limit
                    elif currency == clients_info["Futures"][client_idx]["value_currency"].upper():
                        value += asset_data["Futures"]["amount"][currency][client_idx]
                    else:
                        clients_info["Futures"][client_idx]["cannot_find_market"].append(currency)
                
                asset_data["Futures"]["value"].append(value)
                
            break
                
        except Exception as e:
            logger.error("Exception in " + calc_asset_value.__name__ + "(), error : " + str(e))
            fetch_try += 1
            if fetch_try >= 5:
                logger.error("Program exit")
                exit()

def print_assets():
    ### Spot ###
    print("****** SPOT ******")
    tb_spot = pt.PrettyTable()
    header = ["Nickname"]
    for nickname in asset_data["Spot"]["header"]:
        header.append(nickname)
    tb_spot.field_names = header
    for currency in asset_data["Spot"]["amount"]:
        data = [currency] + asset_data["Spot"]["amount"][currency]
        tb_spot.add_row(data)
    empty_row = ["--------"]
    footer = ["value"]
    for value_idx, value in enumerate(asset_data["Spot"]["value"]):
        empty_row.append("------------")
        footer.append(str(value) + " " + clients_info["Spot"][value_idx]["value_currency"])
    tb_spot.add_row(empty_row)
    tb_spot.add_row(footer)
    print(tb_spot)
    
    # Not calculated currencies. Currencies in the list below are not listed on the market.
    print("*** Currencies which are not calculated in the asset value above ***")
    for nickname_idx, nickname in enumerate(asset_data["Spot"]["header"]):
        if len(clients_info["Spot"][nickname_idx]["cannot_find_market"]) == 0:
            continue
        print(nickname + " : " + ", ".join(clients_info["Spot"][nickname_idx]["cannot_find_market"]))

    print("")
    print("")
    
    ### Futures ###
    print("****** FUTURES ******")
    print("*** Positions ***")
    tb_futures_position = pt.PrettyTable()
    header = ["Nickname"]
    for nickname in asset_data["Futures"]["header"]:
        header.append(nickname)
    tb_futures_position.field_names = header
    
    for symbol in asset_data["Futures"]["positions"]:
        data = [symbol] + asset_data["Futures"]["positions"][symbol]
        tb_futures_position.add_row(data)
    print(tb_futures_position)
    
    print("")
    print("*** Asset ***")
    tb_futures_asset = pt.PrettyTable()
    header = ["Nickname"]
    for nickname in asset_data["Futures"]["header"]:
        header.append(nickname)
    tb_futures_asset.field_names = header
    for currency in asset_data["Futures"]["amount"]:
        data = [currency] + asset_data["Futures"]["amount"][currency]
        tb_futures_asset.add_row(data)
    empty_row = ["--------"]
    footer = ["value"]
    for value_idx, value in enumerate(asset_data["Futures"]["value"]):
        empty_row.append("------------")
        footer.append(str(value) + " " + clients_info["Futures"][value_idx]["value_currency"])
    tb_futures_asset.add_row(empty_row)
    tb_futures_asset.add_row(footer)
    print(tb_futures_asset)
    
    # Not calculated currencies. Currencies in the list below are not listed on the market.
    print("*** Currencies which are not calculated in the asset value above ***")
    for nickname_idx, nickname in enumerate(asset_data["Futures"]["header"]):
        if len(clients_info["Futures"][nickname_idx]["cannot_find_market"]) == 0:
            continue
        print(nickname + " : " + ", ".join(clients_info["Futures"][nickname_idx]["cannot_find_market"]))


if __name__ == "__main__":
    logger.info("Reporter is started")
    init_variables()
    
    subscribe_balance()
    fetch_asset_data()
    subscribe_orderbook()
    calc_asset_value()
    
    print_assets()
    
