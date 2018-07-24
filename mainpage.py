import webapp2
import random
import datetime
import jinja2
import os
from google.appengine.ext import ndb
from login import LoginHandler



jinja_env = jinja2.Environment(
    loader= jinja2.FileSystemLoader(os.path.dirname(__file__)),
)

def SearchByName(name):
    newsearch = Event.query().filter(Event.eventnamelower==name.lower())
    return newsearch

def DateTimeConverter(timestring):
    s = datetime.datetime.strptime(timestring, "%Y-%m-%dT%H:%M")
    return s

class Event(ndb.Model):
    eventname = ndb.StringProperty(required=True)
    eventnamelower = ndb.StringProperty(required=True)
    description = ndb.StringProperty(required=True)
    musictag = ndb.StringProperty(required=True)
    dancetag = ndb.StringProperty(required=True)
    theatertag = ndb.StringProperty(required=True)
    end = ndb.DateTimeProperty(required=True)
    start =ndb.DateTimeProperty(required=True)
    location = ndb.StringProperty(required=True)

class MainPageHandler(webapp2.RequestHandler):
    def get(self):
        main_template = jinja_env.get_template('mp.html')
        html = main_template.render()
        self.response.write(html)



class FindEventsHandler(webapp2.RequestHandler):
    def get(self):
        findevents_template = jinja_env.get_template('fe.html')
        html = findevents_template.render()
        self.response.write(html)

class ActiveSearchHandler(webapp2.RequestHandler):
    def get(self):
        search = SearchByName(self.request.get("search_input"))
        search2 = search.get()
        if search2 is not None:
            self.response.write(search2.start)
            self.response.write(search2.eventname)
            self.response.write(search2.description)
            self.response.write(search2.end)
            self.response.write(search2.location)
            self.response.write(search2.theatertag)
            self.response.write(search2.dancetag)
            self.response.write(search2.musictag)

        else:
            self.response.write("Sorry, your seach turned up empty.")


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
        new_event.start = DateTimeConverter(self.request.get('start'))
        new_event.end = DateTimeConverter(self.request.get('end'))
        new_event.location = self.request.get('location')
        new_event.put()

app = webapp2.WSGIApplication([
    ('/', MainPageHandler),
    ('/find', FindEventsHandler),
    ('/new', NewEventHandler),
    ('/create', EventTemplateHandler),
    ('/active', ActiveSearchHandler),
    ('/login', LoginHandler),
    ('/create', EventTemplateHandler),
    ('/login', LoginHandler),
    ('/create', EventTemplateHandler),
    ('/active', ActiveSearchHandler),
],debug=True)
