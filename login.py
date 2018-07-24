import webapp2
import random
import datetime
import jinja2
import os


#
# jinja_env = jinja2.Environment(
#     loader= jinja2.FileSystemLoader(os.path.dirname(__file__)),
# )
#
#
# class LoginHandler(webapp2.RequestHandler):
#     def get(self):
#         login_template= jinja_env.get_template('login.html')
#         html= login_template.render()
#         self.response.write(html)
#
#
# app= webapp2.WSGIApplication([
#     ('/login', LoginHandler)
#     ],debug=True)

import webapp2

from google.appengine.api import users
from google.appengine.ext import ndb

class User(ndb.Model):

  first_name = ndb.StringProperty()
  last_name = ndb.StringProperty()

class LoginHandler(webapp2.RequestHandler):
  def get(self):
    user = users.get_current_user()
    # If the user is logged in...
    if user:
      email_address = user.nickname()
      user = User.get_by_id(user.user_id())
      signout_link_html = '<a href="%s">sign out</a>' % (
          users.create_logout_url('/'))
      # If the user has previously been to our site, we greet them!
      if user:
        self.response.write('''
            Welcome %s %s (%s)! <br> %s <br>''' % (
              user.first_name,
              user.last_name,
              email_address,
              signout_link_html))
      # If the user hasn't been to our site, we ask them to sign up
      else:
        self.response.write('''
            Welcome to our site, %s!  Please sign up! <br>
            <form method="post" action="/">
            <input type="text" name="first_name" placeholder= 'Enter First Name'>
            <input type="text" name="last_name" placeholder= 'Enter Last Name'>
            <input type="submit">
            </form><br> %s <br>
            ''' % (email_address, signout_link_html))
    # Otherwise, the user isn't logged in!
    else:
      self.response.write('''
        Please log in to use our site! <br>
        <a href="%s">Sign in</a>''' % (
          users.create_login_url('/')))

  def post(self):
    user = users.get_current_user()
    if not user:
      # You shouldn't be able to get here without being logged in
      self.error(500)
      return
    user = User(
        first_name=self.request.get('first_name'),
        last_name=self.request.get('last_name'),
        id=user.user_id())
    user.put()
    self.response.write('Thanks for signing up, %s!' %
        user.first_name)

app = webapp2.WSGIApplication([
  ('/login', LoginHandler)
], debug=True)



# make this work and connect to the main page/ home page also, fix mainpage.py. also change location on create event to actual location using google map
