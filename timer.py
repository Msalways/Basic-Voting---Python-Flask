import datetime
import datetime as dt
import time
import time as t


def setTimer(times):
    end = str(times).replace('T', ' ')
    year = int(end[0:4])
    mon = int(end[5:7])
    day = int(end[8:10])
    hour = int(end[11:13])
    minu = int(end[14:16])
    print(year, mon, day, hour, minu)
    now = datetime.datetime.today()
    finishAt = datetime.datetime(year, mon, day, hour, minu)
    dif = finishAt - now
    totSec = dif.total_seconds()
    return totSec
