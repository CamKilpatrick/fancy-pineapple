import webapp2
import random
import datetime
import jinja2
import os



jinja_env = jinja2.Environment(
    loader= jinja2.FileSystemLoader(os.path.dirname(__file__)),
)


class LoginHandler(webapp2.RequestHandler):
    def get(self):
        login_template= jinja_env.get_template('login.html')
        html= login_template.render()
        self.response.write(html)


app= webapp2.WSGIApplication([
    ('/login', LoginHandler)
    ],debug=True)
