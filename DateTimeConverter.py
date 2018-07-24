import datetime

def DateTimeConverter(timestring):
    s = datetime.datetime.strptime(timestring, "%Y-%m-%dT%H:%M")
    return s
#2018-04-05T20:00
#0123456789123456
