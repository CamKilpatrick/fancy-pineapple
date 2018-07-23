
import jinja2
import os
from google.appengine.ext import ndb
import random
import webapp2

import model


class FindEventsHandler(webapp2.RequestHandler):
    def get(self)

















app = webapp2.WSGIApplication([
(‘/’, MainHandler),
(‘/find’, FindEventsHandler),
(‘/description’, DescriptionHandler),
(‘/create’, CreateHandler),
], debug=True)
