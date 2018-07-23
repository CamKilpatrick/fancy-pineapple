from google.appengine.ext import ndb

class Event(ndb.Model):
    eventname = ndb.StringProperty(required=True)
    description = ndb.StringProperty(required=True)
    tags = ndb.StringProperty(required=True)
    end = ndb.StringProperty(required=True)
    start =ndb.StringProperty(required=True)
    location = ndb.StringProperty(required=True)
