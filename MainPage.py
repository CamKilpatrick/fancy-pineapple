import webapp2
import random
import datetime
import jinja2
import os
from google.appengine.ext import ndb
import Event
from FindEvents import FindEventsHandler
from SearchResults import SearchResultsHandler
from CreateEvent import EventTemplateHandler
from login import LoginHandler
from CreateEvent import NewEventHandler
from FindEvents import ActiveSearchHandler
from myevent import MyEventHandler


jinja_env = jinja2.Environment(
    loader= jinja2.FileSystemLoader(os.path.dirname(__file__)),
)
class MainPageHandler(webapp2.RequestHandler):
    def get(self):
        main_template = jinja_env.get_template('MP.html')
        html = main_template.render()
        self.response.write(html)

app = webapp2.WSGIApplication([
    ('/', MainPageHandler),
    ('/find', FindEventsHandler),
    ('/results', SearchResultsHandler),
    ('/new', NewEventHandler),
    ('/create', EventTemplateHandler),
    ('/active', ActiveSearchHandler),
    ('/login', LoginHandler),
    ('/create', EventTemplateHandler),
    ('/login', LoginHandler),
    ('/create', EventTemplateHandler),
    ('/active', ActiveSearchHandler),
    ('/myevent', MyEventHandler),
],debug=True)
