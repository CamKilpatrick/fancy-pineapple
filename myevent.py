import webapp2
import jinja2
import os
jinja_env = jinja2.Environment(
    loader= jinja2.FileSystemLoader(os.path.dirname(__file__)),
)
class MyEventHandler(webapp2.RequestHandler):
    def get(self):
        myevent_template= jinja_env.get_template('myevent.html')
        html= myevent_template.render()
        self.response.write(html)
