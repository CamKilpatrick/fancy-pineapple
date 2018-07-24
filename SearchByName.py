import Event

def SearchByName(name):
    newsearch = Event.Event.query().filter(Event.Event.eventname==name)
    return newsearch
