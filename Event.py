from google.appengine.ext import ndb
import datetime

class Event(ndb.Model):
    eventname = ndb.StringProperty(required=True)
    description = ndb.StringProperty(required=True)
    tags = ndb.StringProperty(required=True)
    end = ndb.DateTimeProperty(required=True)
    start =ndb.DateTimeProperty(required=True)
    location = ndb.StringProperty(required=True)
