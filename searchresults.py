import jinja2
import os
from google.appengine.ext import ndb
import random
import webapp2
import Event
from MainPage import FindEventsHandler
from MainPage import ActiveSearchHandler

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
)


class SearchResultsHandler(webapp2.RequestHandler):
    def get(self):
        #self.response.write("Your search term was this thing")
        findevents_template = jinja_env.get_template('sr.html')
        html = findevents_template.render()
