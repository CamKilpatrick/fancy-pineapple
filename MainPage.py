import webapp2
import random
import datetime
import jinja2
import os
from FindEvents import FindEventsHandler
<<<<<<< HEAD
from SearchResults import SearchResultsHandler
=======
from google.appengine.ext import ndb
import Event

>>>>>>> a6a2d9b4b92d837d99c2670288c4dc8cf06fb156

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
    ('/results', SearchResultsHandler)
],debug=True)
