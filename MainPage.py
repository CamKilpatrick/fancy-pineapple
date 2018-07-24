import webapp2
import random
import datetime
import jinja2
import os
from google.appengine.ext import ndb
import Event
from login import LoginHandler
from SearchByName import SearchByName
from DateTimeConverter import DateTimeConverter


jinja_env = jinja2.Environment(
    loader= jinja2.FileSystemLoader(os.path.dirname(__file__)),
)
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
        self.response.write(search2.start)
        self.response.write(search2.eventname)
        self.response.write(search2.description)
        self.response.write(search2.tags)
        self.response.write(search2.end)
        self.response.write(search2.location)

class EventTemplateHandler(webapp2.RequestHandler):
    def get(self):
        createvent_template= jinja_env.get_template('CE.html')
        html= createvent_template.render()
        self.response.write(html)

class NewEventHandler(webapp2.RequestHandler):
    def get(self):
        new_event = Event.Event()
        print self.request.get('start')
        new_event.eventname = self.request.get('eventname')
        new_event.description = self.request.get('description')
        new_event.tags = self.request.get('tags')
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
