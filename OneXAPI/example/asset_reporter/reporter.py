from turtle import fd
import OneXAPI
from config import *

import time, logging
import prettytable as pt

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
    futures_asset["unrealizedPnl"]={}
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
            futures_asset["unrealizedPnl"].clear()
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
                    raise Exception("Spot fetchBalance() failed, message is '" + str(balance_resp) + "'")
                
            # Futures
            for client_idx, client in enumerate(futures_clients):
                positions_resp = client.fetchPositions({})
                if positions_resp["success"]:
                    for position in positions_resp["data"]["positions"]:
                        # positionAmt
                        if position["symbol"] not in futures_asset["positions"]:
                            futures_asset["positions"][position["symbol"]] = []
                            for i in range(client_idx):
                                futures_asset["positions"][position["symbol"]].append(0.0)
                        futures_asset["positions"][position["symbol"]].append(float(position["positionAmt"]))
                        # unrealizedPnl
                        if position["quoteCurrency"] not in futures_asset["unrealizedPnl"]:
                            futures_asset["unrealizedPnl"][position["quoteCurrency"]] = []
                        for i in range(client_idx + 1):
                            futures_asset["unrealizedPnl"][position["quoteCurrency"]].append(0.0)
                        futures_asset["unrealizedPnl"][position["quoteCurrency"]][-1] += float(position["unrealizedProfit"])
                    for symbol in futures_asset["positions"]:
                        if len(futures_asset["positions"][symbol]) < client_idx + 1:
                            futures_asset["positions"][symbol].append(0.0)
                    if positions_resp["data"]["requestedApiCount"] > 0:
                        time.sleep(0.5)     # Wait for avoiding rate limit
                else:
                    raise Exception("Futures fetchPositions() failed, message is '" + str(positions_resp) + "'")
                
                
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
            for client_idx, client in enumerate(spot_clients):
                query = dict()
                query["market"] = []
                for currency in spot_asset["amount"]:
                    query["market"].append({"baseCurrency":currency,"quoteCurrency":spot_clients_info[client_idx]["value_currency"]})
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
            spot_asset["value"].clear()
            futures_asset["value"].clear()
            
            # Spot
            for client_idx, client in enumerate(spot_clients):
                markets_resp = client.fetchMarkets({})
                markets = []
                if markets_resp["success"]:
                    for market in markets_resp["data"]["markets"]:
                        markets.append([market["baseCurrency"], market["quoteCurrency"]])
                else:
                    raise Exception("Spot fetchMarkets() failed, message is '" + str(markets_resp) + "'")
                
                value = 0.0
                spot_clients_info[client_idx]["cannot_find_market"] = []
                
                for currency in spot_asset["amount"]:
                    if spot_asset["amount"][currency][client_idx] == 0:
                        continue
                    elif [currency, spot_clients_info[client_idx]["value_currency"].upper()] in markets:
                        query = {
                            "baseCurrency" : currency,
                            "quoteCurrency" : spot_clients_info[client_idx]["value_currency"]
                        }
                        fetchOrderbook_resp = client.fetchOrderbook(query)
                        
                        if not fetchOrderbook_resp["success"]:
                            raise Exception("Spot fetchOrderbook() failed, message is '" + str(fetchOrderbook_resp) + "'")
                        
                        bid = float(fetchOrderbook_resp["data"]["bids"][0]["price"])
                        
                        value += spot_asset["amount"][currency][client_idx] * bid
                        
                        if fetchOrderbook_resp["data"]["requestedApiCount"] > 0:
                            time.sleep(0.5)     # Wait for avoiding rate limit
                    elif currency == spot_clients_info[client_idx]["value_currency"].upper():
                        value += spot_asset["amount"][currency][client_idx]
                    else:
                        spot_clients_info[client_idx]["cannot_find_market"].append(currency)
                            
                spot_asset["value"].append(value)
                
            # Futures
            for client_idx, client in enumerate(futures_clients):
                markets_resp = client.fetchMarkets({})
                markets = []
                if markets_resp["success"]:
                    for market in markets_resp["data"]["markets"]:
                        markets.append([market["baseCurrency"], market["quoteCurrency"], market["expiration"]])
                else:
                    raise Exception("Futures fetchMarkets() failed, message is '" + str(markets_resp) + "'")
                
                value = 0.0
                for currency in futures_asset["unrealizedPnl"]:
                    futures_asset["amount"][currency][client_idx] += futures_asset["unrealizedPnl"][currency][client_idx]
                
                futures_clients_info[client_idx]["cannot_find_market"] = []
                
                for currency in futures_asset["amount"]:
                    if futures_asset["amount"][currency][client_idx] == 0:
                        continue
                    elif [currency, futures_clients_info[client_idx]["value_currency"].upper(), "PERP"] in markets:
                        query = {
                            "baseCurrency" : currency,
                            "quoteCurrency" : futures_clients_info[client_idx]["value_currency"]
                        }
                        fetchOrderbook_resp = client.fetchOrderbook(query)
                        
                        if not fetchOrderbook_resp["success"]:
                            raise Exception("Futures fetchOrderbook() failed, message is '" + str(fetchOrderbook_resp) + "'")
                        
                        bid = float(fetchOrderbook_resp["data"]["bids"][0]["price"])
                        
                        value += futures_asset["amount"][currency][client_idx] * bid
                        
                        if fetchOrderbook_resp["data"]["requestedApiCount"] > 0:
                            time.sleep(0.5)     # Wait for avoiding rate limit
                    elif currency == futures_clients_info[client_idx]["value_currency"].upper():
                        value += futures_asset["amount"][currency][client_idx]
                    else:
                        futures_clients_info[client_idx]["cannot_find_market"].append(currency)
                
                futures_asset["value"].append(value)
                
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
    for nickname in spot_asset["header"]:
        header.append(nickname)
    tb_spot.field_names = header
    for currency in spot_asset["amount"]:
        data = [currency] + spot_asset["amount"][currency]
        tb_spot.add_row(data)
    empty_row = ["--------"]
    footer = ["value"]
    for value_idx, value in enumerate(spot_asset["value"]):
        empty_row.append("------------")
        footer.append(str(value) + " " + spot_clients_info[value_idx]["value_currency"])
    tb_spot.add_row(empty_row)
    tb_spot.add_row(footer)
    print(tb_spot)
    
    # Not calculated currencies. Currencies in the list below are not listed on the market.
    print("*** Currencies which are not calculated in the asset value above ***")
    for nickname_idx, nickname in enumerate(spot_asset["header"]):
        if len(spot_clients_info[nickname_idx]["cannot_find_market"]) == 0:
            continue
        print(nickname + " : " + ", ".join(spot_clients_info[nickname_idx]["cannot_find_market"]))

    print("")
    print("")
    
    ### Futures ###
    print("****** FUTURES ******")
    print("*** Positions ***")
    tb_futures_position = pt.PrettyTable()
    header = ["Nickname"]
    for nickname in futures_asset["header"]:
        header.append(nickname)
    tb_futures_position.field_names = header
    
    for symbol in futures_asset["positions"]:
        data = [symbol] + futures_asset["positions"][symbol]
        tb_futures_position.add_row(data)
    print(tb_futures_position)
    
    print("")
    print("*** Asset ***")
    tb_futures_asset = pt.PrettyTable()
    header = ["Nickname"]
    for nickname in futures_asset["header"]:
        header.append(nickname)
    tb_futures_asset.field_names = header
    for currency in futures_asset["amount"]:
        data = [currency] + futures_asset["amount"][currency]
        tb_futures_asset.add_row(data)
    empty_row = ["--------"]
    footer = ["value"]
    for value_idx, value in enumerate(futures_asset["value"]):
        empty_row.append("------------")
        footer.append(str(value) + " " + futures_clients_info[value_idx]["value_currency"])
    tb_futures_asset.add_row(empty_row)
    tb_futures_asset.add_row(footer)
    print(tb_futures_asset)
    
    # Not calculated currencies. Currencies in the list below are not listed on the market.
    print("*** Currencies which are not calculated in the asset value above ***")
    for nickname_idx, nickname in enumerate(futures_asset["header"]):
        if len(futures_clients_info[nickname_idx]["cannot_find_market"]) == 0:
            continue
        print(nickname + " : " + ", ".join(futures_clients_info[nickname_idx]["cannot_find_market"]))


if __name__ == "__main__":
    logger.info("Reporter is started")
    init_variables()
    
    subscribe_balance()
    fetch_asset_data()
    subscribe_orderbook()
    calc_asset_value()
    
    print_assets()
    
