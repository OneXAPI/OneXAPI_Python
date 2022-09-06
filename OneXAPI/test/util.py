import time

def searchLog(nowTime, searchText):
    filename = './OneXAPI_Logs/OneXAPI_' + time.strftime('%Y-%m-%d', nowTime) + '.log'
    searchTime = time.strftime('%Y-%m-%d %H:%M', nowTime)

    with open(filename) as fp:
        logData = fp.readlines()
        for line in logData:
            if searchTime in line and searchText in line:
                return True
			
    return False