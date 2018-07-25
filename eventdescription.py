import webapp2
import jinja2
import os
import Event

jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
)

class EventHandler(webapp2.RequestHandler):
    def get(self):
        specific_event = Event.query().filter(Event.name=="test event 3")
        event_template = jinja_env.get_template('ED.html')
        html = event_template.render({
        'event_title': specific_event.title,
        'event_description': specific_event.description,
        'tags': specific_event.tags
###trying to retreive information from localhost:8000, need to run "Event.py" first ^^^
        })
        self.response.write(html)

app = webapp2.WSGIApplication([
    ('/ED', EventHandler),
], debug=True)
