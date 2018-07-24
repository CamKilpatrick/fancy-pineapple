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
    newsearch = Event.query().filter(Event.eventname==name)
    return newsearch

def DateTimeConverter(timestring):
    s = datetime.datetime.strptime(timestring, "%Y-%m-%dT%H:%M")
    return s

class Event(ndb.Model):
    eventname = ndb.StringProperty(required=True)
    description = ndb.StringProperty(required=True)
    musictag = ndb.StringProperty(required=True)
    dancetag = ndb.StringProperty(required=True)
    theatertag = ndb.StringProperty(required=True)
    end = ndb.DateTimeProperty(required=True)
    start =ndb.DateTimeProperty(required=True)
    location = ndb.StringProperty(required=True)

class MainPageHandler(webapp2.RequestHandler):
    def get(self):
        main_template = jinja_env.get_template('MP.html')
        html = main_template.render()
        self.response.write(html)



class FindEventsHandler(webapp2.RequestHandler):
    def get(self):
        findevents_template = jinja_env.get_template('FE.html')
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
            self.response.write(search2.tags)
            self.response.write(search2.end)
            self.response.write(search2.location)
        else:
            self.response.write("Sorry, your seach turned up empty.")



class EventTemplateHandler(webapp2.RequestHandler):
    def get(self):
        createvent_template= jinja_env.get_template('CE.html')
        html= createvent_template.render()
        self.response.write(html)

class NewEventHandler(webapp2.RequestHandler):
    def get(self):
        new_event = Event()
<<<<<<< HEAD
=======
        myevent_template= jinja_env.get_template('myevent.html')
        html= myevent_template.render()
        self.response.write(html)
>>>>>>> 911a1d6d39369e99a67b29f78c94a7761c27b86a
        new_event.eventname = self.request.get('eventname')
        new_event.description = self.request.get('description')
        new_event.tags = self.request.get('tags')
        new_event.start = DateTimeConverter(self.request.get('start'))
        new_event.end = DateTimeConverter(self.request.get('end'))
        new_event.location = self.request.get('location')
        new_event.put()
        print "#######################################"
        print self.request.get('musictag')
        print "#######################################"

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
