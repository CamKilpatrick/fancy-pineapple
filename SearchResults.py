import jinja2
import os
from google.appengine.ext import ndb
import random
import webapp2
import Event

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
)


class SearchResultsHandler(webapp2.RequestHandler):
    def get(self):
        searchvar = self.request.get("search_input")
        self.response.write("Your search term was" ())
        findevents_template = jinja_env.get_template('SR.html')
        html = findevents_template.render()
