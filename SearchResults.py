import jinja2
import os
from google.appengine.ext import ndb
import random
import webapp2
import Event
from FindEvents import FindEventsHandler
from FindEvents import ActiveSearchHandler

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
)


class SearchResultsHandler(webapp2.RequestHandler):
    def get(self):
        searchvar = self.request.get("self.search_input")
        ###########i ended here. the line above and/or below is having serious problems
        #######i am trying to define a variable (i think) and get stuff i put on
        #one page to show up on the next page. actually on second thought ,i realize we kinda
        # did that before,
        self.response.write("Your search term was %s" % (search_input))
        findevents_template = jinja_env.get_template('SR.html')
        html = findevents_template.render()
