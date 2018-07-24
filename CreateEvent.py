import Event
import webapp2
import random
import datetime
import jinja2
import os
from DateTimeConverter import DateTimeConverter

jinja_env = jinja2.Environment(
    loader= jinja2.FileSystemLoader(os.path.dirname(__file__)),
)

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
    ('/create', EventTemplateHandler),
    ('/new', NewEventHandler)
], debug=True)
