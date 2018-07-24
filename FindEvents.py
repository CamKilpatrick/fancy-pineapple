
import jinja2
import os
from google.appengine.ext import ndb
import random
import webapp2
import Event

# import model

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
)

class FindEventsHandler(webapp2.RequestHandler):
    def get(self):
        findevents_template = jinja_env.get_template('FE.html')
        html = findevents_template.render()
        self.response.write(html)


class ActiveSearchHandler(webapp2.RequestHandler):
    def get(self):
        searchvar = self.request.get("search_input")
        query = Event.Event.query().filter(Event.Event.eventname=="searchvar")
        query = query.get()
        print query

        # search = model.Search()
        # search.search_input = raw_input


        #self.response.write(html) ****don't know if i need this.
        #i got this from madlibs

# class Search(ndb.model):
#     def get(self):
#         search_input = ndb.StringProperty(required=True)

#####i was trying to figure out search, but before i do that i want to insert the login button and create event button for links later.


####to be a new page

# class SearchResultsHandler
#     def get(self):
#
#
#     findevents_template = jinja_env.get_template('SR.html')
#     html = findevents_template.render()
#
#










# app = webapp2.WSGIApplication([
# ('/', MainHandler),
# ('/find', FindEventsHandler),
# ('/description', DescriptionHandler),
# ('/create', CreateHandler),
#
# ], debug=True)
