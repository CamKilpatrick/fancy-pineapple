import webapp2
import random
import datetime
import jinja2
import os
from google.appengine.ext import ndb

jinja_env = jinja2.Environment(
    loader= jinja2.FileSystemLoader(os.path.dirname(__file__)),
)

def SearchByName(name):
    new_search = Event.query().filter(Event.eventnamelower==name.lower())
    return new_search

def StandardTime(MiliTime):
    time = int(MiliTime)
    if time >= 1300:
        time = time - 1200
        time = str(time)
        time = time[0,2]+':'+time[2,4]+"PM"
    else:
        time = str(time)
        time = time[0,2]+':'+time[2,4]+"AM"


def SearchByID(ID):
    retrieve_all = Event.query().iter()
    print retrieve_all
    print ID
    for item in retrieve_all:
        print item.key.id()
        if str(item.key.id()) == str(ID):
            return item
    pass
###########trying to iron this out

def SearchByTag(tagname):
    if tagname=="theatertag":
        newsearch = Event.query().filter(Event.theatertag=="on")
        return newsearch
    elif tagname=="musictag":
        newsearch = Event.query().filter(Event.musictag=="on")
        return newsearch
    elif tagname=="dancetag":
        newsearch = Event.query().filter(Event.dancetag=="on")
        return newsearch
    elif tagname=="foodtag":
        newsearch = Event.query().filter(Event.foodtag=="on")
        return newsearch
    elif tagname=="fitnesstag":
        newsearch = Event.query().filter(Event.fitnesstag=="on")
        return newsearch
    else:
        pass


def MakeLink(event):
    event.link = "/" + str(event.key.id)

def DateTimeConverter(timestring):
    s = datetime.datetime.strptime(timestring, "%Y-%m-%dT%H:%M")
    return s

class Event(ndb.Model):
    eventname = ndb.StringProperty(required=True)
    eventnamelower = ndb.StringProperty(required=True)
    description = ndb.StringProperty(required=True)
    musictag = ndb.StringProperty(required=True)
    dancetag = ndb.StringProperty(required=True)
    foodtag = ndb.StringProperty(required=True)
    fitnesstag = ndb.StringProperty(required=True)
    theatertag = ndb.StringProperty(required=True)
    end = ndb.DateTimeProperty(required=True)
    start =ndb.DateTimeProperty(required=True)
    location = ndb.StringProperty(required=True)
    linknum = ndb.StringProperty(required=False)
    start_time = ndb.StringProperty(required=False)
    end_time = ndb.StringProperty(required=False)

class MainPageHandler(webapp2.RequestHandler):
    def get(self):
        main_template = jinja_env.get_template('mp.html')
        html = main_template.render()
        self.response.write(html)

class FindEventsHandler(webapp2.RequestHandler):
    def get(self):
        findevents_template = jinja_env.get_template('fe.html')
        # display_events = SearchEvent.fetch()
        # search_iter = display_events.iter()
        # self.response.write(display_events)
        html = findevents_template.render({
        # 'listevents': search_iter,
        })
        self.response.write(html)
        # displayquery = Event.query().order(Event.start)
        # return displayquery
        #I was trying to make a query that will show all the events on one page on the find events page

class ActiveSearchHandler(webapp2.RequestHandler):
    def get(self):
        search = SearchByName(self.request.get("search_input"))
        search_iter = search.iter()
        if search.get() is not None:
            event_template = jinja_env.get_template('sr.html')
            html = event_template.render({
            'navigation': search_iter,
           })
            self.response.write(html)
        else:
            event_template = jinja_env.get_template('nr.html')
            html = event_template.render()
            self.response.write(html)

class TheaterSearchHandler(webapp2.RequestHandler):
    def get(self):
        search3 = SearchByTag("theatertag")
        tagsearch = search3.iter()
        theater_template = jinja_env.get_template('sr.html')
        html = theater_template.render({
        'navigation': tagsearch,
        })
        self.response.write(html)

class FoodSearchHandler(webapp2.RequestHandler):
    def get(self):
        search3 = SearchByTag("foodtag")
        tagsearch = search3.iter()
        food_template = jinja_env.get_template('sr.html')
        html = food_template.render({
        'navigation': tagsearch,
        })
        self.response.write(html)

class FitnessSearchHandler(webapp2.RequestHandler):
    def get(self):
        search3 = SearchByTag("fitnesstag")
        tagsearch = search3.iter()
        fitness_template = jinja_env.get_template('sr.html')
        html = fitness_template.render({
        'navigation': tagsearch,
        })
        self.response.write(html)

class MusicSearchHandler(webapp2.RequestHandler):
    def get(self):
        search3 = SearchByTag("musictag")
        tagsearch = search3.iter()
        music_template = jinja_env.get_template('sr.html')
        html = music_template.render({
        'navigation': tagsearch,
        })
        self.response.write(html)


class DanceSearchHandler(webapp2.RequestHandler):
    def get(self):
        search3 = SearchByTag("dancetag")
        tagsearch = search3.iter()
        dance_template = jinja_env.get_template('sr.html')
        html = dance_template.render({
        'navigation': tagsearch,
        })
        self.response.write(html)

class EventTemplateHandler(webapp2.RequestHandler):
    def get(self):
        createvent_template= jinja_env.get_template('ce.html')
        html= createvent_template.render()
        self.response.write(html)

class NewEventHandler(webapp2.RequestHandler):
    def get(self):
        new_event = Event()
        myevent_template= jinja_env.get_template('myevent.html')
        html= myevent_template.render()
        self.response.write(html)
        new_event.eventnamelower = self.request.get('eventname').lower()
        new_event.eventname = self.request.get('eventname')
        new_event.description = self.request.get('description')
        new_event.musictag = self.request.get('musictag')
        new_event.theatertag = self.request.get('theatertag')
        new_event.dancetag = self.request.get('dancetag')
        new_event.fitnesstag = self.request.get('fitnesstag')
        new_event.foodtag = self.request.get('foodtag')
        new_event.start = DateTimeConverter(self.request.get('start'))
        new_event.end = DateTimeConverter(self.request.get('end'))
        new_event.location = self.request.get('location')
        new_event.start_time = new_event.start.strftime('%I:%M %p')
        new_event.end_time = new_event.end.strftime('%I:%M %p')
        new_event.put()

class EventHandler(webapp2.RequestHandler):
    def get(self):
        event1 = SearchByID(self.request.get("key"))
        event_template = jinja_env.get_template('ed.html')
        html = event_template.render({
        'item':event1
        })
        self.response.write(html)

app = webapp2.WSGIApplication([
    ('/', MainPageHandler),
    ('/find', FindEventsHandler),
    ('/new', NewEventHandler),
    ('/create', EventTemplateHandler),
    ('/active', ActiveSearchHandler),
    ('/ed', EventHandler),
    ('/theater', TheaterSearchHandler),
    ('/music', MusicSearchHandler),
    ('/dance', DanceSearchHandler),
    ('/ed', EventHandler),
    ('/food', FoodSearchHandler),
    ('/fitness', FitnessSearchHandler),

],debug=True)
