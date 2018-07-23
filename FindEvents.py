
import jinja2
import os
from google.appengine.ext import ndb
import random
import webapp2
import Event

import model

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__))
)

class FindEventsHandler(webapp2.RequestHandler):
    def get(self):
        search = model.Search()
        search.search_input = raw_input?????
        search.put()
        findevents_template = jinja_env.get_template('FE.html')
        html = findevents_template.render()
        #self.response.write(html) ****don't know if i need this.
        #i got this from madlibs
class Search(ndb.model):
    def get(self):
        search_input = ndb.StringProperty(required=True)

















app = webapp2.WSGIApplication([
(‘/’, MainHandler),
(‘/find’, FindEventsHandler),
(‘/description’, DescriptionHandler),
(‘/create’, CreateHandler),
], debug=True)
