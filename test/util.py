import time
import sys
import os

def searchLog(nowTime, searchText):
    path = os.path.dirname(os.path.abspath(sys.argv[0]))
    filename = (path + '/OneXAPI_Logs/OneXAPI_' + time.strftime('%Y-%m-%d', nowTime) + '.log').replace('\\', '/')
    searchTime = time.strftime('%Y-%m-%d %H:%M', nowTime)

    with open(filename, encoding='utf-8') as fp:
        logData = fp.readlines()
        for line in logData:
            if searchTime in line and searchText in line:
                return True
			
    return False
