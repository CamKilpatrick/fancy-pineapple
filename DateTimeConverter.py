import datetime

def DateTimeConverter(timestring):
    t = datetime.datetime.strptime(timestring, %Y-%M-%DT%I:%M)
    return t

2018-04-05T20:00
