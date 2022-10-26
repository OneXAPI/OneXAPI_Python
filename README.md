# OneXAPI – One eXchange API

[![PyPI](https://img.shields.io/pypi/v/onexapi.svg)](https://pypi.python.org/pypi/onexapi) [![PyPI Downloads](https://img.shields.io/pypi/dm/onexapi.svg)](https://pypi.python.org/pypi/onexapi) ![Discord](https://img.shields.io/discord/1029941678938792028?logo=discord&logoColor=white) ![Supported Exchanges](https://img.shields.io/badge/exchanges-2-blue.svg)  

**OneXAPI**, an abbreviation for One eXchange API, was created with the aim of communicating with exchanges in one unified API.  
OneXAPI helps Quant Traders focus on algorithmic research without wasting time on SDK development.  

OneXAPI has the following advantages.  
1. Standardization
  - OneXAPI has standardized API input and output. Users can develop programs by referring only to OneXAPI documents without having to refer to each exchange API documents. 
  - Since OneXAPI uses the same API input/output for all exchanges, it is easy to transfer to the exchange without changing the code.
2. Simplification
  - You don't have to worry about the decimal places supported by the exchange when using orders/withdrawals, etc. The value is automatically converted to the decimal point supported by the exchange.
  - It's easy to decide whether to include fees deducted from your withdrawal or pay separately.
  - Simplify WebSocket usage. If you pass only the information that you want to receive through WebSocket, the connection and maintenance are automatically performed on the background.
  - You can receive as many past Candle Data as you want regardless of the limit of the exchange.
  - It is easy to use by newly developing and integrating functions that were not provided by the exchange API or were complicated.
3. Quickness
  - OneXAPI has been developed as C++ and boasts fast performance.
  - There is no delay because it communicates directly with the exchange without going through the intermediate server.
4. Maintenance
  - If the exchange API changes, an immediate update is performed. Users can use the same algorithm only with OneXAPI updates without changing the code.
5. Safety
  - OneXAPI does not collect the user's API key, so there is no risk of stealing the API key.

---

## Documentation
Read [API Docs](https://onexapi.github.io/OneXAPI-Reference/) for more details

---
## Install
### Python
[**PyPI**](https://pypi.python.org/pypi/onexapi) (Python 3.6+)
```python
pip install OneXAPI
```
```python
import OneXAPI

print(OneXAPI.getInfo()) # Print all supported exchanges
```

---

## Supported Exchanges  
| Logo | Exchange | Spot | Futures |
|:----:|:--------:|:----:|:-------:|
| <img src="https://user-images.githubusercontent.com/19239391/197909079-5c8a2727-cbc1-4f26-927d-cc60d6dbb076.png" width="130" height="40"/> | [Binance](https://www.binance.com/en) | 🟢 | 🟢 |
| <img src="https://user-images.githubusercontent.com/19239391/197908208-4520dfd8-b142-4a80-9dac-36b10a73b985.png" width="130" height="40"/> | [Upbit](https://www.upbit.com) | 🟢 | 🔴 |

---
## Contribution
Read [CONTRIBUTION](https://github.com/OneXAPI/OneXAPI_Python/blob/master/CONTRIBUTION.md) for more details

---
## Contact
ceo@libera.or.kr