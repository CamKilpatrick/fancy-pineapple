import webapp2
import jinja2
import os

jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
)


class EventHandler(webapp2.RequestHandler):
    def get(self):
        event_template = jinja_env.get_template('templates/ED.html')
        html = event_template.render({
        'event_title': 'My cool event',
        'event_description': 'Cool stuff will be happening at this event',
        'tags': 'fun, stuff'
        # 'noun2': self.request.get('noun2'),
        # 'presentVerb': self.request.get('presentVerb'),
        # 'verb2': self.request.get('verb2'),
        # 'name': self.request.get('name'),
        # 'adjective': self.request.get('adjective'),
        # 'pronoun': self.request.get('pronoun')
        })
        self.response.write(html)

app = webapp2.WSGIApplication([
    ('/ED', EventHandler),
], debug=True)
